from faulthandler import disable
from http import server
from pydoc import plain
from stat import filemode
from tkinter import *
import tkinter.font as TkFont
from tkinter import StringVar
import tkinter.messagebox
import socket
import time
import json
from turtle import clear, update
exploreDataStatus = True
unpredict = True
class Clock:
    def __init__(self):
        self.time1 = ''
        self.time2 = time.strftime('%H:%M:%S')
        self.mFrame = Frame()
        self.mFrame.pack(side=TOP)

        self.watch = Label(self.mFrame, text=self.time2,font=('Microsoft YaHei Light',30,'bold'),fg="Blue",bg='powder blue')
        self.watch.pack()

        self.changeLabel() #first call it manually

    def changeLabel(self): 
        self.time2 = time.strftime('%H:%M:%S')
        self.watch.configure(text=self.time2)
        self.mFrame.after(200, self.changeLabel) #it'll call itself continuously


try:
    with open('statics.json','r',encoding='utf-8') as j:
        getdata = json.load(j)
        exploreDataStatus = True
        j.close()
    with open('statics_players.json','r') as j:
        getStatic = json.load(j)
        j.close()
except :
    exploreDataStatus = False


#Client
root = Tk()
root.geometry("1600x800+0+0")
#root.attributes('-fullscreen', True)  
root.title("Tic-tac-toe")
root.configure(background='powder blue')
messagetry = StringVar()
modeNow = StringVar()
modeMainFrame = StringVar()
Tops = Frame(root,width=1600,height=400,bg="powder blue",relief=SUNKEN)
Tops.pack(side=TOP)

f0 = Frame(Tops,bg="powder blue",relief=SUNKEN)
f0.grid(row=0,column=0)

#label
lblInfo = Label(f0,font=('Microsoft YaHei Light',50,'bold'),
                text="TIC-TAC-TOE",fg="Blue",bd=10,background='powder blue')
lblInfo.grid(row=0,column=0)
lblRole = Label(f0,font=('Microsoft YaHei Light',40,'bold'),
                textvariable=modeMainFrame,fg="Blue",bd=10,background='powder blue')
lblRole.grid(row=1,column=0)
#bank zone
#===============================================================
f0a = Frame(Tops,bg="powder blue",relief=SUNKEN)
f0a.grid(row=0,column=1)
lblAir = Label(f0a,font=('Microsoft YaHei Light',25,'bold'),
                text="\t\t\tMode",fg="Blue",bd=10,background='powder blue')
lblAir.grid(row=0,column=0)
lblAir2 = Label(f0a,font=('Microsoft YaHei Light',25,'bold'),
                text="\t\tClient to Client",fg="Blue",bd=10,background='powder blue')
lblAir2.grid(row=1,column=0)








# lblAir3 = Label(f0a,font=('Microsoft YaHei Light',30,'bold'),
#                 text="Button1",fg="Blue",bd=10,background='powder blue')
# lblAir3.grid(row=1,column=1)
# lblAir4 = Label(f0a,font=('Microsoft YaHei Light',30,'bold'),
#                 text="Button2",fg="Blue",bd=10,background='powder blue')
# lblAir4.grid(row=2,column=1)
#===============================================================
#hall
f0b = Frame(Tops,bg="powder blue",relief=SUNKEN)
f0b.grid(row=0,column=2)
clock = Clock()
lblHall = Label(f0b,font=('Microsoft YaHei Light',50,'bold'),
                textvariable=str(clock),fg="Blue",background='powder blue')
lblHall.grid(row=0,column=0)
lblHall2 = Label(f0b,font=('Microsoft YaHei Light',40,'bold'),
                text='\t'*2,fg="Blue",bd=10,background='powder blue')
lblHall2.grid(row=2,column=0)





# lblInfo3 = Label(f0,font=('Microsoft YaHei Light',50,'bold'),
#                 text="\t\t",fg="Blue",bd=10)
# lblInfo3.grid(row=0,column=2)
# lblRole3 = Label(f0,font=('Microsoft YaHei Light',40,'bold'),
#                 text="\t\t",fg="Blue",bd=10)
# lblRole3.grid(row=1,column=2)


Bottoms = Frame(root,width=1600,bg="powder blue",relief=SUNKEN)
Bottoms.pack(side=BOTTOM)
f1 = Frame(Bottoms,width=800,height=700,bg="",relief=SUNKEN)
f1.grid(row=1,column=1)
f2 = Frame(Bottoms,width=600,height=700,relief=SUNKEN)
f2.grid(row=1,column=2)
f2.configure(background='powder blue')
f3 = Frame(Bottoms,width=500,height=700,relief=SUNKEN,bg="powder blue")
f3.grid(row=1,column=3)
lblInfox = Label(f3,font=('Microsoft YaHei Light',50,'bold'),
                text="Hall of Fame",fg="Blue",bd=10,anchor='w',bg="powder blue")
lblInfox.grid(row=0,column=0)
txtHall = Text(f3,font=('TH Sarabun New',17,'bold'), bd=8,width=45,height=15,bg="powder blue")
txtHall.grid(row=1,column=0)

chkTime = 0

#tool>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def extract(x):
    y = []
    distance = 0 #name []
    distance2 = 0 #number {}
    state = False
    state2 = False
    for i in range(len(x)):
        if x[i]=='[':
            state = True
        if x[i]==']':
            state = False
        if state:
            distance+=1
        if x[i]=='{':
            state2 = True
        if x[i]=='}':
            state2 = False
        if state2:
            distance2+=1
        
    y.append(x[1:distance])
    y.append(x[distance+2:distance+1+distance2])
    distance = 0
    distance2 = 0
    return y
def TheTrain(x):#data '[round]{win}<lose>(draw)'
    result = []
    distance = 0
    distanceWin = 0
    distancelose = 0
    distancedraw = 0
    state = False
    stateWin = False
    statelose = False
    statedraw = False
    for i in range(len(x)):
        if x[i]=='[':
            state = True
        if x[i]==']':
            state = False
        if state:
            distance+=1

        if x[i]=='{':
            stateWin = True
        if x[i]=='}':
            stateWin = False
        if stateWin:
            distanceWin+=1

        if x[i]=='<':
            statelose = True
        if x[i]=='>':
            statelose = False
        if statelose:
            distancelose+=1

        if x[i]=='(':
            statedraw = True
        if x[i]==')':
            statedraw = False
        if statedraw:
            distancedraw+=1
        
    result.append(x[1:distance])
    result.append(x[distance+2:distance+1+distanceWin])
    result.append(x[distance+1+distanceWin+2:distance+1+distanceWin+1+distancelose])
    result.append(x[distance+1+distanceWin+1+distancelose+2:distance+1+distanceWin+1+distancelose+1+distancedraw])
    distance = 0
    distanceWin = 0
    distancelose = 0
    distancedraw = 0
    return result
#tool>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#OX CtoC code =======================================================================

def EndGame(touch):
    global endGame,count,socker
    endGame = False
   # sendMessage = str(touch)
    socker.send(str.encode(str(touch)))
    socker.close()
    default('CtoC')

def check_CtoC(touch):
    global count
    global msg
    global useSlot,endGame,opponent,myself
    count=0
    
    print('turn: '+str(count))
    if (msg[0] == msg[1]) and (msg[1] == msg[2]):         
        if (msg[0] == 'x'):
            print (str(myself)+"   WIN !!!!!!!!!!!!!!")    
            statePlayer.set(str(myself)+"   WIN !!!!!!!!!!!!!!")
            EndGame(touch)
        if (msg[0] == 'o'):
            print (str(opponent)+"   WIN !!!!!!!!!!!!!!")
            statePlayer.set(str(opponent)+"   WIN !!!!!!!!!!!!!!")
            EndGame(0)
        
        
                     
    elif (msg[3] == msg[4]) and (msg[4] == msg[5]):        
        if (msg[3] == 'x'):
            print (str(myself)+"   WIN !!!!!!!!!!!!!!")
            statePlayer.set(str(myself)+"   WIN !!!!!!!!!!!!!!")
            EndGame(touch)
        if (msg[3] == 'o'):
            print (str(opponent)+"   WIN !!!!!!!!!!!!!!")
            statePlayer.set(str(opponent)+"   WIN !!!!!!!!!!!!!!")
            EndGame(0)
        
    elif (msg[6] == msg[7]) and (msg[7] == msg[8]):
        if (msg[6] == 'x'):
            print (str(myself)+"   WIN !!!!!!!!!!!!!!")
            statePlayer.set(str(myself)+"   WIN !!!!!!!!!!!!!!")
            EndGame(touch) 
        if (msg[6] == 'o'):
            print (str(opponent)+"   WIN !!!!!!!!!!!!!!")
            statePlayer.set(str(opponent)+"   WIN !!!!!!!!!!!!!!")
            EndGame(0)
    elif (msg[0] == msg[3]) and (msg[3] == msg[6]):        
        if (msg[0] == 'x'):
            print (str(myself)+"   WIN !!!!!!!!!!!!!!")
            statePlayer.set(str(myself)+"   WIN !!!!!!!!!!!!!!")
            EndGame(touch)  
        if (msg[0] == 'o'):
            print (str(opponent)+"   WIN !!!!!!!!!!!!!!")
            statePlayer.set(str(opponent)+"   WIN !!!!!!!!!!!!!!")
            EndGame(0)
    elif (msg[1] == msg[4]) and (msg[4] == msg[7]):
        if (msg[1] == 'x'):
            print (str(myself)+"   WIN !!!!!!!!!!!!!!")  
            statePlayer.set(str(myself)+"   WIN !!!!!!!!!!!!!!")
            EndGame(touch)  
        if (msg[1] == 'o'):
            print (str(opponent)+"   WIN !!!!!!!!!!!!!!")
            statePlayer.set(str(opponent)+"   WIN !!!!!!!!!!!!!!")
            EndGame(0)  
    elif (msg[2] == msg[5]) and (msg[5] == msg[8]):        
        if (msg[2] == 'x'):
            print (str(myself)+"   WIN !!!!!!!!!!!!!!")
            statePlayer.set(str(myself)+"   WIN !!!!!!!!!!!!!!")
            EndGame(touch)
        if (msg[2] == 'o'):
            print (str(opponent)+"   WIN !!!!!!!!!!!!!!")
            statePlayer.set(str(opponent)+"   WIN !!!!!!!!!!!!!!")
            EndGame(0)
    elif (msg[0] == msg[4]) and (msg[4] == msg[8]):
        if (msg[0] == 'x'):
            print (str(myself)+"   WIN !!!!!!!!!!!!!!")
            statePlayer.set(str(myself)+"   WIN !!!!!!!!!!!!!!")
            EndGame(touch)
        if (msg[0] == 'o'):
            print (str(opponent)+"   WIN !!!!!!!!!!!!!!")
            statePlayer.set(str(opponent)+"   WIN !!!!!!!!!!!!!!")
            EndGame(0)
                  
    elif (msg[2] == msg[4]) and (msg[4] == msg[6]):
        if (msg[2] == 'x'):
            print (str(myself)+"   WIN !!!!!!!!!!!!!!")    
            statePlayer.set(str(myself)+"   WIN !!!!!!!!!!!!!!")
            EndGame(touch)  
        if (msg[2] == 'o'):
            print (str(opponent)+"   WIN !!!!!!!!!!!!!!")
            statePlayer.set(str(opponent)+"   WIN !!!!!!!!!!!!!!")
            EndGame(0)
    else:
        for i in msg:
            if i.isnumeric()==False:
                count+=1
                if count == 9:
                    print ("   Draw !!!!!!!!!!!!!!")
                    statePlayer.set(" Draw!!!!")
                    EndGame(99)#sp case
            else:
                count = 0


def clientPlay2(touch):#opponent
    touch = int(touch)
    global msg
    global count,socker
    global useSlot,endGame
    print("clientPlay2")
    for element in msg:
        if element.isnumeric()==True:
            break
    if touch == 99:#signal draw
        position = 0
        for element in msg:#find element not x,y
            if element.isnumeric()==True:
                (msg[int(position)]) = 'o'
                putSlot(int(position))
                check_CtoC(position)
                #endGame = False
                #print ("   Draw !!!!!!!!!!!!!!")
                socker.close()
                break
            else:
                position +=1
        
      

    elif touch != 0:
        (msg[int(touch)-1]) = 'o'
        putSlot(int(touch))
        #====================================
        touch = str(touch)
    #====================================
    
    
    try:
        #s.send(touch.encode('ascii'))
        pass
    except ValueError:
        print("Server disconnect")
    except ConnectionAbortedError:
        print("Server disconnect") 
    except UnboundLocalError:
        print("Server disconnect")
    except ConnectionResetError:
        print("Server disconnect")
    print_table(msg)
    if touch!=99:
        check_CtoC(touch)
    
    print('endgame'+str(endGame))
     

def clientPlay1(touch):#my self
    touch = int(touch)
    global msg    
    global count,socker
    global useSlot,endGame
    print("clientPlay1")
    
    if touch == 99:#signal draw
        position = 0
        for element in msg:#find element not x,y
            if element.isnumeric()==True:
                (msg[int(position)]) = 'o'
                putSlot(int(position))
                check_CtoC(position)
                endGame = False
                break
            else:
                position +=1
        
    elif touch != 0:
        (msg[int(touch)-1]) = 'x'
        putSlot(int(touch))
        #====================================
        touch = str(touch)
    #====================================
    
    try:
        #s.send(touch.encode('ascii'))
        pass
    except ValueError:
        print("Server disconnect")
    except ConnectionAbortedError:
        print("Server disconnect") 
    except UnboundLocalError:
        print("Server disconnect")
    except ConnectionResetError:
        print("Server disconnect")
    print_table(msg)
    if touch!=99:
        check_CtoC(touch)
    
    print('endgame'+str(endGame))


def playWithClient():
    global endGame,opponent,socker,receiveMessage
    
    if endGame==False:
        print('endGame1')
        upDate()
        socker.close()
        default('CtoC')
    else:
        try:
            print('receiveMessage')
            print_table(msg)
            getMessage = bytes.decode(socker.recv(4096))#wait mess
            print('getMessage'+getMessage)
            onButton()
            if getMessage == '0':
                receiveMessage=0
            else:
                unZip = extract(getMessage)
                receiveMessage = unZip[1] #get num from opponent
                
                opponent = unZip[0] # get opponent's name
                #if receiveMessage == 'disconnected':
                #    socker.close()
                 #   default('CtoC')
                if receiveMessage == '99':#signal draw
                    position = 0
                    for element in msg:#find element not x,y
                        if element.isnumeric()==True:
                            number[int(position)]=' O '
                            putSlot(int(position))
                            print_table(msg)

                            upDate()
                            endGame = False
                            print ("   Draw !!!!!!!!!!!!!!")
                            socker.close()
                            default('CtoC')
                            break
                        else:
                            position +=1
                else:
                    number[int(receiveMessage)-1]=' O '
                upDate()
            print('lllllllllllllllllllll')
            print('getValue'+str(receiveMessage))
            statePlayer.set("Your turn")
            # print_table(msg)
        except ConnectionAbortedError:
            print('deny access')#full player in server wait server reset
            
        except ConnectionResetError:
            print("Server disconnected")
            endGame = False
            socker.close()
        
    
        if receiveMessage == 'disconnected':
            print(opponent+" : "+receiveMessage)
            endGame = False
            socker.close()
            
        else:
            print(str(receiveMessage)+'\n')
            clientPlay2(receiveMessage)
    
    
    


#OX CtoC code =======================================================================
#OX code =======================================================================
ip_recent = ''
port_recent = ''


numberToSend=0
count = 0
stateServer= StringVar()
statePlayer= StringVar()
def print_table(msg):
    #os.system("cls")
    print ("")
    print (" "+str(msg[0])+" | "+str(msg[1])+" | "+str(msg[2])+" ")
    print (" "+str(msg[3])+" | "+str(msg[4])+" | "+str(msg[5])+" ")
    print (" "+str(msg[6])+" | "+str(msg[7])+" | "+str(msg[8])+" ")
    print ("") 
def check():
    print("check")
    global count
    global msg
    global useSlot,c,allowButton
    if (msg[0] == msg[1]) and (msg[1] == msg[2]):     
        allowButton = False
        if (msg[0] == 'x'):
            print ("Client WIN !!!!!!!!!!!!!!")
            whoWin(1)            
        if (msg[0] == 'o'):
            print ("Server WIN !!!!!!!!!!!!!!")
            whoWin(2)
        count = 10  
        if whatRole == 1:
            s.close()
            playAgain() 
            default("Client")
        if whatRole == 2:
            c.close()   
            messagetry.set('')
            playAgain() 
            default("Server")   
    if (msg[3] == msg[4]) and (msg[4] == msg[5]):  
        allowButton = False      
        if (msg[3] == 'x'):
            print ("Client WIN !!!!!!!!!!!!!!")
            whoWin(1)
        if (msg[3] == 'o'):
            print ("Server WIN !!!!!!!!!!!!!!")
            whoWin(2)
        count = 10
        if whatRole == 1:
            s.close()
            playAgain() 
            default("Client")   
        if whatRole == 2:
            c.close()   
            messagetry.set('')
            playAgain() 
            default("Server")
    if (msg[6] == msg[7]) and (msg[7] == msg[8]):
        allowButton = False
        if (msg[6] == 'x'):
            print ("Client WIN !!!!!!!!!!!!!!")
            whoWin(1)            
        if (msg[6] == 'o'):
            print ("Server WIN !!!!!!!!!!!!!!")
            whoWin(2)
        count = 10  
        if whatRole == 1:
            s.close()
            messagetry.set('')
            playAgain()
            default("Client")   
        if whatRole == 2:
            c.close()   
            playAgain()
            default("Server")               
    if (msg[0] == msg[3]) and (msg[3] == msg[6]): 
        allowButton = False       
        if (msg[0] == 'x'):
            print ("Client WIN !!!!!!!!!!!!!!")
            whoWin(1)
        if (msg[0] == 'o'):
            print ("Server WIN !!!!!!!!!!!!!!")
            whoWin(2)
        count = 10    
        if whatRole == 1:
            s.close()
            playAgain()
            default("Client")   
        if whatRole == 2:
            c.close()   
            messagetry.set('')
            playAgain()
            default("Server")          
    if (msg[1] == msg[4]) and (msg[4] == msg[7]):
        allowButton = False
        if (msg[1] == 'x'):
            print ("Client WIN !!!!!!!!!!!!!!")
            whoWin(1)            
        if (msg[1] == 'o'):
            print ("Server WIN !!!!!!!!!!!!!!")
            whoWin(2)
        count = 10  
        if whatRole == 1:
            s.close()
            playAgain()
            default("Client")   
        if whatRole == 2:
            c.close()   
            messagetry.set('')
            playAgain()
            default("Server")       
    if (msg[2] == msg[5]) and (msg[5] == msg[8]): 
        allowButton = False       
        if (msg[2] == 'x'):
            print ("Client WIN !!!!!!!!!!!!!!")
            whoWin(1)
        if (msg[2] == 'o'):
            print ("Server WIN !!!!!!!!!!!!!!")
            whoWin(2)
        count = 10  
        if whatRole == 1:
            s.close()
            playAgain()
            default("Client")   
        if whatRole == 2:
            c.close()   
            messagetry.set('')
            playAgain()
            default("Server")    
    if (msg[0] == msg[4]) and (msg[4] == msg[8]):
        allowButton = False
        if (msg[0] == 'x'):
            print ("Client WIN !!!!!!!!!!!!!!")  
            whoWin(1)          
        if (msg[0] == 'o'):
            print ("Server WIN !!!!!!!!!!!!!!")
            whoWin(2)
        count = 10 
        if whatRole == 1:
            s.close()
            messagetry.set('')
            playAgain()
            default("Client")   
        if whatRole == 2:
            c.close()   
            playAgain()
            default("Server")                       
    if (msg[2] == msg[4]) and (msg[4] == msg[6]):
        allowButton = False
        if (msg[2] == 'x'):
            print ("Client WIN !!!!!!!!!!!!!!")
            whoWin(1)          
        if (msg[2] == 'o'):
            print ("Server WIN !!!!!!!!!!!!!!")
            whoWin(2)
        count = 10    
        if whatRole == 1:
            s.close()
            messagetry.set('')
            playAgain()
            default("Client")   
        if whatRole == 2:
            c.close()   
            playAgain()
            default("Server")     
            

def disConnected():
    print("disconnected call")
    if whatRole == 1:
        s.close()
        default("Client")   
        statePlayer.set("disconnected")
        actionWindow("Reconnect for play again.")
    if whatRole == 2:
        c.close()   
        default("Server")   
        statePlayer.set("disconnected")
        actionWindow("Reconnect for play again.")  


def clientPlay(tmp):
    print("clientPlay")
    global msg    
    global count
    global useSlot
    if whatRole == 1:
        count+=1
        print("Count"+str(count))
        (msg[int(tmp)-1]) = 'x'
        number[int(tmp)-1]=' X '
        print(number)
        upDate()
        #====================================AttributeError: 'int' object has no attribute 'encode'
        tmp = str(tmp)
        #====================================
        try:
            s.send(tmp.encode('ascii'))
        except ValueError:
            print("Server disconnect")
            statePlayer.set("Server disconnect")
            default("Client")
        except ConnectionAbortedError:
            print("Server disconnect") 
            statePlayer.set("Server disconnect")
            default("Client")
        except UnboundLocalError:
            print("Server disconnect")
            statePlayer.set("Server disconnect")
            default("Client")
        except ConnectionResetError:
            print("Server disconnect")
            statePlayer.set("Server disconnect")
            default("Client")
        except OSError:
            print("Server disconnect")
            statePlayer.set("Server disconnect")
            offButton()
            clearButton()
    elif whatRole == 2:
        count+=1
        print("Count"+str(count))
        if count== 10:      
            c.close()
            default("Server")
            offButton()
            btnSend["state"]= "disabled"
            count=0
        else:
            try:
                tmpS = c.recv(20)
                putSlot(int(tmpS))
                print(useSlot)
                (msg[int(tmpS)-1]) = 'o'
                number[int(tmpS)-1]=' O '
                print(number)
                upDate()
                
                onButton()
            except ValueError:
                print("ValueError")
                statePlayer.set("Client disconnect")
                default("Server")
            except ConnectionAbortedError:
                print("ConnectionAbortedErrort") 
                statePlayer.set("Client disconnect")
                default("Server")
            except UnboundLocalError:
                print("UnboundLocalError")
                statePlayer.set("Client disconnect")
                default("Server")
            except ConnectionResetError :
                print("ConnectionResetError")
                statePlayer.set("Client disconnect")
                default("Server")
    print_table(msg)
    check()
    print ("Please Wait !!!")  


def putSlot(index):
    print("putSlot call")
    global useSlot
    if useSlot[index-1] == '0':
        useSlot[index-1] = '1'
        return True
    else:
        return False

def whoWin(winner):
    print("whoWin call")
    if winner == 1:
        statePlayer.set("You win")
        #tryAgain()
    else:
        statePlayer.set("You lose")
        #tryAgain()

def serverPlay(tmp):
    print("serverPlay")
    global msg,unpredict,allowButton
    global count
    
    if whatRole == 1:
        count+=1
        print("Count"+str(count))
        if count== 10:
            s.close()
            default("Client")
            count=0
        else:    
            try:
                tmp = s.recv(20)
                if tmp == 'unknown':
                    statePlayer.set("pls check mode")
                    stateServer.set("pls check mode")
                    s.close()
                
                putSlot(int(tmp))
                print(useSlot)
                (msg[int(tmp)-1]) = 'o'
                number[int(tmp)-1]=' O '
                statePlayer.set("Your turn")
                print(number)
                upDate()
            except ValueError:
                 
                 s.close()

                 default('client')
                 stateServer.set('detect error')
                 unpredict =True
                 
            except ConnectionAbortedError:
                print("ConnectionAbortedError") 
            except UnboundLocalError:
                print("UnboundLocalError")
            except ConnectionResetError :
                print("ConnectionResetError")
            except OSError :
                print('OSError')
                unpredict =True
                allowButton = False
    elif whatRole == 2:
        count+=1
        print("Count"+str(count))
        if count== 10:
            c.close()
            default("Server")
            count=0
        else:
            (msg[int(tmp)-1]) = 'X'
        #====================================AttributeError: 'int' object has no attribute 'encode'
            tmp = str(tmp)
            print("###")
            print(useSlot)
            putSlot(int(tmp))
            number[int(tmp)-1]=' X '
            print(number)
            upDate()
            try:
                c.send(tmp.encode('ascii'))
                statePlayer.set("Your turn")
                clientPlay(0)
            except ValueError:
                print("Client disconnect")
            except ConnectionAbortedError:
                print("Client disconnect") 
            except UnboundLocalError:
                print("Client disconnect")
            except ConnectionResetError :
                print("Client disconnect")
    if unpredict==False:
        print_table(msg)
        if allowButton:
            print('<=====>')
            check()

#OX code =======================================================================
#Variable
name_Input = StringVar()
ip_Input = StringVar()
port_Input = StringVar()

text1 = StringVar()
text2 = StringVar()
text3 = StringVar()
text4 = StringVar()
text5 = StringVar()
text6 = StringVar()
text7 = StringVar()
text8 = StringVar()
text9 = StringVar()

changeModeLabel = StringVar()


def configMode():  
    print("configMode call")
    if configAllow == True:
        if whatRole==1:
            modeNow.set('Server')
            default('Server')
            btnConfig['text']='Server'
        elif whatRole==2:
            modeNow.set('Client')
            default('Client')
            btnConfig['text']='Client'
        elif whatRole==3:
            txtName.configure(state='disabled',disabledbackground='powder blue')
            btnClient['text']='On'
            if recentRole == 1:
                modeNow.set('Server')
                default('Server')
                btnConfig['text']='Server'
            elif recentRole == 2:
                modeNow.set('Client')
                default('Client')
                btnConfig['text']='Client'
    else:
        print("Not allow")

def changeModeClient():  
    print("changeModeClient call")
    if configAllow == True:
        if(btnClient['text']=='On'):
            default('CtoC')
            modeMainFrame.set('Client to Client')
            txtName.configure(state='normal')
            btnClient['text']='Off'
        elif(btnClient['text']=='Off'):
            txtName.configure(state='disabled',disabledbackground='powder blue')
            if recentRole == 1:
                default('Client')
            elif recentRole == 2:
                default('Server')
            btnClient['text']='On'
    else:
        print("Not allow")
    
configAllow = True
# def configuration():
#     print("configuration call")
#     global btnConfig,btnClient
#     def close():
#         changeModeLabel.set("")
#         made.destroy()
#     try:
#         made = Toplevel(root)
#         made.geometry('300x300')
#         made.title("Config")
#         made.configure(bg="powder blue")
#         fr1 = Frame(made,width=1600,height=400,bg="powder blue",relief=SUNKEN)
#         fr1.pack(side=TOP)
#         txtLabel=Label(fr1,font=('Microsoft YaHei Light',13,'bold'),text="Config",bg="powder blue")
#         txtLabel.grid(row=0,column=0)
#         fr2 = Frame(made,width=1600,height=400,bg="powder blue",relief=SUNKEN)
#         fr2.pack(side=TOP)
#         txtCh=Label(fr2,font=('Microsoft YaHei Light',13,'bold'),text="Mode\t",bg="powder blue")
#         txtCh.grid(row=0,column=0)
#         txtAir=Label(fr2,font=('Microsoft YaHei Light',13,'bold'),text="\n\n",bg="powder blue")
#         txtAir.grid(row=1,column=0)
#         txtCh2=Label(fr2,font=('Microsoft YaHei Light',13,'bold'),text="Client with Client\t",bg="powder blue")
#         txtCh2.grid(row=1,column=0)
#         if whatRole == 1:
#             btnConfig=Button(fr2,font=('Microsoft YaHei Light',11,'bold'),text='Server',command=configMode)
#             btnConfig.grid(row=0,column=1)
#             btnClient=Button(fr2,font=('Microsoft YaHei Light',11,'bold'),text='On',command=changeModeClient)
#             btnClient.grid(row=1,column=1)
#         elif whatRole == 2:
#             btnConfig=Button(fr2,font=('Microsoft YaHei Light',11,'bold'),text='Client',command=configMode)
#             btnConfig.grid(row=0,column=1)
#             btnClient=Button(fr2,font=('Microsoft YaHei Light',11,'bold'),text='On',command=changeModeClient)
#             btnClient.grid(row=1,column=1)
#         elif whatRole == 3:
#             if recentRole == 1:
#                 btnConfig=Button(fr2,font=('Microsoft YaHei Light',11,'bold'),text='Server',command=configMode)
#                 btnConfig.grid(row=0,column=1)
#             elif recentRole == 2:
#                 btnConfig=Button(fr2,font=('Microsoft YaHei Light',11,'bold'),text='Client',command=configMode)
#                 btnConfig.grid(row=0,column=1)
#             btnClient=Button(fr2,font=('Microsoft YaHei Light',11,'bold'),text='Off',command=changeModeClient)
#             btnClient.grid(row=1,column=1)
#         socket.AI_NUMERICSERV=Label(fr2,font=('Microsoft YaHei Light',11,'bold'),text='\n\n\n\n\n\n\n\n\n\n\n\n',bg='powder blue').grid(row=2,column=2)
#         btnClose=Button(fr2,font=('Microsoft YaHei Light',11,'bold'),text='close',command=close).grid(row=2,column=2)
#         made.mainloop()
#     except:
#         print('Tk exception')
allowServerSend = False

def hallOfFrame():
    global getdata,getStatic
    txtHall.delete("1.0","end")
    
    if exploreDataStatus:
        ranking = 0
        txtHall.insert(END,"Rank"+"\tName"+"\tRound"+"\tWin"+"\tLoss"+"\tDraw" + '\n')
        ranking = 0
        for played in getdata :
                bogie = TheTrain(getStatic[played])
                ranking += 1
                txtHall.insert(END,str(ranking)+'\t'+str(played)+'\t'+str(bogie[0]) +'\t'+ str(bogie[1]) +'\t'+ str(bogie[2]) +'\t'+ str(bogie[3]) + '\n')

    else:
        txtHall.insert(END,'No Data Detected')
    txtHall.configure(state='disabled')


#Default
def default(role):
    print("default call")
    hallOfFrame()
    # every global
    global ip_Input,port_Input,unpredict
    #global role
    # 1 = client
    # 2 = server
    global whatRole,count,chkTime,recentRole
    count=0
    #global client
    global msg,useSlot,operator,number,stateBtn,s,configAllow
    #global server
    global serversocket,c,addr,allowServerSend
    
    #global client to client 
    global endGame,ADDRESS,name,userName,state,socker,allowButton
    global opponent,myself
    unpredict =False
    allowButton = True
    if role == "Client":
        print("Client mode")
        whatRole = 1
        recentRole = whatRole
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        modeMainFrame.set('Client')
        modeNow.set('Server')
        txtName.configure(state='disabled',disabledbackground='powder blue')
    elif role =="Server":
        print("Server mode")
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        allowServerSend = False
        whatRole = 2
        recentRole = whatRole
        modeMainFrame.set('Server')
        modeNow.set('Client')
        txtName.configure(state='disabled',disabledbackground='powder blue')
    elif role == "CtoC":
        print("Server mode")
        socker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        whatRole = 3
        count=0
        endGame = True
        txtName.configure(state='normal')
        print("CtoC mode")
        
        
    clearButton()
    if chkTime == 1:
        ip_Input.set('')
        port_Input.set('')
    else:
        ip_Input.set(ip_recent)
        port_Input.set(port_recent)
    #index in table
    msg = ['1','2','3','4','5','6','7','8','9']
    #number = ['1','2','3','4','5','6','7','8','9']
    useSlot = ['0','0','0','0','0','0','0','0','0']
    operator = True
    number = ['    ','    ','    ','    ','    ','    ','    ','    ','    ']
    stateBtn=[False,False,False,False,False,False,False,False,False]
    onConnection()
    offButton()
    btnSend["state"]= "disabled"
    stateServer.set("Input Ip/Port")

def offConnection():
    print('offConnection')
    global configAllow
    txtIp["state"] = "disabled"
    txtPort["state"] = "disabled"
    btnStart["state"] = "disabled"
    txtName.configure(state='disabled',disabledbackground='powder blue')
    configAllow = False
    

def onConnection():
    print('onConnection')
    global configAllow
    txtIp["state"] = "normal"
    txtPort["state"] = "normal"
    btnStart["state"] = "normal"
    configAllow = True
    
def clearButton():
    text1.set('    ')
    text2.set('    ')
    text3.set('    ')
    text4.set('    ')
    text5.set('    ')
    text6.set('    ')
    text7.set('    ')
    text8.set('    ')
    text9.set('    ')

def offButton():
    print('offButton')
    btn1["state"] = "disabled"
    btn1.configure(bg="#49A")
    btn2["state"] = "disabled"
    btn2.configure(bg="#49A")
    btn3["state"] = "disabled"
    btn3.configure(bg="#49A")
    btn4["state"] = "disabled"
    btn4.configure(bg="#49A")
    btn5["state"] = "disabled"
    btn5.configure(bg="#49A")
    btn6["state"] = "disabled"
    btn6.configure(bg="#49A")
    btn7["state"] = "disabled"
    btn7.configure(bg="#49A")
    btn8["state"] = "disabled"
    btn8.configure(bg="#49A")
    btn9["state"] = "disabled"
    btn9.configure(bg="#49A")
    return 0
    
def onButton():
    print('onButton')
    btn1["state"] = "normal"
    btn1.configure(bg="Green")
    btn2["state"] = "normal"
    btn2.configure(bg="Green")
    btn3["state"] = "normal"
    btn3.configure(bg="Green")
    btn4["state"] = "normal"
    btn4.configure(bg="Green")
    btn5["state"] = "normal"
    btn5.configure(bg="Green")
    btn6["state"] = "normal"
    btn6.configure(bg="Green")
    btn7["state"] = "normal"
    btn7.configure(bg="Green")
    btn8["state"] = "normal"
    btn8.configure(bg="Green")
    btn9["state"] = "normal"
    btn9.configure(bg="Green")
    return 0 


def communication():
    print('communication call')
    global numberToSend,count,allowServerSend,endGame,unpredict
    if whatRole == 1:
        if count== 10:
            s.close()
            default("Client")
            count=0
        else:
            clientPlay(numberToSend)#server -1 แล้ว
            serverPlay(numberToSend)
            if unpredict==False:
                onButton()
    elif whatRole == 2:
        if count== 10:
            c.close()
            default("Server")
            count=0
        else:
            onButton()
            if allowServerSend == False:
                clientPlay(numberToSend)#server -1 แล้ว
                
            else:
                
                serverPlay(numberToSend)
                allowServerSend = False
    elif whatRole == 3:
        print('role 3')
        if endGame:#=================================================================
            try:
                sendMessage =  numberToSend
                print('sendMessage'+str(sendMessage))
                count+=1
                clientPlay1(sendMessage)
                if endGame:
                    sendMessage = str(sendMessage)
                    socker.send(str.encode(sendMessage))
            
            except:
                print("Server disconnected")
                endGame = False
                socker.close()
        playWithClient()
    
    btnSend["state"]= "disabled"
def upDate():
    print("update call")
    text1.set(number[0])
    text2.set(number[1])
    text3.set(number[2])
    text4.set(number[3])
    text5.set(number[4])
    text6.set(number[5])
    text7.set(number[6])
    text8.set(number[7])
    text9.set(number[8])         

def btnClick(numbers):
    print("btnClick call num = "+str(numbers))
    global operator,numberToSend,allowServerSend,count
    numberToSend = numbers
    if whatRole == 1:
        if count== 10:
            s.close()
            default("Client")
            count=0
        else:
            if stateBtn[numbers-1]==False:
                if putSlot(numbers)==False:
                    print("used")
                    statePlayer.set("select another")
                else:
                    stateBtn[numbers-1]=True
                    operator = True   
                    statePlayer.set("Wait server")
                    number[int(numbers)-1]=' X '
                    upDate()
                    offButton()
                    btnSend["state"]= "normal"
    elif whatRole == 2:
        if count== 9:
           
            c.close()
            default("Server")
            offButton()
            btnSend["state"]= "disabled"
            count=0
        else:
            if stateBtn[numbers-1]==False:
                if putSlot(numbers)==False:
                    print("used")
                    statePlayer.set("select another")
                else:
                    stateBtn[numbers-1]=True
                    operator = True   
                    statePlayer.set("Wait Client")
                    number[int(numbers)-1]=' X '
                    upDate()
                    offButton()
                    btnSend["state"]= "normal"
                    allowServerSend = True
    elif whatRole == 3:
       statePlayer.set("wait opponent")
       if stateBtn[numbers-1]==False:
        if putSlot(numbers)==False:
            print("used")
            statePlayer.set("select another")
        else:
            stateBtn[numbers-1]=True
            operator = True   
            number[int(numbers)-1]=' X '
            upDate()
            offButton()
            btnSend["state"]= "normal"
            allowServerSend = True
def playAgain():
    pass

def getRecent():
    print("ip:"+str(ip_recent))
    print("port:"+str(port_recent))


def closeGame():
    End = tkinter.messagebox.askyesno("TIC TAC TOE","Confirm exit")
    if End > 0:
        root.destroy()
        return              
def tryAgain():
    pass        


def actionWindow(whatAction):
    print("actionWindow call")
    top = Toplevel(root) 
    top.geometry("500x200")
    l2 = Label(top,padx=16,pady=16,bd=8,fg="black",
            font=font1, text = whatAction) 
    l2.pack()
    top.mainloop()  

    
def getStart(playTime):
    print('getStart call:'+ str(playTime))
    global c,addr,ip_recent,port_recent,chkTime
    chkTime = playTime
    global myself,opponent
    firstTime = True if playTime == 1 else False
    
    if (len(ip_Input.get())==0 or len(port_Input.get())==0) and firstTime:
        actionWindow("ip/port error")
    else:
        if whatRole == 1:
            try:
                if playTime == 1:
                    server = ip_Input.get()
                    port = int(port_Input.get())
                    if port >1025 and port < 65535:
                        try:
                            connected = False  
                            passConnect = False
                            #s.connect((server, port))
                            tryToConnect = 0
                            while not connected:  
                            # attempt to reconnect, otherwise sleep for 2 seconds  
                                try:  

                                    s.connect((server, port))
                                    connected = True 
                                    passConnect =  connected
                                    print( "re-connection successful" )  
                                except socket.error: 
                                    stateServer.set("try to connect")
                                    print( "connect failed" )   
                                    tryToConnect+=1
                                    print(tryToConnect)
                                    if tryToConnect == 3:
                                        s.close()
                                        connected = True 
                                        passConnect = False
                                        stateServer.set('re-open this mode')
                                except TypeError:
                                    stateServer.set('invalid input')

                            if passConnect:  
                                onButton()
                                offConnection()
                                stateServer.set("Welcome to XO Game")
                                statePlayer.set("Your turn")
                        except TimeoutError:
                            stateServer.set("Server not response")
                            print("TimeoutError")
                            actionWindow("ip/port error")
                        except ConnectionRefusedError:
                            stateServer.set("Server not response")
                            print("ConnectionRefusedError ")
                            actionWindow("ip/port error")
                        except ConnectionResetError :
                            stateServer.set("Server not response")
                            print("ConnectionResetError")
                            actionWindow("ip/port error")
                        except OSError:
                            stateServer.set("Server not response")
                            print("OSError")
                            actionWindow("ip/port error")
                        
                        except UnboundLocalError:
                            stateServer.set("Server not response")
                            print("UnboundLocalError ")
                            actionWindow("ip/port error")
                        
                    else:
                        stateServer.set("invalid input")
            except TypeError:
                stateServer.set("invalid input")
            except ValueError:
                stateServer.set("invalid input")
            
            
        elif whatRole == 2:
           
                if playTime == 1:
                    ip = ip_Input.get()
                    port = int(port_Input.get())
                    if port <1025 or port > 65535:
                        port = "x"

                    try:
                        ip = ip_Input.get()
                        port = int(port_Input.get())
                        ip_recent = ip_Input.get()
                        port_recent = port_Input.get()
                    except TypeError:
                        stateServer.set("invalid input")

                        
                      
                    try:
                        serversocket.bind((ip, port))
                        serversocket.listen(5)
                        c,addr = serversocket.accept()
                        offButton()
                        offConnection()
                        stateServer.set("Welcome to XO Game")
                        statePlayer.set("your turn")
                        clientPlay(0)
                
                    except TimeoutError:
                        stateServer.set("ip/port error")
                        print("TimeoutError")
                        actionWindow("ip/port error")
                    except ConnectionRefusedError:
                        stateServer.set("ip/port error")
                        print("ConnectionRefusedError ")
                        actionWindow("ip/port error")
                    except ConnectionResetError :
                        stateServer.set("ip/port error")
                        print("ConnectionResetError")
                        actionWindow("ip/port error")
                    except OSError:
                        stateServer.set("ip/port error")
                        print("OSError")
                        actionWindow("ip/port error")
        if whatRole == 3:
            server = ip_Input.get()
            port = int(port_Input.get())
            nameOfPlayer = name_Input.get()
            if len(nameOfPlayer)==1 and nameOfPlayer.isnumeric():
                print('forbidden')
                name_Input.set("")
                nameOfPlayer=""
                allowPlay = False
                actionWindow("Name can't 1 number")
            else:
                for scan in nameOfPlayer:
                    if scan =='[' or scan == ']' or scan == '{' or scan == '}':
                        print('forbidden')
                        name_Input.set("")
                        nameOfPlayer=""
                        allowPlay = False
                        actionWindow("Name can't contain [ ] or {""}")
                    else:
                        print('Allow Connect')
                        allowPlay = True
                if allowPlay:
            
                    try:
                        ADDRESS = (server,port)
                        socker.connect(ADDRESS)
                        statePlayer.set("Your turn")
                        print('pass')
                    except:
                        print('reconect')
                    else:
                        print('end connecting')
                        
                    try:
                        messageFromServer = bytes.decode(socker.recv(4096))
                        print('messageFromServer'+str(messageFromServer))
                        name = nameOfPlayer
                        myself = nameOfPlayer
                        userName = str.encode(name)
                        state_CtoC = True
                        socker.send(userName)
                        offButton()
                        offConnection()
                    except ConnectionResetError:
                        print("Server disconnected")
                        state_CtoC = False
                    except OSError:
                        stateServer.set("Pls re-open this mode")
                        print("OSError ")
                        state_CtoC = False
                    if state_CtoC:
                        playWithClient()
            
    
#==========================Fonts==========================================
#font.Font(family='Helvetica', size=12, weight='bold')
font1 = TkFont.Font(family="Microsoft YaHei Light",size = 20,weight = 'bold')

#===============================Calculator Frame===========================
txtDisplayState = Label(f2,font=font1,
                text="State",fg="Blue",bd=10,anchor='w',bg='powder blue')


txtDisplayState.grid(columnspan=4)
txtDisplay = Entry(f2,font=font1,
                   textvariable=statePlayer,bd=30,insertwidth=4,
                   bg="#49A",justify='right',state='disabled',disabledbackground='powder blue')
txtDisplay.grid(columnspan=4)



#=======================================================================================================
whatRole = 1
fr1 = Frame(f0a,width=10,height=10,bg="powder blue",relief=SUNKEN)
fr1.grid(row=0,column=1)
fr2 = Frame(f0a,width=10,height=10,bg="powder blue",relief=SUNKEN)
fr2.grid(row=1,column=1)


if whatRole == 1:
    btnConfig=Button(fr1,font=('Microsoft YaHei Light',11,'bold'),text='Server',command=lambda:configMode())
    btnConfig.grid(row=0,column=1)
    
    
    txtEmpty=Label(fr2,font=('Microsoft YaHei Light',13,'bold'),text="",bg="powder blue")
    txtEmpty.grid(row=0,column=1)

    btnClient=Button(fr2,font=('Microsoft YaHei Light',11,'bold'),text='On',command=lambda:changeModeClient())
    btnClient.grid(row=1,column=1)
    
elif whatRole == 2:
    btnConfig=Button(fr1,font=('Microsoft YaHei Light',11,'bold'),text='Client',command=lambda:configMode())
    btnConfig.grid(row=0,column=1)

    txtEmpty=Label(fr2,font=('Microsoft YaHei Light',13,'bold'),text="",bg="powder blue")
    txtEmpty.grid(row=0,column=1)

    btnClient=Button(fr2,font=('Microsoft YaHei Light',11,'bold'),text='On',command=lambda:changeModeClient())
    btnClient.grid(row=1,column=1)
elif whatRole == 3:
    if recentRole == 1:
        btnConfig=Button(fr2,font=('Microsoft YaHei Light',11,'bold'),text='Server',command=lambda:configMode())
        btnConfig.grid(row=0,column=1)
    elif recentRole == 2:
        btnConfig=Button(fr2,font=('Microsoft YaHei Light',11,'bold'),text='Client',command=lambda:configMode())
        btnConfig.grid(row=0,column=1)
    btnClient=Button(fr2,font=('Microsoft YaHei Light',11,'bold'),text='Off',command=lambda:changeModeClient())
    btnClient.grid(row=1,column=1)


#=======================================================================================================





btnWidth = 5
btnHeight = 1

#===============================Row5=======================================
btn1 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text1,width=btnWidth,
              height=btnHeight,
              bg="#49A",command=lambda:btnClick(1))
btn1.grid(row=3,column=0)

btn2 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text2,width=btnWidth,
              height=btnHeight,bg="#49A",command=lambda:btnClick(2))
btn2.grid(row=3,column=1)

btn3 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text3,width=btnWidth,
              height=btnHeight,bg="#49A",command=lambda:btnClick(3))
btn3.grid(row=3,column=2)
#===============================Row4=======================================
btn4 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text4,width=btnWidth,
              height=btnHeight,bg="#49A",command=lambda:btnClick(4))
btn4.grid(row=4,column=0)

btn5 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text5,width=btnWidth,
              height=btnHeight,bg="#49A",command=lambda:btnClick(5))
btn5.grid(row=4,column=1)

btn6 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text6,width=btnWidth,
              height=btnHeight,bg="#49A",command=lambda:btnClick(6))
btn6.grid(row=4,column=2)

#===============================Row3=======================================

btn7 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text7,width=btnWidth,
              height=btnHeight,bg="#49A",command=lambda:btnClick(7))
btn7.grid(row=5,column=0)

btn8 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text8,width=btnWidth,
              height=btnHeight,bg="#49A",command=lambda:btnClick(8))
btn8.grid(row=5,column=1)

btn9 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text9,width=btnWidth,
              height=btnHeight,bg="#49A",command=lambda:btnClick(9))
btn9.grid(row=5,column=2)

btnSend = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              text="SEND",width=23,
              height=btnHeight,bg="#49A",command=communication)
btnSend.grid(row=6,columnspan=3)

offButton()

lblReference = Label(f1,font=font1, text="State",
                     bd=16,anchor='w',bg="powder blue").grid(row=0,column=0)  
txtReference = Entry(f1,font=font1,textvariable=stateServer,
                     bd=10,insertwidth=4,bg='#49A',justify='right',state='disabled',disabledbackground='powder blue').grid(row=0,column=1)

#-----------------------------------------------------------------------------------------------------
lblIp = Label(f1,font=font1, text="ip"
                 ,bd=16,anchor='w',bg="powder blue").grid(row=1,column=0)  
txtIp = Entry(f1,font=font1,textvariable=ip_Input,
                     bd=10,insertwidth=4,bg='white',justify='right')
txtIp.grid(row=1,column=1)

#-----------------------------------------------------------------------------------------------------
lblPort = Label(f1,font=font1, text="port"
                 ,bd=16,anchor='w',bg="powder blue").grid(row=2,column=0)  
txtPort = Entry(f1,font=font1,textvariable=port_Input,
                     bd=10,insertwidth=4,bg='white',justify='right')
txtPort.grid(row=2,column=1)  

lblName = Label(f1,font=font1, text="Name"
                 ,bd=16,anchor='w',bg="powder blue").grid(row=3,column=0)  
txtName = Entry(f1,font=font1,textvariable=name_Input,
                     bd=10,insertwidth=4,bg='white',justify='right')
txtName.grid(row=3,column=1)  



btnStart = Button(f1,padx=16,pady=16,bd=16,fg="black",font=font1,
                  width=10,text="Connect",bg="#49A",command=lambda:getStart(1))
btnStart.grid(row=7,column=1)
btnTry = Button(f1,padx=16,pady=16,bd=16,fg="black",font=font1,
                  width=5,text="Exit",bg="#49A",command=closeGame)
btnTry.grid(row=8,column=1)
menubar= Menu(root)
filemenu = Menu(menubar, tearoff =0,font= 'Helvetica 30 bold')
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="End",command=disConnected)
filemenu.add_command(label="Exit", command = closeGame)
root.config(menu=menubar)
root.attributes('-fullscreen', True)  
#root.resizable(False,False)
hallOfFrame()
default("Client")
root.mainloop()  
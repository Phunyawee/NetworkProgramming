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
from turtle import update
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
                text="Client",fg="Blue",bd=10,background='powder blue')
lblRole.grid(row=1,column=0)
#bank zone
#===============================================================
f0a = Frame(Tops,bg="powder blue",relief=SUNKEN)
f0a.grid(row=0,column=1)
lblAir = Label(f0a,font=('Microsoft YaHei Light',50,'bold'),
                text="\t     ",fg="Blue",bd=10,background='powder blue')
lblAir.grid(row=0,column=0)
lblAir2 = Label(f0a,font=('Microsoft YaHei Light',40,'bold'),
                text="\t     ",fg="Blue",bd=10,background='powder blue')
lblAir2.grid(row=1,column=0)
#===============================================================
#hall
f0b = Frame(Tops,bg="powder blue",relief=SUNKEN)
f0b.grid(row=0,column=2)

lblHall = Label(f0b,font=('Microsoft YaHei Light',50,'bold'),
                text="Hall of frame",fg="Blue",bd=10,background='powder blue')
lblHall.grid(row=0,column=0)
lblHall2 = Label(f0b,font=('Microsoft YaHei Light',40,'bold'),
                text="Client",fg="Blue",bd=10,background='powder blue')
lblHall2.grid(row=1,column=0)





# lblInfo3 = Label(f0,font=('Microsoft YaHei Light',50,'bold'),
#                 text="\t\t",fg="Blue",bd=10)
# lblInfo3.grid(row=0,column=2)
# lblRole3 = Label(f0,font=('Microsoft YaHei Light',40,'bold'),
#                 text="\t\t",fg="Blue",bd=10)
# lblRole3.grid(row=1,column=2)


Bottoms = Frame(root,width=1600,bg="powder blue",relief=SUNKEN)
Bottoms.pack(side=BOTTOM)

f1 = Frame(Bottoms,width=800,height=700,bg="",relief=SUNKEN)
#f1.pack(side=LEFT)
f1.grid(row=1,column=1)

f2 = Frame(Bottoms,width=600,height=700,relief=SUNKEN)
#f2.pack(side=LEFT)
#f2.pack(side=RIGHT)
f2.grid(row=1,column=2)
f2.configure(background='powder blue')
f3 = Frame(Bottoms,width=500,height=700,relief=SUNKEN)
#f3.pack(side=RIGHT)
f3.grid(row=1,column=3)
lblInfox = Label(f3,font=('Microsoft YaHei Light',50,'bold'),
                text="TIC-TAC-TOE",fg="Blue",bd=10,anchor='w')
lblInfox.grid(row=0,column=0)
lblRolex = Label(f3,font=('Microsoft YaHei Light',40,'bold'),
                textvariable=modeMainFrame,fg="Blue",bd=10,anchor='w')
lblRolex.grid(row=1,column=0)

#f2.pack(side=RIGHT)
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
#tool>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#OX CtoC code =======================================================================

def EndGame(touch):
    global endGame,count,socker
    endGame = False
   # sendMessage = str(touch)
    socker.send(str.encode(str(touch)))
    socker.close()

def check_CtoC(touch):
    global count
    global msg
    global useSlot,endGame,opponent,myself
    count=0
    for i in msg:
        if i.isnumeric()==False:
            count+=1
            if count == 9:
                print ("   Draw !!!!!!!!!!!!!!")
                EndGame(99)#sp case
                default("CtoC")
        else:
            count = 0
    #print('turn: '+str(count))
    if (msg[0] == msg[1]) and (msg[1] == msg[2]):         
        if (msg[0] == 'x'):
            print (str(myself)+"   WIN !!!!!!!!!!!!!!")    
            EndGame(touch)
        if (msg[0] == 'o'):
            print (str(opponent)+"   WIN !!!!!!!!!!!!!!")
            EndGame(0)
        default("CtoC")
        
                     
    if (msg[3] == msg[4]) and (msg[4] == msg[5]):        
        if (msg[3] == 'x'):
            print (str(myself)+"   WIN !!!!!!!!!!!!!!")
            EndGame(touch)
        if (msg[3] == 'o'):
            print (str(opponent)+"   WIN !!!!!!!!!!!!!!")
            EndGame(0)
        default("CtoC")
    if (msg[6] == msg[7]) and (msg[7] == msg[8]):
        if (msg[6] == 'x'):
            print (str(myself)+"   WIN !!!!!!!!!!!!!!")
            EndGame(touch) 
        if (msg[6] == 'o'):
            print (str(opponent)+"   WIN !!!!!!!!!!!!!!")
            EndGame(0)
        default("CtoC")
    if (msg[0] == msg[3]) and (msg[3] == msg[6]):        
        if (msg[0] == 'x'):
            print (str(myself)+"   WIN !!!!!!!!!!!!!!")
            EndGame(touch)  
        if (msg[0] == 'o'):
            print (str(opponent)+"   WIN !!!!!!!!!!!!!!")
            EndGame(0)
        default("CtoC")
    if (msg[1] == msg[4]) and (msg[4] == msg[7]):
        if (msg[1] == 'x'):
            print (str(myself)+"   WIN !!!!!!!!!!!!!!")  
            EndGame(touch)  
        if (msg[1] == 'o'):
            print (str(opponent)+"   WIN !!!!!!!!!!!!!!")
            EndGame(0)  
        default("CtoC")
    if (msg[2] == msg[5]) and (msg[5] == msg[8]):        
        if (msg[2] == 'x'):
            print (str(myself)+"   WIN !!!!!!!!!!!!!!")
            EndGame(touch)
        if (msg[2] == 'o'):
            print (str(opponent)+"   WIN !!!!!!!!!!!!!!")
            EndGame(0)
        default("CtoC")
    if (msg[0] == msg[4]) and (msg[4] == msg[8]):
        if (msg[0] == 'x'):
            print (str(myself)+"   WIN !!!!!!!!!!!!!!")
            EndGame(touch)
        if (msg[0] == 'o'):
            print (str(opponent)+"   WIN !!!!!!!!!!!!!!")
            EndGame(0)
        default("CtoC")
    if (msg[2] == msg[4]) and (msg[4] == msg[6]):
        if (msg[2] == 'x'):
            print (str(myself)+"   WIN !!!!!!!!!!!!!!")    
            EndGame(touch)  
        if (msg[2] == 'o'):
            print (str(opponent)+"   WIN !!!!!!!!!!!!!!")
            EndGame(0)
        default("CtoC")
                        





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
                (msg[int(position)]) = 'x'
                putSlot(int(position))
                endGame = False
                print ("   Draw !!!!!!!!!!!!!!")
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
    global endGame,opponent,socker
    
    if endGame==False:
        print('endGame1')
        upDate()
        socker.close()
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
    global useSlot,c
    if (msg[0] == msg[1]) and (msg[1] == msg[2]):         
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
    global msg
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
                putSlot(int(tmp))
                print(useSlot)
                (msg[int(tmp)-1]) = 'o'
                number[int(tmp)-1]=' O '
                statePlayer.set("Your turn")
                print(number)
                upDate()
            except ValueError:
                print("ValueError")
            except ConnectionAbortedError:
                print("ConnectionAbortedError") 
            except UnboundLocalError:
                print("UnboundLocalError")
            except ConnectionResetError :
                print("ConnectionResetError")
            except OSError :
                print("OSError")
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
        
    print_table(msg)
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
def configuration():
    print("configuration call")
    global btnConfig,btnClient
    def close():
        changeModeLabel.set("")
        made.destroy()
    try:
        made = Toplevel(root)
        made.geometry('300x300')
        made.title("Config")
        made.configure(bg="powder blue")
        fr1 = Frame(made,width=1600,height=400,bg="powder blue",relief=SUNKEN)
        fr1.pack(side=TOP)
        txtLabel=Label(fr1,font=('Microsoft YaHei Light',13,'bold'),text="Config",bg="powder blue")
        txtLabel.grid(row=0,column=0)
        fr2 = Frame(made,width=1600,height=400,bg="powder blue",relief=SUNKEN)
        fr2.pack(side=TOP)
        txtCh=Label(fr2,font=('Microsoft YaHei Light',13,'bold'),text="Mode\t",bg="powder blue")
        txtCh.grid(row=0,column=0)
        txtAir=Label(fr2,font=('Microsoft YaHei Light',13,'bold'),text="\n\n",bg="powder blue")
        txtAir.grid(row=1,column=0)
        txtCh2=Label(fr2,font=('Microsoft YaHei Light',13,'bold'),text="Client with Client\t",bg="powder blue")
        txtCh2.grid(row=1,column=0)
        if whatRole == 1:

            btnConfig=Button(fr2,font=('Microsoft YaHei Light',11,'bold'),text='Server',command=configMode)
            btnConfig.grid(row=0,column=1)
            btnClient=Button(fr2,font=('Microsoft YaHei Light',11,'bold'),text='On',command=changeModeClient)
            btnClient.grid(row=1,column=1)
        elif whatRole == 2:
            btnConfig=Button(fr2,font=('Microsoft YaHei Light',11,'bold'),text='Client',command=configMode)
            btnConfig.grid(row=0,column=1)
            btnClient=Button(fr2,font=('Microsoft YaHei Light',11,'bold'),text='On',command=changeModeClient)
            btnClient.grid(row=1,column=1)
        elif whatRole == 3:
            if recentRole == 1:
                btnConfig=Button(fr2,font=('Microsoft YaHei Light',11,'bold'),text='Server',command=configMode)
                btnConfig.grid(row=0,column=1)
            elif recentRole == 2:
                btnConfig=Button(fr2,font=('Microsoft YaHei Light',11,'bold'),text='Client',command=configMode)
                btnConfig.grid(row=0,column=1)
            btnClient=Button(fr2,font=('Microsoft YaHei Light',11,'bold'),text='Off',command=changeModeClient)
            btnClient.grid(row=1,column=1)
        btnClose=Button(fr2,font=('Microsoft YaHei Light',11,'bold'),text='close',command=close).pack(side=BOTTOM)
        made.mainloop()
    except:
        print('Tk exception')
allowServerSend = False
#Default
def default(role):
    print("default call")
    # every global
    global ip_Input,port_Input
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
    global endGame,ADDRESS,name,userName,state,socker
    global opponent,myself
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
        
        
    text1.set('    ')
    text2.set('    ')
    text3.set('    ')
    text4.set('    ')
    text5.set('    ')
    text6.set('    ')
    text7.set('    ')
    text8.set('    ')
    text9.set('    ')
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
    


def offButton():
    print('offButton')
    btn1["state"] = "disabled"
    btn2["state"] = "disabled"
    btn3["state"] = "disabled"
    btn4["state"] = "disabled"
    btn5["state"] = "disabled"
    btn6["state"] = "disabled"
    btn7["state"] = "disabled"
    btn8["state"] = "disabled"
    btn9["state"] = "disabled"
    return 0
    
def onButton():
    print('onButton')
    btn1["state"] = "normal"
    btn2["state"] = "normal"
    btn3["state"] = "normal"
    btn4["state"] = "normal"
    btn5["state"] = "normal"
    btn6["state"] = "normal"
    btn7["state"] = "normal"
    btn8["state"] = "normal"
    btn9["state"] = "normal"
    return 0 


def communication():
    print('communication call')
    global numberToSend,count,allowServerSend,endGame
    if whatRole == 1:
        if count== 10:
            s.close()
            default("Client")
            count=0
        else:
            clientPlay(numberToSend)#server -1 แล้ว
            serverPlay(numberToSend)
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
                    ip_recent = ip_Input.get()
                    port_recent = port_Input.get()
                elif playTime == 2:
                    time.sleep(10)
                    server = ip_recent
                    port = int(port_recent)
                    ip_Input.set(server)
                    port_Input.set(port_recent)
                    default("Client")
            except ValueError:
                stateServer.set("Server not response")
            try:
                connected = False  
                #s.connect((server, port))
                while not connected:  
                # attempt to reconnect, otherwise sleep for 2 seconds  
                    try:  
                        s.connect((server, port))
                        connected = True  
                        print( "re-connection successful" )  
                    except socket.error: 
                        stateServer.set("try to connect")
                        print( "connect failed" )   
                        time.sleep(2)
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
            
        elif whatRole == 2:
            try:
                if playTime == 1:
                    ip = ip_Input.get()
                    port = int(port_Input.get())
                    ip_recent = ip_Input.get()
                    port_recent = int(port_Input.get())
                elif playTime == 2:
                    ip = ip_recent
                    port = port_recent
                    ip_Input.set(ip)
                    port_Input.set(port)
                    default("Server")
                serversocket.bind((ip, port))
                serversocket.listen(5)
            except ValueError:
                stateServer.set("Server not response")
            try:
                c,addr = serversocket.accept()
                offButton()
                offConnection()
                stateServer.set("Welcome to XO Game")
                statePlayer.set("your turn")
                clientPlay(0)
                #upDate()
                #onButton()
            # sentToServer()
            except TimeoutError:
                stateServer.set("Client not response")
                print("TimeoutError")
                actionWindow("ip/port error")
            except ConnectionRefusedError:
                stateServer.set("Client not response")
                print("ConnectionRefusedError ")
                actionWindow("ip/port error")
            except ConnectionResetError :
                stateServer.set("Client not response")
                print("ConnectionResetError")
                actionWindow("ip/port error")
            except OSError:
                stateServer.set("Client not response")
                print("OSError")
                actionWindow("ip/port error")
        if whatRole == 3:
            server = ip_Input.get()
            port = int(port_Input.get())
            nameOfPlayer = name_Input.get()
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
                
            #print("Name: "+nameOfPlayer)
            
        # except UnboundLocalError:
            #  stateServer.set("Client not response")
            #  print("UnboundLocalError ")
            # actionWindow("ip/port error")
    
    
#==========================Fonts==========================================
#font.Font(family='Helvetica', size=12, weight='bold')
font1 = TkFont.Font(family="Microsoft YaHei Light",size = 20,weight = 'bold')

#===============================Calculator Frame===========================
txtDisplayState = Label(f2,font=font1,
                text="State",fg="Blue",bd=10,anchor='w')


txtDisplayState.grid(columnspan=4)
txtDisplay = Entry(f2,font=font1,
                   textvariable=statePlayer,bd=30,insertwidth=4,
                   bg="#49A",justify='right',state='disabled',disabledbackground='powder blue')
txtDisplay.grid(columnspan=4)

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
filemenu.add_command(label="Config",command=configuration)
filemenu.add_command(label="test",command=playAgain)
filemenu.add_command(label="End",command=disConnected)
filemenu.add_command(label="Exit", command = closeGame)
root.config(menu=menubar)
#root.attributes('-fullscreen', True)  
#root.resizable(False,False)
default("Client")
root.mainloop()  
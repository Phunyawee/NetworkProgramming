from ast import Num
from http import server
from stat import filemode
from tkinter import *
import tkinter.font as TkFont
from tkinter import StringVar
import tkinter.messagebox
import socket
import time
#Client
root = Tk()
root.geometry("1600x800+0+0")
#root.attributes('-fullscreen', True)  
root.title("Tic-tac-toe")

Tops = Frame(root,width=1600,height=50,bg="powder blue",relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root,width=300,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

modeNow = StringVar()

#label
lblInfo = Label(Tops,font=('TH Sarabun New',50,'bold'),
                text="Tic-tac-toe",fg="Blue",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
lblRole = Label(Tops,font=('TH Sarabun New',40,'bold'),
                textvariable=modeNow,fg="Blue",bd=10,anchor='w')
lblRole.grid(row=1,column=0)
#OX code =======================================================================
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
    global count
    global msg
    global useSlot
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
            default("Client")   
            actionWindow("Reconnect for play again.")
        if whatRole == 2:
            c.close()   
            default("Server")   
            actionWindow("Reconnect for play again.")
                         
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
            default("Client")   
            actionWindow("Reconnect for play again.")
        if whatRole == 2:
            c.close()   
            default("Server")   
            actionWindow("Reconnect for play again.")  
                 
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
            default("Client")   
            actionWindow("Reconnect for play again.")
        if whatRole == 2:
            c.close()   
            default("Server")   
            actionWindow("Reconnect for play again.")       
                           
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
            default("Client")   
            actionWindow("Reconnect for play again.")
        if whatRole == 2:
            c.close()   
            default("Server")   
            actionWindow("Reconnect for play again.")   
                         
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
            default("Client")   
            actionWindow("Reconnect for play again.")
        if whatRole == 2:
            c.close()   
            default("Server")   
            actionWindow("Reconnect for play again.")     
             
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
            default("Client")   
            actionWindow("Reconnect for play again.")
        if whatRole == 2:
            c.close()   
            default("Server")   
            actionWindow("Reconnect for play again.")    
                       

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
            default("Client")   
            actionWindow("Reconnect for play again.")
        if whatRole == 2:
            c.close()   
            default("Server")   
            actionWindow("Reconnect for play again.")      
                         
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
            default("Client")   
            actionWindow("Reconnect for play again.")
        if whatRole == 2:
            c.close()   
            default("Server")   
            actionWindow("Reconnect for play again.")  

def disConnected():
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

    
    #print_table(msg)
    #====================================
    #====================================
    
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
            print("Client disconnect")
            statePlayer.set("Client disconnect")
            default("Server")
        except ConnectionAbortedError:
            print("Client disconnect") 
            statePlayer.set("Client disconnect")
            default("Server")
        except UnboundLocalError:
            print("Client disconnect")
            statePlayer.set("Client disconnect")
            default("Server")
        except ConnectionResetError :
            print("Client disconnect")
            statePlayer.set("Client disconnect")
            default("Server")
    print_table(msg)
    check()
    print ("Please Wait !!!")  


def putSlot(index):
    global useSlot
    if useSlot[index-1] == '0':
        useSlot[index-1] = '1'
        return True
    else:
        return False





def whoWin(winner):
    if winner == 1:
        statePlayer.set("You win")
    else:
        statePlayer.set("You lose")

def serverPlay(tmp):
    print("serverPlay")
    global msg
    global count
    if whatRole == 1:
        count+=1
        print("Count"+str(count))
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
            
            
            statePlayer.set("Wait Client")
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
    if configAllow == True:
        if(btnConfig['text']=='Server'):
            btnConfig['text']='Client'
            modeNow.set('Client')
            default('Client')
            #default()
        else:
            btnConfig['text']='Server'
            modeNow.set('Server')
            default('Server')
            #default()
    else:
        print("Not allow")

    
configAllow = True
def configuration():
    
    global btnConfig
    def close():
        changeModeLabel.set("")
        made.destroy()
    made = Tk()
    made.geometry('300x300')
    made.title("Config")
    txtLabel=Label(made,font=('arial',13,'bold'),text="Mode")
    txtLabel.pack()
    btnConfig=Button(made,font=('arial',11,'bold'),text='Client',command=configMode)
    btnConfig.pack()
    
    btnClose=Button(made,font=('arial',11,'bold'),text='close',command=close).pack(side=BOTTOM)
    made.mainloop()
allowServerSend = False
#Default
def default(role):

    #global role
    global whatRole,count
    count=0
    #global client
    global msg,useSlot,operator,number,stateBtn,ip_Input,port_Input,s,configAllow
    #global server
    global serversocket,c,addr,allowServerSend
    if role == "Client":
        whatRole = 1
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        modeNow.set('Client')
    elif role =="Server":
        allowServerSend = False
        whatRole = 2
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        modeNow.set('Server')
    text1.set('    ')
    text2.set('    ')
    text3.set('    ')
    text4.set('    ')
    text5.set('    ')
    text6.set('    ')
    text7.set('    ')
    text8.set('    ')
    text9.set('    ')
    ip_Input.set('')
    port_Input.set('')
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
    global configAllow
    txtIp["state"] = "disabled"
    txtPort["state"] = "disabled"
    btnStart["state"] = "disabled"
    configAllow = False
    

def onConnection():
    global configAllow
    txtIp["state"] = "normal"
    txtPort["state"] = "normal"
    btnStart["state"] = "normal"
    configAllow = True
    


def offButton():
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
    global numberToSend,count,allowServerSend
   
    if whatRole == 1:
        if count== 10:
            s.close()
            default("Client")
            count=0
        else:
            clientPlay(numberToSend)#server -1 แล้ว
            serverPlay(numberToSend)
            onButton()
            #s.close()
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
                
            
            
            #s.close()
    btnSend["state"]= "disabled"
def upDate():
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
    global operator,numberToSend,allowServerSend
    numberToSend = numbers
    if whatRole == 1:

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
                
                

def actionWindow(whatAction):
    top = Toplevel(root) 
    top.geometry("500x200")
    l2 = Label(top,padx=16,pady=16,bd=8,fg="black",
            font=font1, text = whatAction) 
    l2.pack()
    top.mainloop()  

    
def getStart():
    global c,addr
    if len(ip_Input.get())==0 or len(port_Input.get())==0:
        actionWindow("ip/port error")
    else:
       
        
        if whatRole == 1:
            
            try:
                server = ip_Input.get()
                port = int(port_Input.get())
            except ValueError:
                stateServer.set("Server not response")
            try:
                s.connect((server, port))
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
                ip = ip_Input.get()
                port = int(port_Input.get())
                serversocket.bind((ip, port))
                serversocket.listen(5)
            except ValueError:
                stateServer.set("Server not response")
            try:
                c,addr = serversocket.accept()
                offButton()
                offConnection()
                stateServer.set("Welcome to XO Game")
                statePlayer.set("Wait Client")
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
            
           # except UnboundLocalError:
              #  stateServer.set("Client not response")
              #  print("UnboundLocalError ")
              # actionWindow("ip/port error")

        

    
    #print(server)
    #print(port)
#==========================Fonts==========================================
#font.Font(family='Helvetica', size=12, weight='bold')
font1 = TkFont.Font(family="Consolas",size = 20,weight = 'bold')

#===============================Calculator Frame===========================
txtDisplayState = Label(f2,font=font1,
                text="State",fg="Blue",bd=10,anchor='w')


txtDisplayState.grid(columnspan=4)
txtDisplay = Entry(f2,font=font1,
                   textvariable=statePlayer,bd=30,insertwidth=4,
                   bg="powder blue",justify='right',state='disabled',disabledbackground='powder blue')
txtDisplay.grid(columnspan=4)

btnWidth = 5
btnHeight = 1

#===============================Row5=======================================
btn1 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text1,width=btnWidth,
              height=btnHeight,
              bg="powder blue",command=lambda:btnClick(1))
btn1.grid(row=3,column=0)

btn2 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text2,width=btnWidth,
              height=btnHeight,bg="powder blue",command=lambda:btnClick(2))
btn2.grid(row=3,column=1)

btn3 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text3,width=btnWidth,
              height=btnHeight,bg="powder blue",command=lambda:btnClick(3))
btn3.grid(row=3,column=2)
#===============================Row4=======================================
btn4 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text4,width=btnWidth,
              height=btnHeight,bg="powder blue",command=lambda:btnClick(4))
btn4.grid(row=4,column=0)

btn5 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text5,width=btnWidth,
              height=btnHeight,bg="powder blue",command=lambda:btnClick(5))
btn5.grid(row=4,column=1)

btn6 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text6,width=btnWidth,
              height=btnHeight,bg="powder blue",command=lambda:btnClick(6))
btn6.grid(row=4,column=2)

#===============================Row3=======================================

btn7 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text7,width=btnWidth,
              height=btnHeight,bg="powder blue",command=lambda:btnClick(7))
btn7.grid(row=5,column=0)

btn8 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text8,width=btnWidth,
              height=btnHeight,bg="powder blue",command=lambda:btnClick(8))
btn8.grid(row=5,column=1)

btn9 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text9,width=btnWidth,
              height=btnHeight,bg="powder blue",command=lambda:btnClick(9))
btn9.grid(row=5,column=2)

btnSend = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              text="send",bg="powder blue",command=communication)
btnSend.grid(row=6,column=2)

offButton()

lblReference = Label(f1,font=font1, text="State",
                     bd=16,anchor='w').grid(row=0,column=0)  
txtReference = Entry(f1,font=font1,textvariable=stateServer,
                     bd=10,insertwidth=4,bg='powder blue',justify='right',state='disabled',disabledbackground='powder blue').grid(row=0,column=1)

#-----------------------------------------------------------------------------------------------------
lblIp = Label(f1,font=font1, text="ip"
                 ,bd=16,anchor='w').grid(row=1,column=0)  
txtIp = Entry(f1,font=font1,textvariable=ip_Input,
                     bd=10,insertwidth=4,bg='powder blue',justify='right')
txtIp.grid(row=1,column=1)

#-----------------------------------------------------------------------------------------------------
lblPort = Label(f1,font=font1, text="port"
                 ,bd=16,anchor='w').grid(row=2,column=0)  
txtPort = Entry(f1,font=font1,textvariable=port_Input,
                     bd=10,insertwidth=4,bg='powder blue',justify='right')
txtPort.grid(row=2,column=1)  

btnStart = Button(f1,padx=16,pady=16,bd=16,fg="black",font=font1,
                  width=10,text="Connect",bg="powder blue",command=getStart)
btnStart.grid(row=7,column=1)
menubar= Menu(root)
filemenu = Menu(menubar, tearoff =0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="Config",command=configuration)
filemenu.add_command(label="End",command=disConnected)

root.config(menu=menubar)


default("Client")
root.mainloop()  
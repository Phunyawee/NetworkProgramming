from socket import *
from threading import Thread
import threading
from time import ctime
from tkinter import *
import tkinter.font as TkFont
from tkinter import StringVar
import tkinter.messagebox
import codecs
import time
import json
getdata = {}
#start value
count= 0
gameRunning = True
haveWinner = True
nameSet = True 
exploreDataStatus = False
runnerServer = False
stopState = False
BUFSIZE = 4096

try:
    with open('statics.json','r') as j:
        getdata = json.load(j)
        exploreDataStatus = True
        j.close()
except :
    with open('statics.json','w',encoding='utf-8') as file:
        json.dump(getdata,file)
        file.close()
    print('New File created!')
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
msg = ['1','2','3','4','5','6','7','8','9']
msg_monitor = ['1','2','3','4','5','6','7','8','9']
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>server manage<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def check():
    global count
    global msg,gameRunning,msg_monitor 
    global useSlot,endGame
    count+=1
    print("turn :"+str(count))
    if (msg[0] == msg[1]) and (msg[1] == msg[2]):     
        gameRunning = False
        if (msg[0] == 'x'):
            print (str(record.player1)+"   WIN !!!!!!!!!!!!!!")    
            return record.player1
        if (msg[0] == 'o'):
            print (str(record.player2)+"   WIN !!!!!!!!!!!!!!")
            return record.player2
    if (msg[3] == msg[4]) and (msg[4] == msg[5]):        
        gameRunning = False
        if (msg[3] == 'x'):
            print (str(record.player1)+"   WIN !!!!!!!!!!!!!!")
            return record.player1
        if (msg[3] == 'o'):
            print (str(record.player2)+"   WIN !!!!!!!!!!!!!!")
            return record.player2
    if (msg[6] == msg[7]) and (msg[7] == msg[8]):
        gameRunning = False
        if (msg[6] == 'x'):
            print (str(record.player1)+"   WIN !!!!!!!!!!!!!!")
            return record.player1
        if (msg[6] == 'o'):
            print (str(record.player2)+"   WIN !!!!!!!!!!!!!!")
            return record.player2
    if (msg[0] == msg[3]) and (msg[3] == msg[6]):     
        gameRunning = False
        if (msg[0] == 'x'):
            print (str(record.player1)+"   WIN !!!!!!!!!!!!!!")
            return record.player1
        if (msg[0] == 'o'):
            print (str(record.player2)+"   WIN !!!!!!!!!!!!!!")
            return record.player2
    if (msg[1] == msg[4]) and (msg[4] == msg[7]):
        gameRunning = False
        if (msg[1] == 'x'):
            print (str(record.player1)+"   WIN !!!!!!!!!!!!!!")      
            return record.player1
        if (msg[1] == 'o'):
            print (str(record.player2)+"   WIN !!!!!!!!!!!!!!")
            return record.player2
    if (msg[2] == msg[5]) and (msg[5] == msg[8]):   
        gameRunning = False
        if (msg[2] == 'x'):
            print (str(record.player1)+"   WIN !!!!!!!!!!!!!!")
            return record.player1
        if (msg[2] == 'o'):
            print (str(record.player2)+"   WIN !!!!!!!!!!!!!!")
            return record.player2
    if (msg[0] == msg[4]) and (msg[4] == msg[8]):
        gameRunning = False
        if (msg[0] == 'x'):
            print (str(record.player1)+"   WIN !!!!!!!!!!!!!!")
            return record.player1
        if (msg[0] == 'o'):
            print (str(record.player2)+"   WIN !!!!!!!!!!!!!!")
            return record.player2
    if (msg[2] == msg[4]) and (msg[4] == msg[6]):
        gameRunning = False
        if (msg[2] == 'x'):
            print (str(record.player1)+"   WIN !!!!!!!!!!!!!!")    
            return record.player1
        if (msg[2] == 'o'):
            print (str(record.player2)+"   WIN !!!!!!!!!!!!!!")
            return record.player2
    else:
        if count == 9:
            gameRunning = False
            haveWinner = False
        return 'Draw'
    return 'None'
def resetToDefault():
    print('resetToDefault')
    statePlayer.set('')
    global gameRunning,msg,msg_monitor
    gameRunning = True
    msg = ['1','2','3','4','5','6','7','8','9']
    msg_monitor = ['1','2','3','4','5','6','7','8','9']
    upDate()

def print_table(msg):
    #os.system("cls")
    print ("")
    print (" "+str(msg[0])+" |"+str(msg[1])+"|"+str(msg[2])+" ")
    print (" "+str(msg[3])+" |"+str(msg[4])+"|"+str(msg[5])+" ")
    print (" "+str(msg[6])+" |"+str(msg[7])+"|"+str(msg[8])+" ")
    print ("") 

def print_table_monitor(msg_monitor):
    global threadLock,CONNECTIONS_LIST,server,record
    #os.system("cls")
    print ("")
    print (" "+str(msg_monitor[0])+" |"+str(msg_monitor[1])+"|"+str(msg_monitor[2])+" ")
    print (" "+str(msg_monitor[3])+" |"+str(msg_monitor[4])+"|"+str(msg_monitor[5])+" ")
    print (" "+str(msg_monitor[6])+" |"+str(msg_monitor[7])+"|"+str(msg_monitor[8])+" ")
    print ("") 

def Monitor(touch,getNumPy,choose):#my self
    global gameRunning,getdata,stopState
    if touch == 'disconnected':
        touch = 0
    touch = int(touch)
    global msg,msg_monitor 
    global count
    global useSlot
    print("Monitor")
    
    if touch == 99:
        pass
    elif touch != 0:
        (msg_monitor[int(touch)-1]) = getNumPy
        (msg[int(touch)-1]) = choose
        #====================================AttributeError: 'int' object has no attribute 'encode'
        #touch = str(touch)
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
    print_table_monitor(msg_monitor)
    getWinner = check()
    if gameRunning == False: 
        if count == 9 and haveWinner==False:
            print("Draw !!!!!")
            statePlayer.set("Draw !!!!!")
            statePlayer.set('Server ready')

        else:
            print (getWinner+" winner !!!")  
            statePlayer.set(getWinner+" winner !!!")
            stopState = True
            stateServer.set('Server ready')
            chosen = getWinner
            if len(getdata)==0:
                getdata[chosen]=1
            else:
                for key in getdata:
                    if chosen == key:
                        tempWin = getdata[chosen]+1
                        getdata[chosen]=tempWin
                        
                        break
            try:

                with open('statics.json','w',encoding='utf-8') as file:
                    json.dump(getdata,file)
                    file.close()
            except FileNotFoundError:
                stateServer.set('FileNotFoundError')

class chatRecord():
    def __init__(self):
        self.data = []
        self.countPlayer = 0
        self.boolTable = True
        self.player1 = ""
        self.player2 = ""
        
    def returnCount(self):
        print("returnCount"+str(self.countPlayer))
        return self.countPlayer
        
    def addMessage(self,message):
        print('addMessage')
        self.data.append(message)
        
    def getMessage(self,messageID):
        print('getMessage')
        if len(self.data) == 0:
            return 'No message yet!'
        elif messageID == 0:
            return '\n'.join(self.data)
        elif messageID !=0:
            temp = self.data[messageID:]
            return '\n'.join(temp)
        else:
            return "\n"
       
class clientHandler(Thread):
    def __init__(self,client,record,address):
        Thread.__init__(self)
        self._client = client
        self._record = record
        self._address = address
        self._numPlayer = record.countPlayer
        
       
                
        
    def broadCastingMessage(self,activeClient,message):
        global gameRunning
        print('broadCastingMessage')
        for socket in CONNECTIONS_LIST:
            if socket != server and socket != activeClient:
                print("active")
                print('player:' +str(record.countPlayer))
                if record.countPlayer==1:
                    message = '['+self._name+']'+'{disconnected}'
                try:
                    
                    print('pre==========================')
                    extractMessage = extract(message)
                    name = extractMessage[0]
                    select = extractMessage[1]
                    print("console: "+ name + " select: "+select)
                    if stopState == False:
                        statePlayer.set(name + " select: "+select)
                    if gameRunning == True:
                        if select == 99:
                            position = 0
                            for element in msg:#find element not x,y
                                if element.isnumeric()==True:
                                    if record.boolTable == True:
                                        record.player1 = str(name)
                                        record.boolTable = False
                                        Monitor(position,name,'x')
                                        upDate()
                                    else:
                                        record.player2 = str(name)
                                        record.boolTable = True
                                        Monitor(position,name,'o')
                                        upDate()
                                    break
                                else:
                                    position +=1
                        else:
                            if record.boolTable == True:
                                record.player1 = str(name)
                                record.boolTable = False
                                Monitor(select,name,'x')
                                upDate()
                            else:
                                record.player2 = str(name)
                                record.boolTable = True
                                Monitor(select,name,'o')
                                upDate()
                   
                    broadcastMessage = str.encode(message)
                    socket.send(broadcastMessage)
                    print('set==========================')
                except ConnectionAbortedError:
                    print('ConnectionAbortedError')
                    server.close()
                except ConnectionResetError:
                    print("Client {%s} is offline"%self._address)
                    #broadCastingMessage(socket,("Client (%s) is offline" %self._address))
                    print('!!!!!!!SSSSSS!!!!!!!')
                    packet = '['+self._name+']'+'{disconnected}' #send noti loss connect
                    record.countPlayer -= 1
                    self._record.addMessage(packet)
                    #====================send disconect
                    threadLock.acquire()
                    self.broadCastingMessage(packet,message)
                    threadLock.release()
                    #====================send disconect
                    CONNECTIONS_LIST.remove(socket)
                    if len(CONNECTIONS_LIST)==1:
                        record.data.clear()
                        record.countPlayer = 0
                        print(record.countPlayer)
                        print('Clear')
                        server.close()
                        default()
                        onConnection()
            else:
                print('out if\n')
        else:
            print('out for\n')
        
    
    def run(self):
        global nameSet
        print('run')
        try:
            self._client.send(str.encode('Welcome to the TIC TAC TOE room'))
            self._name = bytes.decode(self._client.recv(BUFSIZE))#get name client
            print('-'*20)
            print(str(self._name)+ '  joined the game')
            if nameSet:
                nameSet = False
                player1Label.set(self._name)
            else:
                player2Label.set(self._name)
            print('-'*20)
            #allMessage = self._record.getMessage(0)
            if self._numPlayer % 2== 0:#statrt game signal
                print('*'*10)
                print('Game start')
                i = 0
                self._client.send(str.encode(str(i)))
                print('*'*10)
            goto = True
        except ConnectionResetError:
                print(str(self._address)+' disconnectedC\n')
                packet = '['+self._name+']'+'{disconnected}' #send noti loss connect
                record.countPlayer -= 1
                self._record.addMessage(packet)
                threadLock.acquire()
                self.broadCastingMessage(self._client,packet)
                threadLock.release()
                self._client.close()
                CONNECTIONS_LIST.remove(self._client)
                print('!!!!!!!AAAAA!!!!!!!')
                print(CONNECTIONS_LIST)
                if len(CONNECTIONS_LIST)==1:
                    record.data.clear()
                    record.countPlayer = 0
                    print(record.countPlayer)
                    print('Clear')
                    server.close()
                    default()
                    onConnection()
                goto = False
        if goto:
            print('goto')
            while True:
                try:
                    message = bytes.decode(self._client.recv(BUFSIZE))#get mess fr clie
                    if not message or message =='bye':
                        print(str(self._address)+' left chat\n')
                        packet = '['+self._name+']'+'{disconnected}' #send noti loss connect
                        self._record.addMessage(packet)
                        #====================send disconect
                        record.countPlayer -= 1
                        self.broadCastingMessage(self._client,packet)
                        threadLock.acquire()
                        #====================send disconect
                        self._client.close()
                        print('!!!!!!!QQQQQ!!!!!!!')
                        CONNECTIONS_LIST.remove(self._client)
                        threadLock.release()
                        print('user '+str(CONNECTIONS_LIST))
                        if len(CONNECTIONS_LIST)==1:
                            record.data.clear()
                            record.countPlayer = 0
                            print(record.countPlayer)
                            print('Clear')
                            server.close()
                            default()
                            onConnection()
                        break
                    else:
                        #message = message
                        message = '['+self._name+']'+'{'+message+'}' #send mess from c to c
                        self._record.addMessage(message)
                        #====================send disconect
                        threadLock.acquire()
                        self.broadCastingMessage(self._client,message)
                        threadLock.release()
                        #====================send disconect
                except ConnectionAbortedError and ConnectionResetError and OSError:
                    print(str(self._address)+' disconnected\n')
                    packet = '['+self._name+']'+'{disconnected}' #send noti loss connect

                    record.countPlayer -= 1
                    self._record.addMessage(packet)
                    threadLock.acquire()
                    self.broadCastingMessage(self._client,packet)
                    threadLock.release()
                    self._client.close()
                    CONNECTIONS_LIST.remove(self._client)
                    print('!!!!!!!!!!!!!!!!!!!')
                    print(CONNECTIONS_LIST)
                    if len(CONNECTIONS_LIST)==1:
                        record.data.clear()
                        record.countPlayer = 0
                       
                        print(record.countPlayer)
                        print('Clear')
                        server.close()
                        default()
                        onConnection()
                        
                    break
                
                    
                
              
#
#Client
root = Tk()
root.geometry("1600x800+0+0")
#root.attributes('-fullscreen', True)  
root.title("Tic-tac-toe(Server)")
root.configure(background='powder blue')
messagetry = StringVar()
modeNow = StringVar()
modeMainFrame = StringVar()
player1Label = StringVar()
player2Label = StringVar()
player1Label.set('Name')
player2Label.set('Name')
Tops = Frame(root,width=1600,height=400,bg="powder blue",relief=SUNKEN)
Tops.pack(side=TOP)

f0 = Frame(Tops,bg="powder blue",relief=SUNKEN)
f0.grid(row=0,column=0)

#label
lblInfo = Label(f0,font=('Microsoft YaHei Light',50,'bold'),
                text="Player1",fg="Blue",bd=10,background='powder blue')
lblInfo.grid(row=0,column=0)
lblRole = Label(f0,font=('Microsoft YaHei Light',40,'bold'),
                textvariable=player1Label,fg="Blue",bd=10,background='powder blue')
lblRole.grid(row=1,column=0)
#bank zone
#===============================================================
f0a = Frame(Tops,bg="powder blue",relief=SUNKEN)
f0a.grid(row=0,column=2)
lblAir = Label(f0a,font=('Microsoft YaHei Light',50,'bold'),
                text="Player2",fg="Blue",bd=10,background='powder blue')
lblAir.grid(row=0,column=0)
lblAir2 = Label(f0a,font=('Microsoft YaHei Light',40,'bold'),
                textvariable=player2Label,fg="Blue",bd=10,background='powder blue')
lblAir2.grid(row=1,column=0)
#===============================================================
#hall
f0b = Frame(Tops,bg="powder blue",relief=SUNKEN)
f0b.grid(row=0,column=1)

lblHall = Label(f0b,font=('Microsoft YaHei Light',50,'bold'),
                text="\tMonitor\t\t",fg="Blue",bd=10,background='powder blue')
lblHall.grid(row=0,column=0)
lblHall2 = Label(f0b,font=('Microsoft YaHei Light',40,'bold'),
                textvariable=str(Clock()),fg="Blue",bd=10,background='powder blue')
lblHall2.grid(row=1,column=0)

statePlayer=StringVar()
stateServer=StringVar()
ip_Input=StringVar()
port_Input=StringVar()
name_Input=StringVar()
text1 = StringVar()
text2 = StringVar()
text3 = StringVar()
text4 = StringVar()
text5 = StringVar()
text6 = StringVar()
text7 = StringVar()
text8 = StringVar()
text9 = StringVar()

# lblInfo3 = Label(f0,font=('Microsoft YaHei Light',50,'bold'),
#                 text="\t\t",fg="Blue",bd=10)
# lblInfo3.grid(row=0,column=2)
# lblRole3 = Label(f0,font=('Microsoft YaHei Light',40,'bold'),
#                 text="\t\t",fg="Blue",bd=10)
# lblRole3.grid(row=1,column=2)


def setNameWinner(name):
    global winner_name
    pass



def hallOfFrame():
    global getdata
    txtHall.delete("1.0","end")
    txtHall.insert(END,"Name"  +'\t\t\t\t\t'+  "Win" + '\n')
    for played in getdata :
            txtHall.insert(END,str(played)  +'\t\t\t\t\t   '+ str(getdata[played]) + '\n')
    txtHall.configure(state='disabled')
    



def communication():
    print('communication')
    pass

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
def closeGame():
    global server,runnerServer
    if runnerServer:
        server.close()
    root.destroy()
    return 0

def onConnection():
    print('onConnection')
    global configAllow
    txtIp["state"] = "normal"
    txtPort["state"] = "normal"
    btnStart["state"] = "normal"
    btnClear["state"] = "normal"
    configAllow = True
def offConnection():
    print('offConnection')
    global configAllow
    txtIp["state"] = "disabled"
    txtPort["state"] = "disabled"
    btnStart["state"] = "disabled"
    btnClear["state"] = "disabled"
    configAllow = False
def configuration():
    print("configuration")
    pass
def playAgain():
    print("playAgain")
    pass

def disConnected():
    print("disConnected")
    pass
def upDate():
    print("update call")
    text1.set(msg_monitor[0])
    text2.set(msg_monitor[1])
    text3.set(msg_monitor[2])
    text4.set(msg_monitor[3])
    text5.set(msg_monitor[4])
    text6.set(msg_monitor[5])
    text7.set(msg_monitor[6])
    text8.set(msg_monitor[7])
    text9.set(msg_monitor[8]) 




def default():
    global record,server,threadLock,CONNECTIONS_LIST,PORT,BUFSIZE
    global msg,msg_monitor,nameSet,count,stopState
    hallOfFrame()
    stopState = False
    count = 0
    nameSet = True 
    runnerServer = False
    player1Label.set('Name')
    player2Label.set('Name')    
    msg_monitor = ['1','2','3','4','5','6','7','8','9']
    msg = ['1','2','3','4','5','6','7','8','9']
    ip_Input.set('')
    port_Input.set('')
    



def startServer():
    global threadLock,CONNECTIONS_LIST,server,record,msg_monitor,nameSet,runnerServer
    runnerServer = True
    resetToDefault()
    if (len(ip_Input.get())==0 or len(port_Input.get())==0) :
        print('No input')
    else:

        IPADDRESS =ip_Input.get()
        PORT =  int(port_Input.get())
        ADDRESS = (IPADDRESS,PORT)
        CONNECTIONS_LIST = []
        try:
            threadLock = threading.Lock()
            record = chatRecord()
            server = socket(AF_INET,SOCK_STREAM)
            server.bind(ADDRESS)
            server.listen(10)
            CONNECTIONS_LIST.append(server)
            print('List')
            print(CONNECTIONS_LIST)
        except OSError:
            print('OSError')
        except TypeError:
            print('TypeError')
        print("Chat server started on IP Address : ",IPADDRESS)
        print("Chat server started on port : "+str(PORT))
        
        offConnection()
        #====================================
        print('Waiting for connection...')
        print('player now:'+ str(record.returnCount()))
        gamePlay = True
        while(1):
            try:
                if (record.returnCount())<2:
                    client,address = server.accept()
                    record.countPlayer+=1
                    print('Player: '+str(record.countPlayer))
                    print("...connected from:"+str(client)+" addr "+str(address))
                    
                    threadLock.acquire()
                    CONNECTIONS_LIST.append(client)
                    print('xxxxxxxxxxxxxxx')
                    print(CONNECTIONS_LIST)
                    threadLock.release()
                    handler = clientHandler(client,record,address)
                    handler.start()
                else:
                    gamePlay=False
                    print('full')
                    break
            except OSError:
                stateServer.set('detect error pls restart.')
        stateServer.set('Server currently running')


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>server manage<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
Bottoms = Frame(root,width=1600,bg="powder blue",relief=SUNKEN)
Bottoms.pack(side=BOTTOM)

f1 = Frame(Bottoms,width=800,height=700,bg="",relief=SUNKEN)
f1.grid(row=0,column=1)

f2 = Frame(Bottoms,width=600,height=700,relief=SUNKEN)
f2.grid(row=0,column=2)
f2.configure(background='powder blue')
f3 = Frame(Bottoms,width=500,height=700,bg='powder blue')
f3.grid(row=0,column=3)
lblInfox = Label(f3,font=('Microsoft YaHei Light',40,'bold'),
                text="      Hall of Fame",fg="Blue",bd=5,bg='powder blue')
lblInfox.grid(row=0,column=0)
txtHall = Text(f3,font=('TH Sarabun New',17,'bold'), bd=8,width=45,height=15,bg="powder blue")
txtHall.grid(row=1,column=0)

chkTime = 0



#==========================Fonts==========================================
#font.Font(family='Helvetica', size=12, weight='bold')
font1 = TkFont.Font(family="Microsoft YaHei Light",size = 20,weight = 'bold')

#===============================Calculator Frame===========================
txtDisplayState = Label(f2,font=font1,
                text="State",fg="Blue",bd=10,bg='powder blue')


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
              bg="#49A")
btn1.grid(row=3,column=0)

btn2 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text2,width=btnWidth,
              height=btnHeight,bg="#49A")
btn2.grid(row=3,column=1)

btn3 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text3,width=btnWidth,
              height=btnHeight,bg="#49A")
btn3.grid(row=3,column=2)
#===============================Row4=======================================
btn4 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text4,width=btnWidth,
              height=btnHeight,bg="#49A")
btn4.grid(row=4,column=0)

btn5 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text5,width=btnWidth,
              height=btnHeight,bg="#49A")
btn5.grid(row=4,column=1)

btn6 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text6,width=btnWidth,
              height=btnHeight,bg="#49A")
btn6.grid(row=4,column=2)

#===============================Row3=======================================

btn7 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text7,width=btnWidth,
              height=btnHeight,bg="#49A")
btn7.grid(row=5,column=0)

btn8 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text8,width=btnWidth,
              height=btnHeight,bg="#49A")
btn8.grid(row=5,column=1)

btn9 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text9,width=btnWidth,
              height=btnHeight,bg="#49A")
btn9.grid(row=5,column=2)

btnClear = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              text="CLEAR",width=23,
              height=btnHeight,bg="#49A",command=lambda:resetToDefault())
btnClear.grid(row=6,columnspan=3)

#offButton()

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


btnStart = Button(f1,padx=16,pady=16,bd=16,fg="black",font=font1,
                  width=10,text="Connect",bg="#49A",command=lambda:startServer())
btnStart.grid(row=7,column=1)
btnTry = Button(f1,padx=16,pady=16,bd=16,fg="black",font=font1,
                  width=5,text="Exit",bg="#49A",command=closeGame)
btnTry.grid(row=8,column=1)
menubar= Menu(root)
filemenu = Menu(menubar, tearoff =0,font= 'Helvetica 30 bold')
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="Config",command=configuration)
filemenu.add_command(label="End",command=disConnected)
filemenu.add_command(label="Exit", command = closeGame)
root.config(menu=menubar)
root.attributes('-fullscreen', True)  
#root.resizable(False,False)
hallOfFrame()
upDate()
root.mainloop()  
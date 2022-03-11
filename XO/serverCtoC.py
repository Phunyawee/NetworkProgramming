# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 14:45:33 2022
6230300613
@author: MISTER_M
"""
from socket import *
from threading import Thread
import threading
from time import ctime

count= 0
gameRunning = True
def check():
    global count
    global msg,gameRunning,msg_monitor 
    global useSlot,endGame
    count+=1
    print("turn :"+str(count))
    if count == 9:
        gameRunning = False
        return 'Draw'
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
    return 'None'
def resetToDefault():
    global gameRunning,msg,msg_monitor
    record.player1=""
    record.player2=""
    gameRunning = True
    msg = ['1','2','3','4','5','6','7','8','9']
    msg_monitor = ['1','2','3','4','5','6','7','8','9']

def print_table(msg):
    #os.system("cls")
    print ("")
    print (" "+str(msg[0])+" |"+str(msg[1])+"|"+str(msg[2])+" ")
    print (" "+str(msg[3])+" |"+str(msg[4])+"|"+str(msg[5])+" ")
    print (" "+str(msg[6])+" |"+str(msg[7])+"|"+str(msg[8])+" ")
    print ("") 

def print_table_monitor(msg):
    #os.system("cls")
    print ("")
    print (" "+str(msg_monitor[0])+" |"+str(msg_monitor[1])+"|"+str(msg_monitor[2])+" ")
    print (" "+str(msg_monitor[3])+" |"+str(msg_monitor[4])+"|"+str(msg_monitor[5])+" ")
    print (" "+str(msg_monitor[6])+" |"+str(msg_monitor[7])+"|"+str(msg_monitor[8])+" ")
    print ("") 

def Monitor(touch,getNumPy,choose):#my self
    global gameRunning
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
    print_table_monitor(msg)
    getWinner = check()
    if gameRunning == False: 
        if count == 9:
            print("Draw !!!!!")
        else:
            print (getWinner+" winner !!!")  
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
                    if gameRunning == True:
                        if record.boolTable == True:
                            record.player1 = str(name)
                            record.boolTable = False
                            Monitor(select,name,'x')
                        else:
                            record.player2 = str(name)
                            record.boolTable = True
                            Monitor(select,name,'o')
                   
                    broadcastMessage = str.encode(message)
                    socket.send(broadcastMessage)
                    print('set==========================')
                    
                except ConnectionAbortedError and ConnectionResetError:
                    print("Client {%s} is offline"%self._address)
                    broadCastingMessage(socket,("Client (%s) is offline" %self._address))
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
                        resetToDefault()
                        print(record.countPlayer)
                        print('Clear')
                        server.close()
            else:
                print('out if\n')
        else:
            print('out for\n')
        
    
    def run(self):
        print('run')
        try:
            
            self._client.send(str.encode('Welcome to the TIC TAC TOE room'))
            self._name = bytes.decode(self._client.recv(BUFSIZE))#get name client
            print('-'*20)
            print(str(self._name)+ '  joined the game')
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
                    resetToDefault()
                    print(record.countPlayer)
                    print('Clear')
                    server.close()
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
                            resetToDefault()
                            print(record.countPlayer)
                            print('Clear')
                            server.close()
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
                        resetToDefault()
                        print(record.countPlayer)
                        print('Clear')
                        server.close()
                    break
                
                    
                
              
            
def default():
    global record,server,threadLock,CONNECTIONS_LIST,PORT,BUFSIZE
    global msg,msg_monitor
           
    msg_monitor = ['1','2','3','4','5','6','7','8','9']
    msg = ['1','2','3','4','5','6','7','8','9']
        
    HOSTNAME = gethostname()
    #IPADDRESS = gethostbyname(gethostname())
    IPADDRESS ='127.0.0.1'
    PORT = 5000
    BUFSIZE = 4096
    ADDRESS = (IPADDRESS,PORT)
    
    CONNECTIONS_LIST = []
    
    threadLock = threading.Lock()
    
    record = chatRecord()
    server = socket(AF_INET,SOCK_STREAM)
    server.bind(ADDRESS)
    server.listen(10)
    
    CONNECTIONS_LIST.append(server)
    print('zzzzzzzzzzzzzzzzz')
    print(CONNECTIONS_LIST)
    print("Chat server started on hostname : ",HOSTNAME)
    print("Chat server started on IP Address : ",IPADDRESS)
    print("Chat server started on port : "+str(PORT))



def startServer():
    print('Waiting for connection...')
    print('player now:'+ str(record.returnCount()))
    gamePlay = True
    while gamePlay:
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
            #print('over store')
            #pass
            #client,address = server.accept()
            #client.close()
            #print(CONNECTIONS_LIST)
            print('full')
       
default()
startServer()

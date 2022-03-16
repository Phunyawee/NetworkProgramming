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
getStatic = {}
#start value
count= 0
gameRunning = True
haveWinner = True
nameSet = True 
exploreDataStatus = False
runnerServer = False
stopState = False
BUFSIZE = 4096
namelst=[]
walklst=[]
playerCollector = []
try:

    #============================Sort data
    with open('statics.json','r') as j:
        getdata = json.load(j)  
        j.close()
    sorted_dt = {key: value for key, value in sorted(getdata.items(), key=lambda item: item[1],reverse=True)}
    with open('statics.json','w') as file:
        file.write(json.dumps(sorted_dt,indent=1))
        file.close()
    with open('statics.json','r') as j:
        getdata = json.load(j)
        j.close()
    with open('statics_players.json','r') as j:
        getStatic = json.load(j)
        j.close()
    #============================Sort data
except :
    with open('statics.json','w',encoding='utf-8') as file:
        file.write(json.dumps(getdata,indent=1))
        #json.dump(getdata,file)
        file.close()
    with open('statics_players.json','w',encoding='utf-8') as file:
        file.write(json.dumps(getdata,indent=1))
        #json.dump(getdata,file)
        file.close()
    print('New File created!')
class Clock:
    def __init__(self):
        self.time1 = ''
        self.time2 = time.strftime('%H:%M:%S')
        self.mFrame = Frame()
        self.mFrame.pack()
        self.watch = Label(self.mFrame, text=self.time2,font=('Fixedsys',30,'bold'),fg="#f8f9fa",bg='#6f85ff')
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
msg = ['1','2','3','4','5','6','7','8','9']
msg_monitor = ['1','2','3','4','5','6','7','8','9']
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>server manage<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def check():
    global count
    global msg,gameRunning,msg_monitor
    global useSlot,endGame,haveWinner
    count+=1
    print("turn :"+str(count))
    if (msg[0] == msg[1]) and (msg[1] == msg[2]):     
        gameRunning = False
        haveWinner = True
        if (msg[0] == 'x'):
            print (str(record.player1)+"   1WIN !!!!!!!!!!!!!!")    
            return record.player1
        if (msg[0] == 'o'):
            print (str(record.player2)+"   2WIN !!!!!!!!!!!!!!")
            return record.player2
    if (msg[3] == msg[4]) and (msg[4] == msg[5]):        
        gameRunning = False
        haveWinner = True
        if (msg[3] == 'x'):
            print (str(record.player1)+"   3WIN !!!!!!!!!!!!!!")
            return record.player1
        if (msg[3] == 'o'):
            print (str(record.player2)+"   4WIN !!!!!!!!!!!!!!")
            return record.player2
    if (msg[6] == msg[7]) and (msg[7] == msg[8]):
        gameRunning = False
        haveWinner = True
        if (msg[6] == 'x'):
            print (str(record.player1)+"   5WIN !!!!!!!!!!!!!!")
            return record.player1
        if (msg[6] == 'o'):
            print (str(record.player2)+"   6WIN !!!!!!!!!!!!!!")
            return record.player2
    if (msg[0] == msg[3]) and (msg[3] == msg[6]):     
        gameRunning = False
        haveWinner = True
        if (msg[0] == 'x'):
            print (str(record.player1)+"   7WIN !!!!!!!!!!!!!!")
            return record.player1
        if (msg[0] == 'o'):
            print (str(record.player2)+"   8WIN !!!!!!!!!!!!!!")
            return record.player2
    if (msg[1] == msg[4]) and (msg[4] == msg[7]):
        gameRunning = False
        haveWinner = True
        if (msg[1] == 'x'):
            print (str(record.player1)+"   9WIN !!!!!!!!!!!!!!")      
            return record.player1
        if (msg[1] == 'o'):
            print (str(record.player2)+"   10WIN !!!!!!!!!!!!!!")
            return record.player2
    if (msg[2] == msg[5]) and (msg[5] == msg[8]):   
        gameRunning = False
        haveWinner = True
        if (msg[2] == 'x'):
            print (str(record.player1)+"   11WIN !!!!!!!!!!!!!!")
            return record.player1
        if (msg[2] == 'o'):
            print (str(record.player2)+"   12WIN !!!!!!!!!!!!!!")
            return record.player2
    if (msg[0] == msg[4]) and (msg[4] == msg[8]):
        gameRunning = False
        haveWinner = True
        if (msg[0] == 'x'):
            print (str(record.player1)+"   13WIN !!!!!!!!!!!!!!")
            return record.player1
        if (msg[0] == 'o'):
            print (str(record.player2)+"   14WIN !!!!!!!!!!!!!!")
            return record.player2
    if (msg[2] == msg[4]) and (msg[4] == msg[6]):
        gameRunning = False
        haveWinner = True
        if (msg[2] == 'x'):
            print (str(record.player1)+"   15WIN !!!!!!!!!!!!!!")    
            return record.player1
        if (msg[2] == 'o'):
            print (str(record.player2)+"   16WIN !!!!!!!!!!!!!!")
            return record.player2
    else:
        if count == 9:
            gameRunning = False
            haveWinner = False
        haveWinner == False
        return 'Draw'
    return 'None'
def resetToDefault():
    print('resetToDefault')
    statePlayer.set('')

    namelst.clear()
    walklst.clear()
    playerCollector.clear()
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

def Monitor(touch,getNamePlayer,choose):#my self
    global gameRunning,getdata,stopState,getStatic
    if touch == 'disconnected':
        touch = 0
    touch = int(touch)
    global msg,msg_monitor 
    global count
    global useSlot
    print("Monitor")
    
    if touch == 99:
        print('draw occur')
        position = 0
        for element in msg:#find element not x,y
            if element.isnumeric()==True:
                print('element not x,y : '+str(position))
                if record.boolTable == True:
                    record.player1 = str(getNamePlayer)
                    Monitor(position+1,getNamePlayer,'o')
                    upDate()
                else:
                    record.player2 = str(getNamePlayer)
                    Monitor(position+1,getNamePlayer,'x')
                    upDate()
                break
            else:
                position +=1
    elif touch != 0:
        addHistory(getNamePlayer,touch)
        (msg_monitor[int(touch)-1]) = getNamePlayer
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
    print('getWinner'+getWinner)
    print('haveWin'+str(haveWinner))
    if getWinner == 'Draw' and haveWinner == False:
        gameRunning = False
   
    if gameRunning == False: 
        if count == 10 and haveWinner==False:
            print("Draw !!!!!")
            statePlayer.set("Draw !!!!!")
            #statePlayer.set('Server ready')

        else:
            print (getWinner+" winner !!!")  
            loser=""
            if getWinner==record.player1:
                print('loser :'+ str(record.player2))
                loser =  str(record.player2)
            else:
                print('loser : '+ str(record.player1))
                loser =  str(record.player2)

            statePlayer.set(getWinner+" winner !!!")
            stopState = True
            stateServer.set('Server ready')
            chosen = getWinner
            #============================Sort data
            with open('statics.json','r') as j:
                getdata = json.load(j)
                j.close()
            sorted_dt = {key: value for key, value in sorted(getdata.items(), key=lambda item: item[1],reverse=True)}
            with open('statics.json','w') as file:
                file.write(json.dumps(sorted_dt,indent=1))
                #json.dump(sorted_dt,file)
                file.close()
            #============================Sort data
            with open('statics.json','r') as j:
                getdata = json.load(j)
                j.close()
            getDataList = []
            for key in getdata:
                getDataList.append(key)
            if chosen != 'Draw':
                print('Winner: '+chosen)
                print('Loser: '+loser)
                
                
                print('getDataList:'+str(getDataList))
                if chosen not in getDataList:
                    print('add winner')
                    print('####################################################################')
                    with open('statics.json','r') as j:
                        getdata = json.load(j)
                        j.close()
                    with open('statics.json','w') as file:#play first time
                        getdata[chosen]=1
                        file.write(json.dumps(getdata,indent=1))
                        #json.dump(getdata,file)
                        file.close()
                    with open('statics_players.json','r') as j:
                        getdata = json.load(j)
                        j.close()
                    with open('statics_players.json','w') as file:#play first time
                        getdata[chosen]='[1]{1}<0>(0)'
                        file.write(json.dumps(getdata,indent=1))
                        #json.dump(getdata,file)
                        file.close()
                    if loser not in getDataList:
                        print('add loser')
                        print('####################################################################')
                        with open('statics.json','r') as j:
                            getdata = json.load(j)
                            j.close()
                        with open('statics.json','w') as file:#play first time
                            getdata[loser]=0
                            file.write(json.dumps(getdata,indent=1))
                            #json.dump(getdata,file)
                            file.close()   
                        with open('statics_players.json','r') as j:
                            getdata = json.load(j)
                            j.close()
                        with open('statics_players.json','w') as file:#play first time
                            getdata[loser]='[1]{0}<1>(0)'
                            file.write(json.dumps(getdata,indent=1))
                            #json.dump(getdata,file)
                            file.close()
                        ####################################################################
                    else:
                        print('update loser')
                        print('####################################################################')
                        with open('statics_players.json','r') as file:##other time
                            getStatic=json.load(file)
                            file.close()
                            unZip = TheTrain(getStatic[loser])
                            round = int(unZip[0])+1
                            win = int(unZip[1])+0
                            loss = int(unZip[2])+1
                            draw = int(unZip[3])+0
                        with open('statics_players.json','w') as file:##other time
                            getStatic[loser]='['+str(round)+']'+'{'+str(win)+'}'+'<'+str(loss)+'>'+'('+str(draw)+')'
                            file.write(json.dumps(getStatic,indent=1))
                            #json.dump(getStatic,file)
                            file.close()
                
                if loser not in getDataList:
                    print('add loser')
                    print('####################################################################')
                    ####################################################################
                    with open('statics.json','r') as j:
                            getdata = json.load(j)
                            j.close()
                    with open('statics.json','w') as file:#play first time
                        getdata[loser]=0
                        file.write(json.dumps(getdata,indent=1))
                        #json.dump(getdata,file)
                        file.close()   
                    with open('statics_players.json','r') as j:
                        getdata = json.load(j)
                        j.close()
                    with open('statics_players.json','w') as file:#play first time
                        getdata[loser]='[1]{0}<1>(0)'
                        file.write(json.dumps(getdata,indent=1))
                        #json.dump(getdata,file)
                        file.close()
                    ####################################################################
                    if chosen not in getDataList:
                        print('add winner')
                        print('####################################################################')
                        with open('statics.json','r') as j:
                            getdata = json.load(j)
                            j.close()
                        with open('statics.json','w') as file:#play first time
                            getdata[chosen]=1
                            file.write(json.dumps(getdata,indent=1))
                            #json.dump(getdata,file)
                            file.close()
                        with open('statics_players.json','r') as j:
                            getdata = json.load(j)
                            j.close()
                        with open('statics_players.json','w') as file:#play first time
                            getdata[chosen]='[1]{1}<0>(0)'
                            file.write(json.dumps(getdata,indent=1))
                            #json.dump(getdata,file)
                            file.close()
                        ####################################################################
                    else:
                        print('update winner')
                        print('####################################################################')
                        with open('statics.json','r') as file:#play first time
                            getdata =json.load(file)
                            file.close()
                        with open('statics.json','w') as file:#play first time
                            tempWin = getdata[chosen]
                            getdata[chosen]= tempWin+1
                            file.write(json.dumps(getdata,indent=1))
                            #json.dump(getdata,file)
                            file.close()

                        with open('statics_players.json','r') as file:##other time
                            getStatic=json.load(file)
                            file.close()
                            unZip = TheTrain(getStatic[chosen])
                            round = int(unZip[0])+1
                            win = int(unZip[1])+1
                            loss = int(unZip[2])+0
                            draw = int(unZip[3])+0
                        with open('statics_players.json','w') as file:##other time
                            getStatic[chosen]='['+str(round)+']'+'{'+str(win)+'}'+'<'+str(loss)+'>'+'('+str(draw)+')'
                            file.write(json.dumps(getStatic,indent=1))
                            #json.dump(getStatic,file)
                            file.close()
                        ####################################################################
                if loser in getDataList and chosen in getDataList:
                    print('update loser')
                    print('####################################################################')
                    with open('statics_players.json','r') as file:##other time
                        getStatic=json.load(file)
                        file.close()
                        unZip = TheTrain(getStatic[loser])
                        round = int(unZip[0])+1
                        win = int(unZip[1])+0
                        loss = int(unZip[2])+1
                        draw = int(unZip[3])+0
                    with open('statics_players.json','w') as file:##other time
                        getStatic[loser]='['+str(round)+']'+'{'+str(win)+'}'+'<'+str(loss)+'>'+'('+str(draw)+')'
                        file.write(json.dumps(getStatic,indent=1))
                        #json.dump(getStatic,file)
                        file.close()

                    print('update winner')
                    print('####################################################################')
                    with open('statics.json','r') as file:#play first time
                        getdata =json.load(file)
                        file.close()
                    with open('statics.json','w') as file:#play first time
                        tempWin = getdata[chosen]
                        getdata[chosen]= tempWin+1
                        file.write(json.dumps(getdata,indent=1))
                        #json.dump(getdata,file)
                        file.close()

                    with open('statics_players.json','r') as file:##other time
                        getStatic=json.load(file)
                        file.close()
                        unZip = TheTrain(getStatic[chosen])
                        round = int(unZip[0])+1
                        win = int(unZip[1])+1
                        loss = int(unZip[2])+0
                        draw = int(unZip[3])+0
                    with open('statics_players.json','w') as file:##other time
                        getStatic[chosen]='['+str(round)+']'+'{'+str(win)+'}'+'<'+str(loss)+'>'+'('+str(draw)+')'
                        file.write(json.dumps(getStatic,indent=1))
                        #json.dump(getStatic,file)
                        file.close()

                
                


                
                       
                            
                            
            elif chosen == 'Draw':
                
                print(str(playerCollector[0])+' vs '+str(playerCollector[1])+' = Draw')
                if playerCollector[0] not in getDataList:
                     #---------------------Set key statics.json-------------------------
                    print('add draw')
                    print('####################################################################')
                    with open('statics.json','r') as j:
                        getdata = json.load(j)
                        j.close()
                    with open('statics.json','w') as file:#play first time
                        getdata[playerCollector[0]]=0
                        file.write(json.dumps(getdata,indent=1))
                        #json.dump(getdata,file)
                        file.close()
                     #---------------------Set key statics.json-------------------------
                    with open('statics_players.json','r') as j:
                        getdata = json.load(j)
                        j.close()
                    with open('statics_players.json','w') as file:#play first time
                        getdata[playerCollector[0]]='[1]{0}<0>(1)'
                        file.write(json.dumps(getdata,indent=1))
                        #json.dump(getdata,file)
                        file.close()
                else: 
                    print('update draw')
                    print('####################################################################')
                    #---------------------Set key statics.json-------------------------
                    with open('statics_players.json','r') as file:#play draw
                        getStatic=json.load(file)
                        file.close()
                        unZip = TheTrain(getStatic[str(playerCollector[0])])
                        round = int(unZip[0])+1
                        win = int(unZip[1])+0
                        loss = int(unZip[2])+0
                        draw = int(unZip[3])+1
                    with open('statics_players.json','w') as file:#play draw
                        getStatic[str(playerCollector[0])]='['+str(round)+']'+'{'+str(win)+'}'+'<'+str(loss)+'>'+'('+str(draw)+')'
                        file.write(json.dumps(getStatic,indent=1))
                        #json.dump(getStatic,file)
                        file.close()
                
                if playerCollector[1] not in getDataList:
                    print('add draw')
                    print('####################################################################')
                    #---------------------Set key statics.json-------------------------
                    with open('statics.json','r') as j:
                        getdata = json.load(j)
                        j.close()
                    with open('statics.json','w') as file:#play first time
                        getdata[playerCollector[1]]=0
                        file.write(json.dumps(getdata,indent=1))
                        #json.dump(getdata,file)
                        file.close()
                    #---------------------Set key statics.json-------------------------
                    with open('statics_players.json','r') as j:
                        getdata = json.load(j)
                        j.close()
                    with open('statics_players.json','w') as file:#play first time
                        getdata[playerCollector[1]]='[1]{0}<0>(1)'
                        file.write(json.dumps(getdata,indent=1))
                        #json.dump(getdata,file)
                        file.close()
                else:
                    print('update draw')
                    print('####################################################################')
                     #---------------------Set key statics.json-------------------------
                    with open('statics_players.json','r') as file:#play draw
                        getStatic=json.load(file)
                        file.close()
                        unZip = TheTrain(getStatic[str(playerCollector[1])])
                        round = int(unZip[0])+1
                        win = int(unZip[1])+0
                        loss = int(unZip[2])+0
                        draw = int(unZip[3])+1
                    with open('statics_players.json','w') as file:#play draw
                        getStatic[str(playerCollector[1])]='['+str(round)+']'+'{'+str(win)+'}'+'<'+str(loss)+'>'+'('+str(draw)+')'
                        file.write(json.dumps(getStatic,indent=1))
                        #json.dump(getStatic,file)
                        file.close()
                
                            
                            
                        
                
                

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
                            pass
                        else:
                            print('continue')
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
                except RuntimeError:
                    print('RuntimeError')
                    server.close()
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
            if (self._name).isnumeric()==True:
                if 1<= int(self._name) and int(self._name)<10:
                    self.broadCastingMessage(self._client,'unknown')
                    record.countPlayer=3
                    server.close()
                
            if nameSet:
                nameSet = False
                player1Label.set(self._name)
                if self._name not in playerCollector:playerCollector.append(self._name)
                
            else:
                player2Label.set(self._name)
                if self._name not in playerCollector:playerCollector.append(self._name)
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
root.configure(background='#6f85ff')
messagetry = StringVar()
modeNow = StringVar()
modeMainFrame = StringVar()
player1Label = StringVar()
player2Label = StringVar()
player1Label.set('Name')
player2Label.set('Name')
Tops = Frame(root,width=1600,height=400,bg="#6f85ff",relief=SUNKEN)
Tops.pack(side=TOP)

f0 = Frame(Tops,bg="#6f85ff",relief=SUNKEN)
f0.grid(row=0,column=0)

#label
lblInfo = Label(f0,font=('Fixedsys',35,'bold'),
                text="Player1",fg="#f8f9fa",bd=10,background='#6f85ff')
lblInfo.grid(row=0,column=0)
lblRole = Label(f0,font=('Fixedsys',35,'bold'),
                textvariable=player1Label,fg="#f8f9fa",bd=10,background='#6f85ff')
lblRole.grid(row=1,column=0)
#bank zone
#===============================================================
f0a = Frame(Tops,bg="#6f85ff",relief=SUNKEN)
f0a.grid(row=0,column=2)
lblAir = Label(f0a,font=('Fixedsys',35,'bold'),
                text="Player2",fg="#f8f9fa",bd=10,background='#6f85ff')
lblAir.grid(row=0,column=0)
lblRole2 = Label(f0a,font=('Fixedsys',35,'bold'),
                textvariable=player2Label,fg="#f8f9fa",bd=10,background='#6f85ff')
lblRole2.grid(row=1,column=0)
#===============================================================
#hall
f0b = Frame(Tops,bg="#6f85ff",relief=SUNKEN)
f0b.grid(row=0,column=1)

lblHall = Label(f0b,font=('Fixedsys',50,'bold'),
                text="\tMONITOR\t\t",fg="#fcbc02",background='#6f85ff')
lblHall.grid(row=0,column=0)
lblHall2 = Label(f0b,font=('Fixedsys',40,'bold'),
                textvariable=str(Clock()),fg="#f8f9fa",background='#6f85ff')
lblHall2.grid(row=2,column=0)

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

# lblInfo3 = Label(f0,font=('Fixedsys',50,'bold'),
#                 text="\t\t",fg="#f8f9fa",bd=10)
# lblInfo3.grid(row=0,column=2)
# lblRole3 = Label(f0,font=('Fixedsys',40,'bold'),
#                 text="\t\t",fg="#f8f9fa",bd=10)
# lblRole3.grid(row=1,column=2)


def setNameWinner(name):
    global winner_name
    pass

def clearHall():
    End = tkinter.messagebox.askyesno("TIC TAC TOE","Confirm clear?")
    if End > 0:
        emptyDict = {}
        with open('statics.json','w',encoding='utf-8') as file:
            file.write(json.dumps(emptyDict,indent=1))
            #json.dump(emptyDict,file)
            file.close()
        with open('statics_players.json','w',encoding='utf-8') as file:
            file.write(json.dumps(emptyDict,indent=1))
            #json.dump(emptyDict,file)
            file.close()
        print('clear hall data. ')
        return
    

def hallOfFrame():
    global getdata,getStatic
    txtHall.delete("1.0","end")
    txtHall.insert(END,"Rank"+"\tName"+"\tRound"+"\tWin"+"\tLoss"+"\tDraw" + '\n')
    ranking = 0
    with open('statics.json','r') as j:
        getdata = json.load(j)
        j.close()
    for played in getdata :
            bogie = TheTrain(getStatic[played])
            ranking += 1
            txtHall.insert(END,str(ranking)+'\t'+str(played)+'\t'+str(bogie[0]) +'\t'+ str(bogie[1]) +'\t'+ str(bogie[2]) +'\t'+ str(bogie[3]) + '\n')
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
    End = tkinter.messagebox.askyesno("TIC TAC TOE","Confirm exit")
    if End > 0:
        if runnerServer:
            server.close()
        root.destroy()
        return
    
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
def addHistory(name,walk):
    global namelst,walklst
    print('addHistory call')
    namelst.append(name)
    walklst.append(walk)
def logWalk():
    print("logWalk call")
    global txtWalk
    try:
        made = Toplevel(root)
        made.geometry('400x500')
        made.title("Walk log")
        made.configure(bg="#6f85ff")
        fr1 = Frame(made,width=1000,height=200,bg="#6f85ff",relief=SUNKEN)
        fr1.pack(side=TOP)
        txtWalkLabel = Label(fr1,text='History',font=('TH Sarabun New',17,'bold'),bg="#6f85ff")
        txtWalkLabel.grid(row=0,column=0)
        fr2 = Frame(made,width=1000,height=200,bg="#6f85ff",relief=SUNKEN)
        txtWalk = Text(fr2,font=('TH Sarabun New',18,'bold'), bd=8,width=25,height=15,bg="#6f85ff")
        txtWalk.grid(row=0,column=0)
        txtWalk.insert(END,'=======================')

        
        if len(namelst)==0:
            txtWalk.insert(END,'No history\n')
        else:
            txtWalk.insert(END,'Name\t\tWalk\n')
        for i in range(len(namelst)):
            txtWalk.insert(END,str(namelst[i])+' \t\t'+str(walklst[i])+' \n')
        txtWalk.insert(END,'=======================')
        txtWalk.configure(state='disabled')
        fr2.pack(side=BOTTOM)
        made.resizable(False,False)
        made.mainloop()
    except:
        print('Tk exception')
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
    print('default call')
    global record,server,threadLock,CONNECTIONS_LIST,PORT,BUFSIZE
    global msg,msg_monitor,nameSet,count,stopState,runnerServer,haveWinner
    global getdata,getStatic
    #hallOfFrame()
    #stateServer.set('Server ready')
    stopState = False
    count = 0
    nameSet = True 
    runnerServer = False
    haveWinner = True
    player1Label.set('Name')
    player2Label.set('Name')    
    msg_monitor = ['1','2','3','4','5','6','7','8','9']
    msg = ['1','2','3','4','5','6','7','8','9']
    ip_Input.set('')
    port_Input.set('')
    



def startServer():
    global threadLock,CONNECTIONS_LIST,server,record,msg_monitor,nameSet,runnerServer
    
    resetToDefault()
    if (len(ip_Input.get())==0 or len(port_Input.get())==0) :
        print('No input')
        stateServer.set('Error ip/port')
    else:
        try:
            runnerServer = True
            IPADDRESS =ip_Input.get()
            PORT =  int(port_Input.get())
            if PORT <1025 or PORT > 65535:
                PORT = "x"
            ADDRESS = (IPADDRESS,PORT)
            CONNECTIONS_LIST = []
        except ValueError:
            runnerServer = False
            stateServer.set('invalid input')
    
        try:
            threadLock = threading.Lock()
            record = chatRecord()
            server = socket(AF_INET,SOCK_STREAM)
            server.bind(ADDRESS)
            server.listen(2)
            CONNECTIONS_LIST.append(server)
            print('List')
            print(CONNECTIONS_LIST)
            gamePlay = True
        except OSError:
            runnerServer = False
            stateServer.set('Ip/port already in use')
            gamePlay = False
        except TypeError:
            runnerServer = False
            gamePlay = False
            print('TypeError')
            stateServer.set('invalid input')
        if gamePlay:
            print("Chat server started on IP Address : ",IPADDRESS)
            print("Chat server started on port : "+str(PORT))
            
            offConnection()
            #====================================
            print('Waiting for connection...')
            print('player now:'+ str(record.returnCount()))
            stateServer.set('Server currently running')

        
        while(gamePlay):
            try:
                if (record.returnCount())<2:
                    client,address = server.accept()
                    record.countPlayer+=1
                    print('Player: '+str(record.countPlayer))
                    print("...connected from:"+str(client)+" addr "+str(address))
                    runnerServer = True
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
                runnerServer = False
                stateServer.set('detect error pls restart.')
                server.close()
                onConnection()
        

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>server manage<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
Bottoms = Frame(root,width=1600,bg="#6f85ff",relief=SUNKEN)
Bottoms.pack(side=BOTTOM)

f1 = Frame(Bottoms,width=800,height=700,bg="",relief=SUNKEN)
f1.grid(row=0,column=1)

f2 = Frame(Bottoms,width=600,height=700,relief=SUNKEN)
f2.grid(row=0,column=2)
f2.configure(background='#6f85ff')
f3 = Frame(Bottoms,width=500,height=700,bg='#6f85ff')
f3.grid(row=0,column=3)
lblInfox = Label(f3,font=('Fixedsys',30,'bold'),
                text="Hall Of Fame",fg="#f8f9fa",bd=5,bg='#6f85ff')
lblInfox.grid(row=0,column=0)
txtHall = Text(f3,font=('TH Sarabun New',17,'bold'), bd=8,width=45,height=15,bg="#feeafa")
txtHall.grid(row=1,column=0)


chkTime = 0



#==========================Fonts==========================================
#font.Font(family='Helvetica', size=12, weight='bold')
font1 = TkFont.Font(family="Fixedsys",size = 20,weight = 'bold')

#===============================Calculator Frame===========================
txtDisplayState = Label(f2,font=font1,
                text="State",fg="#f8f9fa",bd=10,bg='#6f85ff')


txtDisplayState.grid(columnspan=4)
txtDisplay = Entry(f2,font=font1,
                   textvariable=statePlayer,bd=30,insertwidth=4,
                   bg="#49A",justify='right',state='disabled',disabledbackground='#6f85ff')
txtDisplay.grid(columnspan=4)

btnWidth = 5
btnHeight = 1

#===============================Row5=======================================
btn1 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text1,width=btnWidth,
              height=btnHeight,
              bg="#fec89a")
btn1.grid(row=3,column=0)

btn2 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text2,width=btnWidth,
              height=btnHeight,bg="#fec89a")
btn2.grid(row=3,column=1)

btn3 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text3,width=btnWidth,
              height=btnHeight,bg="#fec89a")
btn3.grid(row=3,column=2)
#===============================Row4=======================================
btn4 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text4,width=btnWidth,
              height=btnHeight,bg="#fec89a")
btn4.grid(row=4,column=0)

btn5 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text5,width=btnWidth,
              height=btnHeight,bg="#fec89a")
btn5.grid(row=4,column=1)

btn6 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text6,width=btnWidth,
              height=btnHeight,bg="#fec89a")
btn6.grid(row=4,column=2)

#===============================Row3=======================================

btn7 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text7,width=btnWidth,
              height=btnHeight,bg="#fec89a")
btn7.grid(row=5,column=0)

btn8 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text8,width=btnWidth,
              height=btnHeight,bg="#fec89a")
btn8.grid(row=5,column=1)

btn9 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text9,width=btnWidth,
              height=btnHeight,bg="#fec89a")
btn9.grid(row=5,column=2)

btnClear = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              text="CLEAR",width=23,
              height=btnHeight,bg="#f07167",command=lambda:resetToDefault())
btnClear.grid(row=6,columnspan=3)

#offButton()

lblReference = Label(f1,font=font1, text="State",
                     bd=16,anchor='w',bg="#6f85ff").grid(row=0,column=0)  
txtReference = Entry(f1,font=font1,textvariable=stateServer,
                     bd=10,insertwidth=4,bg='#49A',justify='right'
                     ,state='disabled',disabledbackground='#6f85ff').grid(row=0,column=1)

#-----------------------------------------------------------------------------------------------------
lblIp = Label(f1,font=font1, text="ip"
                 ,bd=16,anchor='w',bg="#6f85ff").grid(row=1,column=0)  
txtIp = Entry(f1,font=font1,textvariable=ip_Input,
                     bd=10,insertwidth=4,bg='white',justify='right')
txtIp.grid(row=1,column=1)

#-----------------------------------------------------------------------------------------------------
lblPort = Label(f1,font=font1, text="Port"
                 ,bd=16,anchor='w',bg="#6f85ff").grid(row=2,column=0)  
txtPort = Entry(f1,font=font1,textvariable=port_Input,
                     bd=10,insertwidth=4,bg='white',justify='right')
txtPort.grid(row=2,column=1)  


btnStart = Button(f1,padx=8,pady=10,bd=16,fg="black",font=font1,
                  width=10,text="Connect",bg="#7ac000",command=lambda:startServer())
btnStart.grid(row=7,column=1)
btnTry = Button(f1,padx=50,pady=10,bd=16,fg="black",font=font1,
                  width=5,text="Exit",bg="#7ac000",command=closeGame)
btnTry.grid(row=8,column=1)
menubar= Menu(root)
filemenu = Menu(menubar, tearoff =0,font= 'Helvetica 30 bold')
menubar.add_cascade(label="File",font= 'Helvetica 30 bold',menu=filemenu)
filemenu.add_command(label="Walk History ",command=logWalk)
filemenu.add_command(label="Clear hall Of  fame",command=clearHall)
filemenu.add_command(label="Exit", command = closeGame)

root.config(menu=menubar)
root.attributes('-fullscreen', True)  
#root.resizable(False,False)
hallOfFrame()
upDate()
root.mainloop()  
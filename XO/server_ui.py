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
                text="Player1\t",fg="Blue",bd=10,background='powder blue')
lblInfo.grid(row=0,column=0)
lblRole = Label(f0,font=('Microsoft YaHei Light',40,'bold'),
                text="Name\t",fg="Blue",bd=10,background='powder blue')
lblRole.grid(row=1,column=0)
#bank zone
#===============================================================
f0a = Frame(Tops,bg="powder blue",relief=SUNKEN)
f0a.grid(row=0,column=2)
lblAir = Label(f0a,font=('Microsoft YaHei Light',50,'bold'),
                text="\tPlayer2     ",fg="Blue",bd=10,background='powder blue')
lblAir.grid(row=0,column=0)
lblAir2 = Label(f0a,font=('Microsoft YaHei Light',40,'bold'),
                text="\tName    ",fg="Blue",bd=10,background='powder blue')
lblAir2.grid(row=1,column=0)
#===============================================================
#hall
f0b = Frame(Tops,bg="powder blue",relief=SUNKEN)
f0b.grid(row=0,column=1)

lblHall = Label(f0b,font=('Microsoft YaHei Light',50,'bold'),
                text="\tMonitor",fg="Blue",bd=10,background='powder blue')
lblHall.grid(row=0,column=0)
lblHall2 = Label(f0b,font=('Microsoft YaHei Light',40,'bold'),
                textvariable=Clock(),fg="Blue",bd=10,background='powder blue')
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

def communication():
    pass

def offButton():
    pass
def closeGame():
    root.destroy()
    return 0

def configuration():
    pass
def playAgain():
    pass

def disConnected():
    pass
def default(mode):
    pass
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
f3 = Frame(Bottoms,width=500,height=700,bg='powder blue')
#f3.pack(side=RIGHT)
f3.grid(row=1,column=3)
lblInfox = Label(f3,font=('Microsoft YaHei Light',40,'bold'),
                text="ROW0\t      ",fg="Blue",bd=5,bg='powder blue')
lblInfox.grid(row=0,column=0)
lblRolex = Label(f3,font=('Microsoft YaHei Light',40,'bold'),
                text='ROW1\t      ',fg="Blue",bd=10,bg='powder blue')
lblRolex.grid(row=1,column=0)
lblRolex1 = Label(f3,font=('Microsoft YaHei Light',40,'bold'),
                text='ROW2\t      ',fg="Blue",bd=10,bg='powder blue')
lblRolex1.grid(row=2,column=0)
lblRolex2 = Label(f3,font=('Microsoft YaHei Light',40,'bold'),
                text='ROW3\t      ',fg="Blue",bd=10,bg='powder blue')
lblRolex2.grid(row=3,column=0)
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
              text="SERVER",width=23,
              height=btnHeight,bg="#49A",state="disabled")
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


btnStart = Button(f1,padx=16,pady=16,bd=16,fg="black",font=font1,
                  width=10,text="Connect",bg="#49A")
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
default("Client")
root.mainloop()  
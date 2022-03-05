from tkinter import *
import tkinter.font as TkFont
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
#label
lblInfo = Label(Tops,font=('TH Sarabun New',50,'bold'),
                text="Tic-tac-toe",fg="Blue",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)


#function
stateServer= StringVar()
statePlayer= StringVar()
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

#Default
text1.set('  ')
text2.set('  ')
text3.set('  ')
text4.set('  ')
text5.set('  ')
text6.set('  ')
text7.set('  ')
text8.set('  ')
text9.set('  ')
#inform inpit
operator = True
number = ['  ','  ','  ','  ','  ','  ','  ','  ','  ']
stateBtn=[False,False,False,False,False,False,False,False,False]

buttons = []
def btnClick(numbers):
    global operator
    if operator == True:
        
        if stateBtn[numbers-1]==False:
           stateBtn[numbers-1]=True
           number[numbers-1]='x'
           operator = False
        
        
    else:
        
        if stateBtn[numbers-1]==False:
           stateBtn[numbers-1]=True
           number[numbers-1]='o'
           operator = True   
    text1.set(number[0])
    text2.set(number[1])
    text3.set(number[2])
    text4.set(number[3])
    text5.set(number[4])
    text6.set(number[5])
    text7.set(number[6])
    text8.set(number[7])
    text9.set(number[8])
def getStart():
    if len(ip_Input.get())==0 or len(port_Input.get())==0:
        top = Toplevel(root) 
        top.geometry("500x200")
        l2 = Label(top,padx=16,pady=16,bd=8,fg="black",
              font=font1, text = "ip/port error") 
        l2.pack()
        top.mainloop()  
    else:
        try:
            server = ip_Input.get()
            port = int(port_Input.get())
        except ValueError:
            stateServer.set("Server not response")
        try:
            s.connect((server, port))
            state = True
            stateServer.set("Connected")
        except ConnectionResetError and TimeoutError and OSError :
            state = False
            stateServer.set("Server not response")
            print("Server not response")
    
    print(server)
    print(port)
#==========================Fonts==========================================
#font.Font(family='Helvetica', size=12, weight='bold')
font1 = TkFont.Font(family="Consolas",size = 20,weight = 'bold')

#===============================Calculator Frame===========================
txtDisplayState = Label(f2,font=font1,
                text="State",fg="Blue",bd=10,anchor='w')


txtDisplayState.grid(columnspan=4)
txtDisplay = Entry(f2,font=font1,
                   textvariable=statePlayer,bd=30,insertwidth=4,bg="powder blue",justify='right',state='disabled',disabledbackground='powder blue')
txtDisplay.grid(columnspan=4)
#===============================Row5=======================================
btn1 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text1,bg="powder blue",command=lambda:btnClick(1)).grid(row=5,column=0)

btn2 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text2,bg="powder blue",command=lambda:btnClick(2)).grid(row=5,column=1)

btn3 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text3,bg="powder blue",command=lambda:btnClick(3)).grid(row=5,column=2)
#===============================Row4=======================================
btn4 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text4,bg="powder blue",command=lambda:btnClick(4)).grid(row=4,column=0)

btn5 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text5,bg="powder blue",command=lambda:btnClick(5)).grid(row=4,column=1)

btn6 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text6,bg="powder blue",command=lambda:btnClick(6)).grid(row=4,column=2)

#===============================Row3=======================================

btn7 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text7,bg="powder blue",command=lambda:btnClick(7)).grid(row=3,column=0)

btn8 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text8,bg="powder blue",command=lambda:btnClick(8)).grid(row=3,column=1)

btn9 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=font1,
              textvariable=text9,bg="powder blue",command=lambda:btnClick(9)).grid(row=3,column=2)





lblReference = Label(f1,font=font1, text="State",
                     bd=16,anchor='w').grid(row=0,column=0)  
txtReference = Entry(f1,font=font1,textvariable=stateServer,
                     bd=10,insertwidth=4,bg='powder blue',justify='right',state='disabled',disabledbackground='powder blue').grid(row=0,column=1)

#-----------------------------------------------------------------------------------------------------
lblMenu1 = Label(f1,font=font1, text="ip"
                 ,bd=16,anchor='w').grid(row=1,column=0)  
txtMenu1 = Entry(f1,font=font1,textvariable=ip_Input,
                     bd=10,insertwidth=4,bg='powder blue',justify='right').grid(row=1,column=1)

#-----------------------------------------------------------------------------------------------------
lblMenu2 = Label(f1,font=font1, text="port"
                 ,bd=16,anchor='w').grid(row=2,column=0)  
txtMenu2 = Entry(f1,font=font1,textvariable=port_Input,
                     bd=10,insertwidth=4,bg='powder blue',justify='right').grid(row=2,column=1)  

btnStart = Button(f1,padx=16,pady=16,bd=16,fg="black",font=font1,
                  width=10,text="Start",bg="powder blue",command=getStart).grid(row=7,column=1)
root.mainloop()  
from tkinter import *
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
text_Input= StringVar()
ip_Input = StringVar()
port_Input = StringVar()

#inform inpit
operator = True
number = ['1','2','3','4','5','6','7','8','9']
def btnClick(numbers):
    global operator
    if operator == True:
        operator = False
        number[numbers-1]='x'
        
    else:
        operator = True
        number[numbers-1]='o'

    print(number[0])
    btn1['text']=number[0]
    btn2['text']=number[1]
    btn3['text']=number[2]
    btn4['text']=number[3]
    btn5['text']=number[4]
    btn6['text']=number[5]
    btn7['text']=number[6]
    btn8['text']=number[7]
    btn9['text']=number[8]
    


def getStart():
    pass


#===============================Calculator Frame===========================
txtDisplayState = Label(f2,font=('TH Sarabun New',40,'bold'),
                text="State",fg="Blue",bd=10,anchor='w')


txtDisplayState.grid(columnspan=4)
txtDisplay = Entry(f2,font=('TH Sarabun New',20,'bold'),
                   textvariable=text_Input,bd=30,insertwidth=4,bg="powder blue",justify='right',state='disabled',disabledbackground='powder blue')
txtDisplay.grid(columnspan=4)

#===============================Row3=======================================

btn7 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=('TH Sarabun New',20,'bold'),
              text="7",bg="powder blue",command=lambda:btnClick(7)).grid(row=3,column=0)

btn8 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=('TH Sarabun New',20,'bold'),
              text="8",bg="powder blue",command=lambda:btnClick(8)).grid(row=3,column=1)

btn9 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=('TH Sarabun New',20,'bold'),
              text="9",bg="powder blue",command=lambda:btnClick(9)).grid(row=3,column=2)

#===============================Row4=======================================
btn4 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=('TH Sarabun New',20,'bold'),
              text="4",bg="powder blue",command=lambda:btnClick(4)).grid(row=4,column=0)

btn5 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=('TH Sarabun New',20,'bold'),
              text="5",bg="powder blue",command=lambda:btnClick(5)).grid(row=4,column=1)

btn6 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=('TH Sarabun New',20,'bold'),
              text="6",bg="powder blue",command=lambda:btnClick(6)).grid(row=4,column=2)

#===============================Row5=======================================
btn1 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=('TH Sarabun New',20,'bold'),
              text="1",bg="powder blue",command=lambda:btnClick(1)).grid(row=5,column=0)

btn2 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=('TH Sarabun New',20,'bold'),
              text="2",bg="powder blue",command=lambda:btnClick(2)).grid(row=5,column=1)

btn3 = Button(f2,padx=16,pady=16,bd=8,fg="black",
              font=('TH Sarabun New',20,'bold'),
              text="3",bg="powder blue",command=lambda:btnClick(3)).grid(row=5,column=2)

lblReference = Label(f1,font=('TH Sarabun New',18,'bold'), text="State",
                     bd=16,anchor='w').grid(row=0,column=0)  
txtReference = Entry(f1,font=('TH Sarabun New',18,'bold'),textvariable="test",
                     bd=10,insertwidth=4,bg='powder blue',justify='right').grid(row=0,column=1)

#-----------------------------------------------------------------------------------------------------
lblMenu1 = Label(f1,font=('TH Sarabun New',18,'bold'), text="ip"
                 ,bd=16,anchor='w').grid(row=1,column=0)  
txtMenu1 = Entry(f1,font=('TH Sarabun New',18,'bold'),textvariable=ip_Input,
                     bd=10,insertwidth=4,bg='powder blue',justify='right').grid(row=1,column=1)

#-----------------------------------------------------------------------------------------------------
lblMenu2 = Label(f1,font=('TH Sarabun New',18,'bold'), text="port"
                 ,bd=16,anchor='w').grid(row=2,column=0)  
txtMenu2 = Entry(f1,font=('TH Sarabun New',18,'bold'),textvariable=port_Input,
                     bd=10,insertwidth=4,bg='powder blue',justify='right').grid(row=2,column=1)  

btnStart = Button(f1,padx=16,pady=16,bd=16,fg="black",font=("TH Sarabun New",15,'bold'),
                  width=10,text="Start",bg="powder blue",command=getStart).grid(row=7,column=1)
root.mainloop()   
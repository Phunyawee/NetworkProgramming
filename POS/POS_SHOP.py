from tkinter import *
import time
import json
from ftplib import FTP
import codecs
hour = ""
minute= ""
second= ""
shopname = ""
#===========================================TMP SHOP================================================================



#================================FTP Server============================================================
def downloadFile(ftp,filename):
    localfile = open(filename,'wb')
    ftp.retrbinary('RETR '+filename,localfile.write,1024)
    localfile.close()

def uploadFile(ftp,filename):
    ftp.encoding="utf-8"
    ftp.storbinary('STOR '+filename,open(filename,'rb'))

def ConnectFTPServer(FTPServer,Username,Password):
    global ftp
    try:
        ftp = FTP(FTPServer)
        ftp.login(user=Username,passwd = Password)
        ftp.retrlines('LIST')
        ftp.cwd('FTP')
        ftp.retrlines('LIST')
    except TimeoutError:
        print("TimeoutError")
    except ConnectionRefusedError:
        print("ConnectionRefusedError")
    finally:
        print("Success!!!")



#================================UI============================================================
root = Tk()
root.geometry("1600x800+0+0")
root.title("Parking Of Service SHOP")
root.configure(background="#2b2d42")

Tops = Frame(root, width=1600, height=150, bg="#d90429", relief=SUNKEN, bd=20)
Tops.pack(side=TOP,anchor=N)

#Bottom = Frame(root, width=1600, height=450, bg="powder blue", relief=SUNKEN)
#Bottom.pack(side=BOTTOM)

f1 = Frame(root, width=500, height=650, bg="#d90429", relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=500, height=650, bg="#2b2d42", relief=SUNKEN  , bd=10)
f2.pack(side=LEFT)

f3 = Frame(root, width=600, height=650,bg="#d90429", relief=GROOVE)
f3.pack(side=LEFT)

#------------------------------Varible----------------------

#Tops Varible
localtime = time.asctime(time.localtime(time.time()))
shopname_Output = StringVar()
#f1 Varible
showlogin_Output = StringVar()
shopname_Input = StringVar()
ftpserver_Input = StringVar()
username_Input = StringVar()
password_Input = StringVar()

modelogin_Input = IntVar()
loginbtn_Input = StringVar()
#f2 Varible
carrecent_Output = StringVar()
license_Input = StringVar()
amount_Input = StringVar()

#f3 Varible
receipt = StringVar()

#time
now = time.time()

#------------------------------Variable Function ----------------------
#showshopname_Output.set("กรุณาตั้งชื่อร้านของคุณ")
#Tops Function

def clock():
    global hour,minute,second
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%e")
    month = time.strftime("%B")
    year = time.strftime("%y")
    lblInfo.config(text=day+" "+month+" 20"+year+" "+hour+":"+minute+":"+second)
    lblInfo.after(1000,clock)

def Running():
    shopname_Output.set("กรุณาตั้งชื่อร้านของคุณ")
    loginbtn_Input.set("login")
    text_Receipt.insert(END,"ลำดับ     เวลา\t\tทะเบียนรถ\t"+"   จ่ายไป\tร้าน\tสถานะ\n")
    modelogin_Input.set(1)
    LoginMode()
    #Receipt()
    license_plate_entry .config(state='disabled')
    amount_entry .config(state='disabled')
    send_btn.config(state='disabled')
    refresh_btn.config(state='disabled')
#General Function
jsonDict =  {"id":"SE015",
             "carPlate":"532eaabd9574880dbf76b9b8cc00832c20a6ec113d682299550d7a6e0f345e25",
             "timeIn":"Suphapong Bunpunya",
             "Email":"suphapong.b@ku.th",
             "Telno":"0956321391"}

def CarDict(order,carPlate,timeIn,cost,shop,status):
    jsonDict =  {"order":order,
                 "carPlate":carPlate,
                 "timeIn":timeIn,
                 "cost":cost,
                 "shop":shop,
                 "status":status}
    return jsonDict

def WriteFile(filename,dict):
    with open(filename,'w') as file:
        json_object = json.dumps(dict, indent = 4)
        file.write(json_object)

def ReadFile(filename):
    with open(filename,'r') as j:
        userdata = json.load(j)
        print(type(userdata))
        print(userdata)
    return userdata
        

def ShowLogin(text):
    showlogin_Output.set(text)

def CheckSpace(text):
    if text!="":
        return True
    else:
        return False

def toggleText(varBtn,txt1,txt2):
    if varBtn.get() == txt1:
        varBtn.set(txt2)
    else:
        varBtn.set(txt1)
        shopname_entry.config(state='normal')
        ftpserver_entry.config(state='normal')
        username_entry.config(state='normal')
        password_entry.config(state='normal')

        modelogin1_radio.config(state='normal')
        modelogin2_radio.config(state='normal')

        ShowLogin("logout เสร็จสิ้น")


def LoginMode():
    selection = "selected " + str(modelogin_Input.get())
    showlogin_Output.set(selection)
    if modelogin_Input.get()==1:
        ftpserver_label.grid_forget()
        ftpserver_entry.grid_forget()
        username_label.grid_forget()
        username_entry.grid_forget()
        password_label.grid_forget()
        password_entry.grid_forget()
        return 1

    else:
        ftpserver_label.grid(column=0, row=3, sticky=W)
        ftpserver_entry.grid(columnspan=4, row=4)
        username_label.grid(column=0, row=5, sticky=W)
        username_entry.grid(columnspan=4, row=6)
        password_label.grid(column=0, row=7, sticky=W)
        password_entry.grid(columnspan=4,row=8)
        return 2

def LoginBtn():
    if LoginMode() == 1:
        AutoLogin()
    else:
        Login()

def AutoLogin():
    global shopname
    showlogin_Output.set("ShopTEST")
    shopname = shopname_Input.get()
    ftpServer = "10.64.39.141"
    username = "NetPro"
    password = "800"

    #FTPServer(ftpServer,username,password)

    if CheckSpace(shopname_Input.get()):
        ConnectFTPServer(ftpServer,username,password)
        shopname_Output.set(shopname)
        shopname_entry.config(state='disabled')
        modelogin1_radio.config(state='disabled')
        modelogin2_radio.config(state='disabled')

        license_plate_entry .config(state='normal')
        amount_entry .config(state='normal')
        send_btn.config(state='normal')
        refresh_btn.config(state='normal')

        toggleText(loginbtn_Input,"login","logout")
        downloadFile(ftp,'Write.json')
        ShowLogin("login to FTP Server สำเร็จ !")
        print("login สำเร็จ")
    else:
        showlogin_Output.set("กรุณากรอกให้ครบ")

    print("ftpServer:",ftpServer)
    print("username:",username)
    print("password:",password)

def Login():
    global shopname
    showlogin_Output.set("")
    shopname = shopname_Input.get()
    ftpServer = ftpserver_Input.get()
    username = username_Input.get()
    password = password_Input.get()

    #FTPServer(ftpServer,username,password)

    if(CheckSpace(shopname_Input.get()) & CheckSpace(ftpServer) & CheckSpace(username) & CheckSpace(password)):
        ConnectFTPServer(ftpServer,username,password)
        shopname_Output.set(shopname)
        shopname_entry.config(state='disabled')
        ftpserver_entry.config(state='disabled')
        username_entry.config(state='disabled')
        password_entry.config(state='disabled')
        modelogin1_radio.config(state='disabled')
        modelogin2_radio.config(state='disabled')

        license_plate_entry .config(state='normal')
        amount_entry .config(state='normal')
        send_btn.config(state='normal')
        refresh_btn.config(state='normal')

        toggleText(loginbtn_Input,"login","logout")
        downloadFile(ftp,'Write.json')
        ShowLogin("login to FTP Server สำเร็จ !")
        print("login สำเร็จ")
    else:
        showlogin_Output.set("กรุณากรอกให้ครบ")

    print("ftpServer:",ftpServer)
    print("username:",username)
    print("password:",password)
    

#f2 Function
dict_arr = []
carplateList = []
car_order = -1

def CheckCarPlate(customer):
    global carplateList
    userdata = ReadFile('Check.json')
    for car in userdata:
        if car["carPlate"] == customer:
            if car["status"] == 1:
                print(str(customer)+" รถทะเบียนนี้ออกไปเเล้ว")
                carrecent_Output.set(str(customer)+" รถทะเบียนนี้ออกไปเเล้ว")
            else:
                carplateList.append(customer)
                print(str(customer)+" เพิ่มไปเเล้ว")
                #carrecent_Output.set(str(customer)+" รถทะเบียนนี้ออกไปเเล้ว")
                return True
    return False



def Summit():
    global dict_arr, car_order, shopname
    license = license_Input.get()
    cost  = amount_Input.get()
    downloadFile(ftp,'Write.json')

    if(CheckSpace(license) & CheckSpace(cost)):
            if CheckCarPlate(license):
                print("car_order",car_order)
                timeIn = hour+":"+minute+":"+second
                carrecent_Output.set(timeIn+" ทบล: "+license+" จ่าย: "+cost+" บาท")
                dict_arr = ReadFile('Write.json')
                car_order = int(dict_arr[len(dict_arr)-1]["order"])+1
                dict_arr.append(CarDict(car_order,license,timeIn,cost,shopname,0))
                WriteFile('Write.json',dict_arr)
                Receipt()
                print(dict_arr)

                uploadFile(ftp,'Write.json')
                print('Write.json ถูกอัปเเล้ว')
                ftp.retrlines('LIST')

                #Clear & Reset
                license_Input.set("")
                amount_Input.set("")
            else:
                carrecent_Output.set(license+" ไม่มีทะเบียนนี้อยู่ในระบบ")

    else:
        root = Tk()
        root.geometry("250x100+0+0")
        root.title("คำเตือน")
        label = Label(root, text="กรุณากรอกข้อมูลให้ถูกต้อง")
        label.pack(side="top", fill="x", pady=10)
        B1 = Button(root, text="Okay", command = root.destroy)
        B1.pack()
        root.mainloop()

    print(shopname_Output)

def Refresh():
    downloadFile(ftp,'Write.json')
    Receipt()

#f3 Function
def Receipt():
    data = ReadFile('Write.json')
    text_Receipt.delete("1.0","end")
    text_Receipt.insert(END,"ลำดับ      เวลา\t\tทะเบียนรถ\t"+"   จ่ายไป\t     ร้าน\t\t      สถานะ\n")
    for list in data:
        print(list["order"])
        print(list["shop"])
        text_Receipt.insert(END,"   "+str(list["order"])+"         "+str(list["timeIn"])+
                            "\t\t"+str(list["carPlate"])+"\t   "+str(list["cost"])+
                            " ฿\t     "+str(list["shop"])+"\t\t       "+str(list["status"])+"\n")


#--------------------------------TOPS-------------------------------
lblInfo = Label(Tops,font=('TH Sarabun New',60,'bold'),
                    textvariable=shopname_Output,fg="#2b2d42",bd=10,anchor='w',bg="#8d99ae",relief=SUNKEN)
lblInfo.grid(row=0,column=0)

lblInfo = Label(Tops,font=('TH Sarabun New',30,'bold'),
                text="",fg="white",bg="#8d99ae",bd=10,anchor='w',relief=SUNKEN)
lblInfo.grid(row=1,column=0)

lblBlank = Label(f2,font=('TH Sarabun New',50,'bold'),
                text="",fg="#2b2d42",bd=10,anchor='w')
lblBlank.grid(row=7,column=0)

#------------------------f1 Left-----------------------------
showlogin_entry = Entry(f1,font=('TH Sarabun New',30,'bold'),state='disable',disabledbackground='#ef233c',
                        disabledforeground='white',textvariable=showlogin_Output,bd=20,insertwidth=10,
                        bg="powder blue",justify='right')
showlogin_entry.grid(columnspan=4, row=0)

shopname_label = Label(f1, text="ชื่อร้าน:", font=('TH Sarabun New',16,'bold'))
shopname_label.grid(column=0, row=1, sticky=W)
shopname_entry = Entry(f1,font=('TH Sarabun New',16,'bold'),
                       textvariable=shopname_Input,bd=20,insertwidth=5,width=30,
                       bg="white",justify='right')
shopname_entry.grid(columnspan=4, row=2)

ftpserver_label = Label(f1, text="FTP-Server:", font=('TH Sarabun New',16,'bold'))
ftpserver_label.grid(column=0, row=3, sticky=W)
ftpserver_entry = Entry(f1,font=('TH Sarabun New',16,'bold'),
                        textvariable=ftpserver_Input,bd=20,insertwidth=5,width=30,
                        bg="white",justify='right')
ftpserver_entry.grid(columnspan=4, row=4)

username_label = Label(f1, text="Username:", font=('TH Sarabun New',16,'bold'))
username_label.grid(column=0, row=5, sticky=W)
username_entry = Entry(f1,font=('TH Sarabun New',16,'bold'),
                       textvariable=username_Input,bd=20,insertwidth=5,width=30,
                       bg="white",justify='right')
username_entry.grid(columnspan=4, row=6)

password_label = Label(f1, text="Password:", font=('TH Sarabun New',16,'bold'))
password_label.grid(column=0, row=7, sticky=W)
password_entry = Entry(f1,font=('TH Sarabun New',16,'bold'),
                       textvariable=password_Input,bd=20,insertwidth=5,width=30,
                       bg="white",justify='right')
password_entry.grid(columnspan=4,row=8)

modelogin_label = Label(f1, text="login mode:", font=('TH Sarabun New',14,'bold'))
modelogin_label.grid(column=0, row=9, sticky=W,pady=10)
modelogin1_radio = Radiobutton(f1, text="Auto", variable=modelogin_Input, value=1,command=lambda:LoginMode())
modelogin1_radio.grid(column=1,row=9)
modelogin2_radio = Radiobutton(f1, text="Manual", variable=modelogin_Input, value=2,command=lambda:LoginMode())
modelogin2_radio.grid(column=2,row=9)

login_btn = Button(f1,padx=16, fg="black",font=('TH Sarabun New',18,'bold'),width=8,
                   textvariable=loginbtn_Input,command=lambda:LoginBtn()).grid(padx=20,pady=10,column=0,row=10)
"""
autologin_btn = Button(f1,padx=16, fg="black",font=('TH Sarabun New',18,'bold'),width=8,
                   textvariable=loginbtn_Input,command=lambda:AutoLogin()).grid(padx=20, pady=20,column=1,row=10)
"""
#------------------------f2 Center-----------------------------
carrecent_label = Label(f2, text="ลูกค้าที่เข้ามาล่าสุด: ", font=('TH Sarabun New',20,'bold'))
carrecent_label.grid(column=0,row=0,sticky=W)
carrecent_entry = Entry(f2,font=('TH Sarabun New',20,'bold'),state='disable',disabledbackground='#8d99ae',
                            disabledforeground='black',textvariable=carrecent_Output,bd=30,insertwidth=4,width=30,
                            bg="#8d99ae",justify='right')
carrecent_entry.grid(columnspan=4,row=1,sticky=N)

license_plate_labal = Label(f2, text="ป้ายทะเบียนรถ: ", font=('TH Sarabun New',20,'bold'))
license_plate_labal.grid(column=0,row=2,sticky=W)
license_plate_entry = Entry(f2,font=('TH Sarabun New',20,'bold'),
                            textvariable=license_Input,bd=30,insertwidth=4,
                            bg="white",justify='right')
license_plate_entry.grid(columnspan=4,row=3,sticky=N)

amount_label = Label(f2, text="จำนวนเงิน: ", font=('TH Sarabun New',20,'bold'))
amount_label.grid(column=0,row=4,sticky=W)
amount_entry = Entry(f2,font=('TH Sarabun New',20,'bold'),
                     textvariable=amount_Input,bd=30,insertwidth=4,
                     bg="white",justify='right')
amount_entry.grid(columnspan=4,row=5,sticky=N)

send_btn = Button(f2,padx=30, fg="black",font=('TH Sarabun New',18,'bold'),width=8,
                    text="ส่ง",command=lambda:Summit())
send_btn .grid(padx=20, pady=20,columnspan=4,row=6)

refresh_btn = Button(f2,padx=30, fg="black",font=('TH Sarปabun New',18,'bold'),width=8,
                  text="รีเฟรช",command=lambda:Refresh())
refresh_btn.grid(padx=20, pady=20,columnspan=4,row=7)
#------------------------f3 Right-----------------------------
label_Receipt = Label(f3,font=('TH Sarabun New',20,'bold'),
                      text="ประวัติ",bd=2,justify='right')
label_Receipt.grid(column=0,row=1,sticky=W)
text_Receipt = Text(f3,font=('TH Sarabun New',12,'bold'),
                    bd=5,width=60,height=30,bg="#e5dcdc")
text_Receipt.grid(column=0,row=2,sticky=W)


Running()
clock()
















root.mainloop()
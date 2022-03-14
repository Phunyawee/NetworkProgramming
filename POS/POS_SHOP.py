from tkinter import *
import time
import json
from ftplib import FTP
import codecs

hour = ""
minute= ""
second= ""
#===========================================TMP SHOP================================================================



#================================FTP Server============================================================
def downloadFile(ftp,filename):
    filename = 'NetProScore.txt'
    localfile = open(filename,'wb')
    ftp.retrbinary('RETR '+filename,localfile.write,1024)
    localfile.close()

def uploadFile(ftp,filename):
    ftp.encoding="utf-8"
    filename = '6230300923.txt'
    ftp.storbinary('STOR '+filename,open(filename,'rb'))

def ConnectFTPServer(FTPServer,Username,Password):
    try:
        with open('LoginFTPServer.json','r') as j:
            FTPLogin = json.load(j)
            print("FTPServer:", FTPServer)
            print("Username:", Username)
            print("Password:", Password)

        ftp = FTP(FTPServer)
        ftp.login(user=Username,passwd = Password)
        ftp.retrlines('LIST')
        try:
            downloadFile()
        except:
            print("File not found")

        Dict_Allscore = {}
        try:
            input = open("NetProScore.txt")
            for line in input:
                no, id, Score_P1, Score_P2 = line.split()
                Dict_Allscore[id] = int(Score_P1)+int(Score_P2)
        except ValueError:
            print("ValueError")
        except NameError:
            print("NameError")

        AllScore = Dict_Allscore.values()
        Max_Score = max(AllScore)
        Min_Score = min(AllScore)
        Avg_Score = int(sum(AllScore)/len(AllScore))
        My_Score = int(Dict_Allscore["6230300923"])

        try:
            outfile = codecs.open('6230300923.txt',"w","utf-8")

            outfile.write("คะเเนนสูงสุด "+str(Max_Score)+" คะเเนน\n")
            outfile.write("คะเเนนต่ำสุด "+str(Min_Score)+" คะเเนน\n")
            outfile.write("คะเเนนเฉลี่ย "+str(Avg_Score)+" คะเเนน\n")
            outfile.write("รหัส 6230300923 ได้คะเนนรวม "+str(My_Score)+" คะเเนน\n")
            outfile.write("ได้น้อยกว่าคะเเนนสูงสุด "+ str(Max_Score-My_Score)+" คะเเนน\n")
            outfile.write("ได้มากกว่ากว่าคะเเนนต่ำสุด "+ str(My_Score-Min_Score)+" คะเเนน\n")
            if My_Score >= Avg_Score:
                outfile.write("ได้มากกว่าคะเเนนเฉลี่ย "+str(My_Score-Avg_Score)+" คะเเนน\n")
            else:
                outfile.write("ได้น้อยกว่าคะเเนนเฉลี่ย "+str(Avg_Score-My_Score)+" คะเเนน\n")
            outfile.close()
        except IOError:
            print("IOError")
        except NameError:
            print("NameError")

        try:
            ftp.mkd('6230300923')
            ftp.cwd('6230300923')

        except:
            ftp.cwd('6230300923')

        try:
            uploadFile()
        except FileNotFoundError:
            print("No such file or directory")

        ftp.retrlines('LIST')
        ftp.quit()
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
root.configure(background="#ffecad")

Tops = Frame(root, width=1600, height=150, bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP,anchor=N)

#Bottom = Frame(root, width=1600, height=450, bg="powder blue", relief=SUNKEN)
#Bottom.pack(side=BOTTOM)

f1 = Frame(root, width=500, height=650, bg="red", relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=500, height=650, bg="blue", relief=RAISED)
f2.pack(side=LEFT)

f3 = Frame(root, width=600, height=650,bg="yellow", relief=GROOVE)
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
    text_Receipt.insert(END,"ลำดับ     เวลา\t\tทะเบียนรถ\t"+"   จ่ายไป\tสถานะ\n")
    Receipt()

#General Function
jsonDict =  {"id":"SE015",
             "carPlate":"532eaabd9574880dbf76b9b8cc00832c20a6ec113d682299550d7a6e0f345e25",
             "timeIn":"Suphapong Bunpunya",
             "Email":"suphapong.b@ku.th",
             "Telno":"0956321391"}

def CarDict(order,carPlate,timeIn,cost,status):
    jsonDict =  {"order":order,
                 "carPlate":carPlate,
                 "timeIn":timeIn,
                 "cost":cost,
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
        ShowLogin("logout เสร็จสิ้น")


def Login():
    showlogin_Output.set("")
    ftpServer = ftpserver_Input.get()
    username = username_Input.get()
    password = password_Input.get()

    #FTPServer(ftpServer,username,password)

    if(CheckSpace(shopname_Input.get()) & CheckSpace(ftpServer) & CheckSpace(username) & CheckSpace(password)):
        shopname_Output.set(shopname_Input.get())
        shopname_entry.config(state='disabled')
        ftpserver_entry.config(state='disabled')
        username_entry.config(state='disabled')
        password_entry.config(state='disabled')
        ShowLogin("สำเร็จ")
        toggleText(loginbtn_Input,"login","logout")
        print()
    else:
        showlogin_Output.set("กรุณากรอกให้ครบ")

    print("ftpServer:",ftpServer)
    print("username:",username)
    print("password:",password)
    

#f2 Function
dict_arr = []
car_order = -1
def Summit():
    global dict_arr
    license = license_Input.get()
    cost  = amount_Input.get()

    if(CheckSpace(license) & CheckSpace(cost)):
        timeIn = hour+":"+minute+":"+second
        carrecent_Output.set(timeIn+" ทบล: "+license+" จ่าย: "+cost+" บาท")
        dict_arr = ReadFile('Write.json')
        dict_arr.append(CarDict((car_order+1),license,timeIn,cost,0))
        WriteFile('Write.json',dict_arr)
        Receipt()
        print(dict_arr)

        #Clear & Reset
        license_Input.set("")
        amount_Input.set("")

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
#f3 Function

def Receipt():
    data = ReadFile('Write.json')
    text_Receipt.delete("1.0","end")
    text_Receipt.insert(END,"ลำดับ     เวลา\t\tทะเบียนรถ\t"+"   จ่ายไป\tสถานะ\n")
    for list in data:
        print(list["order"])
        text_Receipt.insert(END,str(list["order"])+"           "+str(list["timeIn"])+
                            "\t\t"+str(list["carPlate"])+"\t   "+str(list["cost"])+"\t "+str(list["status"])+"\n")


#--------------------------------TOPS-------------------------------
lblInfo = Label(Tops,font=('TH Sarabun New',50,'bold'),
                textvariable=shopname_Output,fg="Blue",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo = Label(Tops,font=('TH Sarabun New',50,'bold'),
                text="",fg="Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)

lblBlank = Label(f2,font=('TH Sarabun New',50,'bold'),
                text="",fg="Blue",bd=10,anchor='w')
lblBlank.grid(row=7,column=0)

#------------------------f1 Left-----------------------------
showlogin_entry = Entry(f1,font=('TH Sarabun New',30,'bold'),state='disable',disabledbackground='red',
                        disabledforeground='white',textvariable=showlogin_Output,bd=20,insertwidth=10,
                        bg="powder blue",justify='right')
showlogin_entry.grid(columnspan=4, row=0)

shopname_label = Label(f1, text="ชื่อร้าน:", font=('TH Sarabun New',20,'bold'))
shopname_label.grid(column=0, row=1, sticky=W)
shopname_entry = Entry(f1,font=('TH Sarabun New',16,'bold'),
                       textvariable=shopname_Input,bd=20,insertwidth=5,width=30,
                       bg="white",justify='right')
shopname_entry.grid(columnspan=4, row=2)

ftpserver_label = Label(f1, text="FTP-Server:", font=('TH Sarabun New',20,'bold'))
ftpserver_label.grid(column=0, row=3, sticky=W)
ftpserver_entry = Entry(f1,font=('TH Sarabun New',16,'bold'),
                        textvariable=ftpserver_Input,bd=20,insertwidth=5,width=30,
                        bg="white",justify='right')
ftpserver_entry.grid(columnspan=4, row=4)

username_label = Label(f1, text="Username:", font=('TH Sarabun New',20,'bold'))
username_label.grid(column=0, row=5, sticky=W)
username_entry = Entry(f1,font=('TH Sarabun New',16,'bold'),
                       textvariable=username_Input,bd=20,insertwidth=5,width=30,
                       bg="white",justify='right')
username_entry.grid(columnspan=4, row=6)

password_label = Label(f1, text="Password:", font=('TH Sarabun New',20,'bold'))
password_label.grid(column=0, row=7, sticky=W)
password_entry = Entry(f1,font=('TH Sarabun New',16,'bold'),
                       textvariable=password_Input,bd=20,insertwidth=5,width=30,
                       bg="white",justify='right')
password_entry.grid(columnspan=4,row=8)

login_btn = Button(f1,padx=16, fg="black",font=('TH Sarabun New',18,'bold'),width=8,
                   textvariable=loginbtn_Input,command=lambda:Login()).grid(padx=20, pady=20,columnspan=4,row=9)

#------------------------f2 Center-----------------------------
carrecent_label = Label(f2, text="ลูกค้าที่เข้ามาล่าสุด: ", font=('TH Sarabun New',20,'bold'))
carrecent_label.grid(column=0,row=0,sticky=W)
carrecent_entry = Entry(f2,font=('TH Sarabun New',20,'bold'),state='disable',disabledbackground='powder blue',
                            disabledforeground='black',textvariable=carrecent_Output,bd=30,insertwidth=4,width=30,
                            bg="powder blue",justify='right')
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
                    text="ส่ง",command=lambda:Summit()).grid(padx=20, pady=20,columnspan=4,row=6)

#------------------------f3 Right-----------------------------
label_Receipt = Label(f3,font=('TH Sarabun New',20,'bold'),
                      text="ประวัติ",bd=2,justify='right')
label_Receipt.grid(column=0,row=1,sticky=W)
text_Receipt = Text(f3,font=('TH Sarabun New',14,'bold'),
                    bd=5,width=50,height=30,bg="#e5dcdc")
text_Receipt.grid(column=0,row=2,sticky=W)


Running()
clock()





















root.mainloop()
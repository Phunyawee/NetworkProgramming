from tkinter import *
import time
import json
from ftplib import FTP
import codecs

year = ""
month = ""
day = ""
hour = ""
minute = ""
second = ""
shopname = ""
#===========================================TMP SHOP================================================================


#================================FTP Server============================================================
def downloadFile(ftp,filename):
    try:
        localfile = open(filename,'wb')
        ftp.retrbinary('RETR '+filename,localfile.write,1024)
        localfile.close()
    except FileNotFoundError:
        print("No such file or directory")
        showlogin_Output.set("No such file or directory")
        toggleText(loginbtn_Input,"login","logout")
    except:
        print("Error")
        showlogin_Output.set("Error")
        toggleText(loginbtn_Input,"login","logout")

def uploadFile(ftp,filename):
    try:
        ftp.encoding="utf-8"
        localfile = open(filename,'rb')
        ftp.storbinary('STOR '+filename,localfile)
        localfile.close()
    except FileNotFoundError:
        print("No such file or directory")
        showlogin_Output.set("No such file or directory")
        toggleText(loginbtn_Input,"login","logout")
    except:
        print("Error")
        showlogin_Output.set("Error")
        toggleText(loginbtn_Input,"login","logout")


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
        showlogin_Output.set("TimeoutError")
        toggleText(loginbtn_Input,"login","logout")

    except ConnectionRefusedError:
        print("ConnectionRefusedError")
        ShowLogin("ConnectionRefusedError")
        toggleText(loginbtn_Input,"login","logout")

    except NameError:
        print("NameError")
        ShowLogin("NameError")
        toggleText(loginbtn_Input,"login","logout")

    except FileNotFoundError:
        print("No such file or directory")
        showlogin_Output.set("No such file or directory")
        toggleText(loginbtn_Input,"login","logout")

    except:
        ShowLogin("ไม่สามารถเชื่อมต่อ FTP ได้")
        toggleText(loginbtn_Input,"login","logout")








#================================UI============================================================
root = Tk()
root.geometry("1600x800+0+0")
root.title("Parking Of Service SHOP")
root.configure(background="#8d99ae")

Tops = Frame(root, width=1600, height=150, bg="#2b2d42", relief=SUNKEN, bd=20,padx=400)
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

#menubar

addCarPlate_Output = StringVar()
addCarPlate_Input = StringVar()
#------------------------------Variable Function ----------------------
#showshopname_Output.set("กรุณาตั้งชื่อร้านของคุณ")
#Tops Function

def clock():
    global day,year,month,year,hour,minute,second
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%e")
    month = time.strftime("%m")
    year = "20"+time.strftime("%y")
    lblInfo.config(text=day+" | "+month+" | 20"+year+" "+hour+":"+minute+":"+second)
    lblInfo.after(1000,clock)

def Running():
    shopname_Output.set("กรุณาตั้งชื่อร้านของคุณ")
    loginbtn_Input.set("login")
    text_Receipt.insert(END,"ลำดับ    วัน/เวลา\t\t             ทะเบียนรถ\t"+"    จ่ายไป\t          ร้าน\t\t         สถานะ\n")
    modelogin_Input.set(1)
    LoginMode()
    #Receipt()
    license_plate_entry .config(state='disabled')
    amount_entry .config(state='disabled')
    send_btn.config(state='disabled')
    refresh_btn.config(state='disabled')
#General Function

def CarDict(order,carPlate,timeIn,cost,shop,status):
    jsonDict =  {"order":order,
                 "carPlate":carPlate,
                 "timeIn":timeIn,
                 "cost":cost,
                 "shop":shop,
                 "status":status}
    return jsonDict

def WriteFile(filename,dict):
    try:
        localfile = open(filename,'w')
    except FileNotFoundError:
        print("No such file or directory")
        toggleText(loginbtn_Input,"login","logout")
    except ValueError:
        print("ValueError")
        toggleText(loginbtn_Input,"login","logout")
    except NameError:
        print("NameError")
        toggleText(loginbtn_Input,"login","logout")
    except:
        print("Error")
        toggleText(loginbtn_Input,"login","logout")
    else:
        with localfile as file:
            json_object = json.dumps(dict, indent = 4)
            file.write(json_object)
    finally:
        localfile.close()

def WriteFile2(filename,dict):
    try:
        localfile = open(filename,'w')
    except FileNotFoundError:
        print("No such file or directory")
        toggleText(loginbtn_Input,"login","logout")
    except ValueError:
        print("ValueError")
        toggleText(loginbtn_Input,"login","logout")
    except NameError:
        print("NameError")
        toggleText(loginbtn_Input,"login","logout")
    except:
        print("Error")
        toggleText(loginbtn_Input,"login","logout")
    else:
        with localfile as file:
            json_object = json.dumps(dict, indent = 3)
            file.write(json_object)
    finally:
        localfile.close()



def ReadFile(filename):
    try:
        localfile = open(filename,'r')
    except FileNotFoundError:
        print("No such file or directory")
        toggleText(loginbtn_Input,"login","logout")
    except ValueError:
        print("ValueError")
        toggleText(loginbtn_Input,"login","logout")
    except NameError:
        print("NameError")
        toggleText(loginbtn_Input,"login","logout")
    except:
        print("Error")
        toggleText(loginbtn_Input,"login","logout")
    else:
            try:
                with localfile as j:
                    userdata = json.load(j)
            except:
                print("Error")
                toggleText(loginbtn_Input,"login","logout")
            else:
                print(type(userdata))
                print(userdata)
                return userdata
            finally:
                localfile.close()

def ShowLogin(text):
    showlogin_Output.set(text)

def CheckSpace(text):
    if text!="" and not text.isspace():
        return True
    else:
        return False

def toggleText(varBtn,txt1,txt2):
    global addCar
    if varBtn.get() == txt1:
        varBtn.set(txt2)

    else:
        varBtn.set(txt1)
        text_Receipt.delete("1.0","end")
        shopname_entry.config(state='normal')

        username_entry.config(state='normal')
        password_entry.config(state='normal')

        modelogin1_radio.config(state='normal')
        modelogin2_radio.config(state='normal')

        license_plate_entry .config(state='disabled')
        amount_entry .config(state='disabled')
        send_btn.config(state='disabled')
        refresh_btn.config(state='disabled')

        shopname_Output.set("กรุณาตั้งชื่อร้านของคุณ")
        ShowLogin("logout ออก")

        if modelogin_Input == 2:
            ftpserver_entry.config(state='normal')
            modelogin_Input.set(2)
        try:
            addCar.destroy()
        except:
            print("addCar.destroy()")




def LoginMode():
    selection = "selected " + str(modelogin_Input.get())
    showlogin_Output.set(selection)
    if modelogin_Input.get()==1:
        #ftpserver_label.grid_forget()
        #ftpserver_entry.grid_forget()
        ftpserver_entry.config(state='disabled')
        username_label.grid_forget()
        username_entry.grid_forget()
        password_label.grid_forget()
        password_entry.grid_forget()
        f1.config(pady=150)
        return 1

    else:
        f1.config(pady=0)
        ftpserver_entry.config(state='normal')
        ftpserver_label.grid(column=0, row=3, sticky=W)
        ftpserver_entry.grid(columnspan=4, row=4)
        username_label.grid(column=0, row=5, sticky=W)
        username_entry.grid(columnspan=4, row=6)
        password_label.grid(column=0, row=7, sticky=W)
        password_entry.grid(columnspan=4,row=8)
        ftpserver_entry.config(state='normal')
        return 2

def LoginBtn():
    if LoginMode() == 1:
        AutoLogin()
    elif LoginMode() == 2:
        Login()

def AutoLogin():
    global shopname
    #showlogin_Output.set("ShopTEST")
    try:
        file = open("ftp_ip.txt")
        ip,user,passWD = file.read().split(";")
    except IOError:
        print("IOError")
        showlogin_Output.set("IOError")
        toggleText(loginbtn_Input,"login","logout")
    except FileNotFoundError:
        print("No such file or directory")
        showlogin_Output.set("No such file or directory")
        toggleText(loginbtn_Input,"login","logout")
    except:
        print("Error")
        showlogin_Output.set("Error")
        toggleText(loginbtn_Input,"login","logout")
    else:
        print(ip)
        print(user)
        print(passWD)
        file.close()

        shopname = shopname_Input.get()
        ftpServer = ip
        username = user
        password = passWD
        """
        shopname = shopname_Input.get()
        ftpServer = "10.64.39.141"
        username = "NetPro"
        password = "800"
        """

        #FTPServer(ftpServer,username,password)

        if CheckSpace(shopname_Input.get()):
            ConnectFTPServer(ftpServer,username,password)
            try:
                downloadFile(ftp,'Write.json')
            except NameError:
                print("NameError")
                ShowLogin("NameError")
                toggleText(loginbtn_Input,"login","logout")
            except:
                print("Error")
                ShowLogin("Error")
                toggleText(loginbtn_Input,"login","logout")
            else:
                shopname_Output.set(shopname)
                ftpserver_Input.set(ftpServer)

                shopname_entry.config(state='disabled')
                ftpserver_entry.config(state='disabled')
                modelogin1_radio.config(state='disabled')
                modelogin2_radio.config(state='disabled')

                license_plate_entry.config(state='normal')
                amount_entry .config(state='normal')
                send_btn.config(state='normal')
                refresh_btn.config(state='normal')

                filemenu.entryconfig("เพิ่มทะเบียนรถ",state="normal")
                ShowLogin("login to FTP Server สำเร็จ !")
                toggleText(loginbtn_Input,"login","logout")

                #Receipt()
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
        try:
            downloadFile(ftp,'Write.json')
        except NameError:
            print("NameError")
            ShowLogin("NameError")
            toggleText(loginbtn_Input,"login","logout")
        except:
            print("Error")
            ShowLogin("Error")
            toggleText(loginbtn_Input,"login","logout")
        else:
            #Receipt()

            #ShowLogin("ssssslogin to FTP Server สำเร็จ !")
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

            filemenu.entryconfig("เพิ่มทะเบียนรถ",state="normal")
            ShowLogin("login to FTP Server สำเร็จ !")
            toggleText(loginbtn_Input,"login","logout")
            modelogin_Input.set(1)
            print("login สำเร็จ")
    else:
        ShowLogin("กรุณากรอกให้ครบ")

    print("ftpServer:",ftpServer)
    print("username:",username)
    print("password:",password)
    

#f2 Function
dict_arr = []
carplateList = []
deleteReceipt = []
car_order = -1

def CheckCarStatus():
    global carplateList
    checkbill = False
    carplateList = []
    downloadFile(ftp,'carOutData.json')
    downloadFile(ftp,'Write.json')

    userdata = ReadFile('carOutData.json')
    receiptdata = ReadFile('Write.json')
    try:
        for carplate in userdata:
            if carplate["status"] == 0:
                carplateList.append(carplate["carPlate"])#TypeError
            elif carplate["status"] == 2:
                deleteReceipt.append(carplate["carPlate"])
        print("deleteReceipt",deleteReceipt)
    except:
        print("Error")
        ShowLogin("Error")
        toggleText(loginbtn_Input,"login","logout")

    else:
        try:
            print(receiptdata)
            for receipt in receiptdata:
                for carplate in carplateList:
                    print("receipt:",receipt["carPlate"],"carplate:",carplate)
                    if receipt["carPlate"] == carplate:
                        receipt["status"] = 0

        #print("tmp_Delete",tmp_Delete)
        except:
            print("Error")
            ShowLogin("Error")
            toggleText(loginbtn_Input,"login","logout")
        else:
            tmp_Delete = receiptdata
            try:
                for index,receipt in enumerate(receiptdata):
                    for carplatedel in deleteReceipt:
                        if receipt["carPlate"] == carplatedel:
                            tmp_Delete.pop(index)
                receiptdata = tmp_Delete
            except:
               print("IndexError")
               toggleText(loginbtn_Input,"login","logout")
            else:
                WriteFile('Write.json',receiptdata)
                uploadFile(ftp,'Write.json')





def isFloat(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

def CheckCarPlate(customer):
    downloadFile(ftp,'carInData.json')
    #userdata = ReadFile('Check.json')
    userdata = ReadFile('carInData.json')
    for car in userdata:
        if car["carPlate"] == customer:
            if car["status"] == 0:
                print(str(customer)+" รถทะเบียนนี้ออกไปเเล้ว")
                carrecent_Output.set(str(customer)+" รถทะเบียนนี้ออกไปเเล้ว")
                return False

            else:
                carplateList.append(customer)
                print(str(customer)+" เพิ่มไปเเล้ว")
                #carrecent_Output.set(str(customer)+" รถทะเบียนนี้ออกไปเเล้ว")
                return True
    carrecent_Output.set(str(customer)+" ไม่มีทะเบียนนี้อยู่ในระบบ")
    return False



def Summit():
    global dict_arr, car_order, shopname, day,month,year,hour,minute,second
    license = license_Input.get()
    cost  = amount_Input.get()
    CheckCarStatus()
    downloadFile(ftp,'Write.json')
    Receipt()

    if(CheckSpace(license) & CheckSpace(cost) & isFloat(cost)):
            if CheckCarPlate(license):
                print("car_order",car_order)
                timeIn = day+"/"+month+"/"+year+" "+hour+":"+minute
                carrecent_Output.set(timeIn+" ทบล: "+license+" จ่าย: "+cost+" บาท")
                dict_arr = ReadFile('Write.json')
                try:
                    car_order = int(dict_arr[len(dict_arr)-1]["order"])+1
                    dict_arr.append(CarDict(car_order,license,timeIn,cost,shopname,1))
                except IndexError:
                    ShowLogin("IndexError")
                    toggleText(loginbtn_Input,"login","logout")
                except:
                    ShowLogin("Error")
                    toggleText(loginbtn_Input,"login","logout")


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
        carrecent_Output.set("กรุณากรอกข้อมูลให้ถูกต้อง")


    #print(shopname_Output)

def Refresh():
    CheckCarStatus()
    downloadFile(ftp,'Write.json')
    Receipt()

#f3 Function
def Receipt():
    userdata = ReadFile('Write.json')
    #CheckCarStatus()
    text_Receipt.delete("1.0","end")
    text_Receipt.insert(END,"ลำดับ    วัน/เวลา\t\t           ทะเบียนรถ\t"+"    จ่ายไป\t          ร้าน\t\t         สถานะ\n")
    status = ""
    try:
        for list in userdata:
            if list["status"] == 0:
                status = "เช็คเเล้ว"
            elif list["status"] == 1:
                status = "ยังอยู่"

            print(list["order"])
            print(list["shop"])

            text_Receipt.insert(END,"  "+str(list["order"])
                                +"     "+str(list["timeIn"])
                                +
                                "\t\t   "+str(list["carPlate"])
                                +"\t           "+str(list["cost"])+
                                " ฿\t           "+str(list["shop"])
                                +"\t\t          "+status+"\n")
    except: #TypeError
        print("Error")
        ShowLogin("Error")
        toggleText(loginbtn_Input,"login","logout")





#MenuBar Function


def CarPlateDict(order,carPlate,timeIn,cost,status):
    jsonDict =  {"order":order,
                 "carPlate":carPlate,
                 "timeIn":timeIn,
                 "cost":cost,
                 "status":status}
    return jsonDict

def ShowAddCarPlate():
    def AddCarPlate():
        global addCarPlate_Output,addCarPlate_Input,addcar_entry
        carPlate = addcar_entry.get()
        print("carPlate:",carPlate)
        print('check'+str(CheckSpace(carPlate)))
        if CheckSpace(carPlate):
            print('CheckSpace')
            addCarPlate_Output.set("เพิ่มทะเบียนสำเร็จ")
            downloadFile(ftp,'carInData.json')
            cardict_arr = ReadFile('carInData.json')
            carIn_order = int(cardict_arr[len(cardict_arr)-1]["order"])+1
            timeIn = day+"/"+month+"/"+year+" "+hour+":"+minute
            cardict_arr.append(CarPlateDict(carIn_order,carPlate,timeIn,0,1))
            print("cardict_arr:",cardict_arr)
            WriteFile2('carInData.json',cardict_arr)
            uploadFile(ftp,'carInData.json')
            addCar.destroy()

        else:
            addCarPlate_Output.set("กรุณากรอกทะเบียนให้ถูกต้อง")
    global addCarPlate_Output,addCarPlate_Input,addcar_entry,addCar

    addCar = Toplevel(root)
    addCar.geometry("650x300+500+200")
    addCar.title("เพิ่มทะเบียนรถ")
    addCar.configure(background="#8d99ae")
    addCar.resizable(width=False, height=False)

    showaddstatus_label = Label(addCar,text="สถานะ", font=('TH Sarabun New',20,'bold'))
    showaddstatus_label.grid(column=0,row=0,sticky=W)
    showaddstatus_entry = Entry(addCar,font=('TH Sarabun New',25,'bold'),disabledbackground='#ef233c',
                                disabledforeground='white',textvariable=addCarPlate_Output,state='disable',bd=20,insertwidth=10,width=23,
                                bg="powder blue",justify='right')
    showaddstatus_entry.grid(columnspan=4, row=1)

    addcar_label = Label(addCar, text="ทะเบียนรถ: ", font=('TH Sarabun New',20,'bold'))
    addcar_label.grid(column=0,row=2,sticky=W)
    addcar_entry = Entry(addCar,font=('TH Sarabun New',25,'bold'),
                         textvariable=addCarPlate_Input,bd=20,insertwidth=10,width=15,
                         bg="white",justify='right')
    addcar_entry.grid(columnspan=4, row=3)


    addcar_btn = Button(addCar,padx=16, bg="#2b2d42",fg="white",font=('TH Sarabun New',18,'bold'),width=8,
                        text="เพิ่มทะเบียน",command=lambda:AddCarPlate())
    addcar_btn.grid(padx=20,pady=20,column=4,row=3)



#--------------------------------TOPS-------------------------------
lblInfo = Label(Tops,font=('TH Sarabun New',60,'bold'),
                    textvariable=shopname_Output,fg="#2b2d42",bd=10,anchor='w',bg="#8d99ae",relief=SUNKEN)
lblInfo.grid(row=0,column=0)

lblInfo = Label(Tops,font=('TH Sarabun New',30,'bold'),
                text="",fg="white",bg="#8d99ae",bd=10,anchor='w',relief=SUNKEN)
lblInfo.grid(row=1,column=0)



#------------------------f1 Left-----------------------------
showlogin_entry = Entry(f1,font=('TH Sarabun New',25,'bold'),state='disable',disabledbackground='#ef233c',
                        disabledforeground='white',textvariable=showlogin_Output,bd=20,insertwidth=10,width=23,
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
                       bg="white",justify='right',show='*')
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

send_btn = Button(f2,padx=30,bg="#d90429", fg="white",font=('TH Sarabun New',18,'bold'),width=8,disabledforeground='white',
                    text="ส่ง",command=lambda:Summit())
send_btn .grid(padx=20, pady=20,columnspan=4,row=6)

refresh_btn = Button(f2,padx=30,bg="#d90429" , fg="white",font=('TH Sarปabun New',18,'bold'),width=8,disabledforeground='white',
                  text="รีเฟรช",command=lambda:Refresh())
refresh_btn.grid(padx=20, pady=20,columnspan=4,row=7)
#------------------------f3 Right-----------------------------
label_Receipt = Label(f3,font=('TH Sarabun New',20,'bold'),
                      text="ประวัติ",bd=2,justify='right')
label_Receipt.grid(column=0,row=1,sticky=W)
text_Receipt = Text(f3,font=('TH Sarabun New',12,'bold'),
                    bd=5,width=60,height=30,bg="#e5dcdc")
text_Receipt.grid(column=0,row=2,sticky=W)

#=========================Menu Bar==========================

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="เพิ่มทะเบียนรถ",font=('TH Sarabun New',18,'bold'),state="disabled", command=lambda:ShowAddCarPlate())
filemenu.add_separator()
filemenu.add_command(label="Exit",font=('TH Sarabun New',15,'bold'), command=root.destroy)
menubar.add_cascade(label="Menu", menu=filemenu)

root.config(menu=menubar)
#===========================

#============================================================================================

Running()
clock()
root.attributes('-fullscreen',True)
root.mainloop()
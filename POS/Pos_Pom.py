from tkinter import *
from datetime import datetime
import random
import time
import json
import codecs
from ftplib import FTP

root = Tk()
root.geometry("1550x800+0+0")
root.title("POS สำหรับป้อม")
root.configure(background="#ffecad")

Tops = Frame(root, width=1600, height=150, bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width = 1600,height = 800, bg="#ffecad",relief = SUNKEN)
f1.pack(side=TOP)


order = -1
#========================================Function====================================================
def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%e")
    month = time.strftime("%B")
    year = time.strftime("%y")
    lblInfo.config(text=day+" "+month+" 20"+year+" "+hour+":"+minute+":"+second)
    lblInfo.after(1000,clock)

def CarEntrance():
    global order
    order = order+1
    carText = car_In.get()
    print(len(carText))
    t = time.localtime()
    current_time = time.strftime("%d/%m/%Y %H:%M", t)
    if len(carText) == 0:
        car_In.set("")
        root = Tk()
        root.geometry("250x100+0+0")
        root.title("คำเตือน")
        label = Label(root, text="กรุณากรอกข้อมูล")
        label.pack(side="top", fill="x", pady=10)
        B1 = Button(root, text="Okay", command = root.destroy)
        B1.pack()
        root.mainloop()
    for CarChk in carEntranceArr:
        print(carText)
        if CarChk["carPlate"] == carText:
            car_In.set("")
            root = Tk()
            root.geometry("250x100+0+0")
            root.title("คำเตือน")
            label = Label(root, text="ทะเบียนรถนี้มีอยู่ในที่จอดแล้ว โปรดตรวจสอบความถูกต้อง")
            label.pack(side="top", fill="x", pady=10)
            B1 = Button(root, text="Okay", command = root.destroy)
            B1.pack()
            root.mainloop()
            break
    else:
        textIn = "รถเข้าทะเบียน "+str(car_In.get())+" เวลา "+str(current_time)
        carIn_Dict = { 
          "order":order,
          "carPlate":carText,
          "timeIn":current_time,
          "cost":0,
          "status":1
        }
        carEntranceArr.append(carIn_Dict)
        showCarIn.set(textIn)
        with open('carInData.json', 'w') as file:
            json.dump(carEntranceArr, file,indent = 3)
        uploadFile()    
        car_In.set("")
        print("carIn_Json: "+str(carIn_Dict)+"\n")
        print("carEntranceArr: "+str(carEntranceArr)+"\n")


        
        """
        carEntranceArr.append(str(car_In.get()))
        timeInArr.append(str(current_time))
        costSumArr.append(0)
        car_In.set("")
        print(carEntranceArr)
        print(timeInArr)
        print(costSumArr)
        """

"""
def sumCost():
    CarPay = str(carLicPay.get())
    for LicChk in carEntranceArr:
        #print("LicChk = "+LicChk)
        #print("carLicPay.get = ",CarPay)
        if CarPay == LicChk:
            textCost = "รถทะเบียน "+CarPay+" มีค่าใช้จ่าย "+(cost.get())
            ShowCost.set(textCost)
            CarIndex = carEntranceArr.index(CarPay)
            costSumArr[CarIndex] = cost.get()
            print("found is at index ",CarIndex,"in carEntranceArr")
            print(costSumArr)
            carLicPay.set("")
            cost.set("")
            break
            
    else: 
        carLicPay.set("")
        cost.set("")
        root = Tk()
        root.geometry("250x100+0+0")
        root.title("คำเตือน")
        label = Label(root, text="ไม่พบทะเบียนนี้ \n ในระบบโปรดกรอกใหม่ หรือ ติดต่อเจ้าหน้าที่")
        label.pack(side="top", fill="x", pady=10)
        B1 = Button(root, text="Okay", command = root.destroy)
        B1.pack()
        root.mainloop()
"""
def uploadFile():
    ftp = FTP('10.64.39.141')
    ftp.encoding="utf-8"
    ftp.login(user='NetPro', passwd='800')
    print("||||||| Folder in FTP server |||||||")
    ftp.retrlines('LIST')
    print("||||||||||||||||||||||||||||||||||||")
    ftp.cwd('FTP')
    print("||||||| File in FTP folder |||||||")
    ftp.retrlines('LIST')
    print("||||||||||||||||||||||||||||||||||||")
    ftp.encoding="utf-8"
    filename = 'carInData.json'
    ftp.storbinary('STOR '+filename,open(filename,'rb'))
    print("||||||| File in FTP folder |||||||")
    ftp.retrlines('LIST')
    print("||||||||||||||||||||||||||||||||||||")
    ftp.quit()

def downloadFile():
    ftp = FTP('10.64.39.141')
    ftp.login(user='NetPro', passwd='800')
    print("||||||| Folder in FTP server |||||||")
    ftp.retrlines('LIST')
    print("||||||||||||||||||||||||||||||||||||")
    ftp.cwd('FTP')
    print("||||||| File in FTP folder |||||||")
    ftp.retrlines('LIST')
    print("||||||||||||||||||||||||||||||||||||")
    ftp.encoding="utf-8"
    filename = 'Write.json'
    localfile = open(filename,'wb')
    ftp.retrbinary('RETR '+filename,localfile.write,1024)
    localfile.close()
    print("||||||| File in FTP folder |||||||")
    ftp.retrlines('LIST')
    print("||||||||||||||||||||||||||||||||||||")
    ftp.quit()

def ReadFile(filename):
    with open(filename,'r') as j:
        userdata = json.load(j)
        print(type(userdata))
        print(userdata)
    return userdata

def CostCheck(carplate):
    cost = 0
    carEntranceList = ReadFile('Write.json')
    for CarChk in carEntranceList:
        if carplate == CarChk["carPlate"]:
            #CarChk["status"] = 0
            cost += int(CarChk["cost"])
    return cost

def outPay():
    t = time.localtime()
    global parking_fee
    current_time = time.strftime("%d/%m/%Y %H:%M", t)
    CarOut = str(car_Out.get())
    date_format_str = "%d/%m/%Y %H:%M"
    #downloadFile()
    #แก้ตอนเช็ค
    for CarChk in carEntranceArr:
        if CarOut == CarChk["carPlate"]:
            btnOut.config(state='normal')
            global parking_fee
            cost = CostCheck(CarOut)
            timeIn = datetime.strptime(CarChk["timeIn"], date_format_str)
            timeOut = datetime.strptime(current_time, date_format_str)
            diff = timeOut - timeIn
            diff_in_minutes = diff.total_seconds()
            textOut = "รถทะเบียน "+CarOut+"จอดทั้งหมด"+str(diff_in_minutes)+" วินาที"
            showCarPay.set(textOut)
            #อ่านข้อมูล cost ของรถ
            '''data = ReadFile('Write.json')
            for car in data:
                if car["carPlate"] == CarOut:
                    cost += int(car["cost"])'''
            #TimeSum = int(TimeOut) - int(TimeIn)
            #print(CarIndex,cost,TimeIn,TimeOut)
            #print(int(TimeSum))
            if cost > 1000:
                show_cost.set(0)
            if cost >= 100  and cost <= 500:
                if  diff_in_minutes < 60:
                    show_cost.set(0)
                if  diff_in_minutes > 60:
                    parking_fee = 0
                    time_hr = int(diff_in_minutes / 60)-1 #340/6 = 5
                    time_min = diff_in_minutes % 60 #340/6 = 40
                    parking_fee = 30*time_hr
                    if time_min >= 30:
                        parking_fee += 30
                    show_cost.set(parking_fee)
            if cost < 100:
                parking_fee = 0
                time_hr = int(diff_in_minutes / 60) #340/6 = 5
                time_min = diff_in_minutes % 60 #340/6 = 40
                parking_fee = 30*time_hr
                if time_min >= 30:
                    parking_fee += 30
                show_cost.set(parking_fee)  
            break
    
    else: 
        car_Out.set("")
        root = Tk()
        root.geometry("250x100+0+0")
        root.title("คำเตือน")
        label = Label(root, text="ไม่พบทะเบียนนี้ \n ในระบบโปรดกรอกใหม่ หรือ ติดต่อเจ้าหน้าที่")
        label.pack(side="top", fill="x", pady=10)
        B1 = Button(root, text="Okay", command = root.destroy)
        B1.pack()
        root.mainloop()

#เพิ่มส่งค่า status ตอนออก
def CarOut():
    CarOut = str(car_Out.get())
    global sumPay
    global carEntranceArr
    if len(CarOut) == 0:
        btnOut.config(state='disabled')
        car_Out.set("")
        root = Tk()
        root.geometry("250x100+0+0")
        root.title("คำเตือน")
        label = Label(root, text="กรุณากรอกข้อมูลให้ถูกต้อง")
        label.pack(side="top", fill="x", pady=10)
        B1 = Button(root, text="Okay", command = root.destroy)
        B1.pack()
        root.mainloop()
    for CarChk in carEntranceArr:
        if CarOut == CarChk["carPlate"]:
            btnOut.config(state='disabled')
            textOut = "รถทะเบียน "+CarOut+"ออก!!"
            showCarOut.set(textOut)
            car_Out.set("")
            show_cost.set("")
            sumPay += parking_fee
            CarChk["status"] = 0
            with open('carInData.json', 'w') as file:
                json.dump(carEntranceArr, file,indent = 3)
            uploadFile()
            carInData_update = list(filter(lambda i: i['carPlate'] != CarOut, carEntranceArr))
            carEntranceArr = carInData_update
            print(carEntranceArr)
            break
    else:
        car_Out.set("")
        root = Tk()
        root.geometry("250x100+0+0")
        root.title("คำเตือน")
        label = Label(root, text="ไม่พบทะเบียนนี้ \n ในระบบโปรดกรอกใหม่ หรือ ติดต่อเจ้าหน้าที่")
        label.pack(side="top", fill="x", pady=10)
        B1 = Button(root, text="Okay", command = root.destroy)
        B1.pack()
        root.mainloop()
        btnOut.config(state='disabled')


def EndService():
    outputfile = codecs.open('ParkingFeeReport.txt', "w", "utf-8")
    outputfile.write("ยอดเงินที่ได้รับทั้งหมดของวันนี้ : " + str(sumPay) + "บาท")
    outputfile.close()


    
 #========================================TOP====================================================               
  

#========================================Pre-Data====================================================
    #=====================================car=============================================================
car_In = StringVar() # text input ใส่ทะเบียนรถ
car_Out = StringVar()
show_cost = StringVar()
showCarIn = StringVar()
showCarPay = StringVar()
showCarOut = StringVar()
ShowCost = StringVar()
carLicPay = StringVar() #car license Pay
cost = StringVar()
showCarIn.set("รถเข้าทะเบียน    เวลา           "      )
showCarPay.set("รถทะเบียน      จอดทั้งหมด     วินาที")
showCarOut.set("รถทะเบียน      ออก")
carEntranceArr = []
carExitArr = []
sumPay = 0
"""
carEntranceArr = []
timeInArr = []
costSumArr = []
"""


    #=====================================Time=============================================================
lblInfo = Label(Tops,font=('Microsoft YaHei Light',50,'bold'),
               text="",fg="Black",bg="powder blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)


#=========================================In ============================================================
lblCarin = Label(f1,font=('BIZ UDPMincho Medium',24,'bold'),text = "รถเข้า",bg="#ffecad",bd=16,anchor='w')
lblCarin.grid(row=0,column=1)
        #================================CarEntrance============================================================
lblCarLicense = Label(f1,font=('BIZ UDPMincho Medium',18,'bold'),text = "ใส่ทะเบียนรถ",
bd=16,bg="#ffecad",anchor='w')
lblCarLicense.grid(row=1,column=0)

#ใส่ทะเบียนรถเข้า+btn
textCarLicenseIn = Entry(f1,font=('Microsoft JhengHei Light',18,'bold'),textvariable = car_In,
bd=10,insertwidth=4,bg="white",justify = 'right')
textCarLicenseIn.grid(row=1,column=1)
btnIn = Button(f1,padx=16,pady=16,fg="black",
             font=('TH Sarabun New',20,'bold'),
             text="เข้า",bg="#B5EAEA",command=lambda:CarEntrance())
btnIn.grid(row=1,column=2)

lblShowCarIn = Label(f1,font=('Microsoft JhengHei Light',18,'bold'),textvariable = showCarIn,
bd=16,anchor='w',bg="#ffecad")
lblShowCarIn.grid(row=2,column=0)

#=========================================End In  ======================================================



#=========================================Out ============================================================
lblCarOut = Label(f1,font=('Microsoft JhengHei Light',24,'bold'),text = "รถออก",bd=16,anchor='w',
bg="#ffecad")
lblCarOut.grid(row=3,column=1)
        #================================CarOut============================================================
lblCarLicenseOut = Label(f1,font=('Microsoft JhengHei Light',18,'bold'),text = "ใส่ทะเบียนรถ",
bd=16,anchor='w',bg="#ffecad")
lblCarLicenseOut.grid(row=4,column=0)

textCarLicenseOut = Entry(f1,font=('Microsoft JhengHei Light',18,'bold'),textvariable = car_Out,
bd=10,insertwidth=4,bg="white",justify = 'right')
textCarLicenseOut.grid(row=4,column=1)

btnChkCost = Button(f1,padx=16,pady=16,fg="black",
             font=('Microsoft JhengHei Light',20,'bold'),
             text="เช็คค่าใช้จ่าย",bg="#B5EAEA",command=lambda:outPay())
btnChkCost.grid(row=4,column=2)

lblshowCarPay = Label(f1,font=('Microsoft JhengHei Light',18,'bold'),textvariable = showCarPay,
bd=16,anchor='w',bg="#ffecad")
lblshowCarPay.grid(row=5,column=0)

lblCost = Label(f1,font=('Microsoft JhengHei Light',18,'bold'),text = "ต้องจ่ายเงิน  (บาท)",
bd=16,anchor='w',bg="#ffecad")
lblCost.grid(row=6,column=0)

textCost = Entry(f1,font=('Microsoft JhengHei Light',18,'bold'),textvariable = show_cost,
bd=10,insertwidth=4,bg='white',justify = 'right')
textCost.grid(row=6,column=1)

btnOut = Button(f1,padx=16,pady=16,fg="black",
             font=('Microsoft JhengHei Light',20,'bold'),
             text="ออก",bg="#B5EAEA",command=lambda:CarOut())
btnOut.grid(row=6,column=2)
btnOut.config(state='disabled')
lblShowCarOut = Label(f1,font=('Microsoft JhengHei Light',18,'bold'),textvariable = showCarOut,
bd=16,bg="#ffecad",anchor='w')
lblShowCarOut.grid(row=7,column=0)


#=========================================End Out  ======================================================


#=========================================Endservice Butt ============================================================

btnEndService = Button(f1,padx=16,pady=16,fg="black",
             font=('Microsoft JhengHei Light',20,'bold'),
             text="ปิดยอด",bg="#FF7878",command=lambda:EndService())
btnEndService.grid(row=0,column=0)

#=========================================End Endservice Butt ===========================================================
clock()
root.resizable(width=False, height=False)
root.mainloop()
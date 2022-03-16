from tkinter import *
from datetime import datetime
import random
import time
import json
import codecs
from ftplib import FTP
from tkinter import messagebox

root = Tk()
root.geometry("1530x800+0+0")
root.title("POS สำหรับป้อม")
root.configure(background="#ffecad")

Tops = Frame(root, width=1600, height=150, bg="#ffecad", relief=SUNKEN)
Tops.pack(side=TOP)

f0 = Frame(root, width = 20,height = 550, bg="#ffecad",relief = SUNKEN)
f0.pack(side=LEFT,anchor=W)

f1 = Frame(root, width = 600,height = 500, bg="#ffecad",relief = SUNKEN)
f1.pack(side=LEFT,anchor=W)

f2 = Frame(root,width = 400,height = 500,bg="#ffecad",relief = SUNKEN)
f2.pack(side=LEFT,anchor=NE)

f3 = Frame(root,width = 400,height = 500,bg="red",relief = SUNKEN)
f3.pack(side=LEFT,anchor=NE)

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
    #order = order+1
    carText = car_In.get()
    t = time.localtime()
    current_time = time.strftime("%d/%m/%Y %H:%M", t)
    if len(carText) == 0:
        car_In.set("")
        messagebox.showinfo("คำเตือน", "กรุณากรอกข้อมูล")
        #root = Tk()
        #root.geometry("250x100+0+0")
        #root.title("คำเตือน")
        #label = Label(root, text="กรุณากรอกข้อมูล")
        #label.pack(side="top", fill="x", pady=10)
        #B1 = Button(root, text="Okay", command = root.destroy)
        #B1.pack()
        #oot.mainloop()
        return
    downloadFile('carInData.json')
    carEntranceArr = ReadFile('carInData.json')
    for CarChk in carEntranceArr:
        print(carText)
        if CarChk["carPlate"] == carText and CarChk["status"] == 0 :
            textIn = "รถเข้าทะเบียน "+str(car_In.get())+" เวลา "+str(current_time)
            CarChk["timeIn"] = current_time
            CarChk["status"] = 1
            CarChk["cost"] = 0
            showCarIn.set(textIn)
            with open('carInData.json', 'w') as file:
               json.dump(carEntranceArr, file,indent = 3)
            uploadFile() 
            car_In.set("")
            #print("carEntranceArr: "+str(carEntranceArr)+"\n")
            break
        elif CarChk["carPlate"] == carText:
            car_In.set("")
            #root = Tk()
            #root.geometry("250x100+0+0")
            #root.title("คำเตือน")
            #label = Label(root, text="ทะเบียนรถนี้มีอยู่ในที่จอดแล้ว โปรดตรวจสอบความถูกต้อง")
            messagebox.showinfo("คำเตือน", "ทะเบียนรถนี้มีอยู่ในที่จอดแล้ว โปรดตรวจสอบความถูกต้อง")
            #label.pack(side="top", fill="x", pady=10)
            #B1 = Button(root, text="Okay", command = root.destroy)
            #B1.pack()
            #root.mainloop()
            break
    else:
        order = order+1
        downloadFile('carInData.json')
        read = ReadFile('carInData.json')
        textIn = "รถเข้าทะเบียน "+str(car_In.get())+" เวลา "+str(current_time)
        carIn_Dict = { 
          "order":order,
          "carPlate":carText,
          "timeIn":current_time,
          "cost":0,
          "status":1
        }
        read.append(carIn_Dict)
        carEntranceArr.append(carIn_Dict)
        showCarIn.set(textIn)
        with open('carInData.json', 'w') as file:
            json.dump(read, file,indent = 3)
        uploadFile() 
        car_In.set("")
        #print("carIn_Json: "+str(carIn_Dict)+"\n")
        #print("carEntranceArr: "+str(carEntranceArr)+"\n")
        DisplayCarIn()

        
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

def downloadFile(filename):
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
    downloadFile('carInData.json')
    carEntranceArr = ReadFile('carInData.json')
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
        #root = Tk()
        #root.geometry("250x100+0+0")
        #root.title("คำเตือน")
        #label = Label(root, text="ไม่พบทะเบียนนี้ \n ในระบบโปรดกรอกใหม่ หรือ ติดต่อเจ้าหน้าที่")
        messagebox.showinfo("คำเตือน", "ไม่พบทะเบียนนี้ \n ในระบบโปรดกรอกใหม่ หรือ ติดต่อเจ้าหน้าที่")
        #label.pack(side="top", fill="x", pady=10)
        #B1 = Button(root, text="Okay", command = root.destroy)
        #B1.pack()
        #root.mainloop()

#เพิ่มส่งค่า status ตอนออก
def CarOut():
    CarOut = str(car_Out.get())
    global sumPay
    global carEntranceArr
    downloadFile('carInData.json')
    carEntranceArr = ReadFile('carInData.json')
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
            '''carInData_update = list(filter(lambda i: i['carPlate'] != CarOut, carEntranceArr))
            carEntranceArr = carInData_update
            print(carEntranceArr)'''
            break
    else:
        car_Out.set("")
        #root = Tk()
        #root.geometry("250x100+0+0")
        #root.title("คำเตือน")
        #label = Label(root, text="ไม่พบทะเบียนนี้ \n ในระบบโปรดกรอกใหม่ หรือ ติดต่อเจ้าหน้าที่")
        messagebox.showinfo("คำเตือน", "ไม่พบทะเบียนนี้ \n ในระบบโปรดกรอกใหม่ หรือ ติดต่อเจ้าหน้าที่")
        #label.pack(side="top", fill="x", pady=10)
        #B1 = Button(root, text="Okay", command = root.destroy)
        #B1.pack()
        #root.mainloop()
        btnOut.config(state='disabled')


def EndService():
    outputfile = codecs.open('ParkingFeeReport.txt', "w", "utf-8")
    outputfile.write("ยอดเงินที่ได้รับทั้งหมดของวันนี้ : " + str(sumPay) + "บาท")
    outputfile.close()
    downloadFile('carInData.json')
    carEntranceArr = ReadFile('carInData.json')
    for carChk in carEntranceArr:
        if carChk["status"] == 0 :
            carChk["status"] = 2 #สำหรับลบรถที่ค้างอยู่ในระบบ(ร้านค้า)
    with open('carInData.json', 'w') as file:
        json.dump(carEntranceArr, file,indent = 3)
    file.close()
    uploadFile()
    carInData_update = list(filter(lambda i: i['status'] != 2, carEntranceArr)) #ลบข้อมูล
    carEntranceArr = carInData_update


def running():
    text_Receipt.insert(END,"ลำดับ\t    \tทะเบียนรถ\t  \tเวลาเข้า\t\n")

def DisplayCarIn():
    data = ReadFile('carInData.json')
    text_Receipt.delete("1.0","end")
    text_Receipt.insert(END,"ลำดับ\t    \tทะเบียนรถ\t  \tเวลาเข้า\t\n")
    for list in data:
        print(list["order"])
        print(list["carPlate"])
        print(list["timeIn"])
        text_Receipt.insert(END,""+str(list["order"])+"\t    \t"+str(list["carPlate"])+"\t  \t"+str(list["timeIn"])+"\t\n")

def editplate():
    oldplate = oldPlate.get()
    newplate = newPlate.get()
    downloadFile('carInData.json')
    carEntranceArr = ReadFile('carInData.json')
    if(len(oldplate) == 0 or len(newplate) == 0):
        messagebox.showinfo("คำเตือน", "กรุณากรอกข้อมูล")
        oldPlate.set("")
        newPlate.set("")
    print("PrintfromEdit")
    print(carEntranceArr)
    print("old ",oldplate)
    print("new",newplate)
    for platechk in carEntranceArr:
        print("เข้า For")
        if platechk["carPlate"] == oldplate:
            platechk["carPlate"] =  newplate
            print(platechk["carPlate"])
            with open('carInData.json', 'w') as file:
                json.dump(carEntranceArr, file,indent = 3)
            file.close()
            print("edited")
            oldPlate.set("")
            newPlate.set("")
            uploadFile()
            DisplayCarIn()
            break
    else:
        messagebox.showinfo("คำเตือน", "กรุณากรอกข้อมูลให้ถูกต้อง")

    
def qExit():
    root.destroy()
  
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
oldPlate = StringVar()
newPlate = StringVar()
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
               text="",fg="Black",bg="#ffecad",bd=10,anchor='w')
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
lblShowCarIn.grid(row=2,columnspan=3)

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
lblshowCarPay.grid(row=5,columnspan=3)

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
lblShowCarOut.grid(row=7,columnspan=3)


#=========================================End Out  ======================================================


#=========================================Endservice Butt ============================================================


#===================================history=======================================================

label_Receipt = Label(f2,font=('TH Sarabun New',20,'bold'),
                      text="ประวัติ",bd=2,justify='right',bg="#ffecad")
label_Receipt.grid(column=0,row=1,sticky=NW)
text_Receipt = Text(f2,font=('TH Sarabun New',12,'bold'),
                    highlightthickness=5,highlightbackground="#ffecc0",
                    bd=15,width=60,height=25,padx=10,bg="#e5dcdc")
text_Receipt.grid(column=0,row=2,sticky=W)
btnEndService = Button(f2,padx=8,pady=8,fg="black",
             font=('Microsoft JhengHei Light',20,'bold'),
             text="ปิดยอด",bg="#FF7878",command=lambda:EndService())
btnEndService.grid(row=3,column=0)
btnEndService = Button(f2,padx=8,pady=8,fg="black",
             font=('Microsoft JhengHei Light',20,'bold'),
             text="ออกจากระบบ/ปิดระบบ",bg="#FF7878",command=qExit)
btnEndService.grid(row=4,column=0)
#=========================================End Endservice Butt ===========================================================
#=========================================Edit Zone ===========================================================
lblEditText = Label(f3,font=('Microsoft JhengHei Light',10,'bold'),text = "แก้ไขทะเบียนที่ผิดพลาด",
bd=16,anchor='w',bg="#ffecad")
lblEditText.grid(row=0,column=0)
lblOldPlate = Label(f3,font=('Microsoft JhengHei Light',10,'bold'),text = "ใส่ทะเบียนที่ผิด",
bd=16,anchor='w',bg="#ffecad")
lblOldPlate.grid(row=1,column=0)
textCarLicenseEdit = Entry(f3,font=('Microsoft JhengHei Light',10,'bold'),textvariable = oldPlate,
bd=10,insertwidth=4,bg="white",justify = 'right')
textCarLicenseEdit.grid(row=2,column=0)
lblNewPlate = Label(f3,font=('Microsoft JhengHei Light',10,'bold'),text = "ใส่ทะเบียนที่ต้องการแก้ไข",
bd=16,anchor='w',bg="#ffecad")
lblNewPlate.grid(row=3,column=0)
textCarLicenseEdit = Entry(f3,font=('Microsoft JhengHei Light',10,'bold'),textvariable = newPlate,
bd=10,insertwidth=4,bg="white",justify = 'right')
textCarLicenseEdit.grid(row=4,column=0)
btnEndService = Button(f3,padx=8,pady=8,fg="black",
             font=('Microsoft JhengHei Light',8,'bold'),
             text="แก้ไข",bg="#FF7878",command=lambda:editplate())
btnEndService.grid(row=5,column=0)



running()
clock()
DisplayCarIn()
root.attributes('-fullscreen',True)
root.resizable(width=False, height=False)
root.mainloop()
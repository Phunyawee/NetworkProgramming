# POS
ใน Folder นี้ประกอบไปด้วย 6 ไฟล์ได้แก่ <br>
```POS_pom2.py``` <br>
```POS_SHOP.py``` <br>
```carInData.json``` <br>
```carOutData.json``` <br>
```Write.json``` <br>
```ftp_ip.txt``` <br>

## อธิบายโครงสร้างแต่ละ JSON
```carInData.json``` ใช้ในการเก็บค่าทะเบียนรถที่เข้ามาจอดในที่จอดรถ <br>
ประกอบด้วย Order,carPlate,timeIn,cost,และ status รถที่เข้ามา <br>
```carOutData.json``` ใช้ในการเก็บค่าทะเบียนรถที่ออกจากที่จอดเเล้วเพื่อใช้อ้างอิง<br>
ประกอบด้วย Order,carPlate,timeIn,cost,และ status รถที่เข้ามา <br>
```Write.json``` ใช้ในการเก็บใบเสร็จในเเต่ละร้านค้า เเเละเเยกตามทะเบียน<br>
ประกอบด้วย Order,carPlate,timeIn,cost,shop,และ status รถที่เข้ามา <br>

## อธิบายโครงสร้างของ txt
```ftp_ip.txt``` <br>
เก็บ ip,user,passWD ของ FTPServer  <br>
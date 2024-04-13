global root
root=0
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from tkinter import messagebox                             
import sqlite3 as c
from time import strftime,strptime
from datetime import datetime
import re
from tkcalendar import DateEntry
import subprocess


#--RESET ENTRY BOX
global LT
LT=[]
global row
row=0
global ticketdate
global ab
global xyz
def resetpsgnr():
    global root
    global labelframeleft
    global txtcname
    global combo_Gender
    global txtpostcode
    global txtmobile
    global txtemail
    global combo_nationality
    global combo_idproof
    global txtidnumber
    global combo_fromwhere
    global combo_towhere
    global combo_nopassengers
    global Psngr_Details_Table
    global ticketdate
    global txttrainname
    global txttotalfair
    global txtsubtax
    global txtsubtotal

    txtsubtotal.delete(0,END)
    print(txtsubtotal.get())
    while True:
        txtcname.delete(0)
        if str(txtcname.get())=="":
            break

    while True:
        combo_Gender.delete(0)
        if str(combo_Gender.get())=="":
            break 

    while True:
        txtpostcode.delete(0)
        if len(txtpostcode.get())==0:
            break
        
    txtmobile.delete(0,20)
    x=random.randint(6145865252,6999233687)
    txtmobile.insert(0,x)

    while True:
        txtemail.delete(0)
        if str(txtemail.get())=="":
            break

    while True:
        combo_nationality.delete(0)
        if str(combo_nationality.get())=="":
            break
    
    while True:
        combo_idproof.delete(0)
        if str(combo_idproof.get())=="":
            break
        
    while True:
        txtidnumber.delete(0)
        if len(txtidnumber.get())==0:
            break

    while True:
        combo_fromwhere.delete(0)
        if str(combo_fromwhere.get())=="":
            break

    while True:
        combo_towhere.delete(0)
        if str(combo_towhere.get())=="":
            break

    while True:
        txttrainname.delete(0)
        if str(txttrainname.get())=="":
            break

    while True:
        txtsubtax.delete(0)
        if str(txtsubtax.get())=="":
            break
    while True:
        txttotalfair.delete(0)
        if str(txttotalfair.get())=="":
            break

        

        

    



#--plan journeyFRAME--#

def Planjourney():
    global root
    
    root=Tk()

    root.title("Plan Journey")
    root.geometry("1300x680+0+142")

    #title
    lbl_title=Label(root,text="Plan Your Journey",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
    lbl_title.place(x=0,y=0,width=1300,height=50)

    #global 
    
    global labelframeleft
    global txtcname
    global combo_Gender
    global txtpostcode
    global txtmobile
    global txtemail
    global combo_nationality
    global combo_idproof
    global txtidnumber
    global combo_fromwhere
    global combo_towhere
    global combo_nopassengers
    global combo_Search
    global txtSearch
    global ticketdate
    global trainname
    global ticketdate
    global txtsubtotal
    global subtax
    global totalfair
    global LT
    global ab

    labelframeleft=LabelFrame(root,bd=2,relief=RIDGE,text="Passengers Details",padx=2,font=("times new roman",18,"bold"))
    labelframeleft.place(x=5,y=50,width=900,height=510)

    #psngr name

    cname=Label(labelframeleft,font=("arial",11,"bold"),text="Passenger Name:",padx=10,pady=8)
    cname.grid(row=0,column=0,sticky=W)

    txtcname=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
    txtcname.grid(row=0,column=1)

    #Gender combobox

    label_Gender=Label(labelframeleft,font=("arial",11,"bold"),text="Gender:",padx=10,pady=8)
    label_Gender.grid(row=1,column=0,sticky=W)
    
    combo_Gender=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27)
    combo_Gender["value"]=("Male","Female","Other")
    combo_Gender.current(0)   
    combo_Gender.grid(row=1,column=1)

    #post code

    lblpostcode=Label(labelframeleft,font=("arial",11,"bold"),text="Pin Code:",padx=10,pady=8)
    lblpostcode.grid(row=2,column=0,sticky=W)
        
    txtpostcode=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
    txtpostcode.grid(row=2,column=1)

    # mobile number

    
    

    lblmobilenum=Label(labelframeleft,font=("arial",11,"bold"),text="PNR Number:",padx=10,pady=8)
    lblmobilenum.grid(row=3,column=0,sticky=W)
        
    txtmobile=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
    txtmobile.grid(row=3,column=1)

    x=random.randint(6145865252,6999233687)
    txtmobile.insert(0,x)
    
    

    #email

    lblemail=Label(labelframeleft,font=("arial",11,"bold"),text="Email:",padx=10,pady=8)
    lblemail.grid(row=4,column=0,sticky=W)
        
    txtemail=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
    txtemail.grid(row=4,column=1)

    #nationality

    lblnationality=Label(labelframeleft,font=("arial",12,"bold"),text="Nationality:",padx=10,pady=8)
    lblnationality.grid(row=5,column=0,sticky=W)

    combo_nationality=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27)
    combo_nationality["value"]=("Indian","American","British","Other")
    combo_nationality.current(0)
    combo_nationality.grid(row=5,column=1)

    #id proof type combobox

    lblidproof=Label(labelframeleft,font=("arial",12,"bold"),text="ID Proof Type:",padx=10,pady=8)
    lblidproof.grid(row=6,column=0,sticky=W)

    combo_idproof=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27)
    combo_idproof["value"]=("Aadhaar Card","Voter ID")
    combo_idproof.current(0)
    combo_idproof.grid(row=6,column=1)

    #id num

    lblidnum=Label(labelframeleft,font=("arial",11,"bold"),text="ID Number:",padx=10,pady=8)
    lblidnum.grid(row=7,column=0,sticky=W)
        
    txtidnumber=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
    txtidnumber.grid(row=7,column=1)


    
    #fromwhere combobox

    label_fromwhere=Label(labelframeleft,font=("arial",11,"bold"),text="From:",padx=10,pady=8)
    label_fromwhere.grid(row=8,column=0,sticky=W)
    
    combo_fromwhere=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27)
    combo_fromwhere["value"]=("Select","Howrah Junction","Kalyan Junction","Vijaywada Junction","Tatanagar Junction","New Delhi","Kanpur Central","Bangalore","Kharagpur Junction",
    "Bilaspur Junction","Pune","Gaya Junction","Anand Viahr Terminal","Asansol Junction")
    combo_fromwhere.current(0)   
    combo_fromwhere.grid(row=8,column=1)

    #towhere combobox

    label_towhere=Label(labelframeleft,font=("arial",11,"bold"),text="To:",padx=10,pady=8)
    label_towhere.grid(row=9,column=0,sticky=W)
    
    combo_towhere=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27)
    combo_towhere["value"]=("Select","Jhansi","Ghatsila","Mumbai CSMT","Chennai Junction","Lucknow Junction","Kiul Junction","Patna Junction", "Barahiya","Hijli","Hazipur","Adra Junction")
    combo_towhere.current(0)   
    combo_towhere.grid(row=9,column=1)

    #nopassengers combobox

    label_nopassengers=Label(labelframeleft,font=("arial",11,"bold"),text="Total Passangers:",padx=10,pady=8)
    label_nopassengers.grid(row=10,column=0,sticky=W)
    
    combo_nopassengers=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27,state="disabled")
    combo_nopassengers["value"]=("1")
    combo_nopassengers.current(0)   
    combo_nopassengers.grid(row=10,column=1)



    #btns of cust

    btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
    btn_frame.place(x=10,y=440,width=870,height=40)


    #book btn in custbox

    btnAdd=Button(btn_frame,text="Book Ticket",command=add_dataPsngr,font=("arial",12,"bold"),bg="black",fg="gold",activeforeground="gold",activebackground="black",width=42,height=1)
    btnAdd.grid(row=0,column=0,padx=1,pady=2)

    #btn reset

    btnReset=Button(btn_frame,text="Reset",command=resetpsgnr,font=("arial",12,"bold"),bg="black",fg="gold",activeforeground="gold",activebackground="black",width=42,height=1)
    btnReset.grid(row=0,column=2,padx=1,pady=2)

    #--Ticket Date--#
    global ticketdate
    global subtax
    global totalfair
    global txtticketdate
    global txttrainname
    global txttotalfair
    global txtsubtax
    global LT

    ticketdate=Label(labelframeleft,font=("arial",11,"bold"),text="Ticket Date:",padx=10,pady=8)
    ticketdate.place(x=430,y=2)

    txtticketdate=DateEntry(labelframeleft,selectmode='day',date_pattern='dd/mm/y',width=32,font=("times new roman",13,"bold"))
    txtticketdate.place(x=530,y=8)


    totalclass=Label(labelframeleft,font=("arial",11,"bold"),text="Class:",padx=10,pady=8)
    totalclass.place(x=430,y=43)

    txtclass=ttk.Combobox(labelframeleft,font=("arial",11,"bold"),width=29)
    txtclass["value"]=["Air-Conditioned Executive Chair Class (EC)","Air-Conditioned First Class (1AC)","Air-Conditioned Two Tier Class (2AC)","Air-Conditioned Three Tier Class (3AC)","First Class (FC)","Sleeper Class (SL)","AC Chair Class (CC)","Second Class (2S)"]   
    txtclass.current(0)
    txtclass.place(x=530,y=49)

    traintime=Label(labelframeleft,font=("arial",11,"bold"),text="Train Time:",padx=10,pady=8)
    traintime.place(x=430,y=121)

    txttraintime=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
    txttraintime.place(x=530,y=129)



    trainname=Label(labelframeleft,font=("arial",11,"bold"),text="Train Name:",padx=10,pady=8)
    trainname.place(x=430,y=83)

    txttrainname=ttk.Combobox(labelframeleft,font=("arial",11,"bold"),width=29)
    txttrainname["value"]=LT   
    txttrainname.place(x=530,y=89)


    subtotal=Label(labelframeleft,font=("arial",12,"bold"),text="Fair:",padx=10,pady=8)
    subtotal.place(x=430,y=159)

    txtsubtotal=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
    txtsubtotal.place(x=530,y=169)


    subtax=Label(labelframeleft,font=("arial",12,"bold"),text="Tax:",padx=10,pady=8)
    subtax.place(x=430,y=199)

    txtsubtax=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
    txtsubtax.place(x=530,y=208)

    totalfair=Label(labelframeleft,font=("arial",11,"bold"),text="Total:",padx=10,pady=8)
    totalfair.place(x=430,y=231)

    txttotalfair=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
    txttotalfair.place(x=530,y=240)


    def showtrain():
        global combo_fromwhere
        global combo_towhere
        global trainname
        global ticketdate
        global subtax
        global totalfair
        global txtticketdate
        global txttrainname
        global txttotalfair
        global txtsubtax
        global LT

        while True:
            txttrainname.delete(0)
            if str(txttrainname.get())=="":
                break
        while True:
            txtsubtax.delete(0)
            if str(txtsubtax.get())=="":
                break
        while True:
            txttotalfair.delete(0)
            if str(txttotalfair.get())=="":
                break            
        if str(combo_fromwhere.get())=="" or str(combo_fromwhere.get())=="Select" or str(combo_towhere.get())=="" or str(combo_towhere.get())=="Select":
            messagebox.showerror("Error","Please select From and To location",parent=root)
        else:
            L=["Rajdhani Express","Raj Express","Maharaja Express","Vivek Express","Garib Rath Express","Steel Express","Janta Express","Nawab Express","Shri Ram Express","Kailash Express","Amarnath Express"]
            L1=[0,1,2,3,4,5,6,7,8,9,10]
            x=random.choice(L1)
            L1.remove(x)
            b=random.choice(L1)
            L1.remove(b)
            g=random.choice(L1)
            LT=[L[x],L[b],L[g]]
            y=round(random.uniform(10.3,20.5),2)
            z=(random.choice([910,915,920,930,935,950,940,955,965,970,980]))
            txtsubtotal.delete(0,END)
            txtsubtotal.insert(0,z)
            txtsubtax.insert(0,str(y))
            txttotalfair.insert(0,str(z+y))
            LTTime=["03:30 AM","02:00 PM","7:00 AM","9:00 PM","10:00 AM"]

            xbc=random.choice(LTTime)
            



            traintime=Label(labelframeleft,font=("arial",11,"bold"),text="Train Time:",padx=10,pady=8)
            traintime.place(x=430,y=121)

            txttraintime=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
            txttraintime.place(x=530,y=129)

            txttraintime.insert(0,xbc)

            trainname=Label(labelframeleft,font=("arial",11,"bold"),text="Train Name:",padx=10,pady=8)
            trainname.place(x=430,y=83)

            txttrainname=ttk.Combobox(labelframeleft,font=("arial",11,"bold"),width=31)
            txttrainname["value"]=LT 
            txttrainname.current(0)  
            txttrainname.place(x=530,y=89)
    
   
    btnshowtrain=Button(labelframeleft,text="Show Train",command=showtrain,font=("arial",12,"bold"),bg="black",fg="gold",activeforeground="gold",activebackground="black",width=20,height=1)
    btnshowtrain.place(x=650,y=400)


#--ADD TABLES--#

def add_dataPsngr():

   #global 
    
    global labelframeleft
    global txtcname
    global combo_Gender
    global txtpostcode
    global txtmobile
    global txtemail
    global combo_nationality
    global combo_idproof
    global txtidnumber
    global combo_fromwhere
    global combo_towhere
    global combo_nopassengers
    global Psngr_Details_Table
    global ticketdate
    global combo_fromwhere
    global combo_towhere
    global trainname
    global ticketdate
    global subtax
    global totalfair
    global txtticketdate
    global txttrainname
    global txttotalfair
    global txtsubtax   
    global combo_Search
    global txtSearch

    patternEM=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    mobile=str(txtmobile.get())
    email=str(txtemail.get())
    pin=str(txtpostcode.get())

    #Mobile number checking code

    def isvalidmobile(s):
        Pattern=re.compile("(0|91)?[6-9][0-9]{9}")
        return Pattern.match(s)
    
    def isvalidpin(s):
        global m
        regex = "^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$"
        p=re.compile(regex);
        m=re.match(p,s);
        if m is None:
            messagebox.showerror("Error","Incorrect Pincode",parent=root)            
    
    isvalidpin(pin)


    if txtcname.get()=="" or combo_fromwhere.get()=="" or txtmobile.get()=="" or txtpostcode.get()=="" or txtemail.get()=="" or txtidnumber.get()=="" or combo_towhere.get()=="" or combo_nopassengers.get()=="" or str(txtticketdate.get())=="" or str(txttrainname.get())=="" or str(txtsubtax.get())=="" or str(txttotalfair.get())=="":

        messagebox.showerror("Error","All fields are required",parent=root)

    elif (isvalidmobile(mobile)) is None:
        messagebox.showerror("Error","Incorrect Mobile Number"+"\nPlease Enter Indian Mobile Number",parent=root)

    #email check
    elif (re.fullmatch(patternEM,email)) is None:
        messagebox.showerror("Error","Incorrect Email",parent=root)
    
    else:
        try:
            conn=c.connect("train.db")
            my_cursor=conn.cursor()
            
            my_cursor.execute("insert into ticket (Name,Gender,Pincode,Mobile,Email,Nationality,Idproof,Idnumber,Fromwhere,Towhere,TotalPassengers,ticketdate,trainname,subtotal,subtax,totalfair)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(txtcname.get(),combo_Gender.get(),txtpostcode.get(),txtmobile.get(),txtemail.get(),combo_nationality.get(),combo_idproof.get(),txtidnumber.get(),combo_fromwhere.get(),combo_towhere.get(),combo_nopassengers.get(),str(txtticketdate.get()),str(txttrainname.get()),str(txtsubtotal.get()),str(txtsubtax.get()),str(txttotalfair.get())))
            
            conn.commit()

            messagebox.showinfo("Success","Ticket Book has been added",parent=root)

             #fetch data call
            resetpsgnr()
            conn.close()
        except Exception as es:
            messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=root)


    root.mainloop()

def searchpsngr():

    global combo_Search
    global txtSearch
    global Psngr_Details_Table
    
    if str(combo_Search.get())=="PNR":
        xyz="Mobile"
    else:
        xyz="Idnumber"
    

    conn=c.connect("train.db")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from ticket where "+str(xyz)+" LIKE '"+str(txtSearch.get())+"%'")
    rows=my_cursor.fetchall()

    if len(rows)!=0:
        Psngr_Details_Table.delete(*Psngr_Details_Table.get_children(),)
        for i in rows:
            Psngr_Details_Table.insert("",END,values=i)
        conn.commit()
    else:
        messagebox.showerror("Error","No Train Booking details found",parent=root)
    conn.close()

def searchpsngrC():

    global combo_Search
    global txtSearch
    global Psngr_Details_Table
    
    if str(combo_Search.get())=="PNR":
        xyz="Mobile"
    else:
        xyz="Idnumber"
    

    conn=c.connect("train.db")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from cancel where "+str(xyz)+" LIKE '"+str(txtSearch.get())+"%'")
    rows=my_cursor.fetchall()

    if len(rows)!=0:
        Psngr_Details_Table.delete(*Psngr_Details_Table.get_children(),)
        for i in rows:
            Psngr_Details_Table.insert("",END,values=i)
        conn.commit()
    else:
        messagebox.showerror("Error","No Train Booking details found",parent=root)
    conn.close()

def fetch_dataPsngr():


    global labelframeleft
    global txtcname
    global combo_Gender
    global txtpostcode
    global txtmobile
    global txtemail
    global combo_nationality
    global combo_idproof
    global txtidnumber
    global combo_fromwhere
    global combo_towhere
    global combo_nopassengers
    global Psngr_Details_Table
    global row
    global fetch_dataPsngr


    conn=c.connect("train.db")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from ticket")
    rows=my_cursor.fetchall()
    if len(rows)!=0:
        Psngr_Details_Table.delete(*Psngr_Details_Table.get_children())
        for i in rows:
            Psngr_Details_Table.insert("",END,values=i) #inserting into table
        conn.commit()
    conn.close()

def fetch_dataPsngrC():


    global labelframeleft
    global txtcname
    global combo_Gender
    global txtpostcode
    global txtmobile
    global txtemail
    global combo_nationality
    global combo_idproof
    global txtidnumber
    global combo_fromwhere
    global combo_towhere
    global combo_nopassengers
    global Psngr_Details_Table
    global row
    global fetch_dataPsngr


    conn=c.connect("train.db")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from cancel")
    rows=my_cursor.fetchall()
    if len(rows)!=0:
        Psngr_Details_Table.delete(*Psngr_Details_Table.get_children())
        for i in rows:
            Psngr_Details_Table.insert("",END,values=i) #inserting into table
        conn.commit()
    conn.close()



    #--ADD TABLES--#

def addtables():
    conn=c.connect("train.db")
    my_cursor=conn.cursor()
    sql1="CREATE TABLE if not exists ticket (\
        Name varchar(30),\
        Gender char(15),\
        Pincode varchar(20),\
        Mobile varchar(10),\
        Email varchar(50),\
        Nationality varchar(50),\
        Idproof varchar(20),\
        Idnumber varchar(20) UNIQUE,\
        Fromwhere varchar(20),\
        Towhere varchar(20),\
        TotalPassengers varchar(20),\
        ticketdate varchar(20),\
        trainname varchar(40),\
        subtotal varchar(20),\
        subtax varchar(20),\
        totalfair varchar(20),\
        PRIMARY KEY (Mobile));"



    my_cursor.execute(sql1)

    sql2="CREATE TABLE if not exists cancel (\
        Name varchar(30),\
        Gender char(15),\
        Pincode varchar(20),\
        Mobile varchar(10),\
        Email varchar(50),\
        Nationality varchar(50),\
        Idproof varchar(20),\
        Idnumber varchar(20) UNIQUE,\
        Fromwhere varchar(20),\
        Towhere varchar(20),\
        TotalPassengers varchar(20),\
        ticketdate varchar(20),\
        trainname varchar(40),\
        subtotal varchar(20),\
        subtax varchar(20),\
        totalfair varchar(20),\
        PRIMARY KEY (Mobile));"

        

    my_cursor.execute(sql2)

    sql="CREATE TABLE if not exists login (\
        fullname varchar(30),\
        username varchar(30) UNIQUE,\
        contact varchar(30),\
        recode varchar(30),\
        pass varchar(30),\
        conpass varchar(30),\
        PRIMARY KEY (recode));"
    
    my_cursor.execute(sql)



def printdata():
    conn=c.connect("train.db")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from ticket")
    rows=my_cursor.fetchall()
    filename="filerecord.txt"
    f=open(filename,"w")
    f.write("-"*350+"\n")
    f.write("-"*350+"\n")
    f.write("\t\t\t\t\t\t   RESERVATION DATABASE RECORD"+"\n")
    f.write("-"*350+"\n")
    f.write("-"*350+"\n\n")
    f.write("-"*350+"\n")
    f.write("Name\t\tGender\t\tPincode\t\tPNR\t\t Email\t\tNationality\tId Proof\tId Number\t\tFrom Where\t\tTo Where\t Total Passengers\tTicket Date\tTrain Name\t\tFair\t\tSubtax \tTotal Fair")
    f.write("\n"+"-"*350)
    if len(rows)!=0:
        for i in rows:
            f.write("\n"+i[0]+"\t\t"+i[1]+"\t\t"+i[2]+"\t\t"+i[3]+"\t"+i[4]+"\t"+i[5]+"\t\t"+i[6]+"\t"+i[7]+"\t\t\t"+i[8]+"\t\t"+i[9]+"\t\t\t"+i[10]+"\t\t"+i[11]+"\t"+i[12]+"\t\t"+i[13]+"\t\t"+i[14]+"\t"+i[15])
            f.write("\n"+"-"*350+"\n")
    f.flush()
    f.close()
    program="notepad.exe"
    subprocess.Popen([program,filename])

def printbillind():
    global row
    global Psngr_Details_Table
    if (row)!=0:
        i=row
        filename="filebill.txt"
        f=open(filename,"w")
        f.write("-"*350+"\n")
        f.write("-"*350+"\n")
        f.write("\t\t\t\t\t\t   RESERVATION DATABASE RECORD"+"\n")
        f.write("-"*350+"\n")
        f.write("-"*350+"\n\n")
        f.write("-"*350+"\n")
        f.write("Name\t\tGender\t\tPincode\t\tPNR\t\t Email\t\tNationality\tId Proof\tId Number\t\tFrom Where\t\tTo Where\t Total Passengers\tTicket Date\tTrain Name\t\tFair\t\tSubtax \tTotal Fair")
        f.write("\n"+"-"*350)
        f.write("\n"+str(i[0])+"\t\t"+str(i[1])+"\t\t"+str(i[2])+"\t\t"+str(i[3])+"\t"+str(i[4])+"\t"+str(i[5])+"\t\t"+str(i[6])+"\t"+str(i[7])+"\t\t\t"+str(i[8])+"\t\t"+str(i[9])+"\t\t\t"+str(i[10])+"\t\t"+str(i[11])+"\t"+str(i[12])+"\t\t"+str(i[13])+"\t\t"+str(i[14])+"\t"+str(i[15]))
        f.write("\n"+"-"*350+"\n")
        f.flush()
        f.close()
        program="notepad.exe"
        subprocess.Popen([program,filename])


    else:
        messagebox.showerror("Error","Please select details first!!",parent=root)
        
    



def get_cuersorbill(event=""):#wrong spelling dale hai
    global labelframeleft
    global txtcname
    global combo_Gender
    global txtpostcode
    global txtmobile
    global txtemail
    global combo_nationality
    global combo_idproof
    global txtidnumber
    global combo_fromwhere
    global combo_towhere
    global combo_nopassengers
    global Psngr_Details_Table
    global ticketdate
    global subtax
    global totalfair
    global txtticketdate
    global txttrainname
    global txttotalfair
    global txtsubtax
    global combo_Search
    global txtSearch
    global row

    cusrsor_row=Psngr_Details_Table.focus()
    content=Psngr_Details_Table.item(cusrsor_row)
    
    row=content["values"]






#--my bookings FRAME--#

def mybookings():
    global root
    
    root=Tk()

    root.title("MY BOOKINGS")
    root.geometry("1300x680+0+142")
    global labelframeleft
    global txtcname
    global combo_Gender
    global txtpostcode
    global txtmobile
    global txtemail
    global combo_nationality
    global combo_idproof
    global txtidnumber
    global combo_fromwhere
    global combo_towhere
    global combo_nopassengers
    global Psngr_Details_Table
    global ticketdate
    global subtax
    global totalfair
    global txtticketdate
    global txttrainname
    global txttotalfair
    global txtsubtax
    global combo_Search
    global txtSearch
    global row

    #title
    lbl_title=Label(root,text="MY BOOKINGS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
    lbl_title.place(x=0,y=0,width=1300,height=50)

    #cust inside frame


    Table_Frame=LabelFrame(root,bd=2,relief=RIDGE,text="View Details And Search System",padx=2,font=("times new roman",13,"bold"))
    Table_Frame.place(x=10,y=53,width=1400,height=506)

    #search by (red colour)
    lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By",bg="red",fg="white")
    lblSearchBy.grid(row=0,column=0,sticky=W,padx=3)

    #search by

    combo_Search=ttk.Combobox(Table_Frame,font=("arial",12,"bold"),width=24)
    combo_Search["value"]=("PNR","Idnumber")
    combo_Search.current(0)
    combo_Search.grid(row=0,column=1,padx=2)

    #search field

    txtSearch=ttk.Entry(Table_Frame,width=24,font=("times new roman",13,"bold"))
    txtSearch.grid(row=0,column=2,padx=2)

    btnSearch=Button(Table_Frame,text="Search",command=searchpsngr,font=("arial",12,"bold"),bg="black",fg="gold",activeforeground="gold",activebackground="black",width=10)
    btnSearch.grid(row=0,column=3,padx=1,pady=2)

    btnShowAll=Button(Table_Frame,text="Show All",command=fetch_dataPsngr,font=("arial",12,"bold"),bg="black",fg="gold",activeforeground="gold",activebackground="black",width=10)
    btnShowAll.grid(row=0,column=4,padx=1,pady=2)

    btnShowbill=Button(Table_Frame,text="Bill",command=printbillind,font=("arial",12,"bold"),bg="black",fg="gold",activeforeground="gold",activebackground="black",width=10)
    btnShowbill.grid(row=0,column=5,padx=1,pady=2)

    btnShowAllData=Button(Table_Frame,text="All Records",command=printdata,font=("arial",12,"bold"),bg="black",fg="gold",activeforeground="gold",activebackground="black",width=10)
    btnShowAllData.grid(row=0,column=6,padx=1,pady=2)

     #show data table

    Details_Table=Frame(Table_Frame,bd=2,relief=RIDGE)
    Details_Table.place(x=0,y=50,width=1280,height=400)

    #scroll bar 

    scroll_x=ttk.Scrollbar(Details_Table,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(Details_Table,orient=VERTICAL)

    global Psngr_Details_Table

    Psngr_Details_Table=ttk.Treeview(Details_Table,column=("Name","Gender","Pincode","Mobile","Email","Nationality","Idproof","Idnumber","Fromwhere","Towhere","TotalPassengers","ticketdate","trainname","subtotal","subtax","totalfair"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x.config(command=Psngr_Details_Table.xview)

    scroll_y.config(command=Psngr_Details_Table.yview)

    #scroll bar column show like name,Gender,......

    Psngr_Details_Table.heading("Name",text="Name")
    Psngr_Details_Table.heading("Gender",text="Gender")
    Psngr_Details_Table.heading("Pincode",text="Pin Code")
    Psngr_Details_Table.heading("Mobile",text="PNR Number")
    Psngr_Details_Table.heading("Email",text="Email")
    Psngr_Details_Table.heading("Nationality",text="Nationality")
    Psngr_Details_Table.heading("Idproof",text="ID Proof")
    Psngr_Details_Table.heading("Idnumber",text="ID Number")
    Psngr_Details_Table.heading("Fromwhere",text="From")
    Psngr_Details_Table.heading("Towhere",text="To")
    Psngr_Details_Table.heading("TotalPassengers",text="Total Passenegers")
    Psngr_Details_Table.heading("ticketdate",text="Ticket Date")
    Psngr_Details_Table.heading("trainname",text="Train Name")
    Psngr_Details_Table.heading("subtotal",text="Fair")
    Psngr_Details_Table.heading("subtax",text="Total Tax")
    Psngr_Details_Table.heading("totalfair",text="Total Fair")



    #show karenge avi headings

    Psngr_Details_Table["show"]="headings"

    
    #width shape karre columns ka

    Psngr_Details_Table.column("Name",width=70)
    Psngr_Details_Table.column("Gender",width=60)
    Psngr_Details_Table.column("Pincode",width=70)
    Psngr_Details_Table.column("Mobile",width=70)
    Psngr_Details_Table.column("Email",width=80)
    Psngr_Details_Table.column("Nationality",width=70)
    Psngr_Details_Table.column("Idproof",width=80)
    Psngr_Details_Table.column("Idnumber",width=70)
    Psngr_Details_Table.column("Fromwhere",width=90)
    Psngr_Details_Table.column("Towhere",width=70)
    Psngr_Details_Table.column("TotalPassengers",width=70)
    Psngr_Details_Table.column("ticketdate",width=70)
    Psngr_Details_Table.column("trainname",width=80)
    Psngr_Details_Table.column("subtotal",width=70)
    Psngr_Details_Table.column("subtax",width=70)
    Psngr_Details_Table.column("totalfair",width=80)

    Psngr_Details_Table.pack(fill=BOTH,expand=2)

    Psngr_Details_Table.bind("<ButtonRelease-1>",get_cuersorbill)

    fetch_dataPsngr()

    root.mainloop()
def deletecust():
        global row
        global labelframeleft
        global txtcname
        global combo_Gender
        global txtpostcode
        global txtmobile
        global txtemail
        global combo_nationality
        global combo_idproof
        global txtidnumber
        global combo_fromwhere
        global combo_towhere
        global combo_nopassengers
        global Psngr_Details_Table
        global ticketdate
        global subtax
        global totalfair
        global txtticketdate
        global txttrainname
        global txttotalfair
        global txtsubtax
        global combo_Search
        global txtSearch
        global fetch_dataPsngr

        

        mDelete=messagebox.askyesno("Railway Management System","Do you want to delete this booking",parent=root)
        if mDelete>0:
            try:
                conn=c.connect("train.db")
                my_cursor=conn.cursor()
                
                my_cursor.execute("insert into cancel (Name,Gender,Pincode,Mobile,Email,Nationality,Idproof,Idnumber,Fromwhere,Towhere,TotalPassengers,ticketdate,trainname,subtotal,subtax,totalfair)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15]))
                
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=root)

            conn=c.connect("train.db")
            my_cursor=conn.cursor()
            mo=str(row[3])
            sql="delete from ticket where Mobile='%s'"%(str(mo))
            my_cursor.execute(sql)
            
            conn.commit()
            conn.close()
            
            messagebox.showinfo("Deleted","Booking details has been deleted successfully",parent=root)
            fetch_dataPsngr()
            root.destroy()
            cancelticket()

        else:
            if not mDelete:
                return



def get_cuersor(event=""):#wrong spelling dale hai
    global labelframeleft
    global txtcname
    global combo_Gender
    global txtpostcode
    global txtmobile
    global txtemail
    global combo_nationality
    global combo_idproof
    global txtidnumber
    global combo_fromwhere
    global combo_towhere
    global combo_nopassengers
    global Psngr_Details_Table
    global ticketdate
    global subtax
    global totalfair
    global txtticketdate
    global txttrainname
    global txttotalfair
    global txtsubtax
    global combo_Search
    global txtSearch
    global row

    cusrsor_row=Psngr_Details_Table.focus()
    content=Psngr_Details_Table.item(cusrsor_row)
    
    row=content["values"]

def cancelticket():
    global root
    
    root=Tk()

    root.title("MY BOOKINGS")
    root.geometry("1300x680+0+142")
    global labelframeleft
    global txtcname
    global combo_Gender
    global txtpostcode
    global txtmobile
    global txtemail
    global combo_nationality
    global combo_idproof
    global txtidnumber
    global combo_fromwhere
    global combo_towhere
    global combo_nopassengers
    global Psngr_Details_Table
    global ticketdate
    global subtax
    global totalfair
    global txtticketdate
    global txttrainname
    global txttotalfair
    global txtsubtax
    global combo_Search
    global txtSearch
    global row

    #title
    lbl_title=Label(root,text="MY BOOKINGS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
    lbl_title.place(x=0,y=0,width=1300,height=50)

    #cust inside frame


    Table_Frame=LabelFrame(root,bd=2,relief=RIDGE,text="View Details And Search System",padx=2,font=("times new roman",13,"bold"))
    Table_Frame.place(x=10,y=53,width=1400,height=506)

    #search by (red colour)
    lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By",bg="red",fg="white")
    lblSearchBy.grid(row=0,column=0,sticky=W,padx=3)

    #search by

    combo_Search=ttk.Combobox(Table_Frame,font=("arial",12,"bold"),width=24)
    combo_Search["value"]=("PNR","Idnumber")
    combo_Search.current(0)
    combo_Search.grid(row=0,column=1,padx=2)

    #search field

    txtSearch=ttk.Entry(Table_Frame,width=24,font=("times new roman",13,"bold"))
    txtSearch.grid(row=0,column=2,padx=2)

    btnSearch=Button(Table_Frame,text="Search",command=searchpsngr,font=("arial",12,"bold"),bg="black",fg="gold",activeforeground="gold",activebackground="black",width=10)
    btnSearch.grid(row=0,column=3,padx=1,pady=2)

    btnShowAll=Button(Table_Frame,text="Show All",command=fetch_dataPsngr,font=("arial",12,"bold"),bg="black",fg="gold",activeforeground="gold",activebackground="black",width=10)
    btnShowAll.grid(row=0,column=4,padx=1,pady=2)

     #show data table

    Details_Table=Frame(Table_Frame,bd=2,relief=RIDGE)
    Details_Table.place(x=0,y=50,width=1280,height=400)

    #scroll bar 

    scroll_x=ttk.Scrollbar(Details_Table,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(Details_Table,orient=VERTICAL)

    global Psngr_Details_Table

    Psngr_Details_Table=ttk.Treeview(Details_Table,column=("Name","Gender","Pincode","Mobile","Email","Nationality","Idproof","Idnumber","Fromwhere","Towhere","TotalPassengers","ticketdate","trainname","subtotal","subtax","totalfair"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x.config(command=Psngr_Details_Table.xview)

    scroll_y.config(command=Psngr_Details_Table.yview)

    #scroll bar column show like name,Gender,......

    Psngr_Details_Table.heading("Name",text="Name")
    Psngr_Details_Table.heading("Gender",text="Gender")
    Psngr_Details_Table.heading("Pincode",text="Pin Code")
    Psngr_Details_Table.heading("Mobile",text="PNR Number")
    Psngr_Details_Table.heading("Email",text="Email")
    Psngr_Details_Table.heading("Nationality",text="Nationality")
    Psngr_Details_Table.heading("Idproof",text="ID Proof")
    Psngr_Details_Table.heading("Idnumber",text="ID Number")
    Psngr_Details_Table.heading("Fromwhere",text="From")
    Psngr_Details_Table.heading("Towhere",text="To")
    Psngr_Details_Table.heading("TotalPassengers",text="Total Passenegers")
    Psngr_Details_Table.heading("ticketdate",text="Ticket Date")
    Psngr_Details_Table.heading("trainname",text="Train Name")
    Psngr_Details_Table.heading("subtotal",text="Fair")
    Psngr_Details_Table.heading("subtax",text="Total Tax")
    Psngr_Details_Table.heading("totalfair",text="Total Fair")



    #show karenge avi headings

    Psngr_Details_Table["show"]="headings"

    
    #width shape karre columns ka

    Psngr_Details_Table.column("Name",width=70)
    Psngr_Details_Table.column("Gender",width=60)
    Psngr_Details_Table.column("Pincode",width=70)
    Psngr_Details_Table.column("Mobile",width=70)
    Psngr_Details_Table.column("Email",width=80)
    Psngr_Details_Table.column("Nationality",width=70)
    Psngr_Details_Table.column("Idproof",width=80)
    Psngr_Details_Table.column("Idnumber",width=70)
    Psngr_Details_Table.column("Fromwhere",width=90)
    Psngr_Details_Table.column("Towhere",width=70)
    Psngr_Details_Table.column("TotalPassengers",width=70)
    Psngr_Details_Table.column("ticketdate",width=70)
    Psngr_Details_Table.column("trainname",width=80)
    Psngr_Details_Table.column("subtotal",width=70)
    Psngr_Details_Table.column("subtax",width=70)
    Psngr_Details_Table.column("totalfair",width=80)

    Psngr_Details_Table.pack(fill=BOTH,expand=2)

    Psngr_Details_Table.bind("<ButtonRelease-1>",get_cuersor)

            

    btn_frame=Frame(root,bd=2,relief=RIDGE)
    btn_frame.place(x=10,y=530,width=1300,height=40)


    #book btn in custbox

    btncancel=Button(btn_frame,text="Cancel Ticket",command=deletecust,font=("arial",12,"bold"),bg="black",fg="gold",activeforeground="gold",activebackground="black",width=128,height=1)
    btncancel.grid(row=0,column=0,padx=1,pady=2)

   
    fetch_dataPsngr()

    #add data inPsngr
    root.mainloop()

    
def canceled():
    global root
    
    root=Tk()

    root.title("MY BOOKINGS")
    root.geometry("1300x680+0+142")
    global labelframeleft
    global txtcname
    global combo_Gender
    global txtpostcode
    global txtmobile
    global txtemail
    global combo_nationality
    global combo_idproof
    global txtidnumber
    global combo_fromwhere
    global combo_towhere
    global combo_nopassengers
    global Psngr_Details_Table
    global ticketdate
    global subtax
    global totalfair
    global txtticketdate
    global txttrainname
    global txttotalfair
    global txtsubtax
    global combo_Search
    global txtSearch
    global row

    #title
    lbl_title=Label(root,text="CANCELED TICKETS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
    lbl_title.place(x=0,y=0,width=1300,height=50)

    #cust inside frame


    Table_Frame=LabelFrame(root,bd=2,relief=RIDGE,text="View Details And Search System",padx=2,font=("times new roman",13,"bold"))
    Table_Frame.place(x=10,y=53,width=1400,height=506)

    #search by (red colour)
    lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By",bg="red",fg="white")
    lblSearchBy.grid(row=0,column=0,sticky=W,padx=3)

    #search by

    combo_Search=ttk.Combobox(Table_Frame,font=("arial",12,"bold"),width=24)
    combo_Search["value"]=("PNR","Idnumber")
    combo_Search.current(0)
    combo_Search.grid(row=0,column=1,padx=2)

    #search field

    txtSearch=ttk.Entry(Table_Frame,width=24,font=("times new roman",13,"bold"))
    txtSearch.grid(row=0,column=2,padx=2)

    btnSearch=Button(Table_Frame,text="Search",command=searchpsngrC,font=("arial",12,"bold"),bg="black",fg="gold",activeforeground="gold",activebackground="black",width=10)
    btnSearch.grid(row=0,column=3,padx=1,pady=2)

    btnShowAll=Button(Table_Frame,text="Show All",command=fetch_dataPsngrC,font=("arial",12,"bold"),bg="black",fg="gold",activeforeground="gold",activebackground="black",width=10)
    btnShowAll.grid(row=0,column=4,padx=1,pady=2)

     #show data table

    Details_Table=Frame(Table_Frame,bd=2,relief=RIDGE)
    Details_Table.place(x=0,y=50,width=1280,height=400)

    #scroll bar 

    scroll_x=ttk.Scrollbar(Details_Table,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(Details_Table,orient=VERTICAL)

    global Psngr_Details_Table

    Psngr_Details_Table=ttk.Treeview(Details_Table,column=("Name","Gender","Pincode","Mobile","Email","Nationality","Idproof","Idnumber","Fromwhere","Towhere","TotalPassengers","ticketdate","trainname","subtotal","subtax","totalfair"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x.config(command=Psngr_Details_Table.xview)

    scroll_y.config(command=Psngr_Details_Table.yview)

    #scroll bar column show like name,Gender,......

    Psngr_Details_Table.heading("Name",text="Name")
    Psngr_Details_Table.heading("Gender",text="Gender")
    Psngr_Details_Table.heading("Pincode",text="Pin Code")
    Psngr_Details_Table.heading("Mobile",text="PNR Number")
    Psngr_Details_Table.heading("Email",text="Email")
    Psngr_Details_Table.heading("Nationality",text="Nationality")
    Psngr_Details_Table.heading("Idproof",text="ID Proof")
    Psngr_Details_Table.heading("Idnumber",text="ID Number")
    Psngr_Details_Table.heading("Fromwhere",text="From")
    Psngr_Details_Table.heading("Towhere",text="To")
    Psngr_Details_Table.heading("TotalPassengers",text="Total Passenegers")
    Psngr_Details_Table.heading("ticketdate",text="Ticket Date")
    Psngr_Details_Table.heading("trainname",text="Train Name")
    Psngr_Details_Table.heading("subtotal",text="Fair")
    Psngr_Details_Table.heading("subtax",text="Total Tax")
    Psngr_Details_Table.heading("totalfair",text="Total Fair")



    #show karenge avi headings

    Psngr_Details_Table["show"]="headings"

    
    #width shape karre columns ka

    Psngr_Details_Table.column("Name",width=70)
    Psngr_Details_Table.column("Gender",width=60)
    Psngr_Details_Table.column("Pincode",width=70)
    Psngr_Details_Table.column("Mobile",width=70)
    Psngr_Details_Table.column("Email",width=80)
    Psngr_Details_Table.column("Nationality",width=70)
    Psngr_Details_Table.column("Idproof",width=80)
    Psngr_Details_Table.column("Idnumber",width=70)
    Psngr_Details_Table.column("Fromwhere",width=90)
    Psngr_Details_Table.column("Towhere",width=70)
    Psngr_Details_Table.column("TotalPassengers",width=70)
    Psngr_Details_Table.column("ticketdate",width=70)
    Psngr_Details_Table.column("trainname",width=80)
    Psngr_Details_Table.column("subtotal",width=70)
    Psngr_Details_Table.column("subtax",width=70)
    Psngr_Details_Table.column("totalfair",width=80)

    Psngr_Details_Table.pack(fill=BOTH,expand=2)

    fetch_dataPsngrC()

    root.mainloop()


    

def trainmain():
    root=Tk() 
    root.title("Railway Reservation System")
    root.geometry("1550x890+0+0")


        #title "HOTEL MANAGEMENT SYSTEM"

    lbl_title=Label(root,text="RAILWAY RESERVATION SYSTEM",font=("times new roman",60,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
    lbl_title.place(x=0,y=0,width=1550,height=100)


        #MAIN FRAME

    main_frame=Frame(root,bd=4,relief=RIDGE)
    main_frame.place(x=0,y=105,width=1550,height=680)

    #image main center image
    img4=Image.open("imagesaman\\down2nd.jpg")
    img4=img4.resize((1310,680),Image.ANTIALIAS)
    photoimg4=ImageTk.PhotoImage(img4)

    lblimg=Label(main_frame,image=photoimg4,bd=4,relief=RIDGE)
    lblimg.place(x=0,y=0,width=1300,height=680)

    #MENU

    lbl_menu=Label(main_frame,text="MENU",font=("times new roman",30,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
    lbl_menu.place(x=1301,y=5 ,width=230,height=80)



        #BTN FRAME 

    btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
    btn_frame.place(x=1301,y=80,width=231,height=490)

    #PLAN MY JOURNEY btn

    cust_btn=Button(btn_frame,text="PLAN JOURNEY",command=Planjourney,width=20,height=3,font=("times new roman",16,"bold"),bg="black",fg="gold",activeforeground="gold",activebackground="black",bd=0,cursor="hand2")
    cust_btn.grid(row=0,column=0,pady=1)


        #BOOKINGS btn
    
    room_btn=Button(btn_frame,text="PNR SEARCH",command=mybookings,width=20,height=3,font=("times new roman",16,"bold"),bg="black",fg="gold",activeforeground="gold",activebackground="black",bd=0,cursor="hand2")
    room_btn.grid(row=1,column=0,pady=1)


        #CANCEL TICKET btn

    details_btn=Button(btn_frame,text="CANCEL TICKET",command=cancelticket,width=20,height=3,font=("times new roman",16,"bold"),bg="black",fg="gold",activeforeground="gold",activebackground="black",bd=0,cursor="hand2")
    details_btn.grid(row=2,column=0,pady=1)

    hiscancle_btn=Button(btn_frame,text="CANCLED TICKETS",command=canceled,width=20,height=3,font=("times new roman",15,"bold"),bg="black",fg="gold",activeforeground="gold",activebackground="black",bd=0,cursor="hand2")
    hiscancle_btn.grid(row=3,column=0,pady=1)

        #logout btn

    def logoutfunc():
        x=messagebox.askyesno("Logout","Do you want to logout ?",parent=root)
        if x>0:
            root.destroy()
            log() 

    logout_btn=Button(btn_frame,text="LOGOUT",command=logoutfunc,width=20,height=3,font=("times new roman",16,"bold"),bg="black",fg="gold",activeforeground="gold",activebackground="black",bd=0,cursor="hand2")
    logout_btn.grid(row=4,column=0,pady=1)

    

        #2nd down image (after menu option)
    img6=Image.open("imagesaman\\left1.jpg")
    img6=img6.resize((230,180),Image.ANTIALIAS)
    photoimg6=ImageTk.PhotoImage(img6)

    lblimg=Label(main_frame,image=photoimg6,bd=4,relief=RIDGE)
    lblimg.place(x=1301,y=500,width=230,height=180)


    addtables()
    root.mainloop()






def log():
    global root
    global fname_entry
    global l_entry
    global txt_contact
    global txt_recode
    global txt_pass
    global txt_conpass
    root=Tk()
    def Register():
        global fname_entry
        global l_entry
        global txt_contact
        global txt_recode
        global txt_pass
        global txt_conpass
        global checkbtn

        root.title("Register")
        root.geometry("1600x900+0+0")

        #background image

        bg1=ImageTk.PhotoImage(file="imagesaman\\corner1.jpg")
            
        bg1_lbl=Label(root,image=bg1,relief=RIDGE)
        bg1_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #bg 2
        bgimage=Image.open("imagesaman\\left.jpg")
        bgimage=bgimage.resize((460,550),Image.ANTIALIAS)
        bg2=ImageTk.PhotoImage(bgimage)

        
        bg2_lbl=Label(root,image=bg2,bd=4,relief=RIDGE)
        bg2_lbl.place(x=130,y=130,width=460,height=550)

        #side frame

        frame=Frame(root,bg="white")
        frame.place(x=590,y=130,width=800,height=550)

        #frame inside work

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen")
        register_lbl.place(x=20,y=20)

        #--login button--#

        loginbtnreg=Button(frame,command=Login_Window,text="Login Now",font=("Arial",13,"bold"),bd=3,relief=RIDGE,fg="black",bg="aqua",activeforeground="black",activebackground="aqua")
        loginbtnreg.place(x=630,y=20,width=120,height=35)

        #labels and entry fields

        framename=Label(frame,text="First Name",font=("times new roman",20,"bold"),bg="white")
        framename.place(x=50,y=100)

        #entry field for first name

        fname_entry=ttk.Entry(frame,font=("times new roman",16,"bold"))
        fname_entry.place(x=50,y=135,width=230)

        #last name

        l_name=Label(frame,text="User Name",font=("times new roman",20,"bold"),bg="white")
        l_name.place(x=370,y=100)

        l_entry=ttk.Entry(frame,font=("times new roman",16,"bold"))
        l_entry.place(x=370,y=136,width=230)

        #contact

        contact_name=Label(frame,text="Contact No",font=("times new roman",20,"bold"),bg="white")
        contact_name.place(x=50,y=170)

        txt_contact=ttk.Entry(frame,font=("times new roman",16,"bold"))
        txt_contact.place(x=50,y=210,width=230)

        #recovery  code

        recode=Label(frame,text="Recovery Code",font=("times new roman",20,"bold"),bg="white")
        recode.place(x=370,y=170)

        txt_recode=ttk.Entry(frame,font=("times new roman",16,"bold"))
        txt_recode.place(x=370,y=207,width=230)
        
        #password

        password=Label(frame,text="Password",font=("times new roman",20,"bold"),bg="white")
        password.place(x=50,y=245)

        txt_pass=ttk.Entry(frame,font=("times new roman",16,"bold"))
        txt_pass.place(x=50,y=282,width=230)

        #confirm pass

        conpass=Label(frame,text="Confirm Password",font=("times new roman",20,"bold"),bg="white")
        conpass.place(x=370,y=240)

        txt_conpass=ttk.Entry(frame,font=("times new roman",16,"bold"))
        txt_conpass.place(x=370,y=277,width=230)


        #check btn terms and conditions
        global var_check
        var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=var_check,text="I Agree the Terms & Conditions",font=("times new roman",15,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=330)
        def registerclick():
            global var_check
            global fname_entry
            global l_entry
            global txt_contact
            global txt_recode
            global txt_pass
            global txt_conpass



            if str(fname_entry.get())=="" or str(l_entry.get())=="" or str(txt_contact.get())=="" or str(txt_recode.get())=="" or str(txt_pass.get())=="" or str(txt_conpass.get())=="":
                messagebox.showerror("Error","All fields are required",parent=root)

            elif not fname_entry.get().isalpha() or not l_entry.get().isalpha():
                messagebox.showerror("Error","Please Enter Name in alphabets",parent=root)
            elif not str(txt_contact.get()).isdigit() or not str(txt_recode.get()).isdigit():
                messagebox.showerror("Error","Please Enter Digits in the desired box",parent=root)
            elif str(txt_pass.get())!=str(txt_conpass.get()):
                messagebox.showerror("Error","Password & Confirm Password must be same",parent=root)
            elif var_check.get()==0:
                messagebox.showerror("Error","Please agree our terms and conditions",parent=root)
            else:
                messagebox.showinfo("Done","Welcome to our Railway Reservation Project",parent=root)
                conn=c.connect("train.db")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from login where username='%s'"%(str(l_entry.get())))
                row=my_cursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist with same details\nPlease try again",parent=root)
                else:
                    my_cursor.execute("insert into login (fullname,username,contact,recode,pass,conpass)values('%s','%s','%s','%s','%s','%s')"%(str(fname_entry.get()),str(l_entry.get()),str(txt_contact.get()),str(txt_recode.get()),str(txt_pass.get()),str(txt_conpass.get())))
                    conn.commit()
                    messagebox.showinfo("Registered","Data registered successfully",parent=root)
                    conn.close()
        #register now

        img=Image.open("imagesaman\\amansn.jpg")
        img=img.resize((170,50),Image.ANTIALIAS)
        photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=photoimage,borderwidth=0,command=registerclick,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=203,y=390,width=300)

        

        root.mainloop()

    def Login_Window():
        global root
        global fname_entry
        global l_entry
        global txt_contact
        global txt_recode
        global txt_pass
        global txt_conpass
        global txtuser
        global txtpass
        global txt_newpass
        
        root.title("Railway Reservation System Login Pannel")
        root.geometry("1550x800+0+0")

        bgimage=Image.open("imagesaman\\mana.jpg")
        bgimage=bgimage.resize((1550,800),Image.ANTIALIAS)
        bg=ImageTk.PhotoImage(bgimage)

        lbl_bg=Label(root,image=bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(root,bg="black")
        frame.place(x=603,y=175,width=340,height=450) #x and y pos value and width and height size of box

        img1=Image.open("images\\loginicon.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=180,width=100,height=100)

            #get started label

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=107,y=100)

            #user name label

        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=60,y=155)
            
        txtuser=ttk.Entry(frame,font=("times new roman",13,"bold"))       
        txtuser.place(x=35,y=180,width=270)

            #password label

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=60,y=225)

        txtpass=ttk.Entry(frame,font=("times new roman",13,"bold"),show="*")       
        txtpass.place(x=35,y=250,width=270)

            #Icon Images of username 

        img2=Image.open("imagesaman\\indianrailways1st.jpg")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=640,y=330,width=25,height=25)

            #Icon Images of password

        img3=Image.open("imagesaman\\amaph.jpg")
        img3=img3.resize((55,25),Image.ANTIALIAS)
        photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=639,y=400,width=25,height=25)
            
            #login btn in login pannel               here command ka kaam click karne par def login ko call karna hai
        def login():
            global txtuser
            global txtpass
            global txt_recode

            if str(txtuser.get())=="" or str(txtpass.get())=="":
                messagebox.showerror("Error","All fields required",parent=root)
            else:
                conn=c.connect("train.db")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from login where username='%s' and pass='%s'"%(str(txtuser.get()),str(txtpass.get())))
                row=my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Username & Password",parent=root)
                else:
                    root.destroy()
                    trainmain()


        loginbtn=Button(frame,command=login,text="Login",font=("times new roman",13,"bold"),bd=3,relief=RIDGE,fg="black",bg="aqua",activeforeground="black",activebackground="aqua")
        loginbtn.place(x=105,y=300,width=120,height=35)

            # registerbutton for new users

        registerbtn=Button(frame,text="New User Register",command=Register,font=("times new roman",11,"bold"),bd=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=5,y=353,width=160)

            #forgot passbtn
        def forgotpass():
            global txtuser
            global txtpass
            global txt_recode
            global txt_newpass

            if str(txtuser.get())=="":
                messagebox.showerror("Error","Please Enter User Name to reset Password",parent=root)
            else:
                conn=c.connect("train.db")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from login where username='%s'"%(str(txtuser.get())))
                row=my_cursor.fetchone()

                if row==None:
                    messagebox.showerror("Error","Please enter valid username",parent=root)
                else:
                    conn.close()
                    root2=Toplevel()
                    root2.title("Forgot Password")
                    root2.geometry("360x480+590+170")

                    l=Label(root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="blue",bg="cyan")
                    l.place(x=0,y=10,relwidth=1)

                    #recovery  code

                    recode=Label(root2,text="Recovery Code",font=("times new roman",20,"bold"),bg="cyan")
                    recode.place(x=88,y=80)

                    txt_recode=ttk.Entry(root2,font=("times new roman",16,"bold"))
                    txt_recode.place(x=50,y=130,width=250)
                    
                    #password

                    newpassword=Label(root2,text="New Password",font=("times new roman",20,"bold"),bg="cyan")
                    newpassword.place(x=88,y=180)

                    txt_newpass=ttk.Entry(root2,font=("times new roman",16,"bold"))
                    txt_newpass.place(x=50,y=220,width=250)
                    
                    def resetpass():
                        global txtuser
                        global txt_newpass
                        global txt_recode

                        

                        if str(txt_recode.get())=="":
                            messagebox.showerror("Error","Please enter Recovery Code",parent=root2)
                        elif not str(txt_recode.get()).isdigit():
                            messagebox.showerror("Error","Please enter Recovery Code in Digits",parent=root2)
                        else:
                            conn=c.connect("train.db")
                            my_cursor=conn.cursor()
                            my_cursor.execute("select * from login where username='%s' and recode='%s'"%(str(txtuser.get()),str(txt_recode.get())))
                            row=my_cursor.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Please enter Correct Recovery Code",parent=root2)
                            else:
                                my_cursor.execute("update login set pass='%s' where username='%s' and recode='%s'"%(str(txt_newpass.get()),str(txtuser.get()),str(txt_recode.get())))
                                conn.commit()
                                conn.close()
                                messagebox.showinfo("Info","Your password has been reset\nYou can login with your new password",parent=root2) 
                                root2.destroy()


                        



                    #btn for reset

                    btn=Button(root2,text="Reset Password",command=resetpass,font=("times new roman",15,"bold"),fg="white",bg="blue")
                    btn.place(x=100,y=290)

        forgotpassbtn=Button(frame,text="Forgot Password",command=forgotpass,font=("times new roman",11,"bold"),bd=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotpassbtn.place(x=7,y=382,width=140)

        #click login func

        

        root.mainloop()
    Login_Window()


addtables()
log()

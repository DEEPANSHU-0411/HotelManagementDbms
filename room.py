from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
from tkinter import ttk
import random
import mysql.connector 
from time import strptime
from datetime import datetime

class Room_booking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x530+232+240")

        #=====================Variables==================
        self.var_Contact=StringVar()
        self.var_CheckinDate=StringVar()
        self.var_CheckoutDate=StringVar()
        self.var_Roomtype=StringVar()
        self.var_Roomavailable=StringVar()
        self.var_Meal=StringVar()
        self.var_NoOfDays=StringVar()
        self.var_Paidtax=StringVar()
        self.var_Actualtotal=StringVar()
        self.var_Total=StringVar()

        #=====================Title======================
        lbl_title=Label(self.root,text="ROOM BOOKING",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #====================Logo========================
        img2 = Image.open("D:/DEEPANSHU/DBMS_MINI_PROJECT/Image/Logo.png")
        img2 = img2.resize((100, 40),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl_image = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lbl_image.place(x=4, y=4, width=100, height=40)

        #====================Label Frame=================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",font=("times new roman",12,"bold"),padx=2) 
        labelframeleft.place(x=5,y=50,width=425,height=470)

        #====================Label and Entry=============
        #Cust contact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        entry_contact=ttk.Entry(labelframeleft,width=20,textvariable=self.var_Contact,font=("times new roman",13,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)

        #fetch data button
        btnFetchData=Button(labelframeleft,command=self.fetch_contact,text="Fetch Data",font=("times new roman",12,"bold"),bg="black",fg="gold",width=9)
        btnFetchData.place(x=320,y=2)


        #Check_in Date
        check_in_date=Label(labelframeleft,text="Check In Date",font=("times new roman",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtCheck_in_date=ttk.Entry(labelframeleft,width=30,textvariable=self.var_CheckinDate,font=("times new roman",13,"bold"))
        txtCheck_in_date.grid(row=1,column=1)

        #Check_out Date
        check_out_date=Label(labelframeleft,text="Check Out Date",font=("times new roman",12,"bold"),padx=2,pady=6)
        check_out_date.grid(row=2,column=0,sticky=W)
        txtCheck_out_date=ttk.Entry(labelframeleft,width=30,textvariable=self.var_CheckoutDate,font=("times new roman",13,"bold"))
        txtCheck_out_date.grid(row=2,column=1)

        #Room Type
        label_RoomType=Label(labelframeleft,text="Room Type",font=("times new roman",12,"bold"),padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select Roomtype from details")
        row=my_cursor.fetchall()

        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_Roomtype,font=("times new roman",12,"bold"),width=32,state="readonly")
        combo_RoomType["value"]=row
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)
        
        #Available Room
        lblRoomAvailable=Label(labelframeleft,text="Available Room",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
        
        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()

        combo_RoomNo=ttk.Combobox(labelframeleft,textvariable=self.var_Roomavailable,font=("times new roman",12,"bold"),width=32,state="readonly")
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)

        #txtRoomAvailable=ttk.Entry(labelframeleft,width=30,textvariable=self.var_Roomavailable,font=("times new roman",13,"bold"))
        #txtRoomAvailable.grid(row=4,column=1)

        #Meal
        lblMeal=Label(labelframeleft,text="Meal",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)
        txtMeal=ttk.Entry(labelframeleft,width=30,textvariable=self.var_Meal,font=("times new roman",13,"bold"))
        txtMeal.grid(row=5,column=1)

        #No of Days
        lblNoOfDays=Label(labelframeleft,text="No Of Days",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,width=30,textvariable=self.var_NoOfDays,font=("times new roman",13,"bold"))
        txtNoOfDays.grid(row=6,column=1)

        #Paid Tax
        lblPaidTax=Label(labelframeleft,text="Paid Tax",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPaidTax.grid(row=7,column=0,sticky=W)
        txtPaidTax=ttk.Entry(labelframeleft,width=30,textvariable=self.var_Paidtax,font=("times new roman",13,"bold"))
        txtPaidTax.grid(row=7,column=1)

        #Sub Total
        lblSubTotal=Label(labelframeleft,text="Sub Total",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblSubTotal.grid(row=8,column=0,sticky=W)
        txtSubTotal=ttk.Entry(labelframeleft,width=30,textvariable=self.var_Actualtotal,font=("times new roman",13,"bold"))
        txtSubTotal.grid(row=8,column=1)

        #Total Cost
        lblTotalCost=Label(labelframeleft,text="Total Cost",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblTotalCost.grid(row=9,column=0,sticky=W)
        txtTotalCost=ttk.Entry(labelframeleft,width=30,textvariable=self.var_Total,font=("times new roman",13,"bold"))
        txtTotalCost.grid(row=9,column=1)

        #=========================Bill Button
        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)


        #=========================Button====================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=390,width=412,height=40)

        btnAdd=Button(btn_frame,text="ADD",command=self.add_data,font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="UPDADTE",command=self.update,font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="DELETE",command=self.delete,font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="RESET",command=self.reset,font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        #=========================Right side image==========
        img3 = Image.open("D:/DEEPANSHU/DBMS_MINI_PROJECT/Image/Bed.jpg")
        img3 = img3.resize((500, 250),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lbl_image = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lbl_image.place(x=790, y=55, width=500, height=250)


        #==========================Table frame==============
        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details & Search System",font=("times new roman",12,"bold"),padx=2) 
        Table_frame.place(x=435,y=270,width=855,height=250)

        lblsearchBy=Label(Table_frame,text="Search By",font=("times new roman",12,"bold"),bg="red",fg="white")
        lblsearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()

        combo_search=ttk.Combobox(Table_frame,textvariable=self.search_var,font=("times new roman",12,"bold"),width=25,state="readonly")
        combo_search["value"]=("Contact","Room No")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)      

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_frame,width=25,font=("times new roman",13,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)  

        btnSearch=Button(Table_frame,text="Search",command=self.search,font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowall=Button(Table_frame,text="Show all",command=self.fetch_data,font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnShowall.grid(row=0,column=4,padx=1)

        #=======================Show data Table================
        details_table=Frame(Table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=845,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,column=("Contact","CheckinDate","CheckoutDate","Roomtype","Roomavailable","Meal","NoOfDays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Contact",text="Contact")
        self.room_table.heading("CheckinDate",text="Check - In")
        self.room_table.heading("CheckoutDate",text="Check - Out")
        self.room_table.heading("Roomtype",text="Room Type")
        self.room_table.heading("Roomavailable",text="Room No")
        self.room_table.heading("Meal",text="Meal")
        self.room_table.heading("NoOfDays",text="No of Days")
         
        self.room_table["show"]="headings"

        self.room_table.column("Contact",width=100)
        self.room_table.column("CheckinDate",width=100)
        self.room_table.column("CheckoutDate",width=100)
        self.room_table.column("Roomtype",width=100)
        self.room_table.column("Roomavailable",width=100)
        self.room_table.column("Meal",width=100)
        self.room_table.column("NoOfDays",width=100)

        self.room_table.pack(fill=BOTH,expand=True)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    #Add data
    def add_data(self):
        if self.var_Contact.get()=="" or self.var_CheckinDate.get()=="":
            messagebox.showerror("Error","Please Fill the required field.",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(self.var_Contact.get(),self.var_CheckinDate.get(),self.var_CheckoutDate.get(),self.var_Roomtype.get(),self.var_Roomavailable.get(),self.var_Meal.get(),self.var_NoOfDays.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong :{str(es)}",parent=self.root)
    
    #Fetch dat
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",passwd="root",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #Get cursor
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_Contact.set(row[0])
        self.var_CheckinDate.set(row[1])
        self.var_CheckoutDate.set(row[2])
        self.var_Roomtype.set(row[3]) 
        self.var_Roomavailable.set(row[4])        
        self.var_Meal.set(row[5])
        self.var_NoOfDays.set(row[6])

    #Update
    def update(self):
        if self.var_Contact.get()=="":
            messagebox.showerror("Error","Please enter Mobile Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",passwd="root",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set Check_in=%s,Check_out=%s,Roomtype=%s,Roomavailable=%s,Meal=%s,NoOfDays=%s where Contact=%s",(self.var_CheckinDate.get(),self.var_CheckoutDate.get(),self.var_Roomtype.get(),self.var_Roomavailable.get(),self.var_Meal.get(),self.var_NoOfDays.get(),self.var_Contact.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated  successfully",parent=self.root)
    
    #Delete
    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do you want to delete the room details",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",passwd="root",database="management")
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_Contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Delete","Room details has been deleted successfully",parent=self.root)

    #Reset
    def reset(self):
        self.var_Contact.set("")
        self.var_CheckinDate.set("")
        self.var_CheckoutDate.set("")
        self.var_Roomtype.set("")
        self.var_Roomavailable.set("")
        self.var_Meal.set("")
        self.var_NoOfDays.set("")
        self.var_Paidtax.set("")
        self.var_Actualtotal.set("")
        self.var_Total.set("")

    #Search
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",passwd="root",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def fetch_contact(self):
        if self.var_Contact.get()=="":
            messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
            my_cursor=conn.cursor()
            query=("select CName from customer where Mobile=%s")
            value=(self.var_Contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error","Invalid Contact Number",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=450,y=55,width=300,height=180)

                lblName=Label(showDataframe,text="Name :",font=("times new roman",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row[0],font=("times new roman",12,"bold"))
                lbl.place(x=90,y=0)

                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_Contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Gender :",font=("times new roman",12,"bold"))
                lblGender.place(x=0,y=30)

                lbl2=Label(showDataframe,text=row[0],font=("times new roman",12,"bold"))
                lbl2.place(x=90,y=30)

                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_Contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblEmail=Label(showDataframe,text="Email :",font=("times new roman",12,"bold"))
                lblEmail.place(x=0,y=60)

                lbl3=Label(showDataframe,text=row[0],font=("times new roman",12,"bold"))
                lbl3.place(x=90,y=60)

                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_Contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblNationality=Label(showDataframe,text="Nationality :",font=("times new roman",12,"bold"))
                lblNationality.place(x=0,y=90)

                lbl4=Label(showDataframe,text=row[0],font=("times new roman",12,"bold"))
                lbl4.place(x=90,y=90)

                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
                my_cursor=conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_Contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblAddress=Label(showDataframe,text="Address :",font=("times new roman",12,"bold"))
                lblAddress.place(x=0,y=120)

                lbl5=Label(showDataframe,text=row[0],font=("times new roman",12,"bold"))
                lbl5.place(x=90,y=120)

    def total(self):
        inDate=self.var_CheckinDate.get()
        outDate=self.var_CheckoutDate.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_NoOfDays.set(abs(outDate-inDate).days+1)

        if(self.var_Meal.get()=="Breakfast" and self.var_Roomtype.get()=="Luxury"):
            q1=float(300)
            q2=float(600)
            q3=float(self.var_NoOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f" % ((q5)*0.1))
            ST="Rs."+str("%.2f" % ((q5)))
            TT="Rs."+str("%.2f" % (q5+((q5)*0.1)))
            self.var_Paidtax.set(Tax)
            self.var_Actualtotal.set(ST)
            self.var_Total.set(TT)

        elif(self.var_Meal.get()=="Lunch" and self.var_Roomtype.get()=="Luxury"):
            q1=float(300)
            q2=float(800)
            q3=float(self.var_NoOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f" % ((q5)*0.1))
            ST="Rs."+str("%.2f" % ((q5)))
            TT="Rs."+str("%.2f" % (q5+((q5)*0.1)))
            self.var_Paidtax.set(Tax)
            self.var_Actualtotal.set(ST)
            self.var_Total.set(TT)

        elif(self.var_Meal.get()=="Dinner" and self.var_Roomtype.get()=="Luxury"):
            q1=float(300)
            q2=float(950)
            q3=float(self.var_NoOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f" % ((q5)*0.1))
            ST="Rs."+str("%.2f" % ((q5)))
            TT="Rs."+str("%.2f" % (q5+((q5)*0.1)))
            self.var_Paidtax.set(Tax)
            self.var_Actualtotal.set(ST)
            self.var_Total.set(TT)

        elif(self.var_Meal.get()=="Breakfast" and self.var_Roomtype.get()=="Single"):
            q1=float(100)
            q2=float(200)
            q3=float(self.var_NoOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f" % ((q5)*0.1))
            ST="Rs."+str("%.2f" % ((q5)))
            TT="Rs."+str("%.2f" % (q5+((q5)*0.1)))
            self.var_Paidtax.set(Tax)
            self.var_Actualtotal.set(ST)
            self.var_Total.set(TT)

        elif(self.var_Meal.get()=="Lunch" and self.var_Roomtype.get()=="Single"):
            q1=float(100)
            q2=float(400)
            q3=float(self.var_NoOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f" % ((q5)*0.1))
            ST="Rs."+str("%.2f" % ((q5)))
            TT="Rs."+str("%.2f" % (q5+((q5)*0.1)))
            self.var_Paidtax.set(Tax)
            self.var_Actualtotal.set(ST)
            self.var_Total.set(TT)

        elif(self.var_Meal.get()=="Dinner" and self.var_Roomtype.get()=="Single"):
            q1=float(100)
            q2=float(500)
            q3=float(self.var_NoOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f" % ((q5)*0.1))
            ST="Rs."+str("%.2f" % ((q5)))
            TT="Rs."+str("%.2f" % (q5+((q5)*0.1)))
            self.var_Paidtax.set(Tax)
            self.var_Actualtotal.set(ST)
            self.var_Total.set(TT)

        elif(self.var_Meal.get()=="Breakfast" and self.var_Roomtype.get()=="Double"):
            q1=float(200)
            q2=float(300)
            q3=float(self.var_NoOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f" % ((q5)*0.1))
            ST="Rs."+str("%.2f" % ((q5)))
            TT="Rs."+str("%.2f" % (q5+((q5)*0.1)))
            self.var_Paidtax.set(Tax)
            self.var_Actualtotal.set(ST)
            self.var_Total.set(TT)

        elif(self.var_Meal.get()=="Lunch" and self.var_Roomtype.get()=="Double"):
            q1=float(200)
            q2=float(600)
            q3=float(self.var_NoOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f" % ((q5)*0.1))
            ST="Rs."+str("%.2f" % ((q5)))
            TT="Rs."+str("%.2f" % (q5+((q5)*0.1)))
            self.var_Paidtax.set(Tax)
            self.var_Actualtotal.set(ST)
            self.var_Total.set(TT)

        elif(self.var_Meal.get()=="Dinner" and self.var_Roomtype.get()=="Double"):
            q1=float(200)
            q2=float(500)
            q3=float(self.var_NoOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f" % ((q5)*0.1))
            ST="Rs."+str("%.2f" % ((q5)))
            TT="Rs."+str("%.2f" % (q5+((q5)*0.1)))
            self.var_Paidtax.set(Tax)
            self.var_Actualtotal.set(ST)
            self.var_Total.set(TT)

        elif(self.var_Meal.get()=="Breakfast" and self.var_Roomtype.get()=="Duplex"):
            q1=float(500)
            q2=float(400)
            q3=float(self.var_NoOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f" % ((q5)*0.1))
            ST="Rs."+str("%.2f" % ((q5)))
            TT="Rs."+str("%.2f" % (q5+((q5)*0.1)))
            self.var_Paidtax.set(Tax)
            self.var_Actualtotal.set(ST)
            self.var_Total.set(TT)

        elif(self.var_Meal.get()=="Lunch" and self.var_Roomtype.get()=="Duplex"):
            q1=float(500)
            q2=float(700)
            q3=float(self.var_NoOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f" % ((q5)*0.1))
            ST="Rs."+str("%.2f" % ((q5)))
            TT="Rs."+str("%.2f" % (q5+((q5)*0.1)))
            self.var_Paidtax.set(Tax)
            self.var_Actualtotal.set(ST)
            self.var_Total.set(TT)

        elif(self.var_Meal.get()=="Dinner" and self.var_Roomtype.get()=="Duplex"):
            q1=float(500)
            q2=float(850)
            q3=float(self.var_NoOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f" % ((q5)*0.1))
            ST="Rs."+str("%.2f" % ((q5)))
            TT="Rs."+str("%.2f" % (q5+((q5)*0.1)))
            self.var_Paidtax.set(Tax)
            self.var_Actualtotal.set(ST)
            self.var_Total.set(TT)

if __name__ == "__main__":
    root=Tk()
    obj=Room_booking(root)
    root.mainloop()


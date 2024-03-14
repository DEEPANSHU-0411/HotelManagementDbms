from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
from tkinter import ttk
import random
import mysql.connector 

class Staff_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x530+232+240")

        #=====================Variables==================
        self.var_StaffID=StringVar()
        x=random.randint(100,999)
        self.var_StaffID.set(str(x))

        self.var_SName=StringVar()
        self.var_Gender=StringVar()
        self.var_Mobile=StringVar()
        self.var_Email=StringVar()
        self.var_Doj=StringVar()
        self.var_Post=StringVar()
        self.var_ID_Proof=StringVar()
        self.var_ID_Number=StringVar()
        self.var_Address=StringVar()

        #=====================Title======================
        lbl_title=Label(self.root,text="ADD STAFF DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #====================Logo========================
        img2 = Image.open("D:/DEEPANSHU/DBMS_MINI_PROJECT/Image/Logo.png")
        img2 = img2.resize((100, 40),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl_image = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lbl_image.place(x=4, y=4, width=100, height=40)

        #====================Label Frame=================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Staff Details",font=("times new roman",12,"bold"),padx=2) 
        labelframeleft.place(x=5,y=50,width=425,height=470)

        #Staff ID
        staffID=Label(labelframeleft,text="Staff ID",font=("times new roman",12,"bold"),padx=2,pady=6)
        staffID.grid(row=0,column=0,sticky=W)
        txtstaffID=ttk.Entry(labelframeleft,width=30,textvariable=self.var_StaffID,font=("times new roman",13,"bold"))
        txtstaffID.grid(row=0,column=1)

        #CustName
        sname=Label(labelframeleft,text="Staff Name",font=("times new roman",12,"bold"),padx=2,pady=6)
        sname.grid(row=1,column=0,sticky=W)
        txtsname=ttk.Entry(labelframeleft,width=30,textvariable=self.var_SName,font=("times new roman",13,"bold"))
        txtsname.grid(row=1,column=1)

        #Gender
        label_gender=Label(labelframeleft,text="Gender",font=("times new roman",12,"bold"),padx=2,pady=6)
        label_gender.grid(row=2,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_Gender,font=("times new roman",12,"bold"),width=32,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=2,column=1)

        #Mobile
        lblMobile=Label(labelframeleft,text="Mobile",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=3,column=0,sticky=W)
        txtMobile=ttk.Entry(labelframeleft,width=30,textvariable=self.var_Mobile,font=("times new roman",13,"bold"))
        txtMobile.grid(row=3,column=1)

        #Email
        lblEmail=Label(labelframeleft,text="Email",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblEmail.grid(row=4,column=0,sticky=W)
        txtEmail=ttk.Entry(labelframeleft,width=30,textvariable=self.var_Email,font=("times new roman",13,"bold"))
        txtEmail.grid(row=4,column=1)

        #Date of Joining
        lbldoj=Label(labelframeleft,text="Date of Joining",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbldoj.grid(row=5,column=0,sticky=W)
        txtdoj=ttk.Entry(labelframeleft,width=30,textvariable=self.var_Doj,font=("times new roman",13,"bold"))
        txtdoj.grid(row=5,column=1)

        #Post
        label_post=Label(labelframeleft,text="Post",font=("times new roman",12,"bold"),padx=2,pady=6)
        label_post.grid(row=6,column=0,sticky=W)
        combo_post=ttk.Combobox(labelframeleft,textvariable=self.var_Post,font=("times new roman",12,"bold"),width=32,state="readonly")
        combo_post["value"]=("Select","Manager","Receptionist","Maintainance","Security","Housekeeping","Assistant")
        combo_post.current(0)
        combo_post.grid(row=6,column=1)

        #Id proof type combobox
        lblIDProof=Label(labelframeleft,text="ID Proof Type",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblIDProof.grid(row=7,column=0,sticky=W)
        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_ID_Proof,font=("times new roman",12,"bold"),width=32,state="readonly")
        combo_id["value"]=("Adhar Card","Driving Licence","Passport","PAN Card")
        combo_id.current(0)
        combo_id.grid(row=7,column=1)


        #Id number
        lblIDNumber=Label(labelframeleft,text="Id Number",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblIDNumber.grid(row=8,column=0,sticky=W)
        txtIDNumber=ttk.Entry(labelframeleft,width=30,textvariable=self.var_ID_Number,font=("times new roman",13,"bold"))
        txtIDNumber.grid(row=8,column=1)

        #Address
        lblAddress=Label(labelframeleft,text="Address",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAddress.grid(row=9,column=0,sticky=W)
        txtAddress=ttk.Entry(labelframeleft,width=30,textvariable=self.var_Address,font=("times new roman",13,"bold"))
        txtAddress.grid(row=9,column=1)

        #=========================Button====================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=370,width=412,height=40)

        btnAdd=Button(btn_frame,text="ADD",command=self.add_data,font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="UPDADTE",command=self.update,font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="DELETE",command=self.delete,font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="RESET",command=self.reset,font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        #==========================Table frame==============
        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details & Search System",font=("times new roman",12,"bold"),padx=2) 
        Table_frame.place(x=435,y=50,width=855,height=470)

        lblsearchBy=Label(Table_frame,text="Search By",font=("times new roman",12,"bold"),bg="red",fg="white")
        lblsearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()

        combo_search=ttk.Combobox(Table_frame,textvariable=self.search_var,font=("times new roman",12,"bold"),width=25,state="readonly")
        combo_search["value"]=("StaffID","Mobile")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        
        txtSearch=ttk.Entry(Table_frame,width=25,textvariable=self.txt_search,font=("times new roman",13,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)  

        btnSearch=Button(Table_frame,text="Search",command=self.search,font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowall=Button(Table_frame,text="Show all",command=self.fetch_data,font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnShowall.grid(row=0,column=4,padx=1) 

        #=======================Show data Table================
        details_table=Frame(Table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=845,height=360)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Staff_details_table=ttk.Treeview(details_table,column=("StaffID","SName","Gender","Mobile","Email","Doj","Post","Idproof","Idnumber","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Staff_details_table.xview)
        scroll_y.config(command=self.Staff_details_table.yview)

        self.Staff_details_table.heading("StaffID",text="Staff ID")
        self.Staff_details_table.heading("SName",text="Staff Name")
        self.Staff_details_table.heading("Gender",text="Gender")
        self.Staff_details_table.heading("Mobile",text="Mobbile")
        self.Staff_details_table.heading("Email",text="Email Id")
        self.Staff_details_table.heading("Doj",text="Date of Joining")
        self.Staff_details_table.heading("Post",text="Post")
        self.Staff_details_table.heading("Idproof",text="Id Proof")
        self.Staff_details_table.heading("Idnumber",text="Id Number")
        self.Staff_details_table.heading("Address",text="Address")

        self.Staff_details_table["show"]="headings"
        self.Staff_details_table.column("StaffID",width=100)
        self.Staff_details_table.column("SName",width=100)
        self.Staff_details_table.column("Gender",width=100)
        self.Staff_details_table.column("Mobile",width=100)
        self.Staff_details_table.column("Email",width=100)
        self.Staff_details_table.column("Doj",width=100)
        self.Staff_details_table.column("Post",width=100)
        self.Staff_details_table.column("Idproof",width=100)
        self.Staff_details_table.column("Idnumber",width=100)
        self.Staff_details_table.column("Address",width=100)

        self.Staff_details_table.pack(fill=BOTH,expand=True)
        self.Staff_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_Mobile.get()=="" or self.var_SName.get()=="":
            messagebox.showerror("Error","Please Fill the required field.",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into staff values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_StaffID.get(),self.var_SName.get(),self.var_Gender.get(),self.var_Mobile.get(),self.var_Email.get(),self.var_Doj.get(),self.var_Post.get(),self.var_ID_Proof.get(),self.var_ID_Number.get(),self.var_Address.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Staff has been  added successfully.",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong :{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",passwd="root",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from staff")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Staff_details_table.delete(*self.Staff_details_table.get_children())
            for i in rows:
                self.Staff_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.Staff_details_table.focus()
        content=self.Staff_details_table.item(cursor_row)
        row=content["values"]

        self.var_StaffID.set(row[0])
        self.var_SName.set(row[1])
        self.var_Gender.set(row[2]) 
        self.var_Mobile.set(row[3])        
        self.var_Email.set(row[4])
        self.var_Doj.set(row[5])
        self.var_Post.set(row[6])
        self.var_ID_Proof.set(row[7])
        self.var_ID_Number.set(row[8])
        self.var_Address.set(row[9])

    def update(self):
        if self.var_Mobile.get()=="":
            messagebox.showerror("Error","Please enter Mobile Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",passwd="root",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update staff set SName=%s,Gender=%s,Mobile=%s,Email=%s,Doj=%s,Post=%s,IDProof=%s,IDNumber=%s,Address=%s where StaffID=%s",(self.var_SName.get(),self.var_Gender.get(),self.var_Mobile.get(),self.var_Email.get(),self.var_Doj.get(),self.var_Post.get(),self.var_ID_Proof.get(),self.var_ID_Number.get(),self.var_Address.get(),self.var_StaffID.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Staff details has been updated successfully",parent=self.root)

    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do you want to delete this staff",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",passwd="root",database="management")
            my_cursor=conn.cursor()
            query="delete from staff where StaffID=%s"
            value=(self.var_StaffID.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        x=random.randint(100,999)
        self.var_StaffID.set(str(x))
        self.var_SName.set("")
        #self.var_Gender.set("") 
        self.var_Mobile.set("")        
        self.var_Email.set("")
        self.var_Doj.set("")
        #self.var_Post.set("")
        #self.var_ID_Proof.set("")
        self.var_ID_Number.set("")
        self.var_Address.set("")

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",passwd="root",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from staff where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Staff_details_table.delete(*self.Staff_details_table.get_children())
            for i in rows:
                self.Staff_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root=Tk()
    obj=Staff_Win(root)
    root.mainloop()
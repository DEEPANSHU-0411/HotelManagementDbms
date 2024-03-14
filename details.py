from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
from tkinter import ttk
import random
import mysql.connector 
from time import strptime
from datetime import datetime

class DetailsRoom:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x530+232+240")

        #=====================Title======================
        lbl_title=Label(self.root,text="Room Adding Department",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #====================Logo========================
        img2 = Image.open("D:/DEEPANSHU/DBMS_MINI_PROJECT/Image/Logo.png")
        img2 = img2.resize((100, 40),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl_image = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lbl_image.place(x=4, y=4, width=100, height=40)

        #====================Label Frame=================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("times new roman",12,"bold"),padx=2) 
        labelframeleft.place(x=5,y=50,width=425,height=470)

        #Floor
        lbl_floor=Label(labelframeleft,text="Floor",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)
        self.var_floor=StringVar()
        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=30,font=("times new roman",13,"bold"))
        entry_floor.grid(row=0,column=1,sticky=W)

        #Room No
        lbl_RoomNo=Label(labelframeleft,text="Room No",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)
        self.var_roomno=StringVar()
        entry_RoomNo=ttk.Entry(labelframeleft,textvariable=self.var_roomno,width=30,font=("times new roman",13,"bold"))
        entry_RoomNo.grid(row=1,column=1,sticky=W)

        #Room Type
        lbl_RoomType=Label(labelframeleft,text="Room Type",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W)
        self.var_roomtype=StringVar()
        entry_RoomType=ttk.Entry(labelframeleft,textvariable=self.var_roomtype,width=30,font=("times new roman",13,"bold"))
        entry_RoomType.grid(row=2,column=1,sticky=W)

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

        #==========================Table frame==============
        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("times new roman",12,"bold"),padx=2) 
        Table_frame.place(x=435,y=50,width=855,height=470)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(Table_frame,column=("RoomNo","Floor","Roomtype"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("RoomNo",text="Room No")
        self.room_table.heading("Floor",text="Floor")
        self.room_table.heading("Roomtype",text="Room Type")
        
         
        self.room_table["show"]="headings"

        self.room_table.column("RoomNo",width=100)
        self.room_table.column("Floor",width=100)
        self.room_table.column("Roomtype",width=100)

        self.room_table.pack(fill=BOTH,expand=True)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    #Add data
    def add_data(self):
        if self.var_floor.get()=="" or self.var_roomtype.get()=="":
            messagebox.showerror("Error","Please Fill the required field.",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(self.var_roomno.get(),self.var_floor.get(),self.var_roomtype.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New Room Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong :{str(es)}",parent=self.root)
    
    #Fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",passwd="root",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
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

        self.var_roomno.set(row[0])
        self.var_floor.set(row[1])
        self.var_roomtype.set(row[2]) 
        
    #Update
    def update(self):
        if self.var_roomno.get()=="":
            messagebox.showerror("Error","Please enter Room Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",passwd="root",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set Floor=%s,Roomtype=%s where RoomNo=%s",(self.var_floor.get(),self.var_roomtype.get(),self.var_roomtype.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","New Room details has been updated  successfully",parent=self.root)

    #Delete
    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do you want to delete the room details",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",passwd="root",database="management")
            my_cursor=conn.cursor()
            query="delete from details where RoomNo=%s"
            value=(self.var_roomno.get(),)
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
        self.var_roomno.set("")
        self.var_floor.set("")
        self.var_roomtype.set("")
        

if __name__ == "__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()
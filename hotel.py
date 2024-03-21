from tkinter import *
from PIL import Image
from PIL import ImageTk              #pip install pillow
from customer import Cust_Win  
from room import Room_booking
from details import DetailsRoom
from staff import Staff_Win

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        #=================1st image======================
        img1 = Image.open("D:/DEEPANSHU/DBMS_MINI_PROJECT/Image/Hotel1.jpg")
        img1 = img1.resize((1550, 140),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl_image = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lbl_image.place(x=0, y=0, width=1550, height=140)

        #====================Logo========================
        img2 = Image.open("D:/DEEPANSHU/DBMS_MINI_PROJECT/Image/Logo.png")
        img2 = img2.resize((330, 140),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl_image = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lbl_image.place(x=0, y=0, width=140, height=140)

        #=====================Title======================
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        #=====================Main Frame=================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        #=====================Menu=======================
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        #=====================Button Frame=================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=230,height=198)

        cust_btn=Button(btn_frame,text="CUSTOMER DETAILS",command=self.cust_details,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,width=22,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="ROOM BOOKING",command=self.room_allocate,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,width=22,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="ROOM DETAILS",command=self.DetailsRoom,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,width=22,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        staff_btn=Button(btn_frame,text="STAFF DETAILS",command=self.staff_details,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,width=22,cursor="hand1")
        staff_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,width=22,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)

        #====================RIGHT SIDE IMAGE==============
        img3 = Image.open("D:/DEEPANSHU/DBMS_MINI_PROJECT/Image/Reception.jpg")
        img3 = img3.resize((1310, 590),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lbl_image = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lbl_image.place(x=225, y=0, width=1310, height=590)

        #====================DOWN IMAGE====================
        img4 = Image.open("D:/DEEPANSHU/DBMS_MINI_PROJECT/Image/Pool.png")
        img4 = img4.resize((230, 190),Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        lbl_image = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lbl_image.place(x=0, y=225, width=230, height=190)

        img5 = Image.open("D:/DEEPANSHU/DBMS_MINI_PROJECT/Image/Menu.png")
        img5 = img5.resize((230, 190),Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        lbl_image = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lbl_image.place(x=0, y=400, width=230, height=190)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window) 

    def room_allocate(self):
        self.new_window=Toplevel(self.root)
        self.app=Room_booking(self.new_window)

    def DetailsRoom(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)

    def staff_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Staff_Win(self.new_window) 

    def logout(self):
        self.root.destroy()

if __name__ == "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()

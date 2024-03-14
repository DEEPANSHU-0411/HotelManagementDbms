from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector
from customer import Cust_Win  
from room import Room_booking
from details import DetailsRoom
from staff import Staff_Win

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        #=================Background image======================
        self.bg=ImageTk.PhotoImage(file="D:/DEEPANSHU/DBMS_MINI_PROJECT/Image/Login1.jpg")
        lbl_image = Label(self.root, image=self.bg)
        lbl_image.place(x=0, y=0, relwidth=1, relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        #=================1st image======================
        img1 = Image.open("D:/DEEPANSHU/DBMS_MINI_PROJECT/Image/LoginIcon.jpg")
        img1 = img1.resize((100, 100),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl_image = Label(image=self.photoimg1, bg="black",borderwidth=0)
        lbl_image.place(x=730, y=175, width=100, height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg= "white",bg="black")
        get_str.place(x=95, y=100)

        #=================Label====================
        username=lbl=Label(frame, text="Username", font=("times new roman",15,"bold"),fg= "white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame, text="Password", font=("times new roman",15,"bold"),fg= "white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #=====================Icon Images====================
        img2 = Image.open("D:/DEEPANSHU/DBMS_MINI_PROJECT/Image/LoginIcon.jpg")
        img2 = img2.resize((25, 25),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl_image = Label(image=self.photoimg2, bg="black",borderwidth=0)
        lbl_image.place(x=650, y=323, width=25, height=25)

        img3 = Image.open("D:/DEEPANSHU/DBMS_MINI_PROJECT/Image/Lock.png")
        img3 = img3.resize((25, 25),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lbl_image = Label(image=self.photoimg3, bg="black",borderwidth=0)
        lbl_image.place(x=650, y=393, width=25, height=25)

        #===================Login button=============
        loginbtn=Button(frame,text="LOGIN",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=30)

        #====================Register====================
        registerbtn=Button(frame,text="NEW USER REGISTER",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="red")
        registerbtn.place(x=90,y=350,width=150,height=40)

        #==================Forget Password====================
        forgetpassbtn=Button(frame,text="FORGOT PASSWORD",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="red")
        forgetpassbtn.place(x=90,y=380,width=150,height=40)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","Please Fill All Fields")
        elif self.txtuser.get()=="kapss@gmail.com" and self.txtpass.get()=="kapil123":
            messagebox.showinfo("Success","Welcome to Hotel Management System")
            self.new_window=Toplevel(self.root)
            self.app=HotelManagementSystem(self.new_window)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where Email=%s and Password=%s",(self.txtuser.get(),self.txtpass.get()))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username Or Password")
            else:
                open_main=messagebox.askyesno("Yes / No","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.new_window)
                    self.app=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    #======================Reset=========================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select Security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Enter the Answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please Enter New Password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
            my_cursor=conn.cursor()
            query=("select * from register where Email=%s and SecurityQ=%s and SecurityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter Correct Answer",parent=self.root2)
            else:
                qury=("update register set Password=%s where Email=%s")
                values=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(qury,values)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Password has been reset, please login with New Password",parent=self.root2)
                self.root2.destroy()



    #======================Forget Password=========================
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the Email address to reset password.")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
            my_cursor=conn.cursor()
            query=("select * from register where Email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",12,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Pet Name","Your Mother's Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)        

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        #=================Variables==================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        #=================Background image======================
        self.bg=ImageTk.PhotoImage(file="D:/DEEPANSHU/DBMS_MINI_PROJECT/Image/Register4.jpg")
        bg_image = Label(self.root, image=self.bg)
        bg_image.place(x=0, y=0, relwidth=1, relheight=1)

        #=================Left image============================
        #self.bg1=ImageTk.PhotoImage(file="D:/DEEPANSHU/DBMS_MINI_PROJECT/Image/Register1.jpg")
        #left_image = Label(self.root, image=self.bg1)
        #left_image.place(x=100, y=100, relwidth=1, relheight=1)

        #=================Frame for Register Details===================
        frame=Frame(self.root,bg="white",)
        frame.place(x=270,y=150,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        #=================Labels and entry=======================
        #=================Row1==================
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        lname.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)

        #==================Row2===================
        contact=Label(frame,text="Contact",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)

        #===================Row3==================
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",12,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Pet Name","Your Mother's Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)        

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.txt_security.place(x=370,y=270,width=250)

        #================Row4====================
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        #===============Check button=============
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=390)

        #==================Buttons===============
        img=Image.open("D:/DEEPANSHU/DBMS_MINI_PROJECT/Image/RegisterNow.png")
        img=img.resize((200,50),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimg,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=50,y=450,width=200)

        img1=Image.open("D:/DEEPANSHU/DBMS_MINI_PROJECT/Image/LoginNow.png")
        img1=img1.resize((200,50),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimg1,command=self.return_login,borderwidth=0,cursor="hand2")
        b1.place(x=370,y=450,width=200)

    #======================Registering data=================
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm Password must be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists, please try another email",parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(self.var_fname.get(),self.var_lname.get(),self.var_contact.get(),self.var_email.get(),self.var_securityQ.get(),self.var_securityA.get(),self.var_pass.get()))
                conn.commit()
                #self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Registration successfull",parent=self.root)
    def return_login(self):
        self.root.destroy()



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
    main()


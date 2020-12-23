from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk # pip install pillow
from tkinter import messagebox
import sqlite3

class register:
    def __init__(self,root):
        self.root=root
        self.root.configure(bg="dark blue")
        self.root.title("Registeration Window")
        self.root.geometry("1350x700+0+0")
        self.root.maxsize(width=1350,height=700)

        #===LEFT Image===
        self.left=ImageTk.PhotoImage(file="./signin.jpeg")
        left=Label(self.root,image=self.left).place(x=100,y=300)

         #--------Sign In----------------------------
        btn_login=Button(self.root,text="SIGN IN",command=self.signin_window,font=("times new roman",20),bd=3,bg="#B00857",fg="white",cursor="hand2").place(x=170,y=460)

        
        
        
        #===Register Frame===
        frame1=Frame(self.root)
        frame1.place(x=470,y=100,width=700,height=590)

        title=Label(frame1,text="REGISTER",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)

        #--------------------------------Row1
        f_name=Label(frame1,text="FIRST NAME",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="light gray")
        self.txt_fname.place(x=50,y=130,width=250)

        l_name=Label(frame1,text="LAST NAME",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="light gray")
        self.txt_lname.place(x=370,y=130,width=250)

        #---------------------------------Row2
        contact=Label(frame1,text="CONTACT NO",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="light gray")
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame1,text="EMAIL",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="light gray")
        self.txt_email.place(x=370,y=200,width=250)


        #---------------------------------Row3
        question=Label(frame1,text="SECURITY QUESTION",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=50,y=240)
        
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",15),state='readonly',justify=CENTER) 
        self.cmb_quest['values']=("","YOUR FAVOURITE PET","YOUR BIRTH PLACE","YOUR FRIEND NAME")
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)
        

        answer=Label(frame1,text="ANSWER",font=("times new roman",13,"bold"),bg="white",fg="green").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="light gray")
        self.txt_answer.place(x=370,y=270,width=250)

          #---------------------------------Row4
        password=Label(frame1,text="PASSWORD",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="light gray")
        self.txt_password.place(x=50,y=340,width=250)

        cpassword=Label(frame1,text="CONFIRM PASSWORD",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="light gray")
        self.txt_cpassword.place(x=370,y=340,width=250)

        #-------Terms--------
        self.chk_var=IntVar()
        chk=Checkbutton(frame1,text="AGREE TO THE TERMS AND CONDITION",onvalue=1,offvalue=0,variable=self.chk_var,bg="white",font=("times new roman",17)).place(x=50,y=380)

        #-------Button-------
        self.btn_img=ImageTk.PhotoImage(file="./regbtn.jpeg")
        btn=Button(frame1,image=self.btn_img,command=self.register_data,bd=0,cursor="hand2").place(x=50,y=420)

    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("ERROR","All Fields Are Required")
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("ERROR","Password and Confirm Password Must Be Same")
        elif self.chk_var==0:
            messagebox.showerror("ERROR","I Accept Terms and Conditions")
        else:
            try:
                con=sqlite3.connect("studentdb.sqlite")
                cur=con.cursor()
                cur.execute('''SELECT * FROM REGISTER WHERE EMAIL=?''',(self.txt_email.get(),))
                row=cur.fetchone()
                print(row)
                if row!=None:
                    messagebox.showerror("ERROR","User already exists!")
                    self.clear()
                else:
                    cur.execute('''INSERT INTO register (FNAME,LNAME,CONTACT,EMAIL,QUESTION,ANSWER,PASSWORD) VALUES (?,?,?,?,?,?,?)''',
                    ( self.txt_fname.get(), 
                    self.txt_lname.get(), 
                    self.txt_contact.get(),
                    self.txt_email.get(),
                    self.cmb_quest.get(),
                    self.txt_answer.get(),
                    self.txt_password.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Registered Sucessfully")
                    self.clear()

            except Exception as es:
                messagebox.showerror("ERROR",f"Error due to: {str(es)}")


    def clear(self):
        self.txt_fname.delete(0,END) 
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.cmb_quest.current(0)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)


        #===linknig====
    def signin_window(self):
        self.root.destroy()
        import Login






root=Tk()
ob=register(root)
root.mainloop()





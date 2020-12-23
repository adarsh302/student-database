from tkinter import*
import sqlite3
from tkinter import messagebox
class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login page")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="dark blue")

        #===Background Colour=======
        #==left bg colour==========
        left_lbl=Label(self.root,bg="light blue",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)
        #====right bg colour======
        right_lbl=Label(self.root,bg="light blue",bd=0)
        right_lbl.place(x=600,y=0,relheight=1,width=1)
        #====Frame=============
        login_Frame=Frame(self.root,bg="white")
        login_Frame.place(x=250,y=100,width=800,height=500)

        title=Label(login_Frame,text="LOGIN",font=("times new roman",30,"bold"),bg="white",fg="dark blue").place(x=20,y=50)
            
        email=Label(login_Frame,text="EMAIL ADDRESS",font=("times new roman",15,"bold"),bg="white",fg="dark blue").place(x=20,y=150)
        self.txt_email=Entry(login_Frame,font=("times new roman",13),bg="light grey",fg="black")
        self.txt_email.place(x=250,y=150,width=350,height=35)

        
        pass_=Label(login_Frame,text="PASSWORD",font=("times new roman",15,"bold"),bg="white",fg="dark blue").place(x=20,y=250)
        self.txt_pass_=Entry(login_Frame,font=("times new roman",13),bg="light grey",fg="black")
        self.txt_pass_.place(x=250,y=250,width=280,height=35)

        #==Button=========
        #===Signup button==
        btn_reg=Button(login_Frame,text="Signup",command=self.register_window,font=("times new roman",15,"bold"),bg="#B00857",fg="white",cursor="hand2")
        btn_reg.place(x=260,y=350,width=180,height=40)
        #===Login button===
        btn_reg=Button(login_Frame,text="Login",command=self.login,font=("times new roman",18,"bold"),bg="#B00857",fg="white",cursor="hand2")
        btn_reg.place(x=260,y=420,width=180,height=40)

    def login(self):
        if self.txt_email.get()=="" or self.txt_pass_.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=sqlite3.connect('studentdb.sqlite')
                cur=con.cursor()
                cur.execute("select * from REGISTER where email=? and password=?",(self.txt_email.get(),self.txt_pass_.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Email Address & Password",parent=self.root)
                    
                else:
                    messagebox.showinfo("Success","Welcome",parent=self.root)
                    self.root.destroy()
                    import studentdbms
                    con.close()        
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to:{str(es)}",parent=self.root)
        
   
 


#===linking===
    def register_window(self):
         self.root.destroy()
         import register 




        




root=Tk()
obj=login_window(root)
root.mainloop()   




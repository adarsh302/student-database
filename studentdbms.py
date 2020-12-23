from tkinter import * 
from tkinter import ttk
import sqlite3
from tkinter import messagebox
class student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.configure(bg="dark blue")
        self.root.geometry("1350x700+0+0")

        #----------------Initial Heading-------------------------------

        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=('times of roman',40,"bold"),bg="white",fg="dark blue")
        title.pack(side=TOP,fill=X)

        #----------------All variables----------------------------------
        self.USN_var=StringVar()
        self.name_var=StringVar()
        self.branch_var=StringVar()
        self.Sem_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()

        self.searchby_var=StringVar()
        self.search_txt_var=StringVar()

        #-----------Entry Frame-----------
        manage_frame = Frame(self.root,bd=4,relief=RIDGE,bg="light blue")
        manage_frame.place(x=20,y=100,width=500,height=550)
        m_title=Label(manage_frame,text="Student's Details",font=('times of roman',25,"bold"),bg="light blue",fg="black")
        m_title.grid(row=0,columnspan=2,pady=10,sticky="w")

        lb1=Label(manage_frame,text="USN",font=('times of roman',20,"bold"),bg="light blue",fg="black")
        lb1.grid(row=1,column=0,pady=5,padx=20,sticky="w")
        txt1=Entry(manage_frame,textvariable=self.USN_var,bd=3,relief=GROOVE,font=('times of roman',10,"bold"))
        txt1.grid(row=1,column=1,pady=5,padx=20,sticky="w")

        lb2=Label(manage_frame,text="Name",font=('times of roman',20,"bold"),bg="light blue",fg="black")
        lb2.grid(row=2,column=0,pady=5,padx=20,sticky="w")
        txt2=Entry(manage_frame,textvariable= self.name_var,bd=3,relief=GROOVE,font=('times of roman',10,"bold"))
        txt2.grid(row=2,column=1,pady=5,padx=20,sticky="w")

        lb3=Label(manage_frame,text="Branch",font=('times of roman',20,"bold"),bg="light blue",fg="black")
        lb3.grid(row=3,column=0,pady=5,padx=20,sticky="w")
        txt3=Entry(manage_frame,textvariable=self.branch_var,bd=3,relief=GROOVE,font=('times of roman',10,"bold"))
        txt3.grid(row=3,column=1,pady=5,padx=20,sticky="w")

        lb4=Label(manage_frame,text="Sem",font=('times of roman',20,"bold"),bg="light blue",fg="black")
        lb4.grid(row=4,column=0,pady=5,padx=20,sticky="w")
        txt4=Entry(manage_frame,textvariable=self.Sem_var,bd=3,relief=GROOVE,font=('times of roman',10,"bold"))
        txt4.grid(row=4,column=1,pady=5,padx=20,sticky="w")

        lb5=Label(manage_frame,text="Gender",font=('times of roman',20,"bold"),bg="light blue",fg="black")
        lb5.grid(row=5,column=0,pady=5,padx=20,sticky="w")
        combo_gender=ttk.Combobox(manage_frame,textvariable=self.gender_var,font=('times of roman',10,"bold"),state="readonly")
        combo_gender['values']=("Male","Female","Others")
        combo_gender.grid(row=5,column=1,pady=5,padx=20,sticky="w")

        lb6=Label(manage_frame,text="Contact",font=('times of roman',20,"bold"),bg="light blue",fg="black")
        lb6.grid(row=6,column=0,pady=5,padx=20,sticky="w")
        txt6=Entry(manage_frame,textvariable=self.contact_var,bd=3,relief=GROOVE,font=('times of roman',10,"bold"))
        txt6.grid(row=6,column=1,pady=5,padx=20,sticky="w")

        lb7=Label(manage_frame,text="DOB",font=('times of roman',20,"bold"),bg="light blue",fg="black")
        lb7.grid(row=7,column=0,pady=5,padx=20,sticky="w")
        txt7=Entry(manage_frame,textvariable=self.dob_var,bd=3,relief=GROOVE,font=('times of roman',10,"bold"))
        txt7.grid(row=7,column=1,pady=5,padx=20,sticky="w")

        lb8=Label(manage_frame,text="Address",font=('times of roman',20,"bold"),bg="light blue",fg="black")
        lb8.grid(row=8,column=0,pady=5,padx=20,sticky="w")
        self.txt8=Text(manage_frame,bd=3,relief=GROOVE,font=('times of roman',15,"bold"),width=27,height=2)
        self.txt8.grid(row=8,column=1,pady=5,padx=20,sticky="w")

        #-------------------------------Manage Frame Buttons---------------------------
        btn_frame=Frame(manage_frame,bd=2,relief=RIDGE,bg="dark blue")
        btn_frame.place(x=45,y=490,width=402,height=50)

        addbtn=Button(btn_frame,text='Add',width=10,fg="black",command=self.add_Students,cursor="hand2").grid(row=0,column=1,padx=10,pady=10)
        delbtn=Button(btn_frame,text='Delete',width=10,fg="black",command=self.delete_data,cursor="hand2").grid(row=0,column=2,padx=10,pady=10)
        updbtn=Button(btn_frame,text='Update',width=10,fg="black",command=self.update_Students,cursor="hand2").grid(row=0,column=3,padx=10,pady=10)
        clrbtn=Button(btn_frame,text='Clear',width=10,fg="black",command=self.clear,cursor="hand2").grid(row=0,column=4,padx=10,pady=10)



        #----------------------------Detail Frame-------------------
        detail_frame = Frame(self.root,bd=4,relief=RIDGE,bg="light blue")
        detail_frame.place(x=540,y=100,width=800,height=550)

        d_lb1=Label(detail_frame,text="Search ",font=('times of roman',15,"bold"),bg="light blue",fg="black").grid(row=0,column=1,padx=10,pady=10)
        combo_search=ttk.Combobox(detail_frame,textvariable=self.searchby_var, width=10,font=('times of roman',15,"bold"),state="readonly")
        combo_search['values']=("USN","Name","Contact","Branch","Sem")
        combo_search.grid(row=0,column=2,padx=10,pady=10)
        d_txt1=Entry(detail_frame,textvariable=self.search_txt_var,width=12,bd=3,relief=GROOVE,font=('times of roman',15,"bold")).grid(row=0,column=3,padx=10,pady=10)

        #-----------------------------Detail Frame Buttons---------------

        search_btn=Button(detail_frame,text='Serach',command=self.search,width=15,height=1,cursor="hand2").grid(row=0,column=5,padx=10,pady=10)
        showall_btn=Button(detail_frame,text='Show All',command=self.fetch_data,width=15,height=1,cursor="hand2").grid(row=0,column=6,padx=10,pady=10)

        #------------------------------Table Frame------------
        table_frame = Frame(detail_frame,bd=4,relief=RIDGE,bg="light blue")
        table_frame.place(x=10,y=70,width=760,height=470)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(table_frame,columns=("USN","Name","Branch","Sem","Gender","Contact","DOB","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.configure(command=self.Student_table.xview)
        scroll_y.configure(command=self.Student_table.yview)
        self.Student_table.heading("USN",text="USN")
        self.Student_table.heading("Name",text="Name")
        self.Student_table.heading("Branch",text="Branch")
        self.Student_table.heading("Sem",text="Sem")
        self.Student_table.heading("Gender",text="Gender")
        self.Student_table.heading("Contact",text="Contact")
        self.Student_table.heading("DOB",text="DOB")
        self.Student_table.heading("Address",text="Address")
        self.Student_table['show']='headings'
        self.Student_table.column("USN",width=100)
        self.Student_table.column("Name",width=100)
        self.Student_table.column("Branch",width=100)
        self.Student_table.column("Sem",width=100)
        self.Student_table.column("Gender",width=100)
        self.Student_table.column("Contact",width=100)
        self.Student_table.column("DOB",width=100)
        self.Student_table.column("Address",width=100)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        

    #conn = sqlite3.connect('studentdb.sqlite')
    #cur = conn.cursor()
    #cur.execute('DROP TABLE IF EXISTS Students')
    #cur.execute('''CREATE TABLE Students (USN TEXT, Name TEXT,Branch TEXT,Sem INTEGER,Gender TEXT,Contact TEXT,DOB TEXT,Address Text)''')
    #conn.commit()
    #conn.close()
    
    def add_Students(self):
        if (self.USN_var.get()=="") or (self.name_var.get()=="") or (self.branch_var.get()=="") or (self.Sem_var.get()=="") or (self.gender_var.get()=="") or (self.contact_var.get()=="") or (self.dob_var.get()=="") or (self.txt8.get('1.0',END) == "\n"):
            messagebox.showerror("Error","All fields are required!!!")
        else:
            conn = sqlite3.connect('studentdb.sqlite')
            cur = conn.cursor()
            cur.execute('''INSERT INTO Students values(?,?,?,?,?,?,?,?)''',(self.USN_var.get(),
                                                                        self.name_var.get(),
                                                                        self.branch_var.get(),
                                                                        self.Sem_var.get(),
                                                                        self.gender_var.get(),
                                                                        self.contact_var.get(),
                                                                        self.dob_var.get(),
                                                                        self.txt8.get('1.0',END)))
            conn.commit()
            self.fetch_data()
            self.clear()
            conn.close()
            messagebox.showinfo("Sucess","Record added successfully")


    def fetch_data(self):
        conn = sqlite3.connect('studentdb.sqlite')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Students''')
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
                conn.commit()
        conn.close()

    def clear(self):
        self.USN_var.set("")
        self.name_var.set("")
        self.branch_var.set("")
        self.Sem_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt8.delete('1.0',END)
        

    def update_Students(self):
        if (self.USN_var.get()=="") or (self.name_var.get()=="") or (self.branch_var.get()=="") or (self.Sem_var.get()=="") or (self.gender_var.get()=="") or (self.contact_var.get()=="") or (self.dob_var.get()=="") or (self.txt8.get('1.0',END).startswith("\n")):
            messagebox.showerror("Error","All fields are required!!!")
        else:
            conn = sqlite3.connect('studentdb.sqlite')
            cur = conn.cursor()
            cur.execute('''UPDATE Students SET USN=?,Name=?,Branch=?,Sem=?,Gender=?,Contact=?,DOJ=?,Address=? WHERE USN=?''',(self.USN_var.get(),
                                                                        self.name_var.get(),
                                                                        self.branch_var.get(),
                                                                        self.Sem_var.get(),
                                                                        self.gender_var.get(),
                                                                        self.contact_var.get(),
                                                                        self.dob_var.get(),
                                                                        self.txt8.get('1.0',END),
                                                                        self.USN_var.get()))
            conn.commit()
            self.fetch_data()
            self.clear()
            conn.close()
            messagebox.showinfo("Upated","Record Updated Successfully")

    def get_cursor(self,ev):                              
        curosor_row=self.Student_table.focus()            #curosor_row keyword ,get_cursor is pre defined function            
        contents=self.Student_table.item(curosor_row)   
        row=contents['values']
        #print(row)
        self.USN_var.set(row[0])
        self.name_var.set(row[1])
        self.branch_var.set(row[2])
        self.Sem_var.set(row[3])
        self.gender_var.set(row[4])
        self.contact_var.set(row[5])
        self.dob_var.set(row[6])
        self.txt8.delete('1.0',END)
        self.txt8.insert(END,row[7])

    def delete_data(self):
        conn = sqlite3.connect('studentdb.sqlite')
        cur = conn.cursor()
        cur.execute('''DELETE FROM Students WHERE USN=?''', (self.USN_var.get(),))
        conn.commit()
        self.fetch_data()
        self.clear()
        conn.close()
        messagebox.showinfo("Deleted","Record Deleted Successfully")

    def search(self):
        conn = sqlite3.connect('studentdb.sqlite')
        cur = conn.cursor()
        cur.execute("SELECT * FROM Students WHERE "+str(self.searchby_var.get())+" LIKE '%"+str(self.search_txt_var.get())+"%'" )
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
                conn.commit()
        conn.close()


root=Tk()
ob=student(root)
root.mainloop()
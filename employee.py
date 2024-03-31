
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3

class Employee:
    def __init__(self,root):
        self.root = root
        self.root.title("Welcome Our RiseStore Shop")
        self.root.geometry("1170x705+355+95")
        self.root.iconbitmap(r"image/shop_icon.ico")
        self.root.config(bg="#ffffff")
        self.font_family = "arial"
        self.root.focus_force()

        #================ variable =====================
        self.var_searchBy = StringVar()
        self.var_searchTxt = StringVar()

        self.var_emp_id = StringVar()
        self.var_emp_gender = StringVar()
        self.var_emp_contact = StringVar()
        self.var_emp_name = StringVar()
        self.var_emp_name = StringVar()
        self.var_emp_dob = StringVar()
        self.var_emp_doj = StringVar()
        self.var_emp_email = StringVar()
        self.var_emp_pass = StringVar()
        self.var_emp_utype = StringVar()
        self.var_emp_salary = StringVar()

        self.emp_icon = PhotoImage(file="image/emp.png")
        title = Label(self.root,text="Employee Details", image=self.emp_icon,compound=LEFT, font=(self.font_family,20,"bold"),bg="#a7f0fc", fg="#214175",padx=15).place(x=0,y=0,relwidth=1,height=40)
        
        #============== Employee Form  ==================
        emp_id_lbl = Label(self.root,text="Emp Id",font=(self.font_family,12),bg="#ffffff").place(x=40,y=50)
        emp_name_lbl = Label(self.root,text="Name",font=(self.font_family,12),bg="#ffffff").place(x=40,y=100)
        emp_gender_lbl = Label(self.root,text="Gender",font=(self.font_family,12),bg="#ffffff").place(x=40,y=150)
        emp_email_lbl = Label(self.root,text="Email",font=(self.font_family,12),bg="#ffffff").place(x=40,y=200)
        emp_pass_lbl = Label(self.root,text="Password",font=(self.font_family,12),bg="#ffffff").place(x=40,y=250)
        emp_dob_lbl = Label(self.root,text="D.O.B",font=(self.font_family,12),bg="#ffffff").place(x=40,y=300)

        emp_id_txt = Entry(self.root,textvariable=self.var_emp_id,font=(self.font_family,12),bg="#f2fcfb").place(x=150,y=50,width=250,height=30)
        emp_name_txt = Entry(self.root,textvariable=self.var_emp_name,font=(self.font_family,12),bg="#f2fcfb").place(x=150,y=100,width=250,height=30)
        emp_gender_txt = ttk.Combobox(self.root,textvariable=self.var_emp_gender,font=(self.font_family,12),values=("Select","Male","Female"),state='readonly',justify=CENTER)
        emp_gender_txt.place(x=150,y=150,width=250,height=30)
        emp_gender_txt.current(0)
        emp_email_txt = Entry(self.root,textvariable=self.var_emp_email,font=(self.font_family,12),bg="#f2fcfb").place(x=150,y=200,width=250,height=30)
        emp_pass_txt = Entry(self.root,textvariable=self.var_emp_pass,font=(self.font_family,12),bg="#f2fcfb").place(x=150,y=250,width=250,height=30)
        emp_dob_txt = Entry(self.root,textvariable=self.var_emp_dob,font=(self.font_family,12),bg="#f2fcfb").place(x=150,y=300,width=250,height=30)

        emp_contact_lbl = Label(self.root,text="Contact",font=(self.font_family,12),bg="#ffffff").place(x=500,y=50)
        emp_utype_lbl = Label(self.root,text="User Type",font=(self.font_family,12),bg="#ffffff").place(x=500,y=100)
        emp_doj_lbl = Label(self.root,text="D.O.J",font=(self.font_family,12),bg="#ffffff").place(x=500,y=150)
        emp_salary_lbl = Label(self.root,text="Salary",font=(self.font_family,12),bg="#ffffff").place(x=500,y=200)
        emp_add_lbl = Label(self.root,text="Address",font=(self.font_family,12),bg="#ffffff").place(x=500,y=250)

        emp_contact_txt = Entry(self.root,textvariable=self.var_emp_contact,font=(self.font_family,12),bg="#f2fcfb").place(x=600,y=50,width=250,height=30)
        emp_utype_txt = ttk.Combobox(self.root,textvariable=self.var_emp_utype,font=(self.font_family,12),values=("Admin","Employee"),state='readonly',justify=CENTER)
        emp_utype_txt.place(x=600,y=100,width=250,height=30)
        emp_utype_txt.current(0)
        emp_doj_txt = Entry(self.root,textvariable=self.var_emp_doj,font=(self.font_family,12),bg="#f2fcfb").place(x=600,y=150,width=250,height=30)
        emp_salary_txt = Entry(self.root,textvariable=self.var_emp_salary,font=(self.font_family,12),bg="#f2fcfb").place(x=600,y=200,width=250,height=30)
        self.emp_add_txt = Text(self.root,font=(self.font_family,12),bg="#f2fcfb")
        self.emp_add_txt.place(x=600,y=250,width=250,height=80)

        # ================= Button =======================
        save_btn = Button(self.root,text="Save", font=(self.font_family,15,"bold"),cursor="hand2",borderwidth=0,bg="#0000ff",fg="#ffffff",padx=25,pady=10, command=self.add)
        save_btn.place(x=910,y=50,width=220,height=40)
        update_btn = Button(self.root,text="Update", font=(self.font_family,15,"bold"),cursor="hand2",borderwidth=0,bg="#1cbf0a",fg="#ffffff",padx=25,pady=10, command=self.update)
        update_btn.place(x=910,y=130,width=220,height=40)
        delete_btn = Button(self.root,text="Delete", font=(self.font_family,15,"bold"),cursor="hand2",borderwidth=0,bg="#ff0000",fg="#ffffff",padx=25,pady=10,command=self.delete)
        delete_btn.place(x=910,y=210,width=220,height=40)
        clear_btn = Button(self.root,text="Clear", font=(self.font_family,15,"bold"),cursor="hand2",borderwidth=0,bg="#555555",fg="#ffffff",padx=25,pady=10,command=self.clear)
        clear_btn.place(x=910,y=285,width=220,height=40)

        Label(self.root,bg="#8f8e8d").place(x=0,y=350,relwidth=1,height=2)

        #==============search Bar ====================

        search_txt = Entry(self.root,textvariable=self.var_searchTxt,font=(self.font_family,12),bg="#f2fcfb").place(x=40,y=370,width=360,height=30)
        search_btn = Button(self.root,text="Search",command=self.search,font=(self.font_family,15,"bold"),bg="#1cbf0a",borderwidth=0,fg="#ffffff").place(x=400,y=370,width=150,height=30)

        search_box = ttk.Combobox(self.root,textvariable=self.var_searchBy,font=(self.font_family,12),values=("Select","Name","Contact","Email"),state='readonly',justify=CENTER)
        search_box.place(x=600,y=370,width=250,height=30)
        search_box.current(0)
        
        # ============= employee details =====================

        emp_frame = Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=40,y=430,width=1090,height=250)

        scrolly = Scrollbar(emp_frame,orient=VERTICAL)
        scrollx = Scrollbar(emp_frame,orient=HORIZONTAL)

        self.emp_table = ttk.Treeview(emp_frame,columns=("eid","name","gender","contact","dob","doj","email","pass","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.emp_table.xview)
        scrolly.config(command=self.emp_table.yview)
        self.emp_table.heading("eid",text="Id")
        self.emp_table.heading("name",text="Name")
        self.emp_table.heading("gender",text="Gender")
        self.emp_table.heading("contact",text="Contact")
        self.emp_table.heading("dob",text="D.O.B")
        self.emp_table.heading("doj",text="D.O.J")
        self.emp_table.heading("email",text="Email")
        self.emp_table.heading("pass",text="Password")
        self.emp_table.heading("utype",text="U Type")
        self.emp_table.heading("address",text="Address")
        self.emp_table.heading("salary",text="Salary")
        self.emp_table.pack(fill=BOTH,expand=1)

        self.emp_table["show"] = "headings"

        self.emp_table.column("eid",width=90)
        self.emp_table.column("name",width=100)
        self.emp_table.column("gender",width=100)
        self.emp_table.column("contact",width=100)
        self.emp_table.column("dob",width=100)
        self.emp_table.column("doj",width=100)
        self.emp_table.column("email",width=100)
        self.emp_table.column("pass",width=100)
        self.emp_table.column("utype",width=100)
        self.emp_table.column("address",width=100)
        self.emp_table.column("salary",width=100)
        self.emp_table.pack(fill=BOTH,expand=1)
        self.emp_table.bind("<ButtonRelease-1>",self.get_data)

        self.show()

#======================= Back End Code ========================

    #===============================add data start ======================
    def add(self):
        con =  sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee Id Must Be Required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid = ?",(self.var_emp_id.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Employee Id Already Assigned, Try Diifrent",parent=self.root)
                else:
                    cur.execute("Insert into employee (eid,name,gender,contact,dob,doj,email,pass,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                            self.var_emp_id.get(),
                            self.var_emp_name.get(),
                            self.var_emp_gender.get(),
                            self.var_emp_contact.get(),
                            self.var_emp_dob.get(),
                            self.var_emp_doj.get(),
                            self.var_emp_email.get(),
                            self.var_emp_pass.get(),
                            self.var_emp_utype.get(),
                            self.emp_add_txt.get('1.0',END),
                            self.var_emp_salary.get()

                            

                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employe Data Add Successfully",parent=self.root)
                    self.show()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)     

    #=======================show data start ==============================
    def show(self):
        con =  sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            cur.execute("Select * from employee")
            rows = cur.fetchall()
            self.emp_table.delete(*self.emp_table.get_children())
            for row in rows:
                self.emp_table.insert('',END,values=row)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)     

    # ===============get data in text field ==========================

    def get_data(self,ev):
        f = self.emp_table.focus()
        content = (self.emp_table.item(f))
        row  = content['values']
        self.var_emp_id.set(row[0])
        self.var_emp_name.set(row[1])
        self.var_emp_gender.set(row[2])
        self.var_emp_contact.set(row[3])
        self.var_emp_dob.set(row[4])
        self.var_emp_doj.set(row[5])
        self.var_emp_email.set(row[6])
        self.var_emp_pass.set(row[7])
        self.var_emp_utype.set(row[8])
        self.emp_add_txt.delete('1.0',END)
        self.emp_add_txt.insert(END,row[9]),
        self.var_emp_salary.set(row[10])


    #======================update data start =======================
    def update(self):
        con =  sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee Id Must Be Required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid = ?",(self.var_emp_id.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee Id",parent=self.root)
                else:
                    cur.execute("Update employee set name =?,gender=?,contact=?,dob=?,doj=?,email=?,pass=?,utype=?,address=?,salary=? where eid = ?",(
            
                            self.var_emp_name.get(),
                            self.var_emp_gender.get(),
                            self.var_emp_contact.get(),
                            self.var_emp_dob.get(),
                            self.var_emp_doj.get(),
                            self.var_emp_email.get(),
                            self.var_emp_pass.get(),
                            self.var_emp_utype.get(),
                            self.emp_add_txt.get('1.0',END),
                            self.var_emp_salary.get(),
                            self.var_emp_id.get()

                            

                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employe Data Updated Successfully",parent=self.root)
                    self.show()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)     

    # ===========================delete data start ==========================
    def delete(self):
        con =  sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee Id Must Be Required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid = ?",(self.var_emp_id.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee Id",parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm","Do you really want to delete ?",parent=self.root)
                    if op==True:
                        cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Employee data delete successfully")
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)   

    #==================== clear data start =====================
    def clear(self):
        self.var_emp_id.set("")
        self.var_emp_name.set("")
        self.var_emp_gender.set("Select")
        self.var_emp_contact.set("")
        self.var_emp_dob.set("")
        self.var_emp_doj.set("")
        self.var_emp_email.set("")
        self.var_emp_pass.set("")
        self.var_emp_utype.set("Admin")
        self.emp_add_txt.delete('1.0',END)
        self.var_emp_salary.set("")
        self.var_searchTxt.set("")
        self.var_searchBy.set("Select")

        self.show()


    # ============================== search data ========================
    def search(self):
        con =  sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_searchBy.get()== "Select":
                messagebox.showerror("Error","Select Serach By Option",parent=self.root)
            elif self.var_searchTxt.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                cur.execute("Select * from employee where "+self.var_searchBy.get()+" LIKE '%"+self.var_searchTxt.get()+"%'")
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.emp_table.delete(*self.emp_table.get_children())
                    for row in rows:
                        self.emp_table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found !!!",parent=self.root)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)     

    

if __name__ =="__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()
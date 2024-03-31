
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3

class Supplier:
    def __init__(self,root):
        self.root = root
        self.root.title("Welcome Our RiseStore Shop")
        self.root.geometry("1170x705+355+95")
        self.root.iconbitmap(r"image/shop_icon.ico")
        self.root.config(bg="#ffffff")
        self.font_family = "arial"
        self.root.focus_force()

        #================ variable =====================
   
        self.var_searchTxt = StringVar()

        self.var_sup_id = StringVar()
        self.var_sup_name = StringVar()
        self.var_sup_contact = StringVar()
        

        self.emp_icon = PhotoImage(file="image/emp.png")
        title = Label(self.root,text="Supplier Details", image=self.emp_icon,compound=LEFT, font=(self.font_family,20,"bold"),bg="#a7f0fc", fg="#214175",padx=15).place(x=0,y=0,relwidth=1,height=40)
        
        #============== Employee Form  ==================
        sup_id_lbl = Label(self.root,text="Sup Id",font=(self.font_family,12),bg="#ffffff").place(x=40,y=50)
        sup_name_lbl = Label(self.root,text="Name",font=(self.font_family,12),bg="#ffffff").place(x=330,y=50)
        sup_contact_lbl = Label(self.root,text="Contact",font=(self.font_family,12),bg="#ffffff").place(x=615,y=50)
        sup_add_lbl = Label(self.root,text="Description",font=(self.font_family,12),bg="#ffffff").place(x=40,y=125)

        sup_id_txt = Entry(self.root,textvariable=self.var_sup_id,font=(self.font_family,12),bg="#f2fcfb").place(x=43,y=73,width=250,height=30)
        emp_name_txt = Entry(self.root,textvariable=self.var_sup_name,font=(self.font_family,12),bg="#f2fcfb").place(x=330,y=73,width=250,height=30)
        sup_contact_txt = Entry(self.root,textvariable=self.var_sup_contact,font=(self.font_family,12),bg="#f2fcfb").place(x=615,y=73,width=250,height=30)
        self.sup_desc_txt = Text(self.root,font=(self.font_family,12),bg="#f2fcfb")
        self.sup_desc_txt.place(x=43,y=160,width=820,height=140)
        
    

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


        # ============= employee details =====================

        emp_frame = Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=40,y=430,width=1090,height=250)

        scrolly = Scrollbar(emp_frame,orient=VERTICAL)
        scrollx = Scrollbar(emp_frame,orient=HORIZONTAL)

        self.supplier_table = ttk.Treeview(emp_frame,columns=("sid","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplier_table.xview)
        scrolly.config(command=self.supplier_table.yview)
        self.supplier_table.heading("sid",text="Id")
        self.supplier_table.heading("name",text="Name")
        self.supplier_table.heading("contact",text="Contact")
        self.supplier_table.heading("desc",text="Description")
        self.supplier_table.pack(fill=BOTH,expand=1)

        self.supplier_table["show"] = "headings"

        self.supplier_table.column("sid",width=90)
        self.supplier_table.column("name",width=100)
        self.supplier_table.column("contact",width=100)
        self.supplier_table.column("desc",width=100)
        self.supplier_table.pack(fill=BOTH,expand=1)
        self.supplier_table.bind("<ButtonRelease-1>",self.get_data)

        self.show()

#======================= Back End Code ========================

    #===============================add data start ======================
    def add(self):
        con =  sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_id.get() == "":
                messagebox.showerror("Error", "Supplier Id Must Be Required",parent=self.root)
            else:
                cur.execute("Select * from supplier where sid = ?",(self.var_sup_id.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Supplier Id Already Assigned, Try Diifrent",parent=self.root)
                else:
                    cur.execute("Insert into supplier (sid,name,contact,desc) values(?,?,?,?)",(
                            self.var_sup_id.get(),
                            self.var_sup_name.get(),
                            self.var_sup_contact.get(),
                            self.sup_desc_txt.get('1.0',END),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Data Add Successfully",parent=self.root)
                    self.show()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)     

    #=======================show data start ==============================
    def show(self):
        con =  sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            cur.execute("Select * from supplier")
            rows = cur.fetchall()
            self.supplier_table.delete(*self.supplier_table.get_children())
            for row in rows:
                self.supplier_table.insert('',END,values=row)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)     

    # ===============get data in text field ==========================

    def get_data(self,ev):
        f = self.supplier_table.focus()
        content = (self.supplier_table.item(f))
        row  = content['values']
        self.var_sup_id.set(row[0])
        self.var_sup_name.set(row[1])
        self.var_sup_contact.set(row[2])
        self.sup_desc_txt.delete('1.0',END)
        self.sup_desc_txt.insert(END,row[3]),


    #======================update data start =======================
    def update(self):
        con =  sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_id.get() == "":
                messagebox.showerror("Error", "Supplier Id Must Be Required",parent=self.root)
            else:
                cur.execute("Select * from supplier where sid = ?",(self.var_sup_id.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Supplier Id",parent=self.root)
                else:
                    cur.execute("Update supplier set name =?,contact=?,desc=? where sid = ?",(
            
                            self.var_sup_name.get(),
                            self.var_sup_contact.get(),
                            self.sup_desc_txt.get('1.0',END),
                            self.var_sup_id.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Data Updated Successfully",parent=self.root)
                    self.show()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)     

    # ===========================delete data start ==========================
    def delete(self):
        con =  sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_id.get() == "":
                messagebox.showerror("Error", "Supplier Id Must Be Required",parent=self.root)
            else:
                cur.execute("Select * from supplier where sid = ?",(self.var_sup_id.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Supplier Id",parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm","Do you really want to delete ?",parent=self.root)
                    if op==True:
                        cur.execute("delete from supplier where sid=?",(self.var_sup_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Supplier data delete successfully")
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)   

    #==================== clear data start =====================
    #   
    def clear(self):
        self.var_sup_id.set("")
        self.var_sup_name.set("")
        self.var_sup_contact.set("")
        self.sup_desc_txt.delete('1.0',END)
        self.var_searchTxt.set("")
        self.var_searchBy.set("Select")

        self.show()


    # ============================== search data ========================
    def search(self):
        con =  sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_searchTxt.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where sid=?",(self.var_searchTxt.get(),))
                row = cur.fetchone()
                if row!=None:
                    self.supplier_table.delete(*self.supplier_table.get_children())
                    self.supplier_table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found !!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)     
       

if __name__ =="__main__":
    root = Tk()
    obj = Supplier(root)
    root.mainloop()
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3

class Product:
    def __init__(self,root):
        self.root = root
        self.root.title("Welcome Our RiseStore Shop")
        self.root.geometry("1170x705+355+95")
        self.root.iconbitmap(r"image/shop_icon.ico")
        self.root.config(bg="#ffffff")
        self.font_family = "arial"
        self.root.focus_force()

        #===============variable =============
        self.var_searchBy = StringVar()
        self.var_searchTxt = StringVar()

        self.var_pro_pid = StringVar()
        self.var_pro_cat = StringVar()
        self.var_pro_sup = StringVar()
        self.cat_list = []
        self.sup_list = []
        self.fetch_cat_sup()
        self.var_pro_status = StringVar()
        self.var_pro_name = StringVar()
        self.var_pro_price = StringVar()
        self.var_pro_qty = StringVar()

        #==================================title         
        title = Label(self.root,text="Product Details", font=(self.font_family,20,"bold"),bg="#a7f0fc", fg="#214175",padx=15).place(x=0,y=0,relwidth=1,height=40)

        #============== Employee Form  ==================
        pro_cat_lbl = Label(self.root,text="Category",font=(self.font_family,12),bg="#ffffff").place(x=70,y=60)
        pro_sup_lbl = Label(self.root,text="Supplier",font=(self.font_family,12),bg="#ffffff").place(x=425,y=60)
        pro_status_lbl = Label(self.root,text="Status",font=(self.font_family,12),bg="#ffffff").place(x=780,y=60)
        pro_name_lbl = Label(self.root,text="Name",font=(self.font_family,12),bg="#ffffff").place(x=70,y=150)
        pro_price_lbl = Label(self.root,text="Price",font=(self.font_family,12),bg="#ffffff").place(x=425,y=150)
        emp_qty_lbl = Label(self.root,text="Quantity",font=(self.font_family,12),bg="#ffffff").place(x=780,y=150)

        pro_cat_txt = ttk.Combobox(self.root,textvariable=self.var_pro_cat,font=(self.font_family,12),values=self.cat_list,state='readonly',justify=CENTER)
        pro_cat_txt.place(x=73,y=90,width=300,height=30)
        pro_cat_txt.current(0)
        pro_sup_txt = ttk.Combobox(self.root,textvariable=self.var_pro_sup,font=(self.font_family,12),values=self.sup_list,state='readonly',justify=CENTER)
        pro_sup_txt.place(x=428,y=90,width=300,height=30)
        pro_sup_txt.current(0)
        pro_status_txt = ttk.Combobox(self.root,textvariable=self.var_pro_status,font=(self.font_family,12),values=("Active","Inactive"),state='readonly',justify=CENTER)
        pro_status_txt.place(x=783,y=90,width=300,height=30)
        pro_status_txt.current(0)
        pro_name_txt = Entry(self.root,textvariable=self.var_pro_name,font=(self.font_family,12),bg="#f2fcfb").place(x=73,y=180,width=300,height=30)
        pro_price_txt = Entry(self.root,textvariable=self.var_pro_price,font=(self.font_family,12),bg="#f2fcfb").place(x=428,y=180,width=300,height=30)
        pro_qty_txt = Entry(self.root,textvariable=self.var_pro_qty,font=(self.font_family,12),bg="#f2fcfb").place(x=783,y=180,width=300,height=30)
        

        # ================= Button =======================
        save_btn = Button(self.root,text="Save", font=(self.font_family,15,"bold"),cursor="hand2",borderwidth=0,bg="#0000ff",fg="#ffffff",padx=25,pady=10,command=self.add)
        save_btn.place(x=73,y=240,width=220,height=40)
        update_btn = Button(self.root,text="Update", font=(self.font_family,15,"bold"),cursor="hand2",borderwidth=0,bg="#1cbf0a",fg="#ffffff",padx=25,pady=10,command=self.update)
        update_btn.place(x=340,y=240,width=220,height=40)
        delete_btn = Button(self.root,text="Delete", font=(self.font_family,15,"bold"),cursor="hand2",borderwidth=0,bg="#ff0000",fg="#ffffff",padx=25,pady=10,command=self.delete)
        delete_btn.place(x=600,y=240,width=220,height=40)
        clear_btn = Button(self.root,text="Clear", font=(self.font_family,15,"bold"),cursor="hand2",borderwidth=0,bg="#555555",fg="#ffffff",padx=25,pady=10,command=self.clear)
        clear_btn.place(x=860,y=240,width=220,height=40)

        Label(self.root,bg="#8f8e8d").place(x=0,y=350,relwidth=1,height=2)

        #==============search Bar ====================

        search_txt = Entry(self.root,textvariable=self.var_searchTxt,font=(self.font_family,12),bg="#f2fcfb").place(x=73,y=370,width=360,height=30)
        search_btn = Button(self.root,text="Search",command=self.search,font=(self.font_family,15,"bold"),bg="#1cbf0a",borderwidth=0,fg="#ffffff").place(x=400,y=370,width=150,height=30)

        search_box = ttk.Combobox(self.root,textvariable=self.var_searchBy,font=(self.font_family,12),values=("Select","Category","Supplier","Name"),state='readonly',justify=CENTER)
        search_box.place(x=640,y=370,width=250,height=30)
        search_box.current(0)

        pro_frame = Frame(self.root,bd=3,relief=RIDGE)
        pro_frame.place(x=73,y=430,width=1000,height=250)

        scrolly = Scrollbar(pro_frame,orient=VERTICAL)
        scrollx = Scrollbar(pro_frame,orient=HORIZONTAL)

        self.pro_table = ttk.Treeview(pro_frame,columns=("pid","Category","Supplier","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.pro_table.xview)
        scrolly.config(command=self.pro_table.yview)
        self.pro_table.heading("pid",text="Pro Id")
        self.pro_table.heading("Category",text="Category")
        self.pro_table.heading("Supplier",text="Supplier")
        self.pro_table.heading("name",text="Name")
        self.pro_table.heading("price",text="Price")
        self.pro_table.heading("qty",text="Quantity")
        self.pro_table.heading("status",text="Status")
        self.pro_table.pack(fill=BOTH,expand=1)

        self.pro_table["show"] = "headings"

        self.pro_table.column("pid",width=90)
        self.pro_table.column("Category",width=100)
        self.pro_table.column("Supplier",width=100)
        self.pro_table.column("name",width=100)
        self.pro_table.column("price",width=100)
        self.pro_table.column("qty",width=100)
        self.pro_table.column("status",width=100)
        self.pro_table.pack(fill=BOTH,expand=1)
        self.pro_table.bind("<ButtonRelease-1>",self.get_data)

        self.show()


#======================= Back End Code ========================
    def fetch_cat_sup(self):
        con =  sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            cur.execute("Select name from category")
            self.cat_list.append("Empty")
            cat = cur.fetchall()
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
            for i in cat:
                self.cat_list.append(i[0])

            cur.execute("Select name from supplier")
            sup = cur.fetchall()
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
            for i in sup:
                self.sup_list.append(i[0])

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)     


    #===============================add data start ======================
    def add(self):
        con =  sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_pro_cat.get() == "Select"  or self.var_pro_sup.get() == "Select" or self.var_pro_name.get() == "":
                messagebox.showerror("Error", "All fields are Required",parent=self.root)
            else:
                cur.execute("Select * from product where name = ? ",(self.var_pro_name.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Product Already Assigned, Try Diifrent",parent=self.root)
                else:
                    cur.execute("Insert into product (Category,Supplier,name,price,qty,status) values(?,?,?,?,?,?)",(
                            self.var_pro_cat.get(),
                            self.var_pro_sup.get(),
                            self.var_pro_name.get(),
                            self.var_pro_price.get(),
                            self.var_pro_qty.get(),
                            self.var_pro_status.get(),

                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product Data Add Successfully",parent=self.root)
                    self.show()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)     

    def show(self):
        con =  sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            cur.execute("Select * from product")
            rows = cur.fetchall()
            self.pro_table.delete(*self.pro_table.get_children())
            for row in rows:
                self.pro_table.insert('',END,values=row)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
    

    def get_data(self,ev):
        f = self.pro_table.focus()
        content = (self.pro_table.item(f))
        row  = content['values']
        self.var_pro_pid.set(row[0])
        self.var_pro_cat.set(row[1])
        self.var_pro_sup.set(row[2])
        self.var_pro_name.set(row[3])
        self.var_pro_price.set(row[4])
        self.var_pro_qty.set(row[5])
        self.var_pro_status.set(row[6])
                
    def update(self):
        con =  sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_pro_pid.get() == "":
                messagebox.showerror("Error", "Please select product from list",parent=self.root)
            else:
                cur.execute("Select * from product where pid = ?",(self.var_pro_pid.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product",parent=self.root)
                else:
                    cur.execute("Update product set Category =?,Supplier=?,name=?,price=?,qty=?,status=? where pid = ?",(
            
                            self.var_pro_cat.get(),
                            self.var_pro_sup.get(),
                            self.var_pro_name.get(),
                            self.var_pro_price.get(),
                            self.var_pro_qty.get(),
                            self.var_pro_status.get(),
                            self.var_pro_pid.get(),

                            

                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product Data Updated Successfully",parent=self.root)
                    self.show()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)  

    # ===========================delete data start ==========================
    def delete(self):
        con =  sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_pro_pid.get() == "":
                messagebox.showerror("Error", "Select Product from the list",parent=self.root)
            else:
                cur.execute("Select * from product where pid = ?",(self.var_pro_pid.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product",parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm","Do you really want to delete ?",parent=self.root)
                    if op==True:
                        cur.execute("delete from product where pid=?",(self.var_pro_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Product data delete successfully")
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)     
    #==================== clear data start =====================
    def clear(self):
        self.var_pro_cat.set("Select")
        self.var_pro_sup.set("Select")
        self.var_pro_name.set("")
        self.var_pro_price.set("")
        self.var_pro_qty.set("")
        self.var_pro_status.set("Active")
        self.var_searchTxt.set("")
        self.var_searchBy.set("Select")
        
        self.show()

    def search(self):
        con =  sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_searchBy.get()== "Select":
                messagebox.showerror("Error","Select Serach By Option",parent=self.root)
            elif self.var_searchTxt.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                cur.execute("Select * from product where "+self.var_searchBy.get()+" LIKE '%"+self.var_searchTxt.get()+"%'")
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.pro_table.delete(*self.pro_table.get_children())
                    for row in rows:
                        self.pro_table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found !!!",parent=self.root)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)     


if __name__ =="__main__":
    root = Tk()
    obj = Product(root)
    root.mainloop()
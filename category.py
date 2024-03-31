from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3

class Category:
    def __init__(self,root):
        self.root = root
        self.root.title("Welcome Our RiseStore Shop")
        self.root.geometry("700x305+455+250")
        self.root.iconbitmap(r"image/shop_icon.ico")
        self.root.config(bg="#ffffff")
        self.font_family = "arial"
        self.root.focus_force()

        #===============variable ================

        self.var_cat_id = StringVar()
        self.var_cat_name = StringVar()
            
        #====================title ===================
        title = Label(self.root,text="Category Details", font=(self.font_family,20,"bold"),bg="#a7f0fc", fg="#214175",padx=15).place(x=0,y=0,relwidth=1,height=40)

        # ====================category  form ============================
        cat_name_lbl = Label(self.root,text="Category Name",font=(self.font_family,12),bg="#ffffff").place(x=40,y=60)
        sup_id_txt = Entry(self.root,textvariable=self.var_cat_name,font=(self.font_family,12),bg="#f2fcfb").place(x=43,y=90,width=250,height=30)

        save_btn = Button(self.root,text="Save", command=self.add, font=(self.font_family,15,"bold"),cursor="hand2",borderwidth=0,bg="#0000ff",fg="#ffffff",padx=25,pady=10)
        save_btn.place(x=43,y=150,width=250,height=40)

        delete_btn = Button(self.root,text="Delete", command=self.delete, font=(self.font_family,15,"bold"),cursor="hand2",borderwidth=0,bg="#ff0000",fg="#ffffff",padx=25,pady=10)
        delete_btn.place(x=43,y=230,width=250,height=40)

        #=================table frame
        emp_frame = Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=320,y=90,width=350,height=200)

        scrolly = Scrollbar(emp_frame,orient=VERTICAL)
        scrollx = Scrollbar(emp_frame,orient=HORIZONTAL)

        self.category_table = ttk.Treeview(emp_frame,columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.category_table.xview)
        scrolly.config(command=self.category_table.yview)
        self.category_table.heading("cid",text="Category Id")
        self.category_table.heading("name",text="Category Name")
        self.category_table.pack(fill=BOTH,expand=1)

        self.category_table["show"] = "headings"

        self.category_table.column("cid",width=90)
        self.category_table.column("name",width=100)
        self.category_table.bind("<ButtonRelease-1>",self.get_data)

        self.show()

    def add(self):
        con =  sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_cat_name.get() == "":
                messagebox.showerror("Error", "Category Name Must Be Required",parent=self.root)
            else:
                cur.execute("Select * from category where name = ?",(self.var_cat_name.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Supplier Id Already Assigned, Try Diifrent",parent=self.root)
                else:
                    cur.execute("Insert into category (name) values(?)",(self.var_cat_name.get(),))
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
            cur.execute("Select * from category")
            rows = cur.fetchall()
            self.category_table.delete(*self.category_table.get_children())
            for row in rows:
                self.category_table.insert('',END,values=row)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

    def get_data(self,ev):
        f = self.category_table.focus()
        content = (self.category_table.item(f))
        row  = content['values']
        self.var_cat_id.set(row[0])
        self.var_cat_name.set(row[1])

    #=========================delete data start
    def delete(self):
        con =  sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_cat_name.get() == "":
                messagebox.showerror("Error", "Category Name Must Be Required",parent=self.root)
            else:
                cur.execute("Select * from category where name = ?",(self.var_cat_name.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Category Name",parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm","Do you really want to delete ?",parent=self.root)
                    if op==True:
                        cur.execute("delete from category where name=?",(self.var_cat_name.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Category data delete successfully")
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)   
    
    
    #==================== clear data start =====================
    def clear(self):
        self.var_cat_id.set("")
        self.var_cat_name.set("")

        self.show()




if __name__ =="__main__":
    root = Tk()
    obj = Category(root)
    root.mainloop()
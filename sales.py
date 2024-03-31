from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3
import os

class Sales:
    def __init__(self,root):
        self.root = root
        self.root.title("Welcome Our RiseStore Shop")
        self.root.geometry("900x585+455+200")
        self.root.iconbitmap(r"image/shop_icon.ico")
        self.root.config(bg="#ffffff")
        self.font_family = "arial"
        self.root.focus_force()

        #===============variable ================

        self.var_invoice = StringVar()
            
        #====================title ===================
        title = Label(self.root,text="Customer Bills", font=(self.font_family,20,"bold"),bg="#a7f0fc", fg="#214175",padx=15).place(x=0,y=0,relwidth=1,height=40)

        cat_name_lbl = Label(self.root,text="Invoice No.",font=(self.font_family,12),bg="#ffffff").place(x=40,y=60)
        sup_id_txt = Entry(self.root,font=(self.font_family,12),bg="#f2fcfb").place(x=43,y=90,width=250,height=30)

        save_btn = Button(self.root,text="Save", font=(self.font_family,15,"bold"),cursor="hand2",borderwidth=0,bg="#0000ff",fg="#ffffff",padx=25,pady=10)
        save_btn.place(x=320,y=90,width=250,height=30)
        clear_btn = Button(self.root,text="Clear", font=(self.font_family,15,"bold"),cursor="hand2",borderwidth=0,bg="#555555",fg="#ffffff",padx=25,pady=10)
        clear_btn.place(x=600,y=90,width=250,height=30)

        #============Bill list ===============
        sales_frame = Frame(self.root,bd=3,relief=RIDGE)
        sales_frame.place(x=40,y=150,width=300,height=380)

        scrolly = Scrollbar(sales_frame,orient=VERTICAL)
        self.sale_list = Listbox(sales_frame,font=(self.font_family,20,"bold"),bg="#ffffff",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.sale_list.yview)
        self.sale_list.pack(fill=BOTH,expand=1)

        #==============Bill Area =====================
        bill_frame = Frame(self.root,bd=3,relief=RIDGE)
        bill_frame.place(x=350,y=150,width=500,height=380)

        self.bill_label = Label(bill_frame,text="Customer Bill Area", font=(self.font_family,20,"bold"),fg="#a7f0fc", bg="#214175",padx=15).pack(side=TOP,fill=X)

        
        scrolly1 = Scrollbar(sales_frame,orient=VERTICAL)
        self.bill_area = Text(bill_frame,font=(self.font_family,10,"bold"),bg="#f2fcfb",yscrollcommand=scrolly1.set)
        scrolly1.pack(side=RIGHT,fill=Y)
        scrolly1.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)


#======================================
    def show(self):
        self.sale_list.delete(0,END)

if __name__ =="__main__":
    root = Tk()
    obj = Sales(root)
    root.mainloop()
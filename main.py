from tkinter import*
from PIL import Image,ImageTk
from employee import Employee
from supplier import Supplier
from category import Category
from product import Product
from sales import Sales
class IMS:
    def __init__(self,root):
        self.root = root
        self.root.title("Welcome Our RiseStore Shop")
        self.root.geometry("500x500")
        self.root.state("zoomed")
        self.root.iconbitmap(r"image/shop_icon.ico")
        self.root.config(bg="#ffffff")
        self.font_family = "arial"
        #==========================icon image ======================
        self.brand_icon = PhotoImage(file="image/shop.png")
        self.logout_icon = PhotoImage(file="image/logout.png")
        self.dashboard_icon = PhotoImage(file="image/layout.png")
        self.emp_icon = PhotoImage(file="image/emp.png")
        self.supplier_icon = PhotoImage(file="image/supplier.png")
        self.category_icon = PhotoImage(file="image/category.png")
        self.product_icon = PhotoImage(file="image/product.png")
        self.sales_icon = PhotoImage(file="image/sales.png")
        self.exit_icon = PhotoImage(file="image/exit.png")
        

        #==========================header part =====================
        title = Label(self.root,text="RiseStore.", image=self.brand_icon,compound=LEFT, font=(self.font_family,40,"bold"),bg="#214175", fg="#0dccfc",anchor="w",padx=15).place(x=0,y=0,relwidth=1,height=70)
        logout_btn = Button(self.root,text="Logout", image=self.logout_icon, compound=LEFT, font=(self.font_family,18,"bold"),bg="#0dccfc",padx=5).place(x=1300,y=13)
        self.clock = Label(self.root,text="Date: DD-MM-YYYY \t Time: HH:MM:SS", bg="#214175",fg="#a7f0fc",font=(self.font_family,15,"bold"))
        self.clock.place(x=800,y=22)

        #========================= bd start ======================
        Label(self.root,bg="#8f8e8d").place(x=0,y=70,relwidth=1,height=3)

        #=========================menu start ======================
        menu = Frame(self.root,bd=2,relief=RIDGE,bg="#0274ba")
        menu.place(x=0,y=73,width=300,height=740)

        dashboard_title = Label(menu,text="Dashboard",anchor="w",image=self.dashboard_icon,compound=LEFT,font=(self.font_family,23,"bold"),bg="#a7f0fc",fg="#f7a414",padx=25)
        dashboard_title.place(x=0,y=0,relwidth=1,height=80)
        

        emp_btn = Button(menu,text="Employee",image=self.emp_icon, compound=LEFT, font=(self.font_family,15,"bold"),cursor="hand2",borderwidth=0,bg="#ffffff",fg="#000000",padx=25,pady=10,anchor="w",command=self.employee)
        emp_btn.place(x=0,y=90,relwidth=1)
        supplier_btn = Button(menu,text="Supplier",image=self.supplier_icon, compound=LEFT, font=(self.font_family,15,"bold"),cursor="hand2",borderwidth=0,bg="#ffffff",fg="#000000",padx=25,pady=10,anchor="w",command=self.supplier)
        supplier_btn.place(x=0,y=155,relwidth=1)
        category_btn = Button(menu,text="Category",image=self.category_icon, compound=LEFT, font=(self.font_family,15,"bold"),cursor="hand2",borderwidth=0,bg="#ffffff",fg="#000000",padx=25,pady=10,anchor="w",command=self.category)
        category_btn.place(x=0,y=220,relwidth=1)
        product_btn = Button(menu,text="Product",image=self.product_icon, compound=LEFT, font=(self.font_family,15,"bold"),cursor="hand2",borderwidth=0,bg="#ffffff",fg="#000000",padx=25,pady=10,anchor="w",command=self.product)
        product_btn.place(x=0,y=285,relwidth=1)
        sales_btn = Button(menu,text="Sales",image=self.sales_icon, compound=LEFT, font=(self.font_family,15,"bold"),cursor="hand2",borderwidth=0,bg="#ffffff",fg="#000000",padx=25,pady=10,anchor="w",command=self.sales)
        sales_btn.place(x=0,y=350,relwidth=1)
        exit_btn = Button(menu,text="Exit",image=self.exit_icon, compound=LEFT, font=(self.font_family,15,"bold"),cursor="hand2",borderwidth=0,bg="#ffffff",fg="#000000",padx=25,pady=10,anchor="w")
        exit_btn.place(x=0,y=415,relwidth=1)

        #=========================content =====================

        total_emp = Label(self.root,text="Total Employee \n [0]",font=(self.font_family,15,"bold"),bd=4,relief=RIDGE,bg="#f75631").place(x=350,y=100,width=300,height=150)
        total_sup = Label(self.root,text="Total Supplier \n [0]",font=(self.font_family,15,"bold"),bd=4,relief=RIDGE,bg="#17eb57").place(x=740,y=100,width=300,height=150)
        total_cat = Label(self.root,text="Total Category \n [0]",font=(self.font_family,15,"bold"),bd=4,relief=RIDGE,bg="#2e8de6").place(x=1120,y=100,width=300,height=150)
        total_pro = Label(self.root,text="Total Product \n [0]",font=(self.font_family,15,"bold"),bd=4,relief=RIDGE,bg="#e80ea7").place(x=350,y=300,width=300,height=150)
        total_sales = Label(self.root,text="Total Sales \n [0]",font=(self.font_family,15,"bold"),bd=4,relief=RIDGE,bg="#3abef2").place(x=740,y=300,width=300,height=150)

        footer = Label(self.root,text=" 2022-2023 | RiseStore. | All rights reserved.", font=(self.font_family,15,"bold"),bg="#444444", fg="#ffffff").place(x=0,y=810,relwidth=1,height=30)
    
    
    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Employee(self.new_win)
        
    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Supplier(self.new_win)

    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Category(self.new_win)

    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Product(self.new_win)
    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Sales(self.new_win)





if __name__ =="__main__":
        root = Tk()
        obj = IMS(root)
        root.mainloop()
from tkinter import *
import tkinter.messagebox as MessageBox
from tkinter import font as tkFont
import mysql.connector as mysql
from tkinter import ttk
import tkinter as tk

month=""
year=""
income=0
expense=0
savingrs=0
savingper=0
result=""

class Frames(object):
    def __init__(self):
        self.query1=StringVar()
        self.query1.set(0)
        self.query2=StringVar()
        self.query2.set(0)
        self.query3=StringVar()
        self.query3.set(0)
        self.query4=StringVar()
        self.query4.set(0)
        self.query5=StringVar()
        self.query5.set(0)
        self.query6=StringVar()
        self.query6.set(0)
        self.query7=StringVar()
        self.query7.set(0)
        self.query8=StringVar()
        self.query8.set(0)
        self.query9=StringVar()
        self.query9.set(0)
        self.query10=StringVar()
        self.query10.set(0)
        self.query11=StringVar()
        self.query11.set(0)
        self.emonth=tk.StringVar()
        self.emonth.set("January")
        self.eyear=StringVar()
        self.eyear.set("2000")
        
    def table(self):
        page6 = Toplevel(root)
        page6.geometry("930x400")
        l=Label(page6,width=5,text="Table\n",font=('bold',23))
        l.grid(row=0,column=3)
        con=mysql.connect(host="localhost",user="root",password="",database="python")
        cursor=con.cursor()
        cursor.execute("select * from student")
    
        e=Label(page6,width=10,text='Sr. No.',font=('bold',15),borderwidth=2, relief='ridge',bg='yellow')#anchor='w',bg='yellow')
        e.grid(row=1,column=0)
        e=Label(page6,width=10,text='Month',font=('bold',15),borderwidth=2, relief='ridge',bg='yellow')
        e.grid(row=1,column=1)
        e=Label(page6,width=10,text='Year',font=('bold',15),borderwidth=2, relief='ridge',bg='yellow')
        e.grid(row=1,column=2)
        e=Label(page6,width=10,text='Income',font=('bold',15),borderwidth=2, relief='ridge',bg='yellow')
        e.grid(row=1,column=3)
        e=Label(page6,width=10,text='Expense',font=('bold',15),borderwidth=2, relief='ridge',bg='yellow')
        e.grid(row=1,column=4)
        e=Label(page6,width=10,text='Result',font=('bold',15),borderwidth=2, relief='ridge',bg='yellow')
        e.grid(row=1,column=5)
        e=Label(page6,width=10,text='Savings(Rs)',font=('bold',15),borderwidth=2, relief='ridge',bg='yellow')
        e.grid(row=1,column=6)
        e=Label(page6,width=10,text='Savings(%)',font=('bold',15),borderwidth=2, relief='ridge',bg='yellow')
        e.grid(row=1,column=7)
        i=2
        for data in cursor:
            for j in range(len(data)):
                e=Label(page6, text=data[j],font=('bold',15),width=10,borderwidth=2,relief='ridge')
                e.grid(row=i,column=j)
            i=i+1
        
    def update(self):
        con=mysql.connect(host="localhost",user="root",password="",database="python")
        cursor=con.cursor()
        cursor.execute("insert into student(Month, Year, Income, Expense, Result, Save, Savings) values('"+month+"', '"+year+"', '"+str(income)+"', '"+str(expense)+"', '"+str(result)+"', '"+str(savingrs)+"', '"+str(savingper)+"')")
        MessageBox.showinfo("Status","Details Updated Successfully");
        con.close();
        self.finpage()
        
    def calcres(self):
        global savingrs
        global savingper
        global result
        if(income>expense):
            result="Profit"
            savingrs=((income-expense))
            savingper=((100-((expense*100)/income)))
        elif(expense>income):
            result="Loss"
            savingrs=((expense-income))
            savingper=(((expense-income)*100)/income)
        else:
            result="None"
            
    def calcinc(self):
        global month
        month=self.emonth.get()
        global year
        year=self.eyear.get()
        a=int(self.query1.get())
        b=int(self.query2.get())
        c=int(self.query3.get())
        global income
        income=a+b+c
        self.exppage()
        
    def calcexp(self):
        a=int(self.query4.get())
        b=int(self.query5.get())
        c=int(self.query6.get())
        d=int(self.query7.get())
        e=int(self.query8.get())
        f=int(self.query9.get())
        g=int(self.query10.get())
        h=int(self.query11.get())
        global expense
        expense=a+b+c+d+e+f+g+h
        self.calcres()
        self.respage()
        
    def finpage(self):
        page5 = Toplevel(root)
        page5.geometry("400x400")
        l1 = Label(page5, text="Contact Us",font=('bold',20)).place(x=120,y=20)
        button1=Button(page5, text="Table",font=('bold',18),command=self.table).place(x=145,y=180)
        button2=Button(page5, text="Back",font=('bold',18),command=page5.destroy).place(x=80,y=280)
        button3=Button(page5, text="EXIT",font=('bold',18),command=root.destroy).place(x=210,y=280)
        
    def respage(self):
        page4 = Toplevel(root)
        page4.geometry("400x480")
        label1 = Label(page4, text="Result Section",font=('bold',20))
        label1.pack()
        label = Label(page4, text="Month",font=('bold',15)).place(x=40,y=60)
        label = Label(page4, text=month,font=('bold',15)).place(x=250,y=60)
        
        label = Label(page4, text="Year",font=('bold',15)).place(x=40,y=100)
        label = Label(page4, text=year,font=('bold',15)).place(x=250,y=100)
        
        label=Label(page4, text="Income",font=('bold',15)).place(x=40,y=140)
        label=Label(page4, text=income,font=('bold',15)).place(x=250,y=140)
        
        label4=Label(page4, text="Expense",font=('bold',15)).place(x=40,y=180)
        label4=Label(page4, text=expense,font=('bold',15)).place(x=250,y=180)
        
        label6=Label(page4, text=result,font=('bold',18)).place(x=150,y=250)  #Profit pr Loss
        
        label7=Label(page4, text= "Rs."+str(savingrs),font=('bold',18)).place(x=50,y=330)
        label8=Label(page4, text= "%"+str(int(savingper)),font=('bold',18)).place(x=210,y=330)
    
        button1=Button(page4, text="Back",font=('bold',14),command=page4.destroy)
        button1.place(x=80,y=400)
        button2=Button(page4, text="OK",font=('bold',14),command=lambda:[page4.destroy(),self.update()])
        button2.place(x=180,y=400)
        button3=Button(page4, text="EXIT",font=('bold',14),command=root.destroy)
        button3.place(x=290,y=400)
        
    def exppage(self):
        page3 = Toplevel(root)
        page3.geometry("700x420")
        label1 = Label(page3, text="Expense Section",font=('bold',20))
        label1.pack()

        label1=Label(page3,text="Rent",font=('bold',16)).place(x=30,y=100) #1
        labelr1=Label(page3,text="Rs.",font=('bold',16)).place(x=150,y=100)
        entry1=Entry(page3,textvariable=self.query4,font=('bold',16),width=10)
        entry1.place(x=190,y=100)
        
        label2=Label(page3,text="Bills",font=('bold',16)).place(x=30,y=150)     #2
        labelr2=Label(page3,text="Rs.",font=('bold',16)).place(x=150,y=150)
        entry1=Entry(page3,textvariable=self.query5,font=('bold',16),width=10)
        entry1.place(x=190,y=150)

        label3=Label(page3,text="Fees",font=('bold',16)).place(x=30,y=200)      #3
        labelr3=Label(page3,text="Rs.",font=('bold',16)).place(x=150,y=200)
        entry1=Entry(page3,textvariable=self.query6,font=('bold',16),width=10)
        entry1.place(x=190,y=200)

        label4=Label(page3,text="EMI",font=('bold',16)).place(x=30,y=250)      #4
        labelr4=Label(page3,text="Rs.",font=('bold',16)).place(x=150,y=250)
        entry1=Entry(page3,textvariable=self.query7,font=('bold',16),width=10)
        entry1.place(x=190,y=250)

        label5=Label(page3,text="Groceries",font=('bold',16)).place(x=330,y=100) #5
        labelr5=Label(page3,text="Rs.",font=('bold',16)).place(x=510,y=100)
        entry1=Entry(page3,textvariable=self.query8,font=('bold',16),width=10)
        entry1.place(x=550,y=100)

        label6=Label(page3,text="Tax",font=('bold',16)).place(x=330,y=150)      #6
        labelr6=Label(page3,text="Rs.",font=('bold',16)).place(x=510,y=150)
        entry1=Entry(page3,textvariable=self.query9,font=('bold',16),width=10)
        entry1.place(x=550,y=150)

        label7=Label(page3,text="Insurance",font=('bold',16)).place(x=330,y=200) #7
        labelr7=Label(page3,text="Rs.",font=('bold',16)).place(x=510,y=200)
        entry1=Entry(page3,textvariable=self.query10,font=('bold',16),width=10)
        entry1.place(x=550,y=200)

        label8=Label(page3,text="Other Expenses",font=('bold',16)).place(x=330,y=250) #8                
        labelr8=Label(page3,text="Rs.",font=('bold',16)).place(x=510,y=250)
        entry1=Entry(page3,textvariable=self.query11,font=('bold',16),width=10)
        entry1.place(x=550,y=250)

        button1=Button(page3, text="Back",font=('bold',14),command=page3.destroy)
        button1.place(x=140,y=320)
        
        button1=Button(page3, text="OK",font=('bold',14),command=lambda:[page3.destroy(),self.calcexp()])
        button1.place(x=310,y=320)
        
        button3=Button(page3, text="EXIT",font=('bold',14),command=root.destroy)
        button3.place(x=480,y=320)
    
    def incpage(self):
        page2 = Toplevel(root)
        page2.geometry("400x400")
        helv36 = tkFont.Font(family='Helvetica', size=12)
        
        label2 = Label(page2, text="Income Section",font=('bold',20)).place(x=100,y=10)

        bigfont = tkFont.Font()
        dismonth=Label(page2, text = "Select Month :", font = ('bold', 15))
        dismonth.place(x=30,y=60)#, padx = 10, pady = 25)
        monthchoosen = ttk.Combobox(page2,text=self.emonth,font=('bold',15),width = 10)
        monthchoosen['state']='readonly'
        monthchoosen['values'] = ('January','February','March','April','May','June','July','August','September','October','November','December')
        monthchoosen.place(x=30,y=100)

        dismonth=Label(page2, text = "Select Year :", font = ('bold', 15))
        dismonth.place(x=240,y=60)#, padx = 10, pady = 25)
        yearchoosen = ttk.Combobox(page2,text=self.eyear,font=('bold',15),width = 10)
        yearchoosen['state']='readonly'
        yearchoosen['values'] = ("2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021")
        yearchoosen.place(x=240,y=100)
        
        root.option_add("*TCombobox*Listbox*Font", bigfont)
        
        label1=Label(page2,text="Salary",font=('bold',16)).place(x=25,y=170)
        labelr1=Label(page2,text="Rs.",font=('bold',16)).place(x=190,y=170)
        entry1=Entry(page2,textvariable=self.query1,font=('bold',16),width=10)
        entry1.place(x=240,y=170)
    
        label2=Label(page2,text="Bank Interest",font=('bold',16)).place(x=25,y=210)
        labelr2=Label(page2,text="Rs.",font=('bold',16)).place(x=190,y=210)
        entry2=Entry(page2,textvariable=self.query2,font=('bold',16),width=10)
        entry2.place(x=240,y=210)
    
        label3=Label(page2,text="Policy Returns",font=('bold',16)).place(x=25,y=250)
        labelr3=Label(page2,text="Rs.",font=('bold',16)).place(x=190,y=250)
        entry3=Entry(page2,textvariable=self.query3,font=('bold',16),width=10)
        entry3.place(x=240,y=250)
    
        button1=Button(page2, text="Back",font=('bold',14),command=page2.destroy).place(x=70,y=320)
        button2=Button(page2, text="Calc",font=('bold',14),command=lambda:[page2.destroy(),self.calcinc()]).place(x=180,y=320)
        button3=Button(page2, text="EXIT",font=('bold',14),command=root.destroy).place(x=280,y=320)
        
    def mainframe(self,root):
        root.title("Python Mini Project")
        root.geometry("470x420")
        label1 = Label(root, text="Income Expense Manager",width=21,font=('bold',26),relief='solid',borderwidth=1.5).place(x=30,y=10) #bg='yellow',fg='green'
        label2 = Label(root, text="Group 9   SE-ET1 Project",font=('bold',23)).place(x=70,y=75)
        label3=Label(root, text="Enter your name: ",font=('bold',20)).place(x=70,y=170)
        name=Entry(font=('bold',18)).place(x=70,y=220)
        button1=Button(root, text="OK",font=('bold',15),command=self.incpage).place(x=110,y=300)
        button2=Button(root, text="EXIT",font=('bold',15),command=root.destroy).place(x=270,y=300)
        
root=Tk()
app=Frames()
app.mainframe(root)
root.mainloop()

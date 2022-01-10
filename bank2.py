import random

from tkinter import *

root=Tk()
root.title("Banking System")
root.geometry("1x1")


from sqlite3 import *
db=connect("bankdb.db")
d=db.cursor()

def delhome():
    if(k==0):
        rooc()
    elif(k==1):
        root2cb()
    elif(k==2):
        root1wd()
    elif(k==3):
        root3log()
    elif(k==4):
        root4tran()
    elif(k==6):
        root8cp()
    elif(k==7):
        root9cpin()
    elif(k==8):
        root6term()
    elif(k==9):
        root5why()

def rooc():
    global roo
    roo.destroy()

def root2cb():
    global root2
    root2.destroy()

def root1wd():
    global root1
    root1.destroy()

def root3log():
    global root3
    root3.destroy()

def root4tran():
    global root4
    root4.destroy()

def root5why():
    global root5
    root5.destroy()

def root7ho():
    global root7
    root7.destroy()

def root8cp():
    global root8
    root8.destroy()

def root9cpin():
    global root9
    root9.destroy()
    
def root6term():
    global root6
    root6.destroy()
    
def clos():
    global cl
    if(cl==1):
        root8cp()
    elif(cl==2):
        root4tran()
        

def inp():
    global s,s1,s2
    global name,phone,acc,pas,amt,roo
    phone=s1.get()
    acc=random.randint(1000,10000)
    Label(roo,text="Account Number Generated for You {}".format(acc),fg="navy",bg="dodger blue",font=("Arial Rounded MT Bold",12),height=2).place(x=100,y=240)
    db=connect("bankdb.db")
    d=db.cursor()
    d.execute("create table if not exists 'bank'(nam TEXT,phone int,account int,password int,balance int)")
    d.execute("insert into bank values('{}',{},{},{},1000)".format(s.get(),s1.get(),acc,s2.get()))
    db.commit()

def value():
    global s,s1,s2,roo
    n=0
    m=0
    o=0
    val=s.get()
    a=s1.get()
    b=s2.get()
    a1=str(a)
    b2=str(b)
    c=len(a1)
    d=len(b2)
    if(s.get()==""):
        Label(roo,text="Name*",fg="red2",bg="dodger blue",font=("Arial Rounded MT Bold",12),width=20).place(x=150,y=80)
    else:
        o=1
        Label(roo,text="Name",fg="navy",bg="dodger blue",font=("Arial Rounded MT Bold",12),width=20).place(x=150,y=80)
    if(c==10):
        Label(roo,text="Phone",fg="navy",bg="dodger blue",font=("Arial Rounded MT Bold",12),width=20).place(x=150,y=130)
        n=1
    else:
        Label(roo,text="Phone*(10 digit)",fg="red2",bg="dodger blue",font=("Arial Rounded MT Bold",12)).place(x=190,y=130)
    if(d==4):
        Label(roo,text="Password",fg="navy",bg="dodger blue",font=("Arial Rounded MT Bold",12),width=20).place(x=150,y=180)
        m=1
    else:
        Label(roo,text="Password*(4 digit)",fg="red",bg="dodger blue",font=("Arial Rounded MT Bold",12)).place(x=184,y=180)
    if(n==1 and m==1 and o==1):
        inp()

def check():
    global pa,ac,acc,amt,root3
    rec=0
    d.execute("select account from bank where account={}".format(ac.get()))
    r=d.fetchall()
    if not r:
            Label(root3,text="Account Number Not Present",fg="red",bg="dodger blue",font=("Arial Rounded MT Bold",12),width=30).place(x=120,y=350)
    else:
        d.execute("select * from bank where account={}".format(ac.get()))
        rec=d.fetchall()
        for row in rec:
                amt=row[4]
                if(row[3]==pa.get() and row[2]==ac.get()):
                    tran()
                else:
                    Label(root3,text="Wrong Password!!!!",fg="red",bg="dodger blue",font=("Arial Rounded MT Bold",12),width=30).place(x=100,y=350)
                    
def test():
    global pa,ac,root3
    n=0
    m=0
    a=pa.get()
    b=ac.get()
    a1=str(a)
    b2=str(b)
    c=len(a1)
    d=len(b2)
    if(c==4):
        n=1
        Label(root3,text="Please Enter Password",fg="NAVY",bg="dodger blue",font=("Arial Rounded MT Bold",12),width=20).place(x=170,y=130)
    else:
         Label(root3,text="Please Enter Password*",fg="red2",bg="dodger blue",font=("Arial Rounded MT Bold",12)).place(x=167,y=130)
    if(d==4):
            m=1
            Label(root3,text="Pease Enter Account Number",fg="navy",bg="dodger blue",font=("Arial Rounded MT Bold",12),width=25).place(x=145,y=80)
    else:
        Label(root3,text="Pease Enter Account Number*",fg="red2",bg="dodger blue",font=("Arial Rounded MT Bold",12)).place(x=142,y=80)
    if(n==1 and m==1):
        check()

def dele():
    global pa,ac,acc,amt
    db=connect("bankdb.db")
    d=db.cursor()
    d.execute("delete from bank where account={} ".format(ac.get()))
    db.commit()
    home()

def up():
    global pa,ac,acc,amt
    db=connect("bankdb.db")
    d=db.cursor()
    d.execute("update bank set balance={} where account={} ".format(amt,ac.get()))
    db.commit()

def cpup():
    global ac,c4,c3
    a=str(c4.get())
    if(len(a)==4):
        db=connect("bankdb.db")
        d=db.cursor()
        if(cl==2):
            d.execute("update bank set password={} where account={} ".format(c4.get(),ac.get()))
        elif(cl==1):
            d.execute("update bank set password={} where account={} ".format(c4.get(),c3.get()))
        db.commit()
        k=4
        home()
    else:
        Label(root9,text="Password*",fg="red2",bg="dodger blue",font=("Arial Rounded MT Bold",12),width=20).place(x=150,y=10)
def cpin():
    global root9,c4,k
    k=7
    clos()
    root9=Toplevel(root)
    root9.title("hi")
    root9.geometry("500x450")
    root9.resizable(0, 0)
    canvas = Canvas(root9, width=500, height=450, bd=0, highlightthickness=0, highlightbackground="yellow", bg="dodger blue")
    canvas.pack(padx=10, pady=10)
    Label(root9,text="Password",fg="navy",bg="dodger blue",font=("Arial Rounded MT Bold",12),width=20).place(x=150,y=10)
    c4=IntVar()
    Entry(root9,textvariable=c4,bg="gold",fg="orangered4",width=20,show="#").place(x=190,y=50)
    Button(root9,text="SUMBIT",command=cpup,activebackground="red",activeforeground="black",fg="skyblue",bg="darkblue",width=20).place(x=180,y=100)

def why():
    global root5,k
    root8cp()
    k=9
    root5=Toplevel(root)
    root5.title("hi")
    root5.geometry("500x450")
    root5.resizable(0, 0)
    canvas = Canvas(root5, width=500, height=450, bd=0, highlightthickness=0, highlightbackground="yellow", bg="dodger blue")
    canvas.pack(padx=10, pady=10)
    Label(root5,text="QUERY PAGE",fg="NAVY",bg="dodger blue",font=("Jokerman" ,20)).place(x=120,y=20)
    Label(root5,text="MIRAMAR FINANCE BANK",fg="NAVY",bg="dodger blue",font=("Arial Rounded MT Bold",15),width=20).place(x=140,y=500)
    Label(root5,text="1.May You Entered Name Can Be Wrong",fg="navy",bg="dodger blue",font=("Arial Rounded MT Bold",12),wraplength=500).place(x=10,y=100)
    Label(root5,text="2.May You Entered Phone Number Can Be Wrong",fg="navy",bg="dodger blue",font=("Arial Rounded MT Bold",12),wraplength=500).place(x=10,y=150)
    Label(root5,text="3.May You Entered Account Number Can Be Wrong",fg="navy",bg="dodger blue",font=("Arial Rounded MT Bold",12),wraplength=500).place(x=10,y=200)
    Button(root5,text="HOME",command=home,activebackground="red",activeforeground="black",fg="cyan",bg="darkblue",width=20).place(x=180,y=250)

def chpass():
    global c1,c2,c3,root8
    db=connect("bankdb.db")
    d=db.cursor()
    d.execute("select account from bank where account={}".format(c3.get()))
    p=d.fetchall()
    if not p:
            Label(root8,text="Account Number Not Present*",fg="red2",bg="dodger blue",font=("Arial Rounded MT Bold",12),width=30).place(x=120,y=350)
    else:
        d.execute("select * from bank where account={}".format(c3.get()))
        rec=d.fetchall()
        for row in rec:
            if(row[0]==c1.get() and row[1]==c2.get() and row[2]==c3.get()):
                  cpin()
            else:
                Button(root8,text="Why Can Not Change Password?",command=why,activebackground="red",activeforeground="black",fg="skyblue",bg="darkblue",width=40).place(x=120,y=350)
                Label(root8,text="Can Not Change Password",fg="navy",bg="dodger blue",font=("Arial Rounded MT Bold",12),width=30,height=3).place(x=110,y=240)
                 
def change():
    global c1,c2,c3,root8
    a=str(c3.get())
    b=str(c2.get())
    n=0
    m=0
    o=0
    if(c1.get()==""):
         Label(root8,text="Name*",fg="red2",bg="dodger blue",font=("Arial Rounded MT Bold",12),width=20).place(x=150,y=80)
    else:
        o=1
        Label(root8,text="Name",fg="navy",bg="dodger blue",font=("Arial Rounded MT Bold",12),width=20).place(x=150,y=80)
    if(len(a)==4):
        n=1
        Label(root8,text="Account Number",fg="navy",bg="dodger blue",font=("Arial Rounded MT Bold",12),width=20).place(x=150,y=180)
    else:
        Label(root8,text="Account Number*",fg="red2",bg="dodger blue",font=("Arial Rounded MT Bold",12),width=20).place(x=150,y=180)
    if(len(b)==10):
        m=1
        Label(root8,text="Phone",fg="navy",bg="dodger blue",font=("Arial Rounded MT Bold",12),width=20).place(x=150,y=130)
    else:
        Label(root8,text="Phone*",fg="red2",bg="dodger blue",font=("Arial Rounded MT Bold",12),width=20).place(x=150,y=130)
    if(n==1 and m==1 and o==1):
        chpass()
        
def cp():
    global root8,c1,c2,c3,k,cl
    k=6
    cl=1
    root3log()
    root8=Toplevel(root)
    root8.title("hi")
    root8.geometry("500x450")
    root8.resizable(0, 0)
    canvas = Canvas(root8, width=500, height=450, bd=0, highlightthickness=0, highlightbackground="yellow", bg="dodger blue")
    canvas.pack(padx=10, pady=10)
    Label(root8,text="PASSWORD CHANGING PAGE",fg="NAVY",bg="dodger blue",font=("Jokerman" ,20)).place(x=45,y=10)
    Label(root8,text="Name",fg="navy",bg="dodger blue",font=("Arial Rounded MT Bold",12)).place(x=230,y=80)
    c1=StringVar()
    Entry(root8,textvariable=c1,bg="gold",fg="orangered4").place(x=195,y=105)
    c1.get()
    Label(root8,text="Phone",fg="navy",bg="dodger blue",font=("Arial Rounded MT Bold",12)).place(x=225,y=130)
    c2=IntVar()
    Entry(root8,textvariable=c2,bg="gold",fg="orangered4").place(x=195,y=155)
    c2.get()
    Label(root8,text="Account Number",fg="navy",bg="dodger blue",font=("Arial Rounded MT Bold",12)).place(x=188,y=180)
    c3=IntVar()
    Entry(root8,textvariable=c3,bg="gold",fg="orangered4").place(x=195,y=205)
    c3.get()
    Button(root8,text="SUMBIT",command=change,activebackground="red",activeforeground="black",fg="skyblue",bg="darkblue",width=20).place(x=180,y=250)
    Button(root8,text="HOME",command=home,activebackground="red",activeforeground="black",fg="skyblue",bg="darkblue",width=20).place(x=180,y=300)
    Label(root8,text="MIRAMAR FINANCE BANK",fg="NAVY",bg="dodger blue",font=("Arial Rounded MT Bold",15),width=20).place(x=140,y=400)
        
def create():
    root6term()
    global name,phone,acc,pas
    global s,s1,s2,roo,k
    k=0
    roo=Toplevel(root)
    roo.title("hi")
    roo.geometry("500x450")
    roo.resizable(0, 0)
    canvas = Canvas(roo, width=500, height=450, bd=0, highlightthickness=0, highlightbackground="yellow", bg="dodger blue")
    canvas.pack(padx=10, pady=10)
    Label(roo,text="ACCOUNT CREATING PAGE",fg="NAVY",bg="dodger blue",font=("Jokerman" ,20)).place(x=60,y=10)
    acc=random.randint(1000,10000)
    Label(roo,text="Hi Customer Follow the Steps to Create Account",fg="navy",bg="dodger blue",font=("Arial Rounded MT Bold",12)).place(x=80,y=50)
    Label(roo,text="Name",fg="navy",bg="dodger blue",font=("Arial Rounded MT Bold",12)).place(x=230,y=80)
    s=StringVar()
    Entry(roo,textvariable=s,bg="gold",fg="orangered4").place(x=195,y=105)
    name=s.get()
    Label(roo,text="Phone",fg="navy",bg="dodger blue",font=("Arial Rounded MT Bold",12)).place(x=225,y=130)
    s1=IntVar()
    Entry(roo,textvariable=s1,bg="gold",fg="orangered4").place(x=195,y=155)
    Label(roo,text="Password",fg="navy",bg="dodger blue",font=("Arial Rounded MT Bold",12)).place(x=210,y=180)
    s2=IntVar()
    Entry(roo,textvariable=s2,show="#",bg="gold",fg="orangered4").place(x=195,y=205)
    pas=s2.get()
    Button(roo,text="Sumit",command=value,activebackground="red",activeforeground="black",fg="skyblue",bg="darkblue",width=20).place(x=180,y=240)
    Button(roo,text="HOME",command=home,activebackground="red",activeforeground="black",fg="skyblue",bg="darkblue",width=20).place(x=180,y=280)
    Label(roo,text="MIRAMAR FINANCE BANK",fg="NAVY",bg="dodger blue",font=("Arial Rounded MT Bold",15),width=20).place(x=140,y=350)

def login():
    global pa,ac,root3,k,cl
    k=3
    cl=2
    root7ho()
    root3=Toplevel(root)
    root3.title("hi")
    root3.geometry("500x450")
    root3.resizable(0, 0)
    canvas = Canvas(root3, width=500, height=450, bd=0, highlightthickness=0, highlightbackground="yellow", bg="dodger blue")
    canvas.pack(padx=10, pady=10)
    Label(root3,text="LOGIN PAGE",fg="NAVY",bg="dodger blue",font=("Jokerman" ,20)).place(x=180,y=20)
    Label(root3,text="Pease Enter Account Number",fg="navy",bg="dodger blue",font=("Arial Rounded MT Bold",12),width=25).place(x=145,y=80)
    ac=IntVar()
    Entry(root3,textvariable=ac,bg="gold",fg="orangered4").place(x=195,y=105)
    ac.get()
    Label(root3,text="Please Enter Password",fg="NAVY",bg="dodger blue",font=("Arial Rounded MT Bold",12),width=20).place(x=170,y=130)
    pa=IntVar()
    Entry(root3,bg="gold",fg="orangered4",textvariable=pa,show="#").place(x=195,y=155)
    pa.get()
    Button(root3,text="SUMIT",command=test,activebackground="red",activeforeground="black",fg="skyblue",bg="darkblue",width=20).place(x=180,y=200)
    Button(root3,text="HOME",command=home,activebackground="red",activeforeground="black",fg="skyblue",bg="darkblue",width=20).place(x=180,y=240)
    Button(root3,text="DELETE ACCOUNT",command=delt,activebackground="red",activeforeground="black",fg="skyblue",bg="darkblue",width=20).place(x=180,y=280)
    Button(root3,text="FORGET PASSWORD",command=cp,activebackground="red",activeforeground="black",fg="skyblue",bg="darkblue",width=20).place(x=180,y=320)
    Label(root3,text="MIRAMAR FINANCE BANK",fg="NAVY",bg="dodger blue",font=("Arial Rounded MT Bold",15),width=20).place(x=140,y=370)

def bal():
    global amt,root4,k,root2
    k=1
    root4tran()
    root2=Tk()
    root2.title("hi")
    root2.geometry("500x450")
    root2.resizable(0, 0)
    canvas = Canvas(root2, width=500, height=450, bd=0, highlightthickness=0, highlightbackground="yellow", bg="dodger blue")
    canvas.pack(padx=10, pady=10)
    Label(root2,text="Your Balance is \"{}\"".format(amt),fg="navy",bg="dodger blue",width=20,height=2,font=("Arial Rounded MT Bold",12)).place(x=150,y=20)
    Button(root2,text="HOME",command=home,activebackground="red",activeforeground="black",fg="skyblue",bg="darkblue",width=20).place(x=180,y=80)
    Label(root2,text="MIRAMAR FINANCE BANK",fg="NAVY",bg="dodger blue",font=("Arial Rounded MT Bold",15),width=20).place(x=140,y=130)
    
def wit2():
    global wth,amt,root2
    if(100<=wth.get()<=10000):
        if(wth.get()<=amt):
            amt=amt-wth.get()
            up()
            Label(root1,text="Your Balance is {}".format(amt),fg="navy",bg="dodger blue",width=20,height=2,font=("Arial Rounded MT Bold",12)).place(x=165,y=260)
        else:
            Label(root1,text="Your Balance is Low*",fg="red2",bg="dodger blue",width=20,height=2,font=("Arial Rounded MT Bold",12)).place(x=165,y=260)
    else:
         Label(root1,text="Limit Max:₹10000 and Min:₹100*",fg="red2",bg="dodger blue",width=20,wraplength=200,font=("Arial Rounded MT Bold",12)).place(x=150,y=260)
         
def add():
    global wth,amt,root1
    if(100<=wth.get()<=100000):
        amt=amt+wth.get()
        up()
        Label(root1,text="Your Balance is {}".format(amt),fg="navy",bg="dodger blue",width=20,height=2,font=("Arial Rounded MT Bold",12)).place(x=165,y=260)
    else:
         Label(root1,text="Limit Max:₹100000 and Min:₹100*",fg="red2",bg="dodger blue",width=20,wraplength=200,font=("Arial Rounded MT Bold",12)).place(x=152,y=260)
         
def amin():
    global wth,amt,root1,k
    k=2
    root4tran()
    root1=Toplevel(root)
    root1.title("hi")
    root1.geometry("500x450")
    root1.resizable(0, 0)
    canvas = Canvas(root1, width=500, height=450, bd=0, highlightthickness=0, highlightbackground="yellow", bg="dodger blue")
    canvas.pack(padx=10, pady=10)
    Label(root1,text="WITHDRAW\DEPOSIT PAGE",fg="NAVY",bg="dodger blue",font=("Jokerman" ,20)).place(x=80,y=20)
    Label(root1,text="Enter Amount :",fg="navy",bg="dodger blue",font=("Arial Rounded MT Bold",12)).place(x=196,y=80)
    wth=IntVar()
    Entry(root1,textvariable=wth,bg="gold",fg="orangered4").place(x=195,y=105)
    wth.get()
    Button(root1,text="Withdraw",command=wit2,activebackground="red",activeforeground="black",fg="skyblue",bg="darkblue",width=20).place(x=180,y=140)
    Button(root1,text="Deposit",command=add,activebackground="red",activeforeground="black",fg="skyblue",bg="darkblue",width=20).place(x=180,y=180)
    Button(root1,text="HOME",command=home,activebackground="red",activeforeground="black",fg="skyblue",bg="darkblue",width=20).place(x=180,y=220)
    Label(root1,text="Your Balance is {}".format(amt),fg="navy",bg="dodger blue",width=20,height=2,font=("Arial Rounded MT Bold",12)).place(x=165,y=260)
    Label(root1,text="MIRAMAR FINANCE BANK",fg="NAVY",bg="dodger blue",font=("Arial Rounded MT Bold",15),width=20).place(x=140,y=300)
    
def tran():
            global amt,root4,k
            root3log()
            k=4
            root4=Toplevel(root)
            root4.title("hi")
            root4.geometry("500x450")
            root4.resizable(0, 0)
            canvas = Canvas(root4, width=500, height=450, bd=0, highlightthickness=0, highlightbackground="yellow", bg="dodger blue")
            canvas.pack(padx=10, pady=10)
            Label(root4,text="TRANSCATION  PAGE",fg="NAVY",bg="dodger blue",font=("Jokerman" ,20)).place(x=120,y=20)
            Button(root4,text="Check Balance",command=bal,activebackground="red",activeforeground="black",fg="skyblue",bg="darkblue",width=20).place(x=180,y=100)
            Button(root4,text="Withdraw/Deposit",command=amin,activebackground="red",activeforeground="black",fg="skyblue",bg="darkblue",width=20).place(x=180,y=150)
            Button(root4,text="Change Password",command=cpin,activebackground="red",activeforeground="black",fg="skyblue",bg="darkblue",width=20).place(x=180,y=200)
            Button(root4,text="HOME",command=home,activebackground="red",activeforeground="black",fg="skyblue",bg="darkblue",width=20).place(x=180,y=250)
            Label(root4,text="MIRAMAR FINANCE BANK",fg="NAVY",bg="dodger blue",font=("Arial Rounded MT Bold",15),width=20).place(x=140,y=300)
def delt():
    global pa,ac,acc
    d.execute("select * from bank where account={}".format(ac.get()))
    rec=d.fetchall()
    for row in rec:
        if(row[3]==pa.get() and row[2]==ac.get()):
            dele()
        else:
            e()

def take():
    global t1
    if(t1.get()==1):
        create()
    else:
        home()
        
def term():
    global t1,k,root6 
    root7ho()
    k=8
    root6=Toplevel(root)
    root6.title("hi")
    root6.geometry("500x550")
    canvas = Canvas(root6, width=500, height=550, bd=0, highlightthickness=0, highlightbackground="yellow", bg="dodger blue")
    canvas.pack(padx=10, pady=10)
    Label(root6,text="Terms and Conditions",fg="NAVY",bg="dodger blue",font=("Jokerman" ,20)).place(x=120,y=20)
    Label(root6,text="MIRAMAR FINANCE BANK",fg="NAVY",bg="dodger blue",font=("Arial Rounded MT Bold",15),width=20).place(x=140,y=500)
    Label(root6,text="1.You Should Credit Account with ₹1000",fg="navy",bg="dodger blue",font=("Arial Rounded MT Bold",12),wraplength=500).place(x=10,y=100)
    Label(root6,text="2.You Can WithDraw Max:₹10000 and Min:₹100 at a Time",fg="navy",bg="dodger blue",font=("Arial Rounded MT Bold",12),wraplength=500).place(x=10,y=150)
    Label(root6,text="3.Account Number will be Generated AutoMatically",fg="navy",bg="dodger blue",font=("Arial Rounded MT Bold",12),wraplength=500).place(x=10,y=200)
    Label(root6,text="4.You Can Deposit Min:₹100 and Max:₹100000",fg="navy",bg="dodger blue",font=("Arial Rounded MT Bold",12),wraplength=450).place(x=10,y=250)
    Label(root6,text="5.You Can Choose Your Own Password but it Can Have 4 Digit",fg="navy",bg="dodger blue",font=("Arial Rounded MT Bold",12),wraplength=450).place(x=10,y=300)
    t1=IntVar()
    Radiobutton(root6,text="Accept",value=1,variable=t1,fg="NAVY",bg="dodger blue",font=("Arial Rounded MT Bold",12)).place(x=150,y=360)
    Radiobutton(root6,text="Decline",value=0,variable=t1,fg="NAVY",bg="dodger blue",font=("Arial Rounded MT Bold",12)).place(x=300,y=360)
    Button(root6,text="Next",command=take,activebackground="red",activeforeground="black",fg="cyan",bg="darkblue",width=20).place(x=180,y=400)
    Button(root6,text="Home",command=home,activebackground="red",activeforeground="black",fg="cyan",bg="darkblue",width=20).place(x=180,y=450)
    
def home():
    global root7,amt,k
    delhome()
    root7=Toplevel(root)
    root7.title("hi")
    root7.geometry("500x450")
    root7.resizable(0, 0)
    canvas = Canvas(root7, width=500, height=450, bd=0, highlightthickness=0, highlightbackground="yellow", bg="dodger blue")
    canvas.pack(padx=10, pady=10)
    Label(root7,text="HOME  PAGE",fg="NAVY",bg="dodger blue",font=("Jokerman" ,20)).place(x=180,y=20)
    Button(root7,text="Create Account",command=term,activebackground="red",activeforeground="black",fg="cyan",bg="darkblue",width=20).place(x=180,y=100)
    Button(root7,text="Login",command=login,activebackground="red",activeforeground="black",fg="cyan",bg="darkblue",width=20).place(x=180,y=150)
    Label(root7,text="MIRAMAR FINANCE BANK",fg="NAVY",bg="dodger blue",font=("Arial Rounded MT Bold",15),width=20).place(x=140,y=200)
k=-1
cl=0
home()

from tkinter import *
import random
import time;

root = Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant Management System")

##Variables##
text_Input = StringVar()
operator = ""
rand = StringVar()
Fries = StringVar()
Burger = StringVar()
Chx = StringVar()
PulledPork = StringVar()
Ribs = StringVar()
ColeSlaw = StringVar()
CheeseBurger = StringVar()
SubTotal = StringVar()
Tax = StringVar()
Total = StringVar()


Top = Frame(root, width = 1600,height=50,bg="darkseagreen",relief=SUNKEN)
Top.pack(side=TOP)

f1 = Frame(root, width = 800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width = 500,height=800,relief=SUNKEN)
f2.pack(side=RIGHT)

##TIME##
localtime=time.asctime(time.localtime(time.time()))

##INFO##
lblInfo = Label(Top,font=('arial',50,'bold'),text="Restaurant Management System",fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

'''lblInfo = Label(Top,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)'''

##Calculator Function##
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
        global operator 
        operator=""
        text_Input.set("")
        
def btnEquals():
        global operator 
        sumup = str(eval(operator))
        text_Input.set(sumup)
        operator=""

def Ref():
    x = random.randint(6546,505654)
    randomRef = str(x)
    rand.set(randomRef)

    CoF = float(Fries.get())
    CoB = float(Burger.get())
    CoChx = float(Chx.get())
    CoPP = float(PulledPork.get())
    CoR = float(Ribs.get())
    CoCS = float(ColeSlaw.get())
    CoCB = float(CheeseBurger.get())

    PoF = CoF * .99
    PoB = CoB * 5.99
    PoChx = CoChx * 6.99
    PoPP = CoPP * 5.99
    PoR = CoR * 8.99
    PoCS = CoCS * .99
    PoCB = CoCB * 6.10

    CostoMeal = (PoF + PoB + PoChx + PoPP + PoR + PoCS + PoCB)
    PayTax = ((PoF + PoB + PoChx + PoPP + PoR + PoCS + PoCB)* 0.07)
    ToCost =  "$", str('%.2f' % (CostoMeal + PayTax))

    SubTotal.set(CostoMeal)
    Tax.set(PayTax)
    Total.set(ToCost)            


def qExit():
    root.destroy()

def Reset():
    text_Input.set("")
    rand.set("")
    Fries.set("")
    Burger.set("")
    Chx.set("")
    PulledPork.set("")
    Ribs.set("")
    ColeSlaw.set("")
    CheeseBurger.set("")
    SubTotal.set("")
    Tax.set("")
    Total.set("")
    
        
    
txtDisplay=Entry(f2,font=('arial',20,'bold'),textvariable=text_Input,bd=30,insertwidth=4,bg="darkseagreen",justify='right')
txtDisplay.grid(columnspan=5)

##CALCULATOR##
##ROW1##

btn7=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="7",bg="gray",command=lambda: btnClick(7)).grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="8",bg="gray",command=lambda: btnClick(8)).grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="9",bg="gray",command=lambda: btnClick(9)).grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="+",bg="gray",command=lambda: btnClick('+')).grid(row=2,column=3)

##ROW2##
btn4=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="4",bg="gray",command=lambda: btnClick(4)).grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="5",bg="gray",command=lambda: btnClick(5)).grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="6",bg="gray",command=lambda: btnClick(6)).grid(row=3,column=2)

Subtraction=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="-",bg="gray",command=lambda: btnClick("-")).grid(row=3,column=3)

##ROW3##
btn1=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="1",bg="gray",command=lambda: btnClick(1)).grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="2",bg="gray",command=lambda: btnClick(2)).grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="3",bg="gray",command=lambda: btnClick(3)).grid(row=4,column=2)

Multiplication=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="*",bg="gray",command=lambda: btnClick("*")).grid(row=4,column=3)

##ROW4##
btn0=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="0",bg="gray",command=lambda: btnClick(0)).grid(row=5,column=0)

btnClear=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="C",bg="gray",command=btnClearDisplay).grid(row=5,column=1)

btnEquals=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="=",bg="gray",command=btnEquals).grid(row=5,column=2)

Division=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="/",bg="gray",command=lambda: btnClick('/')).grid(row=5,column=3)

##Food Options##
##column 1##
lblReference = Label(f1,font=('arial',16,'bold'),text="Ticket #",bd=16,anchor='w',justify='left')
lblReference.grid(row=0,column=0)
txtReference=Entry(f1,font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="darkseagreen",justify='right')
txtReference.grid(row=0,column=1)

lblFries = Label(f1,font=('arial',16,'bold'),text="Fries",bd=16,anchor='w')
lblFries.grid(row=1,column=0)
txtFries=Entry(f1,font=('arial',16,'bold'),textvariable=Fries,bd=10,insertwidth=4,bg="darkseagreen",justify='right')
txtFries.grid(row=1,column=1)

lblBurger = Label(f1,font=('arial',16,'bold'),text="Burger",bd=16,anchor='w')
lblBurger.grid(row=2,column=0)
txtBurger=Entry(f1,font=('arial',16,'bold'),textvariable=Burger,bd=10,insertwidth=4,bg="darkseagreen",justify='right')
txtBurger.grid(row=2,column=1)

lblCheeseBurger = Label(f1,font=('arial',16,'bold'),text="Cheese Burger",bd=16,anchor='w')
lblCheeseBurger.grid(row=3,column=0)
txtCheeseBurger=Entry(f1,font=('arial',16,'bold'),textvariable=CheeseBurger,bd=10,insertwidth=4,bg="darkseagreen",justify='right')
txtCheeseBurger.grid(row=3,column=1)

lblChx = Label(f1,font=('arial',16,'bold'),text="Chicken Sandwich",bd=16,anchor='w',justify='left')
lblChx.grid(row=4,column=0)
txtChx=Entry(f1,font=('arial',16,'bold'),textvariable=Chx,bd=10,insertwidth=4,bg="darkseagreen",justify='right')
txtChx.grid(row=4,column=1)

lblPork = Label(f1,font=('arial',16,'bold'),text="Pulled Pork",bd=16,anchor='w')
lblPork.grid(row=5,column=0)
txtPork=Entry(f1,font=('arial',16,'bold'),textvariable=PulledPork,bd=10,insertwidth=4,bg="darkseagreen",justify='right')
txtPork.grid(row=5,column=1)

##column 2##
lblRibs = Label(f1,font=('arial',16,'bold'),text="Ribs",bd=16,anchor='w')
lblRibs.grid(row=0,column=2)
txtRibs=Entry(f1,font=('arial',16,'bold'),textvariable=Ribs,bd=10,insertwidth=4,bg="darkseagreen",justify='right')
txtRibs.grid(row=0,column=3)

lblSlaw = Label(f1,font=('arial',16,'bold'),text="Cole Slaw",bd=16,anchor='w')
lblSlaw.grid(row=1,column=2)
txtSlaw=Entry(f1,font=('arial',16,'bold'),textvariable=ColeSlaw,bd=10,insertwidth=4,bg="darkseagreen",justify='right')
txtSlaw.grid(row=1,column=3)

##TOTALS##
lblSubtotal = Label(f1,font=('arial',16,'bold'),text="Subtotal",bd=16,anchor='w')
lblSubtotal.grid(row=2,column=2)
txtSubtotal=Entry(f1,font=('arial',16,'bold'),textvariable=SubTotal,bd=10,insertwidth=4,bg="darkseagreen",justify='right')
txtSubtotal.grid(row=2,column=3)

lblTax = Label(f1,font=('arial',16,'bold'),text="Tax",bd=16,anchor='w')
lblTax.grid(row=3,column=2)
txtTax=Entry(f1,font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="darkseagreen",justify='right')
txtTax.grid(row=3,column=3)

lblTotal = Label(f1,font=('arial',16,'bold'),text="Total",bd=16,anchor='w')
lblTotal.grid(row=4,column=2)
txtTotal=Entry(f1,font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="darkseagreen",justify='right')
txtTotal.grid(row=4,column=3)

##Buttons##
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="gray",command=Ref).grid(row=7,column=1)

btnNew=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="New",bg="gray",command=Reset).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="gray",command=qExit).grid(row=7,column=3)



root.mainloop()
                                                                                                                                                                                                                                                    

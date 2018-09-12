import sys 
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox 
import openpyxl
from openpyxl import load_workbook


window = Tk()
window.title("TMS Invoice Loader")
window.geometry('500x600+0+0')


#Variables
filename = StringVar()
filename.set("No File Selected")
filechosen = None 





#Create Window

Top = Frame(window, width = 500,height=50,relief=SUNKEN)
Top.pack(side=TOP)

Left = Frame(window, width = 100,height=600,relief=SUNKEN)
Left.pack(side=TOP)
Right = Frame(window, width = 250,height=250,relief=SUNKEN)
Right.pack(side=TOP)

#Functions
def openxls():
    #grab invoice in excel file
    filechosen = askopenfilename()
    filename.set(filechosen)

def importxls():
    #import into database
    wb = openpyxl.load_workbook(filechosen)
    sheet = wb.get_sheet_by_name('Sheet1')
    messagebox.showinfo("Excel",sheet)

       

lblTitle = Label(Top,font=('arial',20,'bold'),text="TMS Invoice Loader",fg="Steel Blue",bd=10,anchor='w')
lblTitle.grid(row=0,column=0)

lblFIle = Label(Left,font=('arial',16,'bold'),text="Select Invoice To Import",bd=16,anchor='e',justify='left')
lblFIle.grid(row=0,column=0)

slctbutton = Button(Right,font=('arial',10,'bold'),text="Browse",bd=16,anchor='e',justify='left',command=openxls)
slctbutton.grid(row=1,column=0)

lblfname = Label(Right,font=('arial',8),textvariable=filename,bd=16,anchor='e',justify='center')
lblfname.grid(row=0,column=0)

sbmButton = Button(Right,font=('arial',10,'bold'),text="Submit",bd=16,anchor='e',justify='center',command=importxls)
sbmButton.grid(row=8,column=0)


#move file to done folder

#rename file

window.mainloop()

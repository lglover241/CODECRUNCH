import sys 
from tkinter import *
from tkinter.filedialog import askopenfilename
import openpyxl;
    #Structure the GUI.
def __init__(self):

        #Create a blank window.
        self.root = Tk()

        #Create the frame.
        frameRoot = Frame(self.root)
        frameRoot.pack()

        #Create the menu.
        menu = Menu(self.root)
        self.root.config(menu=menu)

        #Create the "File" submenu.
        fileMenu = Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="Open Image", command=self.openFile)

        #Make a button to open the image file.
        self.fileChosen = None #Prevent the user from mapping without first selecting an image.
        self.buttonFile = Button(frameRoot, text="Open Image...", command=self.openFile)
        self.buttonFile.grid(row=3, column=1)

        #Display the directory path of the file chosen.
        self.fileName = StringVar()
        self.fileName.set("No File Selected")
        self.labelFileName = Label(frameRoot, textvariable=self.fileName, fg="red")
        self.labelFileName.grid(row=4, column=1)

        #Keep the window open.
        self.root.mainloop()

    #Open the image file.
    def openFile(self):
        #Only accept the following file types.
        self.fileChosen = filedialog.askopenfilename(filetypes=[("Bitmap Files", "*.BMP *.bmp *.DIB *.dib"),
                                                              ("JPEG", "*.JPEG *.jpeg *.JPG *.jpg *.JPE *.jpe *JFIF *.jfif"),
                                                              ("PNG", "*.PNG *.png"),
                                                              ("GIF", "*.GIF *.gif"),
                                                              ("TIFF", "*.TIF *.tif *.TIFF *.tiff"),
                                                              ("ICO", "*.ICO *.ico")
                                                             ])

        #If a file was selected, show the file path. Else, inform the user.
        if self.fileChosen:
            self.fileName.set(self.fileChosen)
        else:
            self.fileName.set("No image was selected. Please select an image.")

if __name__ == "__main__":


from tkinter import *
from  tkinter import filedialog
import tkinter as  tk
from PIL import  Image,ImageTk
import  os

def showimage():
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="select Image file",filetype=((" JPG File","*.jpg"),("PNG File","*.png"),("All file","how are you")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image=img


root=Tk()
frame=Frame(root)
frame.pack(side=BOTTOM,padx=15,pady=15)

lbl=Label(root)
lbl.pack()

btn=Button(frame,text="Select Image",command=showimage)
btn.pack(side=tk.LEFT)

btn2=Button(frame,text="exit",command=lambda:exit())
btn2.pack()

root.title("Imagee viewer")
root.geometry("400x450")
root.mainloop()
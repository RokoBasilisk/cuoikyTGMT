from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
import sys
import re
import numpy as np
from PIL import Image, ImageTk
from time import time
import cv2

img = cv2.imread("image/test.png")
b,g,r = cv2.split(img)
img = cv2.merge((r,g,b))
img = cv2.resize(img, (538, 424))

def on_closing():
    if messagebox.askokcancel("QUIT", "Do you want to quit?"):
        sys.exit()

root = Tk()

# root settings Start
root.title('Sentinent Analysis')
root.geometry("1000x600")
root.resizable(0,0)
root.configure(background='white')
# root settings End

# Creating Frame Start
buttonFrame = Frame(root)
videoFrame = Frame(root)
infoFrame = Frame(root)
# Creating Frame End

# buttonFrame Configuration Start
buttonFrame.configure(borderwidth=0, highlightthickness=0)

# buttonFrame Configuration End

# Add Button to buttonFrame Start
onButton = Button(buttonFrame, text="On", background="#FF9494", fg="#FFFFFF", padx=10, pady=5, borderwidth=0)
offButton = Button(buttonFrame, text="Off", background="#969696", fg="#FFFFFF", padx=10, pady=5, borderwidth=0)
selectButton = Button(buttonFrame, text="Image From System", background="#FFFFFF", fg="#FF9494", padx=15, pady=5, borderwidth=0)

onButton.grid(row=0,column=0)
offButton.grid(row=0,column=1)
selectButton.grid(row=0,column=2)
# Add Button to buttonFrame End

# Add Frame to videoFrame Start
im = Image.fromarray(img)
imgtk = ImageTk.PhotoImage(image=im)
# Add Frame to videoFrame End

# Place Frame Start
buttonFrame.place(x=345, y=23)
Label(root, image=imgtk).place(x=53, y=111)
# Place Frame End

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()

import os.path
#import tkinter as tk
import sys
from tkinter import Tk, PhotoImage, Label, TclError
from PIL import Image, ImageTk

dimensions = lambda width, height : f"{width}x{height}"

root = Tk();

try:
    #filename = os.path.basename(__file__).replace("[", ":\\").replace("#", "\\")[:-4]
    filename = sys.argv[1]
    #photo = PhotoImage(file=filename)
    photo = ImageTk.PhotoImage(Image.open(filename))
except (IndexError, TclError):
    filename = "C:\\Users\\green\\OneDrive\\Documents\\Screenshot 2024-08-29 164300.png"
    photo = ImageTk.PhotoImage(Image.open(filename))

root.geometry(dimensions(photo.width(), photo.height()))
#root.title(os.path.basename(os.path.basename(__file__).replace("[", ":\\").replace("#", "\\")[:-4]))
root.title(os.path.basename(filename))
image = Label(root, image=photo)

image.pack()

root.mainloop()


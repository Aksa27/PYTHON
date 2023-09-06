#import required libraries
from tkinter import *
from PIL import ImageTk, Image

# Create an instance of tkinter window
win = Tk()

# Define the geometry of the window
win.geometry("700x500")

frame = Frame(win, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("pexels-dasha-17820791.jpg"))

# Create a Label Widget to display the text or Imagepexels-sunsetoned-5913482 (2160p)
label = Label(frame, image = img)
label.pack()

win.mainloop()
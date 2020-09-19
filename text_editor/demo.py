from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Hello There')
root.iconbitmap('icon.ico')

myimg = ImageTk.PhotoImage(Image.open('img.jpg'))
myimg1 = ImageTk.PhotoImage(Image.open('img.jpg'))
myimg2 = ImageTk.PhotoImage(Image.open('img.jpg'))

image_list = [myimg, myimg1, myimg2]



label = Label(image=myimg)
label.pack()



root.mainloop()
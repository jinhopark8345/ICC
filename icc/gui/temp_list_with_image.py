import tkinter as tk
import os
from PIL import Image

root = tk.Tk()
scrollbar = tk.Scrollbar(root)
scrollbar.pack( side = tk.RIGHT, fill=tk.Y )
mylist = tk.Listbox(root, font = "verdana 15", yscrollcommand = scrollbar.set,  height= 5, width = 10 )

pathToImages = ['/home/jinho/Dropbox/Projects/ICC/assets/image1.jpg',
'/home/jinho/Dropbox/Projects/ICC/assets/image1.jpg','/home/jinho/Dropbox/Projects/ICC/assets/image1.jpg',
'/home/jinho/Dropbox/Projects/ICC/assets/image1.jpg']

def buttonHandler(self):
    bi = Image.open(pathToImages[int(mylist.curselection()[0])])
    bi.show()

a = mylist.insert(tk.END,str('Biscuit'))
b = mylist.insert(tk.END,str('Chocolate'))
c = mylist.insert(tk.END,str('Sandwich'))
d = mylist.insert(tk.END,str('Cake'))

mylist.bind('<<ListboxSelect>>', buttonHandler)


mylist.pack( )
scrollbar.config( command = mylist.yview )
tk.mainloop()

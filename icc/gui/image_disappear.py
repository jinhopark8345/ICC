import tkinter as tk
# import
# from PIL import Image
from PIL import Image, ImageTk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.initImages()                                #Prepare images
        self.master.resizable(width=False, height=False)
        self.index = 0
        self.grid()

    def initImages(self):
        self.images = {}
        buf = Image.open("onion.png")
        buf = buf.resize((20, 20), Image.ANTIALIAS) #The (250, 250) is (height, width)
        self.images['Classic'] = ImageTk.PhotoImage(buf)

        buf = Image.open("onion.png")
        buf = buf.resize((20, 20), Image.ANTIALIAS) #The (250, 250) is (height, width)
        self.images['Jeopardy'] = ImageTk.PhotoImage(buf)

        buf = Image.open("onion.png")
        buf = buf.resize((20, 20), Image.ANTIALIAS) #The (250, 250) is (height, width)
        self.images['On-site'] = ImageTk.PhotoImage(buf)

        buf = Image.open("onion.png")
        buf = buf.resize((20, 20), Image.ANTIALIAS) #The (250, 250) is (height, width)
        self.images['On-line'] = ImageTk.PhotoImage(buf)

    def ShowImages(self, frame_in, type_img, place_img):
        label = tk.Label(frame_in, image=self.images[type_img])
        label.pack(side="right")

        # label = tk.Label(frame_in, image=self.images[place_img])
        # label.pack(side="right")

    def createWidgets(self, dict_of_data):
        frame = tk.Frame(self, relief='sunken')
        frame.grid(row=0, column=self.index, sticky="WN")
        frame_in = tk.Frame(frame)
        frame_in.grid(row=0, sticky="WE", column=self.index)
        #some other code here

root = tk.Tk()

app = Application(root)
app.initImages()
# app.ShowImages(root, "Classic", "Jeopardy")
app.ShowImages(root, "Classic")



root.mainloop()

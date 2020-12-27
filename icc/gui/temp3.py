import tkinter as tk


class ICC_GUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("foo")
        self.init_frame_user_ing()

        self.initGUI()

    def initGUI(self):
        # self.frame_user_ing = tk.Frame(self.root)
        # self.frame_user_ing.pack()

        # temp(root, img)

        # img = tk.PhotoImage(file='onion.png')
        # frame_user_ing = tk.Frame(root, width=600, height=600, background='white')
        # frame_user_ing.pack_propagate(0)
        # frame_user_ing.pack()
        # self.make_label(frame_user_ing, img)
        # self.make_label(frame_user_ing, img)
        # self.make_label(frame_user_ing, img)
        # self.make_label(frame_user_ing, img)
        # self.make_label(frame_user_ing, img)

        self.root.mainloop()


    def make_label(self, parent, img):
        frame = tk.Frame(parent)
        frame.pack()

        label_ing_image = tk.Label(frame, image=img).pack(side="right")
        explanation = "onion"
        label_ing_name = tk.Label(frame,
                                justify=tk.LEFT,
                                padx=10,
                                text=explanation).pack(side="left")

    def init_frame_user_ing(self, width=600, height=600):
        self.frame_user_ing = tk.Frame(self.root,
                                width=width,
                                height=height,
                                background='white')
        frame_user_ing.pack()
        frame_user_ing.pack_propagate(0)

        self.img = tk.PhotoImage(file='onion.png')
        # make_label2(frame_user_ing, "onion.png")
        self.make_label(frame_user_ing, self.img)
        self.make_label(frame_user_ing, self.img)
        self.make_label(frame_user_ing, self.img)
        self.make_label(frame_user_ing, self.img)
        self.make_label(frame_user_ing, self.img)

    # def update_frame_user_ing(self):
    #     self.frame_user_ing



app = ICC_GUI()

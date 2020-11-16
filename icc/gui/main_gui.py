import tkinter as tk
from PIL import Image

from iccjson.jconnect import *
from recommend.compare_recipe import *
from recommend.recommend_recipe import *
from iccdb.db_manage import *

import os.path
from os import path as ospath


class ICC_GUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("foo")
        self.db = Icc_db("icc")
        self.images = []

        self.init_frame_user_ing()

        self.root.mainloop()

    def make_label(self, parent, img_name):
        frame = tk.Frame(parent)
        frame.pack()

        # self.img = tk.PhotoImage(file=img_path)
        path = "/home/jinho/Dropbox/Projects/ICC/assets/ing/"
        # path = "/home/jinho/Dropbox/Projects/temp/ICC_2/assets/ing/"
        img_path = path + img_name + ".png"
        # img_path = path + img_name + ".JPG"
        # img_path = "/home/jinho/Dropbox/Projects/ICC/assets/ing/green_onion.png"

        # print("img_path: ", img_path)

        if not ospath.exists(img_path):
            print(img_name)
            return
        img = tk.PhotoImage(file=img_path)
        self.images.append(img)
        # self.img = tk.PhotoImage(Image.open(img_path))
        label_ing_image = tk.Label(frame, image=img).pack(side="right")
        label_ing_name = tk.Label(frame,
                                  justify=tk.LEFT,
                                  padx=10,
                                  text=img_name).pack(side="left")

    def init_frame_user_ing(self, width=600, height=1200):
        self.frame_user_ing = tk.Frame(self.root,
                                       width=width,
                                       height=height,
                                       background='white')
        self.frame_user_ing.pack()
        self.frame_user_ing.pack_propagate(0)

        user_ings = self.db.find_user_ings()

        for user_ing in user_ings:
            # make_label2(frame_user_ing, "onion.png")

            img_name = user_ing["name"]
            self.make_label(self.frame_user_ing, img_name)

        # self.make_label(frame_user_ing, self.img)
        # self.make_label(frame_user_ing, self.img)
        # self.make_label(frame_user_ing, self.img)
        # self.make_label(frame_user_ing, self.img)

    # def update_frame_user_ing(self):
    #     self.frame_user_ing


# app = ICC_GUI()

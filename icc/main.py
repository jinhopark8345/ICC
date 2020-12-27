from flask import Flask, render_template
app = Flask(__name__)

from iccjson.jconnect import *
from recommend.compare_recipe import *
from recommend.recommend_recipe import *
from iccdb.db_manage import *
from gui.main_gui import *


def main_t():

  icc_db = IccDB("icc")
  icc_db.add_temp_recipe()
  icc_db.add_temp_user_ing()
  icc_db.add_temp_ing_info()

  recommended_recipe = recommed_recipe()
  print("you should make {}".format(recommended_recipe))

  app = ICC_GUI()
  # print("before user ings {}".format(icc_db.find_user_ings(returnID=False)))
  # remove_recipe_ing_from_user_ing(recommended_recipe)
  # print("after user ings {}".format(icc_db.find_user_ings(returnID=False)))
  # remove_recipe_ing_from_user_ing(recommended_recipe)
  # print("after user ings {}".format(icc_db.find_user_ings(returnID=False)))
  pass


# main_t()

# import tkinter as tk

# class IccGUI(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()

#     def create_widgets(self):
#         self.hi_there = tk.Button(self)
#         self.hi_there["text"] = "Hello World\n(click me)"
#         self.hi_there["command"] = self.say_hi
#         self.hi_there.pack(side="top")

#         self.quit = tk.Button(self, text="QUIT", fg="red",
#                               command=self.master.destroy)
#         self.quit.pack(side="bottom")

#     def say_hi(self):
#         print("hi there, everyone!")

# root = tk.Tk()
# app = IccGUI(master=root)
# app.mainloop()


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):

  icc_db = IccDB("icc")
  icc_db.add_temp_recipe()
  icc_db.add_temp_user_ing()
  icc_db.add_temp_ing_info()

  recommended_recipe = recommed_recipe()
  print("you should make {}".format(recommended_recipe))

  ing_info = icc_db.find_ing_infos()
  print(ing_info)

  # client = MongoClient()
  # db = client["icc"]
  # temp = db.user_ing.find({})
  # print(temp)
  return render_template('index.html', data=ing_info)


if __name__ == '__main__':
  app.run(port=5000)

# export FLASK_APP=main.py
# flask run

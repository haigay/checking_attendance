
import tkinter as tk
from define import *
import os
def input_name(entry):
    name = entry.get()
    create_face_folder(name)
    print("name:", name)  
def create_face_folder(name):
    folder = f'datasets/{name}'
    if not os.path.exists(folder):
        os.makedirs(folder)

root = tk.Tk()
root.title("Meow_Collector")
root.resizable(False, False)
        
root.geometry("{}x{}".format(WINDOW_WIDTH, WINDOW_HEIGHT))
root.iconbitmap(PATH_ICON_IMAGE)
root.config(background=BG_COLOR)

info = tk.Label(font="arial 15 bold italic", fg="red", background=BG_COLOR,
            text="Data collect !").grid(row=0, column=0, columnspan=3, padx=2, pady=20)

# Step 1: Input name and create folders for face
step1 = tk.Label(font="arial 13 italic", fg="blue", background=BG_COLOR,
             text="Step1: Input name and wait to take photos").grid(row=5, column=0, columnspan=2, 
                                                                    sticky=tk.W, padx=5, pady=10)

name_tl = tk.Label(font="arial 13", background=BG_COLOR,
                   text="Name").grid(row=6, column=0, sticky=tk.W, padx=5, pady=0)

entry = tk.Entry(root, font="arial 13")
entry.grid(row=6, column=1, sticky=tk.W, padx=0, pady=2)

button = tk.Button(root, font="arial 10", text="Submit", command=lambda: input_name(entry)).grid(row=6, column=2, padx=5)


root.mainloop()

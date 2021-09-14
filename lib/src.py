import tkinter as tk
from tkinter.simpledialog import askinteger
from tkinter import *
from PIL import ImageTk,Image 
import time
class gui():
     def __init__(self):
        self.root = Tk()
        self.root.title("Break Timer")
        ico = Image.open('lib/assets/timer.ico')
        photo = ImageTk.PhotoImage(ico)
        self.root.wm_iconphoto(False, photo)
        self.root.overrideredirect(True)
        self.root.overrideredirect(False)
        self.root.title("Break Timer")
        self.root.attributes('-fullscreen',True)
        self.root.configure(bg='#5C5C5C')
        Label = tk.Label(self.root, 
                          text = 'Rest your eyes. Stretch your legs. Breathe. Relax.',bg="#5C5C5C",fg="white",font=("Helvetica", 40)).pack(pady=5) 
        Label = tk.Label(self.root, 
                          text = "Time for a break!",bg="#5C5C5C",fg="white",font=("Courier", 10)).pack(pady=10) 
        
        button = tk.Button(self.root, 
                  text = 'Quit', bg="skyblue",fg="white",
                  command=quit).pack(pady=8)
        bg_canv = Canvas(self.root,width=500,height=600,bg="#5C5C5C",borderwidth=0,highlightthickness = 0)
        image  = ImageTk.PhotoImage(Image.open("lib/assets/img/no-bg-timer.png"))
        bg_canv.create_image(0,0,anchor=NW,image=image)
        bg_canv.pack()
        self.root.protocol("WM_DELETE_WINDOW", quit)
        self.root.mainloop()
        
     def quit():
         if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()


def job():
   gui()     
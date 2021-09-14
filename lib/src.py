import tkinter as tk
from tkinter.simpledialog import askinteger
from tkinter import *
from PIL import ImageTk,Image 
import time
root = tk.Tk()
class gui():
     def __init__(self):
        global root; 
        root.overrideredirect(True)
        root.overrideredirect(True)
        root.title("Break Timer")
        root.attributes('-fullscreen',True)
        root.configure(bg='white')
        Label = tk.Label(root, 
                          text = 'You Have To Break Some Time',bg="white",fg="Black",font=("Courier", 40)).pack(pady=5) 
        Label = tk.Label(root, 
                          text = "Once you get to that point when you can just be yourself and relax, I just think that you're so much happier in general.",bg="white",fg="Black",font=("Courier", 10)).pack(pady=10) 
        
        button = tk.Button(root, 
                  text = 'Quit', bg="skyblue",fg="white",
                  command=quit).pack(pady=8)
        bg_canv = Canvas(root,width=500,height=600,bg="white",border=0)
        image  = ImageTk.PhotoImage(Image.open("lib/assets/img/no-bg-timer.png"))
        bg_canv.create_image(0,0,anchor=NW,image=image)
        bg_canv.pack()
        root.mainloop()
        
     def getUptime():
        startTime = time.time()
        print(time.time() - startTime)

     def quit():
        root.destroy()


     
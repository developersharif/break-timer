import tkinter as tk
from tkinter.simpledialog import askinteger
import time
root = tk.Tk()
class gui():
     def __init__(self):
        global root; 
        root.overrideredirect(True)
        root.overrideredirect(False)
        root.title("Break Timer")
        root.attributes('-fullscreen',True)
        root.configure(bg='limegreen')
        Label = tk.Label(root, 
                          text = 'You Have To Break Some Time').pack(pady=10) 
        button = tk.Button(root, 
                  text = 'Quit', 
                  command=quit).pack(pady=8)
        root.mainloop()
        
     def getUptime():
        startTime = time.time()
        print(time.time() - startTime)

     def quit():
        root.destroy()


     
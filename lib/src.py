import tkinter as tk
from tkinter.simpledialog import askinteger
import time
root = tk.Tk()
class gui():
     def __init__(self):
        global root; 
        root.overrideredirect(True)
        root.overrideredirect(False)
        root.attributes('-fullscreen',True)
        root.configure(bg='limegreen')
        button = tk.Button(root, 
                          text = 'Click and Quit', 
                          command=quit).pack()
        Label = tk.Label(root, 
                          text = 'Relax sharif....').pack() 
        root.mainloop()
        
     def getUptime():
        startTime = time.time()
        print(time.time() - startTime)

     def quit():
        root.destroy()


     
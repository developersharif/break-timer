from lib.src import *
import schedule
import os
import time
#default value...
Hours = 2
Minutes = 10

#close windwo after setup the ask_time()
def close():
    root.destroy() 
    
#custom break time 
def ask_time():
     global Hours,Minutes
     Hours = askinteger("Input", "Break frequency: Set Hours")
     Minutes = askinteger("Input", "Break frequency: Set Minutes")
     tk.Button(root, 
                  text = 'Exit', bg="red",fg="white",
                  command=close).pack(pady=8)
     
 
root = tk.Tk()
root.title("Break Timer")
root.geometry("500x500")
     
ico = Image.open('lib/assets/timer.ico')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)
tk.Label(root,text="Default Break frequency {} Hours {} Minutes".format(Hours,Minutes)).pack(pady=9)
tk.Button(root, 
                  text = 'Custom time', bg="black",fg="white",
                  command=ask_time).pack(pady=8)
root.iconify()
root.mainloop()


wait =  (Hours * 3600) + (Minutes * 60) 

def job():
    os.system("python3 main.py")
 
   
print(wait)
schedule.every(wait).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
    
    
from lib.src import *
import schedule
import os
import time
#default value...
Hours = 2
Minutes = 10
Images= "lib/assets/img/nature_white.jpg"


class Home_page(Frame):

    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)

        self.image = Image.open(Images)
        self.img_copy= self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self,event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)
    
    def change_image(self, file):
        """Change background image of the window."""
        size = (self.winfo_width(), self.winfo_height())
        self.image = Image.open(file).resize(size)
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


def check_image(x=0):
    if x >= 100000: return # Break the loop
    if x == 500:
        e.change_image('lib/assets/img/nature_white.jpg')
    elif x == 5000:
        e.change_image('lib/assets/img/nature_white.jpg')
    root.after(1, check_image, x+1)
    
#close windwo after setup the ask_time()    
def close():
    root.destroy() 
    
#custom break time 
def ask_time():
     global Hours,Minutes
     Hours = askinteger("Input", "Break frequency: Set Hours")
     Minutes = askinteger("Input", "Break frequency: Set Minutes")
     
     
root = tk.Tk()
root.title("Break Timer")
root.geometry("500x500")
root.configure(bg="white")
ico = Image.open('lib/assets/timer.ico')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)
tk.Label(root,text="Default Break frequency {} Hours {} Minutes".format(Hours,Minutes),bg="white",fg="black",font=("Helvetica", 15)).pack(pady=9)
tk.Button(root, 
                  text = 'Set Timer', bg="black",fg="white",font=("Helvetica",10),
                  command=ask_time).pack(pady=8)

tk.Button(root, 
                  text = 'Exit', bg="red",fg="white",
                  command=close).pack(pady=8)
root.iconify()
e = Home_page(root)
e.pack(fill=BOTH, expand=YES)
check_image()

root.mainloop()

wait =  (Hours * 3600) + (Minutes * 60) 

def job():
    os.system("python3 main.py")
 
   
print(wait)
schedule.every(2).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
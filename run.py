from lib.src import *
root.title("Break Timer")
hrs = askinteger("Input", "Hours")
mint = askinteger("Input", "Minutes")
wait =  (hrs * 3600) + (mint * 60) 
while True:
     time.sleep(3)
     print("trigared")
     gui()
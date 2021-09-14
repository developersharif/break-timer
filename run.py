from lib.src import *
hrs = askinteger("Input", "Hours")
mint = askinteger("Input", "Minutes")
wait =  (hrs * 3600) + (mint * 60) 
while True:
     time.sleep(wait)
     print("trigared")
     gui()
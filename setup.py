import cx_Freeze
import sys
import os

build_exe_options = {"packages": ["os","PIL","time","schedule","playsound","webbrowser","tkinter"],"include_files":['lib','main.py']}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

cx_Freeze.setup(
    name = "Breake Timer",
    version = "0.1",
    description = "A simply python script which reminds you to take a break while working.",
    options = {"build_exe": build_exe_options},
    executables = [cx_Freeze.Executable("run.py", base=base,icon="lib/assets/timer.ico")]
)
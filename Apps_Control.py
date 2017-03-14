import Tkinter
import tkMessageBox
import sys
#Library to Call .sh file in Python Script
import subprocess

import os

#Top is the Master Frame of This Window
top = Tkinter.Tk()
top.resizable(width=True, height=True)
top.minsize(width=666, height=666)
	

#This is method to open Text Editor(gedit) App 
def buttonTextEditor():
	#subprocess.call("gedit.sh", shell=True)
	proc = subprocess.Popen(['gedit'])
	# Wait until first Process kill 
	#proc.wait()



#This is method to open Terminal App 
def buttonTerminal():
	
	#Find the Current Username and Change path to Home direcrtory
	str="/home/"+os.popen('whoami').read() 
	str=str[0:(len(str)-1)]
	os.chdir(str)
	proc = subprocess.Popen(['gnome-terminal'])

#This is method to open Camera App 
def buttonCamera():
	proc = subprocess.Popen(['cheese'])
	#proc.wait()

#This is method to open Exit App 
def buttonExit():
	sys.exit()


#This is method to open Setting App 
def buttonSetting():
	proc = subprocess.Popen(['unity-control-center'])

#This is method to open Calculator App
def buttonCalculator():
	proc = subprocess.Popen(['gnome-calculator'])


textEditor = Tkinter.Button(top, text ="Text Editor", command =buttonTextEditor)
terminal = Tkinter.Button(top, text ="Terminal", command = buttonTerminal)
camera = Tkinter.Button(top, text ="Camera", command = buttonCamera)
setting = Tkinter.Button(top, text ="Setting", command = buttonSetting)
calculator = Tkinter.Button(top, text ="Calculator", command = buttonCalculator)
exit = Tkinter.Button(top, text ="Exit", command = buttonExit)

textEditor.pack()
terminal.pack()
camera.pack()
setting.pack()
calculator.pack()
exit.pack()

	
top.mainloop()

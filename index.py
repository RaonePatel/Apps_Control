import os
#This method includes all the Package that required for Python GUI
commands = ['sudo apt-get install python-tk > /dev/null', 'sudo apt-get install python-imaging -t > /dev/null', 'sudo apt-get install python-pil > /dev/null','sudo apt-get install inkscape > /dev/null','clear']
count = 0
for com in commands:
	_=os.system(com)
	count += 1

import Tkinter
import tkMessageBox
import sys
#Library to Call .sh file in Python Script
import subprocess

from os.path import basename

#top.iconbitmap('favicon.ico')


#Top is the Master Frame of This Window
top = Tkinter.Tk()
#top('Akshar')
top.resizable(width=False, height=False)

#frame1 = Tkinter.Frame(top)
#frame1.pack(side=Tkinter.TOP, fill=Tkinter.X)

def Convert():
	j=[];

	str3="/tmp"
	os.chdir(str3)
	if not(os.path.isdir('./Apps_Control_img')):
		proc=subprocess.Popen(["mkdir","Apps_Control_img"])

	l=["accessories-calculator.svg","accessories-text-editor.svg","system-upgrade.svg","calendar.svg","xfsm-shutdown.svg" , "bash.svg","applets-screenshooter.svg"]
	for i in l:
		a=basename(i)	
		CopyTo(a);
		str4="/tmp/Apps_Control_img/"
		os.chdir(str4)
		j=os.path.splitext(a)[0]+".png"
		#proc2 = subprocess.call(["clear"])		
		proc =  subprocess.call(["inkscape","-z", i ,"-e" , j])
		proc1 = subprocess.call(["clear"])
		#This is all Process
#		proc3 = subprocess.call(["clear"])
#		proc4 = subprocess.call(["clear"])
#		proc5 = subprocess.call(["clear"])
#		proc6 = subprocess.call(["clear"])
#		proc7 = subprocess.call(["clear"])
#		proc8 = subprocess.call(["clear"])
#		proc9 = subprocess.call(["clear"])
#		proc10 = subprocess.call(["clear"])

def CopyTo(fname):
	#print fname
	src="/usr/share/icons/Humanity/apps/48/" + fname
	dest="/tmp/Apps_Control_img/" + fname
	proc=subprocess.call(["cp",src,dest])
	
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

#This is method to open Setting App 
def buttonSetting():
	proc = subprocess.Popen(['unity-control-center'])

#This is method to open Calculator App
def buttonCalculator():
	proc = subprocess.Popen(['gnome-calculator'])

#This is method to open Calculator App
def buttonCalendar():
	proc = subprocess.Popen(['gnome-calendar'])

#This is method to open Home App
#def buttonHome():
#	proc = os.fork()
#	proc.subprocess.Popen(['gnome-nautilus'])


#This is method to open Exit App 
def buttonExit():
	sys.exit()

#This is method to open Shutdown App 
def buttonShutdown():
	tkMessageBox.showinfo("Bye Bye... See you Soon... !!!")
	proc = subprocess.call(["shutdown","now"])



Convert()
#path="/usr/share/icons/hicolor/48x48/apps"
path="/tmp/Apps_Control_img/"
texteditorimg = Tkinter.PhotoImage(file=path+"accessories-text-editor.png")
terminalimg = Tkinter.PhotoImage(file=path+"bash.png")
cameraimg = Tkinter.PhotoImage(file=path+"applets-screenshooter.png")
settingsimg = Tkinter.PhotoImage(file=path+"system-upgrade.png")
calculatorimg = Tkinter.PhotoImage(file=path+"accessories-calculator.png")
calendarimg = Tkinter.PhotoImage(file=path+"calendar.png")
shutdownimg = Tkinter.PhotoImage(file=path+"xfsm-shutdown.png")
#To create a frame for writing text in button
frame1 = Tkinter.Frame(top)
frame1.pack()


#installpackages = Tkinter.Button(top, text ="Install Packages", command =installPackages)
textEditor = Tkinter.Button(frame1,compound=Tkinter.TOP,width=100,height=100,image=texteditorimg,text ="Text Editor", command =buttonTextEditor)
terminal = Tkinter.Button(frame1,compound=Tkinter.TOP,width=100,height=100,image=terminalimg,text ="Terminal", command = buttonTerminal)
camera = Tkinter.Button(frame1,compound=Tkinter.TOP,width=100,height=100,image=cameraimg,text ="Camera", command = buttonCamera)
setting = Tkinter.Button(frame1,compound=Tkinter.TOP,width=100,height=100,image=settingsimg,text ="Setting", command = buttonSetting)
calculator = Tkinter.Button(frame1,compound=Tkinter.TOP,width=100,height=100,image=calculatorimg, text ="Calculator", command = buttonCalculator)
calendar = Tkinter.Button(frame1,compound=Tkinter.TOP,width=100,height=100,image=calendarimg,text ="Calendar", command = buttonCalendar)
#home = Tkinter.Button(top, text ="Home", command = buttonHome)
exit = Tkinter.Button(top, text ="Exit", command = buttonExit)
shutdown = Tkinter.Button(frame1,compound=Tkinter.TOP,width=100,height=100,image=shutdownimg, text ="Shutdown", command = buttonShutdown)

#installpackages.pack()
shutdown.place(x=70,y=70)
shutdown.pack(side=Tkinter.RIGHT,padx=2,pady=2)

textEditor.place(x=10,y=10)
textEditor.pack(side=Tkinter.RIGHT,padx=2,pady=2)

terminal.place(x=20,y=20)
terminal.pack(side=Tkinter.RIGHT,padx=2,pady=2)

setting.place(x=40,y=40)
setting.pack(side=Tkinter.RIGHT,padx=2,pady=2)

calculator.place(x=50,y=50)
calculator.pack(side=Tkinter.RIGHT,padx=2,pady=2)

calendar.place(x=60,y=60)
calendar.pack(side=Tkinter.RIGHT,padx=2,pady=2)

camera.place(x=30,y=30)
camera.pack(side=Tkinter.RIGHT,padx=2,pady=2)
#home.pack()

exit.pack()


	
top.mainloop()

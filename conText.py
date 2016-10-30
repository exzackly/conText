from tkinter import *
from tkinter.filedialog import askopenfilename
import re
import webbrowser
import xml_parser as xp

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500

root = Tk()
root.wm_title("conText by EXZACKLY and ZENO")
root.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)

def getFile():
	filename = askopenfilename()
	name = re.search("/.*/(.*?)\.htm", filename).group(1)
	xp.extract_messages(filename, "{0}.txt".format(name), name)

def exitProgram():
	root.destroy()

def displayHelp():
	webbrowser.open("https://github.com/exzackly/conText", new=2)

def displayResults(percent):
	toplevel = Toplevel()
	label = Label(toplevel, text="test {0} percent".format(percent), height=0, width=50)
	label.pack()
	toplevel.focus()
	
#create menu
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open...", command=getFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exitProgram)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Documentation...", command=displayHelp)

#create header label
headerLabel = Label(root, text="Enter Text To Compare:", font=("Helvetica", 21))
headerLabel.pack()
headerLabel.place(bordermode=OUTSIDE, x = 30, y = 15)

#create textarea
textarea = Text(root, height = 20, width = 54)
textarea.pack()
textarea.place(bordermode=OUTSIDE, x = 30, y = 50)

#create compare button
compareButton = Button(root, text="Compare Text", command=lambda: displayResults(21))
compareButton.pack()
compareButton.place(bordermode=OUTSIDE, x = 200, y = 390)

#create result label
resultLabel = Label(root, text="Text is 21% similar", font=("Helvetica", 21))
resultLabel.pack()
resultLabel.place(bordermode=OUTSIDE, x = 30, y = 420)

root.mainloop()
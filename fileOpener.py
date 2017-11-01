from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

def fileOpener():
	root = Tk()
	root.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select LogicMonitor Report",filetypes = (("CSV files","*.csv"),("all files","*.*")))
	return root.filename
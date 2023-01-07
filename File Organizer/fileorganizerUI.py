import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox
from tkinter import *
import os
import shutil


def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)

def print_path(folder_path):
	if len(folder_path.get()) == 0:
		tkinter.messagebox.showerror(title="Error!", message="Insert folder path!")
	else:
		try:
			path = folder_path.get()
			files = os.listdir(path) #listing all the files in the directory

			for file in files:
				filename, extension = os.path.splitext(file) #splitting the filename and extension
				extension = extension[1:] #getting only the extension by slicing
				print(folder_path.get())
				if os.path.exists(path+'/'+extension.upper()): #if the extension directory is already exist
					shutil.move(path+'/'+file, path+'/'+extension+'/'+file) #it will move it to that directory
				else:
					os.makedirs(path+'/'+extension.upper()) #making new directory
					shutil.move(path+'/'+file, path+'/'+extension+'/'+file) #it will move it to that directory
			tk.messagebox.showinfo(title="Success!", message="Files Organized!")
			root.destroy()
		except:
			tkinter.messagebox.showerror(title="Error!", message="Files can't organize!")

root = Tk()
root.iconbitmap("icon.ico")
root.title('File Organizer')
root.geometry('300x65')
root.resizable(0, 0)
root.config(bg='#F2B33D')
root.eval('tk::PlaceWindow . center')


root.columnconfigure(0, weight=3)
root.columnconfigure(1, weight=3)

folder_path = StringVar()
lbl1 = Entry(master=root,textvariable=folder_path)
lbl1.grid(row=0, column=0, columnspan=4, sticky=N+S+W+E, padx=5, pady=5)

button2 = Button(text="Browse", command=browse_button)
button2.grid(column=0, row=2, columnspan=1, sticky=N+S+W+E, padx=5, pady=5)

button3 = Button(text="Organize", command=lambda: print_path(folder_path))
button3.grid(column=1, row=2, columnspan=3, sticky=N+S+W+E, padx=5, pady=5) 

root.grid_columnconfigure(0, weight=2)
root.grid_columnconfigure(1, weight=4)
mainloop()
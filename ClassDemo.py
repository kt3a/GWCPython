from tkinter import*
from tkinter import Button

#define the quit function
def set_quit():
   top.destroy()
    

#Layout
top = tkinter.Tk()
top.geometry("300x300")

#label
label = tkinter.Label(top, text = "Hello World!")
top.title("First GUI")
label.pack()

#button
qbutton = tkinter.Button(top, text = "Quit", command = set_quit)
qbutton.pack()

#cButton = tkinter.Button(self.window,text = "Change",command=self.change_paint)
top.mainloop()


 

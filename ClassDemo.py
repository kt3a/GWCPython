import tkinter
from tkinter import Button

#define the quit function
def set_quit():
   top.destroy()
    
#to show text
def show_text():
   message.insert(0,e.get())


#Layout
top = tkinter.Tk()
top.geometry("300x300")

#label
label = tkinter.Label(top, text = "Hello World!")
top.title("First GUI")
label.pack()



#Entry Widget
e = tkinter.Entry(top)
e.pack()

#string_input = e.get()
text = tkinter.Label(top, text = "Answer:").pack()

#make a box to display the message
message = tkinter.Entry(top)
message.pack()

#make a button that will display the message when pushed
ans = tkinter.Button(top, text = "Show Message", command = show_text)
ans.pack()


#button
qbutton = tkinter.Button(top, text = "Quit", command = set_quit)
qbutton.pack()

#cButton = tkinter.Button(self.window,text = "Change",command=self.change_paint)
top.mainloop()


 

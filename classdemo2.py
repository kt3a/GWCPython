from tkinter import *

def show_text():
  box.insert(0,text_field.get())

def end_prog():
  top.destroy()
  
top = Tk()
top.geometry("500x500")
top.title("text input")


label1 = Label(top, text = "Give me a message")
label1.pack()


#entry widget
text_field = Entry(top)
text_field.pack()


message  = Button(top, text = "Show Message", command = show_text)
message.pack()

label2 = Label(top,text = "Answer")
label2.pack()

box = Entry(top)
box.pack()

quit = Button(top, text = "Quit", command = end_prog)
quit.pack()

top.mainloop()

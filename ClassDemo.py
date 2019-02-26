import tkinter
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


#here is the problem from today, uncomment the bottom line to run the converter
class Convert():
    #create a window
    def __init__(self):
        self.top = Tk()
        self.top.title('Conversion Calculator')
        self.top.geometry('300x100')

        #define the next method in first init
        self.defineWidgets()
        
        self.top.mainloop()

    def defineWidgets(self):
        self.weightKg = StringVar()
        self.entry = Entry(self.top,textvariable = self.weightKg, width = 10)
        self.entry.grid(row=1,column=2)
        
        self.label1 = Label(self.top, text = 'Kgs')
        self.label1.grid(row = 1,column = 3)

        self.label2 = Label(self.top, text = 'is equal to')
        self.label2.grid(row = 2,column = 1)

        self.label3 = Label(self.top)
        self.label3.grid(row = 2,column = 2)

        self.label4 = Label(self.top, text = 'LBS')
        self.label4.grid(row = 2,column = 3)

        self.button = Button(self.top, text = 'calculate', command = self.calc)
        self.button.grid(row = 3, column = 2)

    def calc(self):
        try:
            weightLbs = 2.20462*float(self.weightKg.get())
            self.label3.config(text = weightLbs)
        except ValueError:
            pass

#c = Convert()
 

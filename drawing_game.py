from turtle import *
from tkinter import *


window = Tk()
window.title("Draw!")
cv = Canvas(window,width=600,height=600)
cv.pack(side = LEFT)



t = RawTurtle(cv)
t.color("blue")
screen = t.getscreen()


screen.setworldcoordinates(0,0,600,600)
screen.bgcolor("white")


# A frame is an invisible widget that holds other widgets. 
   # on the right hand side of the window and holds the buttons and Entry widgets.
frame = Frame(window)
frame.pack(side = RIGHT,fill=BOTH)


pointLabel = Label(frame,text="Width")
pointLabel.pack()

#------------------------------------------------------------------------------------------------------
##add color change buttons here or more lables 





# This entry widget allows the user to pick a width for their lines. 
# With the pointSize variable below you can write pointSize.get() to to 
# the contents of the entry widget and pointSize.set(val) to set the value
# of the entry widget to val. Initially the pointSize is set to 1. str(1) is needed because
# the entry widget must be given a string.
pointSize = StringVar()
pointEntry = Entry(frame,textvariable=pointSize)
pointEntry.pack()
pointSize.set(str(1))


# This is an event handler. Handling the quit button press results in destroying the window
# and quitting the application. 
def quitHandler():
    window.destroy()
    window.quit() 
      
   # This is how a button is created in the frame. The quitHandler is the event handler for button
   # presses of the "Quit" button.
quitButton = Button(frame, text = "Quit", command=quitHandler)
quitButton.pack()
   
   # Here is another event handler. This one handles mouse clicks on the screen.
def clickHandler(x,y): 
    # When a mouse click occurs, get the pointSize entry value and set the width of the 
    # turtle called "t" to the pointSize value. The int(pointSize.get()) is needed because
    # the width is an integer, but the entry widget stores it as a string.
    t.width(int(pointSize.get()))
    t.goto(x,y)
      
# Here is how we tie the clickHandler to mouse clicks.
screen.onclick(clickHandler)
   
# Finally, this code is last. It tells the application to enter its event processing loop
# so the application will respond to events. 
tkinter.mainloop()



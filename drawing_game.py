from turtle import *
from tkinter import *

##This creates the window 
window = Tk()
window.title("Drawing Game")                 ##change the title if you'd like

##the canvas widget allows us to place a turtle drawing onto our tkinter gui
cv = Canvas(window,width=600,height=600)
cv.pack(side = LEFT)

#RawTurtle instead of regular Turtle() (as we used in our demo) allows for adding a
##section called a turtle screen  -- this we place onto the canvas widget so we can draw 
t = RawTurtle(cv)
t.color("pink")             ##try adding and changing colors
screen = t.getscreen()

##this sets the coordinates of where the turtle drawing pen will start on the screen
##try changing the coordinates to move where you want the drawing to start
screen.setworldcoordinates(0,0,600,600)
screen.bgcolor("white")             ##try changing the color of your drawing screen


# A frame is an invisible widget that holds other widgets. 
   # on the right hand side of the window and holds the buttons and Entry widgets.
frame = Frame(window)
frame.pack(side = RIGHT,fill=BOTH)

##A text label to show what the text field is for
pointLabel = Label(frame,text="Choose Thickness of the Pen!")
pointLabel.pack()



# This entry widget allows the user to pick a width for their lines. 
# With the pointSize variable below you can write pointSize.get() to to 
# the contents of the entry widget and pointSize.set(val) to set the value
# of the entry widget to val. Initially the pointSize is set to 1. str(1) is needed because
# the entry widget must be given a string.
pointSize = StringVar()
pointEntry = Entry(frame,textvariable=pointSize)
pointEntry.pack()
pointSize.set(str(1))

#------------------------------------------------------------------------------------------------------
##try to make this code your own by adding buttons that could change the color of the pen
##here and below
##Try to make more lables or other functionality!! Have fun with this!










##This function allows you to quit the gui 
def quitHandler():
    window.destroy()
    window.quit() 

##this is the button you press to use the quitHandler function defined above
quitButton = Button(frame, text = "Quit", command=quitHandler)
quitButton.pack()
   
# Here is another event handler. This one handles mouse clicks on the screen.
def clickHandler(x,y): 
    # When a mouse click occurs, get the pointSize entry value and set the width of the 
    # turtle called "t" to the pointSize value. The int(pointSize.get()) is needed because
    # the width is an integer, but the entry widget stores it as a string.
    t.width(int(pointSize.get()))
    t.goto(x,y)

      
#This calls the clickHandler function and connects the function to mouse clicks
screen.onclick(clickHandler)
   
#This statement ends the gui code 
tkinter.mainloop()



from tkinter import *
from turtle import *
import random


##This is the shell for writing the hangman game. For this code you will need:
##to write the function for the quit button and add the quitt button to the bottom of the page (see below)
##you will create two turtle drawings that appear on screen when you either win or loose the game

##you will need to write in the hangman game logic located in the game() function
    ##you must display the hangman loosing picture if the person guesses wrong
    ##else if the person guesses the word correctly you display the wining picture




##you're encouraged to add more buttons, labels, colors, and features to this gui!!! make it your own!



#----------------------------------------------------------------------------------------------------------------------------------
####FINISH THIS QUIT FUNCTION#######
def end():
    ##this function will close the window, make sure you use the tkinter window variable

#----------------------------------------------------------------------------------------------------------------------------------    




##this is a list of words that the game() function will randomly select from
    ##you can change the words in your list if you'd like
word_list = ['college','awake','python','limes','lemons','puppy','whale','apple','germs','rabbits','uncertainty','parable','beach','doors','antacid','supplant','movie','paradox','never','ending','abyss','tortilla','student','science','grandpa']

##this line chooses a word from the word_list at random and stores it to the answer variable
answer = random.choice(word_list)

##this code scrambles the word so you can print a hint in the gui of the scrambled word
display = list(answer)          ##turned the string into a list first
shuffle(display)                ##the shuffle function shuffles the letters of the list
''.join(display)                ##this statement turns the list back into a string





#create window 
wind = Tk()
wind.title("Hangman")

##the canvas allows you to add the turtle feature to your tkinter gui 
w = Canvas(wind,width = 500, height = 500)
w.pack(side = LEFT)


#create drawing area
t = RawTurtle(w)                                    #this creates a turtle canvas area onto the tkinter gui it is called RawTurtle instead of just Turtle() like in other code we did
screen = t.getscreen()
screen.setworldcoordinates(-270,-270,300,300)
screen.bgcolor("white")                             #you can change the color if you'd like!!          




#----------------------------------------------------------------------------------------------------------------------------------
#####USE TURTLE TO DRAW WHAT WILL HAPPEN WHEN YOU LOOSE THE GAME#####
def draw_man():
    ##add more to this 
    t.circle(50)
    t.right(90)
    t.forward(200)
    t.right(45)
    t.forward(100)
    t.right(180)
    t.forward(100)
    t.right(100)
    t.forward(100)
    t.right(180)
    t.forward(100)
    t.right(35)
    t.forward(120)
    t.right(90)
    t.forward(30)
    t.right(180)
    t.forward(60)
    
   
########USE TURTLE TO DRAW WHAT WILL HAPPEN WHEN YOU WIN THE GAME -- BE CREATIVE!#####
def win():
    ##code here
    


#----------------------------------------------------------------------------------------------------------------------------------






##this creates a frame: or a section to the left of your window that will contain all the labels, buttons and text fields   
frame = Frame(wind, bg = 'cyan', width = 450,height = 600)          ##you may and should play around with colors or sizes 
frame.pack(side = RIGHT, fill = BOTH)

##this shows the text "Guess the word!"
label2 = Label(frame, text = "Guess the Word!")
label2.pack()

##This label provides instructions 
instruct = Label(frame, text = "The word to guess is scrambled as:")
instruct.pack()

##this label shows a scrambled version of the answer         
hint = Label(frame, text = display)
hint.pack()



#----------------------------------------------------------------------------------------------------------------------------------
##put a text box here where you type an answer
##name the variable text1
text1 =         ##write here
                ##need a statement here to add the text box to the frame


#----------------------------------------------------------------------------------------------------------------------------------



##this function places the answer into the second text box
def show_answer():
    ans.insert(0,answer)
    
label3 = Label(frame, text = "\n\n\nAnswer appears here:")
label3.pack()

######This is the text box that displays the correct word after the picture is drawn
###this code is taken care of so you don't have to worry about that
ans = Entry(frame)
ans.pack()






#----------------------------------------------------------------------------------------------------------------------------------
def game():
    text = text1.get()
    #print(text)    use for testing purposes
    attempt = 1
    while attempt < 2:
        result = ""

        ###complete the logic 
        if text ##something answer:
            draw_man()
            
        if text ##something else answer:
            win()
        attempt += 1
        show_answer()

    

#----------------------------------------------------------------------------------------------------------------------------------

#this is the start of game guess button, it is programmed for you
gbutton = Button(frame, text = "Guess", command = lambda: game())
gbutton.pack()





#----------------------------------------------------------------------------------------------------------------------------------
##Write the quit button down here, the name of the variable is written for you: quitt
##you need two lines of code

quitt = ##code here


#----------------------------------------------------------------------------------------------------------------------------------


wind.mainloop()
##end of program


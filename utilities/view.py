"""
In this file store the app views.
"""
from tkinter import *
from tkinter import ttk
from tkinter import font 
import utilities.logic_game as lg
import utilities.win as win

# This variable it´s firts on all TK apps, it´s necesary to initialize de app,
# is the main box for the elements of our app.
rock_paper_scissor = Tk()

# This variable give the width and height of our app. Size in pixels
rock_paper_scissor.geometry("720x560")

# This sentence store the name that we want to give to our app, and show it on the window.
rock_paper_scissor.title("Rock Paper Scissor Game")

# Create a Label for show the Title of the app
Label(rock_paper_scissor, # this indicate the location of th label
      text = "Rock Paper Scissor", # with text var we can give a name to our app 
      font = "normal 20 bold", # choose the font type, size and format
      fg = "blue").pack(pady= 20) # fg set the color of the font, and pady situate the label on
                                  # y axis

# create a new box, inside of the main box to organize our app
frame = Frame(rock_paper_scissor)
# with this choose the format that we use to organize the elements inside of the box
# i choose pack form (is the most easy), but you can use place or grid.
frame.pack()

# Create a texts labels for show the info to the player, l1, l2 & l3
l1 = Label(frame, # you can see that in this case labels are on frame box, not in main box
            text = "Player",
            font = 10)

l2 = Label(frame,
           text = "VS",
           font = "normal 10 bold")

l3 = Label(frame, 
           text = "Computer",
           font = 10)

# with this methods we can move the labels acroos the frame box
l1.pack(side = LEFT, padx = 20) 
# side indicate that we want to put the label on the left of screen, and padx the distance to the x axis
l2.pack(side = LEFT, padx = 20) 
# is the same case but here the padx is the distance of this label to the label after that
l3.pack()

# in this label we store the result of the match, because that the text value are empty
l4 = Label(rock_paper_scissor,
           text = "",
           font = "normal 20 bold",
           bg = "white", # we give a background color 
           width = 15,
           borderwidth = 2, # we give a border
           relief = "solid")

l4.pack(pady= 20)

# create a new box inside the main box to put on that the buttons, it´s situate inmediatly before of the box "frame"
frame1 = Frame(rock_paper_scissor)
frame1.pack()

# create the buttons for choose the game options.
b1 = Button(frame1, # with this indicate where we want put the button
            text = "Rock", # In this var we store the text that we want to show on our button
            font = 10, # The size and options for the font
            width = 7, # The width for our button
            command = lg.rock) # this indicate th script that we use when push the button

b2 = Button(frame1,
             text = "Paper",
             font = 10,
             width = 7,
             command = lg.paper)

b3 = Button(frame1,
            text = "Scissor",
            font = 10,
            width = 7,
            command = lg.scissor)


b1.pack(side = LEFT, pady = 10)
b2.pack(side = LEFT, pady = 10)
b3.pack(pady = 10)

# Another button to reset the game on a match
reset_game_button = Button(rock_paper_scissor, 
       text = "Reset Game",
       font = 10,
       fg = "red",
       bg = "black",
       command = win.reset_game).pack(pady = 20)

# Another box for store the score of the match
frame2 = Frame(rock_paper_scissor)
frame2.pack()
frame3 = Frame(rock_paper_scissor)
frame3.pack()
player_label = Label(frame2,
                     text = "Player Score",
                     font= 15)
computer_label = Label(frame3,
                       text= "Computer Score",
                       font= 15)
player_label.pack(side= LEFT, padx = 10)
computer_label.pack(side=LEFT, padx= 10)
player_score = Label(frame2,
                     text= 0,
                     font= 20,
                     bg = "white",
                     width= 15,
                     borderwidth=2,
                     relief= "solid")
computer_score = Label(frame3,
                     text= 0,
                     font= 20,
                     bg = "white",
                     width= 15,
                     borderwidth=2,
                     relief= "solid")
player_score.pack(padx = 10, pady = 40)
computer_score.pack(padx = 0, pady = 40)

# Other box to show a message when the match are finised and show the Winner
frame4 = Frame(rock_paper_scissor)
frame4.pack()

win_message = Label(frame4,
                    text = "",
                    fg = "green")
win_message.pack()

# Another button to reset the Match
reset_match_button = Button(rock_paper_scissor, 
       text = "Reset Match",
       font = 10,
       fg = "red",
       bg = "black",
       command = win.reset_match).pack(pady = 20)
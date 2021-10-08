"""
This file manage all the logic of the game
"""
import random
import utilities.view as view
import utilities.win as win

# create a dictionary to store the values that the computer use in the game
computer_ia = {
    "0":"Rock",
    "1":"Paper",
    "2":"Scissor"
}
# global variables to store the values of player and computer score and match result
player_score = 0
computer_score = 0
match_result = ""

def rock():
    """ Check the logic of the game when we push the "Rock" button on the app.
    
    Parameters
    ----------
        The value of th Rock button.
        The choice of the computer
        The player_score variable
        The computer_score variable
    
    Returns
    -------
        The comparison from the player choice and computer choice.
        And actualice the value of the player_score and computer_score.
    
    """
    # use global to can use and change the value of the variables inside the function
    global player_score
    global computer_score
    # create a variable to store the computer choice
    c_ia = computer_ia[str(random.randint(0,2))]
    
    # Compare the choice of player and computer to determine the winner
    if c_ia == "Rock":
        match_result = "Draw"
    elif c_ia == "Scissor":
        match_result = "Player Win"
    else:
        match_result = "Computer Win" 
      
    # Actualice the values of the labels to show it on the app  
    view.l4.config(text = match_result)
    view.l1.config(text= "Rock")
    view.l3.config(text= c_ia)
    
    # Actualice of the player_score and computer_score with the result of the match
    if match_result == "Player Win":
        player_score += 1
        view.player_score.config(text = player_score)
    elif match_result == "Computer Win":
        computer_score += 1
        view.computer_score.config(text = computer_score)
    else:
        pass
    
    # calls this functions to check if we have a winner in the match and disable the buttons
    # to avoid the player to break the app
    win.button_disable()
    win.win_condition()

def paper():
    """ Check the logic of the game when we push the "Paper" button on the app.
    
    Parameters
    ----------
        The value of th Paper button.
        The choice of the computer
        The player_score variable
        The computer_score variable
    
    Returns
    -------
        The comparison from the player choice and computer choice.
        And actualice the value of the player_score and computer_score.
    
    
    """
    # use global to can use and change the value of the variables inside the function
    global player_score
    global computer_score
    # create a variable to store the computer choice
    c_ia = computer_ia[str(random.randint(0,2))]
    
    # Compare the choice of player and computer to determine the winner
    if c_ia == "Paper":
        match_result = "Draw"
    elif c_ia == "Scissor":
        match_result = "Computer Win"
    else:
        match_result = "Player Win"
    
    # Actualice the values of the labels to show it on the app    
    view.l4.config(text = match_result)
    view.l1.config(text= "Paper")
    view.l3.config(text= c_ia)
    
    # Actualice of the player_score and computer_score with the result of the match
    if match_result == "Player Win":
        player_score += 1
        view.player_score.config(text = player_score)
    elif match_result == "Computer Win":
        computer_score += 1
        view.computer_score.config(text = computer_score)
    else:
        pass
    
    # calls this functions to check if we have a winner in the match and disable the buttons
    # to avoid the player to break the app
    win.button_disable()
    win.win_condition()
    
def scissor():
    """ Check the logic of the game when we push the "Scissor" button on the app.
    
    Parameters
    ----------
        The value of th Scissor button.
        The choice of the computer
        The player_score variable
        The computer_score variable
    
    Returns
    -------
        The comparison from the player choice and computer choice.
        And actualice the value of the player_score and computer_score.
    
    """
    # use global to can use and change the value of the variables inside the function
    global player_score
    global computer_score
    # create a variable to store the computer choice
    c_ia = computer_ia[str(random.randint(0,2))]
    
    # Compare the choice of player and computer to determine the winner
    if c_ia == "Scissor":
        match_result = "Draw"
    elif c_ia == "Rock":
        match_result = "Computer Win"
    else:
        match_result = "Player Win"
    
    # Actualice the values of the labels to show it on the app  
    view.l4.config(text = match_result)
    view.l1.config(text= "Scissor")
    view.l3.config(text= c_ia)
    
    # Actualice of the player_score and computer_score with the result of the match
    if match_result == "Player Win":
        player_score += 1
        view.player_score.config(text = player_score)
    elif match_result == "Computer Win":
        computer_score += 1
        view.computer_score.config(text = computer_score)
    else:
        pass
    
    # calls this functions to check if we have a winner in the match and disable the buttons
    # to avoid the player to break the app
    win.button_disable()
    win.win_condition()


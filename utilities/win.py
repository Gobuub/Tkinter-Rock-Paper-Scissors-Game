"""
In this file i store the conditions to check the final result of the match,
and functions of reset the game and the match.
"""
import utilities.view as view
import utilities.logic_game as lg


def win_condition():
    """ Determine the winner of the match.
    
    The function check the value of computer_score and player_score and returns
    the winner of the match
    
    Parameters
    ----------
        computer_score value from logic_game file
        player_score value from logic_game file
    
    Return
    ------
        The winner of the match, and show it in the app, in the label that we create for that.
    
    """
    # this sentence indicate from lg (logic_game) take the value of this variable and check
    if lg.computer_score == 2:
        view.win_message.config(text = "COMPUTER WINS")
    elif lg.player_score == 2:
        view.win_message.config(text = "PLAYER WINS")
    else:
        pass

def reset_game():
    """ Reset the game stats.
    
    We use this function to reset the game stats.
    
    Parameters
    ----------
        Value of the buttons and labels
        
    Return
    ------
        Restore the value of the buttons and labels, to it initial state
        
    """
    view.b1["state"] = "active"
    view.b2["state"] = "active"
    view.b3["state"] = "active"
    view.l1.config(text= "Player")
    view.l3.config(text= "Computer")
    view.l4.config(text="")

def button_disable():
    """ Take the state of the buttons and disable it.
    
    This function disable all the buttons to avoid the user to choose another 
    choice and create a problem in the program.
    
    Parameters
    ----------
        The all buttons that we want to change to disable.
        
    Return
    ------
        Change the state to disable to the buttons that we indicate on it.
    """
    view.b1["state"] = "disable"
    view.b2["state"] = "disable"
    view.b3["state"] = "disable"
    
def reset_match():
    """ Restore the values of the Match.
    
    This function put all the values of the app to it initial value.
    
    Parameters
    ----------
        All the elements of the app that we want to be restored.
    
    Return
    ------
        Change the value of all parameters that we indicate to it inital value.
    
    """
    
    view.b1["state"] = "active"
    view.b2["state"] = "active"
    view.b3["state"] = "active"
    view.l1.config(text= "Player")
    view.l3.config(text= "Computer")
    view.l4.config(text="")
    view.player_score.config(text = 0)
    lg.player_score = 0
    view.computer_score.config(text = 0)
    lg.computer_score = 0
    view.win_message.config(text = "") 

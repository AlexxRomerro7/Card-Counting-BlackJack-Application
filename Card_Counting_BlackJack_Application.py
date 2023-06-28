# Alex Romero
# Created on 6/28/2023

# Import Random for the random selection of cards when dealing. Import TKinter for GUI
import random
from tkinter import *

def introduction_page():
    """This is the initial function that will be called upon to initialize the application through tkinter."""
    pass

def tutorial_page():
    """Switches the introduction page to the tuturial page in which Card Counting instructions are given."""
   pass

def game_page():
    """Switches to main game page where the user will be actively playing BlackJack."""
   pass

def hint_button():
    """Button that displays the current count value of the deck."""
   pass

def tutorial_button():
    """Button that gives brief tutorial on card counting, readily available for the user at all times."""
   pass

def create_deck():
    """Gives the user a new deck, should be called upon in any function where cards are dealt."""
   pass

def card_values():
    """Assigns values to all cards that are dealt out."""
   pass

def card_faces():
    """Assigns card faces to each card dealt."""
   pass

def face_down_card():
    """Runs code for the Dealer's faced down card"""
   pass

def place_bets():
    """Locks user into placing a bet without access to any other buttons without a bet."""
   pass

def bet_change():
    """Changes display of how much the user has bet upon final bet."""
   pass

def money_change():
    """Changes display of money left."""
   pass

def bet1():
    """Increases bet value by $1."""
   pass

def bet5():
    """Increases bet value by $5."""
   pass

def bet10():
    """Increase bet value by $10."""
   pass

def bet25():
    """Increase bet value by $25."""
   pass

def bet100():
    """Increase bet value by $100."""
   pass

def deal_cards():
    """Initiates game play by dealing 2 card to each player. 1 dealer card face down."""
   pass

def stand():
    """User choice of no longer receiving cards, initializing dealer play and halting all player buttons."""
   pass

def player_hit():
    """Gives the user one more card."""
   pass

def dealer_hit():
    """Allows dealer to hit IF the dealer respective value is less than 17."""
   pass

def busted():
    """Checks for both Player and Dealer bust upon Stand or Hit"""
   pass

def blackjack():
    """Checks for Blackjack for both the Player and Dealer"""
   pass

def winner():
    """Checks for who won the game if Blackjack isn't achieved by Player or Dealer"""
   pass

def dealer_card_reveal():
    """Displays the turned over Dealer card as its respective card"""
   pass

def game_results():
    """Gives a pop up window showing game results"""
   pass

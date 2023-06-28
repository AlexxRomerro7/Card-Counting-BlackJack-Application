# Alex Romero
# Created on 6/28/2023

# Import Random for the random selection of cards when dealing. Import TKinter for GUI
import random
from tkinter import *

def introduction_page():
    """This is the initial function that will be called upon to initialize the application through tkinter."""

def tutorial_page():
    """Switches the introduction page to the tuturial page in which Card Counting instructions are given."""

def game_page():
    """Switches to main game page where the user will be actively playing BlackJack."""

def hint_button():
    """Button that displays the current count value of the deck."""

def tutorial_button():
    """Button that gives brief tutorial on card counting, readily available for the user at all times."""

def create_deck():
    """Gives the user a new deck, should be called upon in any function where cards are dealt."""

def card_values():
    """Assigns values to all cards that are dealt out."""

def card_faces():
    """Assigns card faces to each card dealt."""

def face_down_card():
    """Runs code for the Dealer's faced down card"""

def place_bets():
    """Locks user into placing a bet without access to any other buttons without a bet."""

def bet_change():
    """Changes display of how much the user has bet upon final bet."""

def money_change():
    """Changes display of money left."""

def bet1():
    """Increases bet value by $1."""

def bet5():
    """Increases bet value by $5."""

def bet10():
    """Increase bet value by $10."""

def bet25():
    """Increase bet value by $25."""

def bet100():
    """Increase bet value by $100."""

def deal_cards():
    """Initiates game play by dealing 2 card to each player. 1 dealer card face down."""

def stand():
    """User choice of no longer receiving cards, initializing dealer play and halting all player buttons."""

def player_hit():
    """Gives the user one more card."""

def dealer_hit():
    """Allows dealer to hit IF the dealer respective value is less than 17."""

def busted():
    """Checks for both Player and Dealer bust upon Stand or Hit"""

def blackjack():
    """Checks for Blackjack for both the Player and Dealer"""

def winner():
    """Checks for who won the game if Blackjack isn't achieved by Player or Dealer"""

def dealer_card_reveal():
    """Displays the turned over Dealer card as its respective card"""

def game_results():
    """Gives a pop up window showing game results"""

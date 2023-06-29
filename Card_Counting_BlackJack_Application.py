# Alex Romero
# Created on 6/28/2023
import sys  
print(sys.executable)

# Import Random for the random selection of cards when dealing. Import TKinter for GUI
import random
import tkinter
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, font
import os

def game_page():
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

def tutorial_page():
    """Switches the introduction page to the tuturial page in which Card Counting instructions are given."""
    global card_counting_intro, button_intro
    button_intro.destroy()
    card_counting_intro = Button(window,
                                 font='Lato',
                                 background='black', fg='white',
                                     text="Card counting is a blackjack strategy used to determine when the player has an\n" \
                                          "advantage on the next hand by keeping a 'count' of the hand.\n" \
                                          "A player bets more on a higher(positive) count and less on a low(negative) count.\n\n" \
                                          "This is the KISS2 method, in which the player counts - \n" \
                                          " - Always start with a count of zero, and on new decks. \n" \
                                          " - Subtract by 1 when you see a K, Q, or J\n" \
                                          " - Add by 1 when you see a 4, 5, 6, or black 2\n"\
                                          " - Ignore these: Aces, Red 2, 3, 7, 8, 9, or 10.\n\n"\
                                          " A tutorial will be made accesible in game.\n"\
                                          "(Click here to continue)",
                                     command=game_page())
    card_counting_intro.place(x=250,y=200)

def intro_window():
    """This is the initial function that will be called upon to initialize the application through tkinter."""
    global window, background_label_intro, button_intro

    # Create the Tkinter window and give it its repective properties. Window title, background image, text (button)
    window = Tk()
    window.title('Card Counting Boot Camp Tutorial')
    window.geometry('1200x720')
    background_image_intro = Image.open('C:/Users/alexr/Pictures/CardsOnTable.jpg')
    background_image_intro = background_image_intro.resize((1200, 720))
    background_intro = ImageTk.PhotoImage(background_image_intro)
    background_label_intro = Label(window, image=background_intro)
    background_label_intro.place(x=0, y=0, relwidth=1, relheight=1)

    button_intro = Button(window,
                        font='Lato',
                        background='white', fg='black',
                        text=   'Welcome to Card Counting Boot Camp!\n'
                                'You should already have an understanding of how\n'
                                'to play BlackJack\n'
                                '\n'
                                'This program simply exists to help you win more money\n'
                                '(click here to continue)',
                        command = tutorial_page)
    button_intro.place(x=380, y=200)

    # Call window to run tkinter
    window.mainloop()

intro_window()
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

def hint():
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


def dealer_card_labels():
    """Creates frame and respective buttons for all cards that are dealt to the dealer, holds 5 cards."""
    global dealer_box1, dealer_box2, dealer_box3, dealer_box4, dealer_box5
    dealer_setup = Frame(window,background='#004000')
    dealer_setup.place(x=480, y=130)

    dealer_frame = LabelFrame(dealer_setup,background='#004000')
    dealer_frame.grid(row=0, column=0)#, padx=20, ipadx=20)

    dealer_box1 = Label(dealer_frame, text='',background='#004000')
    dealer_box1.grid(row=0, column=0, padx=10)

    dealer_box2 = Label(dealer_frame, text='',background='#004000')
    dealer_box2.grid(row=0, column=1, padx=10)

    dealer_box3 = Label(dealer_frame, text='',background='#004000')
    dealer_box3.grid(row=0, column=2, padx=10)

    dealer_box4 = Label(dealer_frame, text='',background='#004000')
    dealer_box4.grid(row=0, column=3, padx=10)

    dealer_box5 = Label(dealer_frame, text='',background='#004000')
    dealer_box5.grid(row=0, column=4, padx=10)


def player_card_labels():
    """Creates frame and respective buttons for all cards that are dealt to the player, holds 5 cards."""
    global player_box1, player_box2, player_box3, player_box4, player_box5
    player_setup = Frame(window)
    player_setup.place(x=480, y=370)

    player_frame = LabelFrame(player_setup,background='#004000')
    player_frame.grid(row=0, column=0)

    player_box1 = Label(player_frame, text='',background='#004000')
    player_box1.grid(row=0, column=0, padx=10)

    player_box2 = Label(player_frame, text='',background='#004000')
    player_box2.grid(row=0, column=1, padx=10)

    player_box3 = Label(player_frame, text='',background='#004000')
    player_box3.grid(row=0, column=2, padx=10)

    player_box4 = Label(player_frame, text='',background='#004000')
    player_box4.grid(row=0, column=3, padx=10)

    player_box5 = Label(player_frame, text='',background='#004000')
    player_box5.grid(row=0, column=4, padx=10)


def chip_buttons():
    """Creates frame and buttons for all of the chips used in betting."""
    # Create a frame holding buttons of poker chips(values) worth 1, 5, 10, 25, 100.
    global poker1_label, poker5_label, poker10_label, poker25_label, poker100_label
    chip_setup = Frame(window, background='#004000')
    chip_setup.place(x=880, y=640)

    chip_frame = LabelFrame(chip_setup, background='#004000', bd=0)
    chip_frame.grid(row=0, column=0)  # , padx=20, ipadx=20)

    pokerchip1 = Image.open("C:\\Users\\alexr\\Pictures\\1yingyang.jpg")
    pokerchip1 = pokerchip1.resize((60,60))
    pokerchip1 = ImageTk.PhotoImage(pokerchip1)
    poker1_label = Button(chip_frame, image = pokerchip1,command=bet1, border=0)
    poker1_label.photo = pokerchip1
    poker1_label.grid(row=0,column=0,pady=10,padx=1)

    pokerchip5 = Image.open("C:\\Users\\alexr\\Pictures\\5yingyang.jpg")
    pokerchip5 = pokerchip5.resize((60,60))
    pokerchip5 = ImageTk.PhotoImage(pokerchip5)
    poker5_label = Button(chip_frame, image = pokerchip5,command=bet5, border=0)
    poker5_label.photo = pokerchip5
    poker5_label.grid(row=0, column=1, pady=10,padx=1)

    pokerchip10 = Image.open("C:\\Users\\alexr\\Pictures\\10yingyang.jpg")
    pokerchip10 = pokerchip10.resize((60,60))
    pokerchip10 = ImageTk.PhotoImage(pokerchip10)
    poker10_label = Button(chip_frame, image = pokerchip10,command=bet10, border=0)
    poker10_label.photo = pokerchip10
    poker10_label.grid(row=0, column=2, pady=10,padx=1)

    pokerchip25 = Image.open("C:\\Users\\alexr\\Pictures\\25yingyang.jpg")
    pokerchip25 = pokerchip25.resize((60,60))
    pokerchip25 = ImageTk.PhotoImage(pokerchip25)
    poker25_label = Button(chip_frame, image = pokerchip25,command=bet25, border=0)
    poker25_label.photo = pokerchip25
    poker25_label.grid(row=0, column=3, pady=10, padx=1)

    pokerchip100 = Image.open("C:\\Users\\alexr\\Pictures\\100yingyang.jpg")
    pokerchip100 = pokerchip100.resize((60,60))
    pokerchip100 = ImageTk.PhotoImage(pokerchip100)
    poker100_label = Button(chip_frame, image = pokerchip100,command=bet100, border=0)
    poker100_label.photo = pokerchip100
    poker100_label.grid(row=0, column=4, pady=10, padx=1)
    #poker100_label.pack()


def player_actions_buttons():
    """Creates frame and respective buttons associated with player actions"""
    global hit_button, stand_button, bet_button, deal_button

    # Create frame centered in the middle of the window where user actions(buttons) related to playing will be.
    # This includes hit(add card), stand(let dealer play), bet(placing a pre-game bet), dealing(new set of cards post game)
    actions_frame = Frame(window, background='')
    actions_frame.place(x=480, y=250)

    hit_button = Button(actions_frame, text="Hit", font='Lato 15', background='#004000', fg='white',command=player_hit)
    hit_button.grid(row=0, column=0, padx=10)

    stand_button = Button(actions_frame, text="Stand", font='Lato 15', background='#004000', fg='white', command=stand)
    stand_button.grid(row=0, column=1, padx=10)

    bet_button = Button(actions_frame, text="Bet", font='Lato 15', background='#004000', fg='white', command = place_bets)
    bet_button.grid(row=0, column=2, padx=10)

    deal_button = Button(actions_frame, text="Deal", font='Lato 15', background='#004000', fg='white', command=deal_cards)
    deal_button.grid(row=0, column=3, padx=10)


def game_page():
    """Game window the user will play on. Initiates stand alone buttons and functions holding buttons the player will use"""
    global card_counting_intro, labrl, bet_value, total_money
    global bet_value_show,bet_value_string, money_value_string

    # Automatically starts the game for the user. Introduce new window
    card_counting_intro.destroy()
    background_label_intro.destroy()
    window.title('Card Counting Boot Camp')

    img = Image.open("C:/Users/alexr/Pictures/Table_with_chair.jpg")
    img = img.resize((1200,720))
    img = ImageTk.PhotoImage(img)
    labrl = Label(window, image=img)
    labrl.photo = img
    labrl.place(x=0, y=0, relwidth=1, relheight=1)

    player_actions_buttons()
    chip_buttons()
    player_card_labels()
    dealer_card_labels()

    # Create hint and tutorial buttons accesible to the user at all time. 
    hint_button = tkinter.Button(window,
                                 text='Hint (Show Count)',
                                 font = 'Lato', background='#004000', fg='white', command = hint)
    hint_button.place(x=00,y=642)

    tutorial_button = tkinter.Button(window,
                                     text='Card Counting Tutorial',
                                     font = 'Lato',
                                     background='#004000', fg='white')
    tutorial_button.place(x=0,y=680)

    # Give user repective bet value and money values available. Also initial values.
    bet_value = 0
    total_money = 1000

    bet_value_string = StringVar()
    bet_value_string.set('Current Bet: ' + str(bet_value))
    bet_value_show = Label(window, textvariable = bet_value_string,font = 'Lato',
                            background='#004000', fg='white')
    bet_value_show.place(x=1039,y=600)

    money_value_string = StringVar()
    money_value_string.set('Money: ' + str(total_money))
    money_value_show = Label(window, textvariable = money_value_string, font = 'Lato',
                             background='#004000', fg='white')
    money_value_show.place(x=900,y=600)

    place_bets()


def tutorial_page():
    """Switches the introduction page to the tuturial page in which Card Counting instructions are given."""
    # Destroy previous button, create new button that displays Card Counting tutorial for user. Take user to game.
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
                                     command=game_page)
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
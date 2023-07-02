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

# Create low deck outside of function so it automatically sets a new deck.
global deck
deck = ["king_spades"]
def create_deck():
    """Gives the player a new deck, should be called upon in any function where cards are dealt."""
    # Create a deck with all cards & faces. Only have to create the list once and multiply by one
    global deck
    global cards
    if len(deck) < 10:
        cards = ["ace_spades", "ace_hearts", "ace_clubs", "ace_diamonds","two_spades", "two_hearts", "two_clubs", "two_diamonds",
                "three_spades", "three_hearts", "three_clubs", "three_diamonds", "four_spades", "four_hearts", "four_clubs", "four_diamonds",
                "five_spades", "five_hearts", "five_clubs", "five_diamonds", "six_spades", "six_hearts", "six_clubs", "six_diamonds",
                "seven_spades", "seven_hearts", "seven_clubs", "seven_diamonds", "eight_spades", "eight_hearts", "eight_clubs", "eight_diamonds",
                "nine_spades", "nine_hearts", "nine_clubs", "nine_diamonds", "ten_spades", "ten_hearts", "ten_clubs", "ten_diamonds",
                "jack_spades", "jack_hearts", "jack_clubs", "jack_diamonds", "queen_spades", "queen_hearts", "queen_clubs", "queen_diamonds",
                "king_spades", "king_hearts", "king_clubs", "king_diamonds"]
        deck = cards * 2
        running_count = 0
        deck_Shuffle = Toplevel()
        deck_Shuffle.title('Deck status')
        deck_Shuffle_String = 'New deck has been given'
        deck_Shuffle_button = Button(deck_Shuffle,
                                 text=deck_Shuffle_String, font='Lato',
                                 background='#004000', fg='white')
        deck_Shuffle_button.pack()

running_count = 0
def card_values(card):
    """Assigns values to all cards that are dealt out."""
    global value
    value = 0
    global running_count
    if any(x in card for x in ["ace_spades", "ace_hearts", "ace_clubs", "ace_diamonds"]):
        value += 11
        running_count += 0
    elif any(x in card for x in ["two_spades", "two_clubs"]):
        value += 2
        running_count += 1
    elif any(x in card for x in ["two_hearts", "two_diamonds"]):
        value += 2
        running_count += 0
    elif any(x in card for x in ["three_spades", "three_hearts", "three_clubs", "three_diamonds"]):
        value += 3
        running_count += 0
    elif any(x in card for x in ["four_spades", "four_hearts", "four_clubs", "four_diamonds"]):
        value += 4
        running_count += 1
    elif any(x in card for x in ["five_spades", "five_hearts", "five_clubs", "five_diamonds"]):
        value += 5
        running_count += 1
    elif any(x in card for x in ["six_spades", "six_hearts", "six_clubs", "six_diamonds"]):
        value += 6
        running_count += 1
    elif any(x in card for x in ["seven_spades", "seven_hearts", "seven_clubs", "seven_diamonds"]):
        value += 7
        running_count += 0
    elif any(x in card for x in ["eight_spades", "eight_hearts", "eight_clubs", "eight_diamonds"]):
        value += 8
        running_count += 0
    elif any(x in card for x in ["nine_spades", "nine_hearts", "nine_clubs", "nine_diamonds"]):
        value += 9
        running_count += 0
    elif any(x in card for x in ["ten_spades", "ten_hearts", "ten_clubs", "ten_diamonds"]):
        value += 10
        running_count += 0
    elif any(x in card for x in ["jack_spades", "jack_hearts", "jack_clubs", "jack_diamonds",
                                 "queen_spades", "queen_hearts", "queen_clubs", "queen_diamonds",
                                 "king_spades", "king_hearts", "king_clubs", "king_diamonds"]):
        value += 10
        running_count -= 1

def card_faces(img):
    """Assigns card faces to each card dealt."""
    card_image = Image.open(f"C:\\Users\\alexr\\Pictures\\{img}.jpg")
    card_image = card_image.resize((50, 75))
    card_image = ImageTk.PhotoImage(card_image)
    card_image.photo = card_image
    return card_image

def hint():
    """Button that displays the current count value of the deck."""
    global hint_window, count_button
    hint_window = Toplevel()
    hint_window.title('Current Count')
    count_string = f'The current count is {running_count}'
    count_button = Button(hint_window,
                          text= count_string,font = 'Lato',
                          background='#004000', fg='white')
    count_button.pack()

def tutorial_button():
    """Button that gives brief tutorial on card counting, readily available for the player at all times."""
    pass

def face_down_card():
    """Runs code for the Dealer's faced down card"""
    global card_cover_image
    card_cover_image = Image.open("C:\\Users\\alexr\\Pictures\\playing_card_cover.png")
    card_cover_image = card_cover_image.resize((50, 75))
    card_cover_image = ImageTk.PhotoImage(card_cover_image)
    card_cover_image.photo = card_cover_image

def stand():
    """Player choice of no longer receiving cards, initializing dealer play and halting all player buttons."""
    dealer_card_reveal()
    dealer_hit()
    dealer_hit()
    dealer_hit()
    winner()

def player_hit():
    """Gives the player one more card."""
    global player_spot, player_hand_value
    if player_spot < 5:
        create_deck()
        new_card = random.choice(deck)
        deck.remove(new_card)
        player.append(new_card)
        card_values(new_card)
        player_hand_value += value
        if player_spot == 3:
            player_card3 = card_faces(player[2])
            player_box3.config(image=player_card3)
            player_spot += 1
            busted()
        elif player_spot == 4:
            player_card4 = card_faces(player[3])
            player_box4.config(image=player_card4)
            player_spot += 1
            busted()
        elif player_spot == 5:
            player_card5 = card_faces(player[4])
            player_box5.config(image=player_card5)
            bet_value = bet_value * 2
            total_money += bet_value
            outcome_string = "Congratulations, you won this round!"
            game_results(outcome_string)
            busted()
    blackjack()

def dealer_hit():
    """Allows dealer to hit IF the dealer respective value is less than 17."""
    create_deck()
    global dealer_hand_value, dealer_spot
    dealer_hand = random.choice(deck)
    if dealer_hand_value < 17:
        dealer_card = random.choice(deck)
        dealer.append(dealer_card)
        card_values(dealer_card)
        deck.remove(dealer_card)
        dealer_hand_value += value
        if dealer_spot == 3:
            dealer_card3 = card_faces(dealer[2])
            dealer_box3.config(image = dealer_card3)
            dealer_spot += 1
            busted()
        elif dealer_spot == 4:
            dealer_card4 = card_faces(dealer[3])
            dealer_box4.config(image = dealer_card4)
            dealer_spot += 1
            busted()
        elif dealer_spot == 5:
            dealer_card_reveal()
            outcome_string = "You lost this hand, better luck next time!"
            game_results(outcome_string)
            busted()

def busted():
    """Checks for both Player and Dealer bust upon Stand or Hit"""
    global player_hand_value, dealer_hand_value, bet_value, total_money
    for card in player:
        if card in ["ace_spades", "ace_hearts", "ace_clubs", "ace_diamonds"] and user_hand_value > 21:
            player_hand_value -= 10
    for card in dealer:
        if card in ["ace_spades", "ace_hearts", "ace_clubs", "ace_diamonds"] and dealer_hand_value > 21:
            dealer_hand_value -= 10
    if player_hand_value > 21:
        bet_value = 0
        bet_change(bet_value)
        outcome_string = "You busted, better luck next time!"
        game_results(outcome_string)
        dealer_card_reveal()
    elif dealer_hand_value > 21:
        bet_value = bet_value*2
        total_money += bet_value
        money_change(total_money)
        bet_value = 0
        bet_change(bet_value)
        outcome_string = "Congratulations, you won this round!"
        dealer_card_reveal()
        game_results(outcome_string)

def blackjack():
    """Checks for Blackjack for both the Player and Dealer"""
    global bet_value, total_money, dealer
    if player_hand_value == 21 and dealer_hand_value == 21:
        dealer_card_reveal()
        total_money += bet_value
        money_change(total_money)
        bet_value = 0
        outcome_string = 'You and the dealer tied!'
        game_results(outcome_string)

    elif player_hand_value == 21 and dealer_hand_value < 21:
        dealer_card_reveal()
        bet_value = bet_value*2
        total_money += bet_value
        money_change(total_money)
        bet_value = 0
        outcome_string = "Blackjack, you won!"
        game_results(outcome_string)

    elif player_hand_value < 21 and dealer_hand_value == 21:
        dealer_card_reveal()
        bet_value = 0
        outcome_string = "You lost this hand, better luck next time!"
        game_results(outcome_string)

def winner():
    """Checks for who won the game if Blackjack isn't achieved by Player or Dealer"""
    global player_hand_value, dealer_hand_value, bet_value, total_money
    # player win, Dealer lost
    if player_hand_value > dealer_hand_value and player_hand_value <= 21:
        dealer_card_reveal()
        bet_value = bet_value*2
        total_money += bet_value
        money_change(total_money)
        bet_value = 0
        outcome_string = "Congratulations, you won this hand!"
        game_results(outcome_string)
    # player lost, Dealer won
    elif player_hand_value < dealer_hand_value and dealer_hand_value <= 21:
        dealer_card_reveal()
        bet_value = 0
        outcome_string = "You lost this hand, better luck next time!"
        game_results(outcome_string)
    # User & Dealer tie
    elif player_hand_value == dealer_hand_value:
        bet_value = 0
        dealer_card_reveal()
        total_money += bet_value
        money_change(total_money)
        outcome_string = 'You and the dealer tied!'
        game_results(outcome_string)

def dealer_card_reveal():
    """Displays the turned over Dealer card as its respective card"""
    global dealer_box1, dealer_box2, player_box1, player_box2
    dealer_card1 = card_faces(dealer[0])
    dealer_box1.config(image=dealer_card1)
    dealer_card2 = card_faces(dealer[1])
    dealer_box2.config(image=dealer_card2)
    user_card1 = card_faces(player[0])
    player_box1.config(image=user_card1)
    user_card2 = card_faces(player[1])
    player_box2.config(image=user_card2)

def game_results(outcome_string):
    """Gives a pop up window showing game results"""  
    global bet_value
    dealer_card_reveal()
    bet_value = 0
    bet_change(bet_value)
    global user_won_window
    hit_button.config(state='disabled')
    stand_button.config(state='disabled')
    bet_button.config(state='normal')
    deal_button.config(state='disabled')
    poker1_label.config(state='disabled')
    poker5_label.config(state='disabled')
    poker10_label.config(state='disabled')
    poker25_label.config(state='disabled')
    poker100_label.config(state='disabled')
    user_won_window = Toplevel()
    user_won_window.title('Game outcome')
    user_won_button = Button(user_won_window,
                             text=outcome_string, font='Lato',
                             background='#004000', fg='white')
    user_won_button.pack()

def deal_cards():
    # Clear cards from player & dealer list
    face_down_card()
    global player, dealer
    player = []
    dealer = []

    # Update player button availability
    hit_button.config(state='normal')
    stand_button.config(state='normal')
    bet_button.config(state='disabled')
    deal_button.config(state='disabled')
    poker1_label.config(state='disabled')
    poker5_label.config(state='disabled')
    poker10_label.config(state='disabled')
    poker25_label.config(state='disabled')
    poker100_label.config(state='disabled')

    # Deal out two cards to both the player and dealer. Assign values, count, and photos.
    global dealer_hand_value, player_hand_value, running_count, player_spot, dealer_spot
    dealer_hand = random.choices(deck, k = 2 )
    dealer_hand_value = 0
    dealer_spot = 3
    for card in dealer_hand:
        create_deck()
        dealer.append(card)
        card_values(card)
        deck.remove(card)
        dealer_hand_value += value
    player_hand = random.choices(deck, k = 2 )
    player_hand_value = 0
    player_spot = 3
    for card in player_hand:
        create_deck()
        player.append(card)
        card_values(card)
        deck.remove(card)
        player_hand_value += value
    dealer_box1.config(image= card_cover_image)
    dealer_card2 = card_faces(dealer[1])
    dealer_box2.config(image=dealer_card2)
    player_card1 = card_faces(player[0])
    player_box1.config(image=player_card1)
    player_card2 = card_faces(player[1])
    player_box2.config(image=player_card2)

    # black_jack()

def place_bets():
    """Locks player into placing a bet without access to any other buttons without a bet."""
    # Disable all other buttons besides betting buttons to force player into betting.
    bet_button.config(state= 'normal')
    hit_button.config(state='disabled')
    stand_button.config(state='disabled')
    deal_button.config(state='disabled')
    poker1_label.config(state= 'normal')
    poker5_label.config(state='normal')
    poker10_label.config(state='normal')
    poker25_label.config(state='normal')
    poker100_label.config(state='normal')

    # Clear all cards so player has clear table.
    dealer_box1.configure(image='')
    dealer_box2.configure(image='')
    dealer_box3.configure(image='')
    dealer_box4.configure(image='')
    dealer_box5.configure(image='')
    player_box1.configure(image='')
    player_box2.configure(image='')
    player_box3.configure(image='')
    player_box4.configure(image='')
    player_box5.configure(image='')

    # Check for values to keep player locked in window.
    if bet_value != 0:
        deal_button.config(state='normal')
    if total_money < 0:
        debt_notice = Toplevel()
        debt_notice.title('Debt Notice')
        debt_notice_string = 'You are now taking out loans against your house.'
        player_won_button = Button(debt_notice,
                                 text=debt_notice_string, font='Lato',
                                 background='#004000', fg='white')
        player_won_button.pack()


def bet_change(bet_value):
    """Changes display of how much the player has bet upon final bet."""
    bet_value_string.set('Current Bet: ' + str(bet_value))

def money_change(total_money):
    """Changes display of money left."""
    money_value_string.set('Money: ' + str(total_money))

def bet1():
    """Increases bet value by $1."""
    global bet_value, total_money
    total_money -= 1
    bet_value += 1
    bet_change(bet_value)
    money_change(total_money)

def bet5():
    """Increases bet value by $5."""
    global bet_value, total_money
    total_money -= 5
    bet_value += 5
    bet_change(bet_value)
    money_change(total_money)

def bet10():
    """Increase bet value by $10."""
    global bet_value, total_money
    total_money -= 10
    bet_value += 10
    bet_change(bet_value)
    money_change(total_money)

def bet25():
    """Increase bet value by $25."""
    global bet_value, total_money
    total_money -= 25
    bet_value += 25
    bet_change(bet_value)
    money_change(total_money)

def bet100():
    """Increase bet value by $100."""
    global bet_value, total_money
    total_money -= 100
    bet_value += 100
    bet_change(bet_value)
    money_change(total_money)


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

    # Create frame centered in the middle of the window where player actions(buttons) related to playing will be.
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
    """Game window the player will play on. Initiates stand alone buttons and functions holding buttons the player will use"""
    global card_counting_intro, labrl, bet_value, total_money
    global bet_value_show,bet_value_string, money_value_string

    # Automatically starts the game for the player. Introduce new window
    card_counting_intro.destroy()
    background_label_intro.destroy()
    window.title('Card Counting Boot Camp')

    img = Image.open("C:/Users/alexr/Pictures/Table_with_chair.jpg")
    img = img.resize((1200,720))
    img = ImageTk.PhotoImage(img)
    labrl = Label(window, image=img)
    labrl.photo = img
    labrl.place(x=0, y=0, relwidth=1, relheight=1)

    # Call functions that create the gameplay player interface
    player_actions_buttons()
    chip_buttons()
    player_card_labels()
    dealer_card_labels()

    # Create hint and tutorial buttons accesible to the player at all time. 
    hint_button = tkinter.Button(window,
                                 text='Hint (Show Count)',
                                 font = 'Lato', background='#004000', fg='white', command = hint)
    hint_button.place(x=00,y=642)

    tutorial_button = tkinter.Button(window,
                                     text='Card Counting Tutorial',
                                     font = 'Lato',
                                     background='#004000', fg='white')
    tutorial_button.place(x=0,y=680)

    # Give player repective bet value and money values available. Also initial values.
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

    # Call bet function to start the game. 
    place_bets()


def tutorial_page():
    """Switches the introduction page to the tuturial page in which Card Counting instructions are given."""
    # Destroy previous button, create new button that displays Card Counting tutorial for player. Take player to game.
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
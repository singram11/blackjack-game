######### Blackjack Game #########


### Game Introduction ###

import time

def instructions():
  """ Function to show the instructions of the game"""
  print("How to play: ")
  print()
  print("During the game you will use your keyboard to control your actions.  Follow the instructions on the screen select the correct letter and hit enter!")
  print()
  print("Have fun!")
  print()
  print("Check out the rules of Blackjack here: https://bicyclecards.com/how-to-play/blackjack")
  print()
  print("Hit enter to return to the Main Menu")
  input("")


def show_menu():
  """ Function to show main menu with options to see instructions, play game or quit
    
    This plays after the welcome function and after a game is completed 

  """
  while True:
#     show the options to: 
    print("Main Menu:")
    print()
    print("[I]nstructions")
    print("[P]lay game")
    print("[E]nd game")
    print()
    print("What would you like to do?")
    choice = input("> ")
    print()
    choice = choice.lower()
#     Ask user for input on what they want to do: 
#       if instructions show them the instructions 
    if choice == "i":
      # show instructions function
      instructions()
    elif choice == "p":
      play_game()
    elif choice == "e":
      print()
      print("Thanks for playing")
      print("Goodbye")
      break 
    else:
      print("Thats not an option.")
      print("Please try again.")

def show_welcome():
  """Intro function gives user option for instructions or to play the game on first arrival"""
  print()
  print("~~~Welcome to the Blackjack Game!~~~")
  print()
  while True:
    print("Do you know how to play? Or would you like to see the instructions?")
    print()
    print("Please choose [I]nstructions or [P]lay game.")
    choice = input("> ")
    print()
    choice = choice.lower()
    if choice == "i":
      instructions()
      break
    elif choice == "p":
      play_game()
      break
    else:
      print()
      print("I didnt get that.")
      print()


### Playing the Game ###

# Set up the deck: 
def create_deck():
  """function to create the deck """
  deck = [
    {"name":"Ace of Hearts","value":11},
    {"name":"Two of Hearts","value":2},
    {"name":"Three of Hearts","value":3},
    {"name":"Four of Hearts","value":4},
    {"name":"Five of Hearts","value":5},
    {"name":"Six of Hearts","value":6},
    {"name":"Seven of Hearts","value":7},
    {"name":"Eight of Hearts","value":8},
    {"name":"Nine of Hearts","value":9},
    {"name":"Ten of Hearts","value":10},
    {"name":"Jack of Hearts","value":10},
    {"name":"Queen of Hearts","value":10},
    {"name":"King of Hearts","value":10},
    {"name":"Ace of Diamonds","value":11},
    {"name":"Two of Diamonds","value":2},
    {"name":"Three of Diamonds","value":3},
    {"name":"Four of Diamonds","value":4},
    {"name":"Five of Diamonds","value":5},
    {"name":"Six of Diamonds","value":6},
    {"name":"Seven of Diamonds","value":7},
    {"name":"Eight of Diamonds","value":8},
    {"name":"Nine of Diamonds","value":9},
    {"name":"Ten of Diamonds","value":10},
    {"name":"Jack of Diamonds","value":10},
    {"name":"Queen of Diamonds","value":10},
    {"name":"King of Diamonds","value":10},
    {"name":"Ace of Spades","value":11},
    {"name":"Two of Spades","value":2},
    {"name":"Three of Spades","value":3},
    {"name":"Four of Spades","value":4},
    {"name":"Five of Spades","value":5},
    {"name":"Six of Spades","value":6},
    {"name":"Seven of Spades","value":7},
    {"name":"Eight of Spades","value":8},
    {"name":"Nine of Spades","value":9},
    {"name":"Ten of Spades","value":10},
    {"name":"Jack of Spades","value":10},
    {"name":"Queen of Spades","value":10},
    {"name":"King of Spades","value":10},
    {"name":"Ace of Clubs","value":11},
    {"name":"Two of Clubs","value":2},
    {"name":"Three of Clubs","value":3},
    {"name":"Four of Clubs","value":4},
    {"name":"Five of Clubs","value":5},
    {"name":"Six of Clubs","value":6},
    {"name":"Seven of Clubs","value":7},
    {"name":"Eight of Clubs","value":8},
    {"name":"Nine of Clubs","value":9},
    {"name":"Ten of Clubs","value":10},
    {"name":"Jack of Clubs","value":10},
    {"name":"Queen of Clubs","value":10},
    {"name":"King of Clubs","value":10},
  ]

  return deck

#Shuffle the deck (would make this a funciton in future)
import random

deck = create_deck()

random.shuffle(deck)

## Hand Actions ## 

def deal_cards():
  """Add a single card to a hand"""
  new_card = deck.pop()
  return new_card

def show_full_hand(hand):
  """Show all cards in a hand"""
  print("----------")
  for card in hand:
    print(f'{card["name"]} - {card["value"]}')
    time.sleep(1)
  print("----------")
  time.sleep(1)
  print(f"Total: {total_hand(hand)}")
  time.sleep(1)
  print()
    
def total_hand(hand):
  """Get total value of hand"""
  total = 0
  for card in hand:
    current_value = card["value"]
    total = current_value + total
  return total


##Setting Up Game play - Dealing the hands ##

def deal_player_hand():
  """Add cards to player hand and show them"""
  print("Lets deal your hand!")
  print()
  player_hand = []
  player_hand.append(deal_cards())
  player_hand.append(deal_cards())
  show_full_hand(player_hand)
  return player_hand
 
def deal_dealer_hand():
  """Add two cards to the dealers hand, show the first card and return the hand"""
  print("Lets see what the dealer has...")
  print()
  dealer_hand = []
  dealer_hand.append(deal_cards())
  dealer_hand.append(deal_cards())
  show_dealer_hand(dealer_hand)
  return dealer_hand

def show_dealer_hand(dealer_hand):
  """Show just the first card in the dealers hand"""
  print("The dealers hand: ")
  print()
  time.sleep(1)
  print("---------")
  print(f'{dealer_hand[0]["name"]} - {dealer_hand[0]["value"]}')
  print("---------")


##### Game play ####

# Function to check for Naturals win 

def check_naturals(player_hand):
  """Function to check for naturals win
    
    Naturals win is an automatic 21 for the player
  """
  has_ace = False
  winner = False
  for card in player_hand: 
    if card["value"] == 11:
      has_ace = True
  if has_ace == True:
    for card in player_hand: 
      if card["value"] == 10:
        winner = True 
  return winner 
      
def change_ace_value(hand):
  """Change the value of ace from 11 to 1
  
  Check if the 
  """
  for card in hand: 
    if card["value"] == 11:
      card["value"] = 1
  return hand

def check_ace_value(hand): 
  """Check if we need to change the value of the ace
  
    Checking if the hand is over 21
  """
  total = total_hand(hand)
  if total > 21: 
    new_hand = change_ace_value(hand)
    return_hand = new_hand
  else: 
    return_hand = hand
  return return_hand


# function for player action

def run_player_turn(player_hand):
  """Function to run the players turn and add cards as appropriate"""
  #check if the player busts
  while total_hand(player_hand) < 21:
    print()
    time.sleep(1)
    print("Would you like to [H]it or [S]tand?")
    user_choice = input("> ")
    user_choice = user_choice.lower()
    if user_choice == "h":
      print()
      print("Dealer hands you another card...")
      print()
      time.sleep(1)
      print("Your hand is now:")
      print()
      player_hand.append(deal_cards())
      #check if value of ace should be 1 or 11
      player_hand = check_ace_value(player_hand)
      show_full_hand(player_hand)
    elif user_choice == "s":
      print()
      print("Stand.")
      print()
      break
    else:
      print()
      print("I didn't get that. Please try again.")
      print()
  total = total_hand(player_hand)
  return total

def run_dealer_turn(dealer_hand):
  """function to run dealer hand and add cards as appropriate"""
  total = total_hand(dealer_hand)
  show_full_hand(dealer_hand) 
  #check if the total is less than or equal to 16 if so the dealer must take another card
  while total <= 16:
    print("The dealer takes another card.")
    dealer_hand.append(deal_cards())
    #check an ace should have value of 11 or 1 
    dealer_hand = check_ace_value(dealer_hand)
    total = total_hand(dealer_hand)
    print("The dealers hand is now:")
    time.sleep(1)
    print()
    show_full_hand(dealer_hand)
  time.sleep(1)
  if total < 21:
    print(f"Dealer stays at {total}")
  return total 

### playing the game ###

def play_game():
  """Function controls the full game play"""
  #Deal hands
  player_hand = deal_player_hand()
  dealer_hand = deal_dealer_hand()
  #check for natural winner
  if check_naturals(player_hand) == True:
    print()
    time.sleep(1)
    print("You win!")
    print()
  else: 
    #player turn and outcomes
    player_total = run_player_turn(player_hand)
    if player_total > 21: 
      time.sleep(1)
      print("Oh no...")
      print("Looks like you bust!")
      print()
    elif player_total == 21:
      time.sleep(1)
      print()
      print("Blackjack! You win!")
      print()
    else: 
      print()
      print("Let's see what the dealer has")
      time.sleep(1)
      #dealer turn and outcomes
      dealer_total = run_dealer_turn(dealer_hand)
      if dealer_total > 21:
        print()
        print("The dealer busts! You win! ")
      elif player_total > dealer_total:
        print()
        print("You win!")
      elif player_total == dealer_total: 
        print()
        print("Looks like its a push.")
      else: 
        print()
        print("Looks like the house wins")
  print()
  print("Round over")
  print("Hit enter to return to main menu.")
  input("")



def full_game():
  """function starts welcome to game and main menu flow"""
  show_welcome()
  show_menu()

full_game()

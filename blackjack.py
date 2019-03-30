import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
busted = False
playing = True
#DECK

class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    def __init__(self):
        self.deck = []
        for rank in ranks:
            for suit in suits:
                self.deck.append(Card(rank,suit))
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
    def __str__(self):
        hand = ''
        for card in self.cards:
            hand += '\n'+card.__str__()
        return hand
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace' and self.value > 21:
            self.value -= 10
            
class Chips:
    def __init__(self):
        self.total = 1000 #can be adjusted
        self.bet = 0
    def win(self):
        self.total += self.bet
    def lose(self):
        self.total -= self.bet

def make_bet(chips):

    while True:
            
        try:
            chips.bet = int(input("How much do you want to bet? "))
        except:
            print("You can only enter integers")
        else:
            if chips.bet > chips.total:
                print("Your bet cannot exceed", chips.total)
            else:
                break
def chips_setup(chips):
    while True:

        answer = input("You start with total of 1000 chips. Do you wish to change that? Y / N ")
        if answer[0].lower() == 'y':
            while True:
                try:
                    answer2 = int(input("Please enter the amount of your starting chips "))
                except:
                    print("Enter integers only")
                else: 
                    if answer2 > 0:
                        chips.total = answer2
                        print("Your total chips adjustet to ",answer2)
                        break
                    else:
                        print("You have to start with atleast 1 chip")
        elif answer[0].lower() == 'n':
            break
        else:
            print("Please enter only Y or N")
            continue
        break
                
def hit(deck,hand):
    hand.add_card(deck.deal())
def hit_or_stand(deck,hand):
    global playing
    while True:
        move = input("Do you wanna HIT or STAND? Enter h/s ")
        if move[0].lower() == 's':
            playing = False
        elif move[0].lower() == 'h':
            hit(deck,hand)
        else:
            print("Enter only h for HIT or s for STAND")
            continue
        break

def show_hand(player):
    print('Your hand:',player)
def show_all(player,dealer):
    print('\n')
    print('Your hand:',player)
    print('\n')
    print('Dealer\'s hand:',dealer)
    print('\n')

#GAME ENDING SCENARIOS
def player_busts(chips):
    chips.lose()
    print("You bust!")
def player_wins(chips):
    chips.win()
    print("You win!")

def dealer_wins(chips):
    chips.lose()
    print("Dealer wins")
def dealer_busts(chips):
    chips.win()
    print("Dealer busts! You win!")
def push():
    print("You and dealer tie! It's a push")


# ACTUAL GAME
print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
Dealer hits until she reaches 17. Aces count as 1 or 11.')
player_chips = Chips()
    
chips_setup(player_chips)

while True:

    new_deck = Deck()
    new_deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(new_deck.deal())
    player_hand.add_card(new_deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(new_deck.deal())
    dealer_hand.add_card(new_deck.deal())

    show_hand(player_hand)

    make_bet(player_chips)
    while playing:
        hit_or_stand(new_deck,player_hand)
        show_hand(player_hand)
        if player_hand.value > 21:
            player_busts(player_chips)
            break
    if player_hand.value <= 21:
        while(dealer_hand.value < 17):
            hit(new_deck,dealer_hand)
        show_all(player_hand,dealer_hand)
        if dealer_hand.value > 21:
            dealer_busts(player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)
        else:
            push()
    print(f'You have total of {player_chips.total} chips')
    again = input("Would you like to play again?")
    if again[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing")
        break
    
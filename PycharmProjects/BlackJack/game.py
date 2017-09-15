from random import shuffle


class Card:
    def __init__(self, card_suit=None, card_rank=None, card_value=[]):
        self._card_value = card_value
        self._card_suit = card_suit
        self._card_rank = card_rank


class DeckOfCards:
    def __init__(self):
        self.deck = self.create_deck()

    def create_deck(self):
        deck = []
        list_of_suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        list_of_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "D", "K", "A"]
        for suit in list_of_suits:
            for rank in list_of_ranks:
                if rank == "A":
                    value = [1, 11]
                elif rank == "J" or rank == "D" or rank == "K":
                    value = [10]
                else:
                    value = [int(rank)]
                card = Card(suit, rank, value)
                deck.append(card)
        shuffle(deck)
        return deck

    def deal_card(self):
        return self.deck.pop()


class Player:
    def __init__(self, name="Player", balance=1000):
        self.name = name
        self._balance = balance

    def set_name(self):
        self.name = input("What is your name? ")
        return self.name

    def set_balance(self):
        #if won self.balance += Game.stake
        #else -= Game.stake
        pass

    def get_balance(self):
        return self._balance



class Hand:
    def __init__(self):
        pass

    dealers_hand = None
    players_hand = None

    def score_hand(self):
        pass


class Game:
    def __init__(self, stake=100):
        self.players_hand = []
        self.dealers_hand = []
        self.stake = stake

    def show_menu(self):
        print("This is the BlackJack game")
        print("What do you want to do?")
        print("a - start playing")
        print("b - set player's name")
        print("c - restart the game")
        print("d - finish game")
        decision = input("Choose one: a, b, c or d ")
        while True:
            if decision == "a":
                pass
            elif decision == "b":
                Player.set_name()
            elif decision == "c":
                pass
            elif decision == "d":
                self.finish_game()
            else:
                decision = input("You should write: a, b, c or d ")
                continue
    #to mi się nie podoba, muszę sobie przemyśleć, jak lepiej ma działać to menu

    def finish_game(self):
        exit()

    def restart(self):
        pass

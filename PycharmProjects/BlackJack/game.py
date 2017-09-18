from random import shuffle


class Card:
    def __init__(self, card_suit, card_rank, card_value):
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
        self._name = name
        self._balance = balance

    def set_name(self):
        self._name = input("What is your name? ")
        return self._name

    def set_balance(self):
        #if won self.balance += Game.stake
        #else -= Game.stake
        pass

    def get_balance(self):
        return self._balance


class Hand:
    def __init__(self):
        self.hand = [self.add_card(), self.add_card()]
        self.hand_value = self.score_hand()

    def add_card(self):
        new_card = DeckOfCards.deal_card()
        return new_card

    def score_hand(self):
        hand_value = 0
        for card in self.hand:
            if card._card_rank != "A":
                hand_value += card._card_value[0]
            else:
                hand_value += card._card_value[1]
        #checking if Aces should have value 1 or 11
        if hand_value > 21:
            for card in self.hand:
                if card._card_rank == "A":
                    hand_value -=10
                elif hand_value <= 11
                    hand_value +=10
        return hand_value




class Game:
    def __init__(self, stake=100):
        self.players_hand = Hand()
        self.dealers_hand = Hand()
        self.player = Player()
        self.stake = stake
        self.game_deck = DeckOfCards()

    def show_menu(self):
        print("This is the BlackJack game")
        print("What do you want to do?")
        print("a - start playing")
        print("b - set player's name")
        print("c - restart the game")
        print("d - finish game")

        while True:
            decision = input("Choose one: a, b, c or d ")
            if decision == "a":
                self.start_game()
            elif decision == "b":
                self.player.set_name()
            elif decision == "c":
                pass
            elif decision == "d":
                self.finish_game()
            else:
                print("You should write: a, b, c or d ")
     #to mi się nie podoba, muszę sobie przemyśleć, jak lepiej ma działać to menu

    def change_stake(self):
        while True:
            print("The current stake is {}".format(self.stake))
            stake_change = input('Do you want to change game stake? "yes" or "no"')
            if stake_change == "yes":
                try:
                    self.stake = int(input("Please write new stake: "))
                    break
                except:
                    print("You have to write a number")
                    continue
            elif stake_change == "no":
                break
            else:
                print('Please, write, "yes" or "no"')

    def start_game(self):

        #The player decides about the game stake:
        self.change_stake()

        #wydrukować kartę dealera
        print("The dealers opened card is:")
        # wydrukować kolor i wartość karty dealera
        print(self.dealers_hand[0]._card_rank, self.dealers_hand[0]._card_suit)

        #początkowa ręka gracza
        print("{} your cards are:".format(self.player._name))
        #wydrukować tylko kolor i wartość karty (dlaczego nie używa mi tego carda???)
        for card in self.players_hand:
            print(self.players_hand._card_rank, self.players_hand._card_suit)


        players_score = self.players_hand.score_hand()
        print("You have {} points".format(players_score))

        print()

        while True:
            print('{} do you want to pull another card?'.format(self.player._name))
            pull = input('"yes" or "no"?')
            if pull == "yes":
                self.players_hand.add_card()
                print(self.players_hand)
                players_score = self.players_hand.score_hand()
                print("You have {} points".format(players_score))
                continue
            elif pull == "no":
                break
            else:
                print("You didn't write correct answer")

        print("Dealer's cards are:")
        print(self.dealers_hand)
        #print dealers score
        while True:
            if dealers_score <= 16:
                self.dealers_hand.append()
                #score hand
                #print dealer's score
                continue
            else:
                break








        pass



    def finish_game(self):
        exit()

    def restart(self):
        pass

def main():
    new_game = Game()
    new_game.show_menu()

main()
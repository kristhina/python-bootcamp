from random import shuffle


class Card:
    """
    Class Card creates new card for the game.
    :type card_suit : string
    :type card_rank : string
    :type card_value : list of int
    """
    def __init__(self, card_suit, card_rank, card_value):
        self.card_value = card_value
        self.card_suit = card_suit
        self.card_rank = card_rank

    def print_card(self):
        """
        prints the suit and rank of the card
        """
        print("{}-{}".format(self.card_suit, self.card_rank))


class DeckOfCards:
    """
    Class DeckOfCards creates new deck of cards and shuffles them.
    :type deck : list of Card
    """
    def __init__(self):
        self.deck = self.create_deck()

    def create_deck(self):
        """
        creates 52 cards and shuffles them
        :return: list of Card
        """
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
        """
        deals one card and removes it from the deck
        :return: Card
        """
        return self.deck.pop()


class Player:
    """
    Class Player crates new player for our game
    :type name : string
    :type balance : int
    """
    def __init__(self, name="Player", balance=1000):
        self.name = name
        self.balance = balance

    def set_name(self):
        """
        Player can set his name
        :return: string
        """
        self.name = input("What is your name? ")
        return self.name


class Hand:
    """
    Class Hand creates new Hand of Cards for player and dealer
    :type hand : list
    """
    def __init__(self):
        self.hand = []

    def add_card(self, card):
        """
        adds new Card to the Hand
        :param card: Card
        """
        self.hand.append(card)

    def score_hand(self):
        """
        counts the total value of cards on the Hand
        :return: int
        """
        hand_value = 0
        aces_number = 0
        for card in self.hand:
            hand_value += card.card_value[0]
            if card.card_rank == "A":
                aces_number += 1
        # checking if Aces should have value 1 or 11
        if (hand_value <= 11) and (aces_number >= 1):
            hand_value += 10
        return hand_value

    def print_hand(self):
        """
        prints the value and list of cards in hand
        """
        print("Hand value: {}".format(self.score_hand()))
        print("Cards in hand:")
        for card in self.hand:
            card.print_card()


class Game:
    """
    Class Game creates new game of BlacJack
    :type players_hand : Hand
    :type dealers_hand : Hand
    :type player : Player
    :type stake : int
    :type game_deck : DeckOfCards
    """
    def __init__(self, stake=100):
        self.players_hand = Hand()
        self.dealers_hand = Hand()
        self.player = Player()
        self.stake = stake
        self.game_deck = DeckOfCards()

    def show_menu(self):
        """
        shows menu for the Game
        Player can choose what to do
        """
        print("--------------------------")
        print("This is the BlackJack game")
        print("Your balance is {}".format(self.player.balance))

        while True:
            print("--------------------------")
            print("What do you want to do?")
            print("a - start playing")
            print("b - set player's name")
            print("c - restart the game")
            print("d - finish game")
            decision = input("Choose one: a, b, c or d ")
            print("--------------------------")
            if decision == "a":
                # if decision is a - starts new game
                self.start_game()
            elif decision == "b":
                # if decision is b - player can set his or her name
                self.player.set_name()
            elif decision == "c":
                # if decision ic c - player can restart of the parameters of the game
                self.restart()
            elif decision == "d":
                # if decision is d - player ends playing game
                self.finish_game()
            else:
                print("You should write: a, b, c or d ")

    def change_stake(self):
        """
        changes stake of the Game
        Player can choose the new stake of the Game
        """
        while True:
            print("The current stake is {}".format(self.stake))
            stake_change = input('Do you want to change game stake? "yes" or "no"')
            if stake_change == "yes":
                try:
                    self.stake = int(input("Please write new stake: "))
                    break
                except ValueError:
                    print("You have to write a number")
                    continue
            elif stake_change == "no":
                break
            else:
                print('Please, write, "yes" or "no"')

        # checks if the stake is not larger than player's balance
        # if it is larger - the player must change the stake or reset game
        if self.stake > self.player.balance:
            print("You do not have enough money")
            print("You can reset the game (initial balance is 1000) or change the stake")
            print("What do you want to do?")
            print("a - change stake")
            print("b - reset game")
            while True:
                decision = input("Choose a or b: ")
                if decision == "a":
                    self.change_stake()
                    break
                elif decision == "b":
                    self.restart()
                    break
                else:
                    print("You should write a or b")

    def start_game(self):
        """
        player starts the game and go step by step throuh the game
        """
        # The player decides about the game stake:
        self.change_stake()

        # deal player's starting cards
        players_card_1 = self.game_deck.deal_card()
        players_card_2 = self.game_deck.deal_card()
        self.players_hand.add_card(players_card_1)
        self.players_hand.add_card(players_card_2)

        # deal dealer's starting cards
        dealers_card_1 = self.game_deck.deal_card()
        dealers_card_2 = self.game_deck.deal_card()
        self.dealers_hand.add_card(dealers_card_1)
        self.dealers_hand.add_card(dealers_card_2)

        # print hands
        print("------------------------")
        print("{}'s Hand:".format(self.player.name))
        self.players_hand.print_hand()
        print("------------------------")
        print("Dealer's opened card:")
        self.dealers_hand.hand[0].print_card()

        # start dealing cards for Player
        while True:
            if self.players_hand.score_hand() > 21:
                self.who_won()
            print("------------------------")
            print('{} do you want to hit or stand?'.format(self.player.name))
            pull = input('write "hit" or "stand"')
            if pull == "hit":
                new_card = self.game_deck.deal_card()
                self.players_hand.add_card(new_card)
                self.players_hand.score_hand()
                print("------------------------")
                print('{} after deal you have:'.format(self.player.name))
                self.players_hand.print_hand()
                continue
            elif pull == "stand":
                break
            else:
                print("You didn't write correct answer")

        # start dealing cards for Dealer
        print("------------------------")
        print("Dealer's cards are:")
        self.dealers_hand.print_hand()
        while True:
            if self.dealers_hand.score_hand() <= 16:
                new_card = self.game_deck.deal_card()
                self.dealers_hand.add_card(new_card)
                self.dealers_hand.score_hand()
                print("------------------------")
                print("Dealer hand after dealing new card")
                self.dealers_hand.print_hand()
                continue
            else:
                self.who_won()

    def who_won(self):
        """
        checks who is the winner of the game
        sets the new balance of the Player - depending on the game result
        """
        dealer_won = False
        player_won = False
        print("-----------------------------")

        # checking who is the winner
        if self.players_hand.score_hand() > 21:
            dealer_won = True
            print("You go bust :(")
            print("Dealer won!")
        elif self.dealers_hand.score_hand() > 21:
            player_won = True
            print("Dealer go bust")
            print("{} won!".format(self.player.name))
        elif self.players_hand.score_hand() > self.dealers_hand.score_hand():
            player_won = True
            print("{} won!".format(self.player.name))
        elif self.dealers_hand.score_hand() > self.players_hand.score_hand():
            dealer_won = True
            print("Dealer won!")
        else:
            print("It is a push. Nobody won!")

        # setting new balance depending on the winner
        if dealer_won:
            self.player.balance -= self.stake
        elif player_won:
            self.player.balance += self.stake
            # if player has BlackJack, he can won 1.5*stake
            # I have to write it but I am not sure how to do it...

        self.new_game_preparation()

    def new_game_preparation(self):
        """
        resets the deck and hands of Player and Dealer
        """
        self.dealers_hand = Hand()
        self.players_hand = Hand()
        self.game_deck = DeckOfCards()
        self.show_menu()

    def finish_game(self):
        """
        ends the game
        """
        exit()

    def restart(self):
        """
        restarts the game: not only the hands and deck but also the balance, stake and player's name
        """
        new_game = Game()
        new_game.show_menu()


def main():
    new_game = Game()
    new_game.show_menu()


main()

import random

class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class DeckOfCards:
    def __init__(self):
        self.deck = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        ranks_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
        for suit in suits:
            for rank, value in ranks_values.items():
                self.deck.append(Card(suit, rank, value))
    def shuffle(self):
        random.shuffle(self.deck)
    def deal_one(self):
        return self.deck.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0
    def add_card(self, card):
        self.hand.append(card)
        self.score += card.value
        if self.score > 21:
            for card in self.hand:
                if card.rank == 'Ace' and self.score > 21:
                    self.score -= 10
    def reset_hand(self):
        self.hand = []
        self.score = 0
    def show_hand(self, show_all=True):
        if show_all:
            return ', '.join(str(card) for card in self.hand)
        else:
            return f"{self.hand[0]} and [Hidden]"

class BlackjackGame:
    def __init__(self):
        self.deck = DeckOfCards()
        self.deck.shuffle()
        self.player = Player("Player")
        self.dealer = Player("Dealer")
    def play_round(self):
        self.player.reset_hand()
        self.dealer.reset_hand()
        for i in range(2):
            self.player.add_card(self.deck.deal_one())
            self.dealer.add_card(self.deck.deal_one())
        print(f"\nYour hand: {self.player.show_hand()} (Score: {self.player.score})")
        print(f"Dealer's hand: {self.dealer.show_hand(show_all=False)}")
        while self.player.score < 21:
            action = input("Do you want to Hit or Stand? (h/s): ").lower()
            if action == 'h':
                self.player.add_card(self.deck.deal_one())
                print(f"\nYour hand: {self.player.show_hand()} (Score: {self.player.score})")
            else:
                break
        if self.player.score > 21:
            print("You busted! Dealer wins.")
            return "lose"
        while self.dealer.score < 17:
            self.dealer.add_card(self.deck.deal_one())
        print(f"\nDealer's hand: {self.dealer.show_hand()} (Score: {self.dealer.score})")
        if self.dealer.score > 21 or self.player.score > self.dealer.score:
            print("You win!")
            return "win"
        elif self.player.score < self.dealer.score:
            print("Dealer wins!")
            return "lose"
        else:
            print("It's a tie!")
            return "tie"
    def start_game(self):
        while True:
            result = self.play_round()
            if result == "win":
                print("Congratulations, you won this round!")
            elif result == "lose":
                print("Better luck next time.")
            else:
                print("It's a tie. No winner this round.")

            play_again = input("\nDo you want to play again? (y/n): ").lower()
            if play_again != 'y':
                print("Thank you for playing Blackjack!")
                break
            
game = BlackjackGame()
game.start_game() 
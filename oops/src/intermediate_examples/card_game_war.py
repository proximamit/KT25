import random
from collections import deque

# -------------------------
# Card
# -------------------------
class Card:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = {
        "2": 2, "3": 3, "4": 4, "5": 5,
        "6": 6, "7": 7, "8": 8, "9": 9,
        "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14
    }

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = Card.values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


# -------------------------
# Deck
# -------------------------
class Deck:
    def __init__(self):
        self.cards = [
            Card(suit, rank)
            for suit in Card.suits
            for rank in Card.values
        ]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_half(self):
        return self.cards[:26], self.cards[26:]


# -------------------------
# Player
# -------------------------
class Player:
    def __init__(self, name, cards):
        self.name = name
        self.cards = deque(cards)

    def has_cards(self):
        return len(self.cards) > 0

    def play_card(self):
        return self.cards.popleft()

    def add_cards(self, won_cards):
        self.cards.extend(won_cards)

    def card_count(self):
        return len(self.cards)


# -------------------------
# War Game
# -------------------------
class WarGame:
    def __init__(self, player1_name, player2_name):
        deck = Deck()
        deck.shuffle()

        half1, half2 = deck.deal_half()
        self.player1 = Player(player1_name, half1)
        self.player2 = Player(player2_name, half2)
        self.rounds = 0

    def play_game(self):
        print("Starting the game of WAR!\n")

        while self.player1.has_cards() and self.player2.has_cards():
            self.rounds += 1
            print(f"--- Round {self.rounds} ---")
            self.play_round()

            if self.rounds >= 1000:
                print("Game stopped after 1000 rounds (too long).")
                break

        self.declare_winner()

    def play_round(self):
        table_cards = []

        card1 = self.player1.play_card()
        card2 = self.player2.play_card()

        table_cards.extend([card1, card2])

        print(f"{self.player1.name} plays {card1}")
        print(f"{self.player2.name} plays {card2}")

        if card1.value > card2.value:
            self.player1.add_cards(table_cards)
            print(f"{self.player1.name} wins the round\n")

        elif card2.value > card1.value:
            self.player2.add_cards(table_cards)
            print(f"{self.player2.name} wins the round\n")

        else:
            print("WAR!")
            self.handle_war(table_cards)

    def handle_war(self, table_cards):
        for _ in range(3):
            if not self.player1.has_cards() or not self.player2.has_cards():
                return

            table_cards.append(self.player1.play_card())
            table_cards.append(self.player2.play_card())

        if not self.player1.has_cards() or not self.player2.has_cards():
            return

        war_card1 = self.player1.play_card()
        war_card2 = self.player2.play_card()

        table_cards.extend([war_card1, war_card2])

        print(f"{self.player1.name} plays {war_card1}")
        print(f"{self.player2.name} plays {war_card2}")

        if war_card1.value > war_card2.value:
            self.player1.add_cards(table_cards)
            print(f"{self.player1.name} wins the war\n")

        elif war_card2.value > war_card1.value:
            self.player2.add_cards(table_cards)
            print(f"{self.player2.name} wins the war\n")

        else:
            print("Another WAR!")
            self.handle_war(table_cards)

    def declare_winner(self):
        print("\n--- Game Over ---")
        if self.player1.card_count() > self.player2.card_count():
            print(f"{self.player1.name} wins the game!")
        elif self.player2.card_count() > self.player1.card_count():
            print(f"{self.player2.name} wins the game!")
        else:
            print("The game is a tie!")


# -------------------------
# Run the Game
# -------------------------
if __name__ == "__main__":
    name_of_player_1 = input("Enter the name of Player 1 : ").strip()
    name_of_player_2 = input("Enter the name of Player 2 : ").strip()
    #game = WarGame("Player 1", "Player 2")
    game = WarGame(name_of_player_1, name_of_player_2)
    game.play_game()

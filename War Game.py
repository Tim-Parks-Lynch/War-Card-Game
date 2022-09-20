from random import shuffle

# Card Class
# SUIT, RANK, VALUE

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = (
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
)

values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Ace": 14,
}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


# Deck Class


class Deck:
    """
    Deck Class:
        * Instantiates a new deck
            * Create all 52 card objects
            * Hold as a list of Card objects
        * Shuffle a deck through a method call
            * Random library shuffle() function
        * Deal cards from the Deck object
            * Pop method from cards list
    """

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create the card object
                created_card = Card(suit, rank)  # Creates all ranks and suits
                self.all_cards.append(created_card)

    def shuffle_deck(self):
        shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


# Player Class


class Player:
    """
    Player Class:
        * Class will be used to hold a player's current list of cards
        * A player should be able to add or remove cards from their 'hand'
            (list of card objects)
        * Player should be able to add a single card or multiple cards to
            their list
        * Keep in mind the last thing we need to think about is translating a
            deck/hand of cards with a top and bottom to a python list
    """

    def __init__(
        self,
        name,
    ):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)  # removes from the front

    def add_cards(self, new_cards):

        # if type(new_cards) == type([]):
        if isinstance(new_cards, list):
            # Checks for multiple cards
            self.all_cards.extend(new_cards)
        else:
            # Single card
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."


# Game Logic


new_deck = Deck()
new_deck.shuffle_deck()
mycard = new_deck.deal_one()

player_1 = Player("Jose")
player_1.add_cards(mycard)
player_1.add_cards([mycard, mycard, mycard])
print(player_1.all_cards[0])
player_1.remove_one()
print(player_1.all_cards[1])
print(player_1)

# print("my card here: ", mycard)
# for card_object in new_deck.all_cards:
#     print(card_object)
# print(len(new_deck.all_cards))

# Game Logic

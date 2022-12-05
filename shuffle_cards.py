# 1. Create an object model to represent a deck of cards. An example of a card is the Ace of Hearts.
#    In this case, Ace is the 'rank' and Hearts is the 'suit'. Each rank/suit combination should appear exactly once.
#    There are 4 suits and 13 ranks, so there should be 4*13=52 unique cards in the deck.
#    The list of suits and ranks is pasted below.
# 2. Construct an instance of a deck and print all cards in the deck to output
# 3. (optional if time) Create a shuffle method which randomizes the card order in the deck.
 
suits = ['clubs', 'diamonds', 'spades', 'hearts']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

class Cards:
    def __init__(self, suits, ranks):
        self.suits = ['clubs', 'diamonds', 'spades', 'hearts']
        self.ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

class Deck(Cards):
    def __init__(self):
        self.card_combo = []
        for suit in suits:
            for rank in ranks:
                self.card_combo.append([suit, ranks])


    def Print(self):
        for i in self.card_combo:
            for j in i[0]:
                for k in i[1]:
                    print((j) + ' ' + 'of' + ' ' + (k))

d = Deck()

print(d.Print())

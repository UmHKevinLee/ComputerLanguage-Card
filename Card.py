from random import randrange

class Card:
    def __init__(self,rank,suit): # define initial which takes rank and suit varialbe.
        self.rank = rank
        self.suit = suit


    def getRank(self):          #gettor for rank.
        return self.rank        


    def getSuit(self):          #gettor for suit.
        return self.suit

    def value(self):            #Blackjack rank value indicates the ranks ace - king
        if self.rank <= 10:
            return self.rank
        else:
            return 10

    def __str__(self):          #toString() for the name of card.
        ranks = ["Ace", "Two", "Three", "Four",
                 "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                 "Jack", "Queen", "King"]
        suits = ["Diamonds", "Clubs", "Hearts", "Spades" ]
        name = ranks[self.rank -1] + " of "

        if self.suit == "d":
            name += suits[0]
        elif self.suit == "c":
            name += suits[1]
        elif self.suit == "h":
            name += suits[2]
        else:
            name += suits[3]

        return name
            

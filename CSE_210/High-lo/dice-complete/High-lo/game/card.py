import random


class Card:
    """A card with a value one through thirteen
   
    Attributes:
        value (int): The number of spots on the side facing up.
    """

    def __init__(self):
        """Constructs a new instance of card.

        Args:
            self (card): An instance of card.
        """
        self.value = 0
        self.points = 0

    def draw(self):
        """Generates a new random value and calculates the points for the card.
        
        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1, 13)
        high_or_low = input("Will the card be higher or lower? [H/L]")
        self.h_l = True 
        self.points = 100 if self.h_l == True else -75 
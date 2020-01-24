#! /usr/bin/env python3
# coding: utf-8


from random import *
from math import ceil



class RussianRoulette:
    """The player bets on a number between 0 and 49"""

    def __init__(self):
        self._wealth = 10000
        print("Your initial fortune is " + str(self._wealth))


    def pick_random_number(self):
        try:
            self._bet_money = int(input("How much money do you want to bet? "))

            if self._bet_money > self._wealth:
                print("You can not bet so much, you just have " + str(self._wealth))
            else:
                try:
                    self._number_player = int(input("What number do you choose (between 0 and 49)? "))
                    # The chance chooses a random number
                    self._number_random = randrange(50)
                    print("Number chosen is: " + str(self._number_random) + "\a")
                    self.show_results()
                except ValueError:
                    print("You need to enter a number")

        except ValueError:
            print("You need to enter a number")



    def show_results(self):
        # The player chose the good number
        # He wins 3x his bet
        if self._number_player == self._number_random:
            self._wealth += self._bet_money*3
            print("Congratulations, you have chosen the good number !")

        # The player didn't choose the good number, but the color is the same
        # He wins 50% of his bet
        elif (self._number_player%2) == (self._number_random%2):
            self._wealth += ceil(self._bet_money/2)
            print("You don't have the good number, but you have the same color !")

        # The player don't have the good number, neither the same color
        # He loses his bet
        else:
            self._wealth -= self._bet_money
            print("Lost ! Try again")

        print("Now, your wealth is: " + str(self._wealth))

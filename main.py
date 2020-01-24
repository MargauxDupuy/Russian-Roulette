#! /usr/bin/env python3
# coding: utf-8

from zcasino import *

want_play = True
game = RussianRoulette()
while want_play:
    game.pick_random_number()
    want_play = bool(int(input("Continue? 1 for yes, 0 for no: ")))
print("See you!")

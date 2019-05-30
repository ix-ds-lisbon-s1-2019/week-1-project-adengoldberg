#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 21:51:58 2019

@author: adengoldberg
"""

import random


class PokerGame():
    
    players = {}
    num_players = 0
    
    def __init__(self):
        self.num_players = int(input("How many players? "))
        for i in range(self.num_players):
            name = input("Enter Player " + str(i + 1) + " Name: ")
            self.players[name] = []
        
    def deal_cards(self):
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        suits = ["C", "D", "H", "S"]
        drawn = []
        for player in list(self.players.keys()):
            self.players[player] = []
            for j in range(5):
                v = random.choice(values)
                s = random.choice(suits)
                while (v, s) in drawn:
                    v = random.choice(values)
                    s = random.choice(suits)
                drawn.append((v, s))
                self.players[player].append((v, s))
        
    def winner(self):
        player_values = {}
        winners = []
        for p in list(self.players.keys()):
            player_values[p] = []
            winners.append(p)
            for i in range(5):
                player_values[p].append(self.players[p][i][0])
        maximum = 0
        count = 0
        while (len(winners) > 1) and (count < 5):
            maximum = 0
            for p in winners:
                c = max(player_values[p])
                player_values[p].remove(c)
                if c > maximum:
                    winners = [p]
                    maximum = c
                elif c == maximum:
                    winners.append(p)
            count = count + 1
        return winners
    
    def run_game(self):
        convert = {2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 
                   10:'10', 11:'J', 12:'Q', 13:'K', 14:'A'}
        self.deal_cards()
        print()
        for p in self.players:
            cards = []
            for i in range(5):
                cards.append(convert[self.players[p][i][0]] + 
                             self.players[p][i][1])
            print(str(p) + ": " + str(cards))
        winners = self.winner()
        print()
        if len(winners) == 1:
            print("Winner is: " + winners[0])
        else:
            print("Winners are: " + winners)
        again = input("Play another hand? Press Y or N: ")
        while again == 'Y':
            self.deal_cards()
            print()
            for p in self.players:
                cards = []
                for i in range(5):
                    cards.append(str(self.players[p][i][0]) + 
                                 str(self.players[p][i][1]))
                print(str(p) + ": " + str(cards))
            winners = self.winner()
            print()
            if len(winners) == 1:
                print("Winner is: " + winners[0])
            else:
                print("Winners are: " + winners)
            again = input("Play another hand? Press Y or N: ")
        
game = PokerGame()
game.run_game()
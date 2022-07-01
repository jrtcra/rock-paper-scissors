from colorama import Fore, Back, Style, init
from plumbum import cli 
from pyfiglet import Figlet
import yaml, ruamel.yaml
import questionary
from questionary import prompt
import os, fnmatch, sys
import random
from os import path
import time

user = ""
user_file = ""
games_won = "won.txt"
games_lost = "lost.txt"

init(autoreset=True)

def print_banner(text):
    print(Fore.RED + Figlet(font='slant').renderText(text))

def add_score(result):
    if result == "lost":
        with open(games_lost, 'a') as entry:
            entry.write("\n1")
    elif result == "won":
        with open(games_won, 'a') as entry:
            entry.write("\n1")
    else:
        return

def add_file():
    user_entry = user + ".txt"
    open(user_entry, 'x')
    print("Created Entry ", user_entry)

def see_score():
    wonscore = open(games_won, 'r')
    content = wonscore.readlines()
    w = 0
    for line in content:
        for i in line:
            if i.isdigit() == True:

                w += int(i)
    print("Games Won: ", w)

    lostscore = open(games_lost, 'r')
    content = lostscore.readlines()
    l = 0
    for line in content:
        for i in line:
            if i.isdigit() == True:

                l += int(i)
    print("Games Lost: ", l)

    main_menu()

def play_game():

    handList = ['Rock', 'Paper', 'Scissors']

    hand = random.choice(handList)

    choice = questionary.select(
        "Choose your hand!",
        choices=[
            'Rock',
            'Paper',
            'Scissors'
        ]).ask()

    if choice == 'Rock' and hand == 'Rock':
        print("The Hand chose...")
        time.sleep(1)
        print_banner(hand + "!")
        time.sleep(0.5)
        print("Tie! Try Again")
        play_game()
    elif choice == 'Rock' and hand == 'Paper':
        print("The Hand chose...")
        time.sleep(1)
        print_banner(hand + "!")
        time.sleep(0.5)
        print("You Lost!")
        add_score("lost")
    elif choice == 'Rock' and hand == 'Scissors':
        print("The Hand chose...")
        time.sleep(1)
        print_banner(hand + "!")
        time.sleep(0.5)
        print("You Won!")
        add_score("won")
    elif choice == 'Paper' and hand == 'Paper':
        print("The Hand chose...")
        time.sleep(1)
        print_banner(hand + "!")
        time.sleep(0.5)
        print("Tie! Try Again")
        play_game()
    elif choice == 'Paper' and hand == 'Scissors':
        print("The Hand chose...")
        time.sleep(1)
        print_banner(hand + "!")
        time.sleep(0.5)
        print("You Lost!")
        add_score("lost")
    elif choice == 'Paper' and hand == 'Rock':
        print("The Hand chose...")
        time.sleep(1)
        print_banner(hand + "!")
        time.sleep(0.5)
        print("You Won!")
        add_score("won")
    elif choice == 'Scissors' and hand == 'Scissors':
        print("The Hand chose...")
        time.sleep(1)
        print_banner(hand + "!")
        time.sleep(0.5)
        print("Tie! Try Again")
        play_game()
    elif choice == 'Scissors' and hand == 'Rock':
        print("The Hand chose...")
        time.sleep(1)
        print_banner(hand + "!")
        time.sleep(0.5)
        print("You Lost!")
        add_score("lost")
    elif choice == 'Scissors' and hand == 'Paper':
        print("The Hand chose...")
        time.sleep(1)
        print_banner(hand + "!")
        time.sleep(0.5)
        print("You Won!")
        add_score("won")

    main_menu()

def main_title():
    print_banner("ROCK")
    print_banner("PAPER")
    print_banner("SCISSORS")

def main_menu():
    print("")
    choice = questionary.select(
        "What would you like to do",
        choices=[
            'Play',
            'See Score',
            'Quit'
    ]).ask()

    if choice == "Play":
            play_game()
    elif choice == 'See Score':
            see_score()
    elif choice == 'Quit':
            pass

class RPS(cli.Application):
    VERSION = '1.0'

    def main(self):
        global user, user_file
        main_title()
        main_menu()

if __name__ == "__main__":
    RPS() 
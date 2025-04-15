# Need the program to randomise three choices

import os
import sys
from colorama import Fore, Style
import time
import random
from collections import Counter


game_list = ['rock', 'paper', 'scissors']

print(Fore.MAGENTA + 'Welcome to Rock, Paper, Scissors - are you ready to beat the computer? \nScore 3 to win the game!')

def countdown(time_secs):
    while time_secs:
        minutes, seconds = divmod(time_secs,
                            60)  # takes two numbers and returns a pair of numbers consisting of their quotient and remainder
        time_format = '{:02d}:{:02d}'.format(minutes, seconds)  # formatting countdown
        print(Fore.CYAN + Style.BRIGHT + 'Computer is choosing... Please wait {} seconds'.format(time_format),
              end='\n')  # overwrites the output for each iteration (each second)
        time.sleep(1)  # restart by default when time runs out
        time_secs -= 1  # decreases by one each second (each iteration)

total_player_score = Counter({'score': 0}) # Score counter
while total_player_score['score'] < 3:
        while True:
            player_choice = input(Fore.MAGENTA + 'Rock, Paper or Scissors?')
            player_choice = player_choice.lower()
            if player_choice in game_list:
                break # exit if one of the three
            else:
                print(Fore.RED + 'Please choose rock, paper or scissors')

        countdown(3) # 3 seconds countdown
        computer_choice = random.choice(game_list).lower()
        print(Fore.CYAN + Style.BRIGHT + 'The computer chose ' + computer_choice + '!')

        if computer_choice == player_choice:
            print('You draw! Try again...')
        elif (computer_choice == 'rock' and player_choice == 'paper') or \
             (computer_choice == 'paper' and player_choice == 'scissors') or \
             (computer_choice == 'scissors' and player_choice == 'rock'):
            total_player_score['score'] += 1
            print('You win!')
        else:
            total_player_score['score'] -= 1
            print('You lose!')

        print(f'Your current score is {total_player_score["score"]}!\n')

print('Well done - you beat the computer!\n')

while True:
    play_again = input(Fore.MAGENTA + 'Would you like to play again?')
    play_again = play_again.lower()
    if play_again == 'yes':
        os.execl(sys.executable, sys.executable, *sys.argv)  # restarts program
    elif play_again == 'no':
        print(Fore.MAGENTA + 'Thank you for playing! Visit again soon!')
        break
    else:
        print(Fore.RED + 'Please type yes or no.')

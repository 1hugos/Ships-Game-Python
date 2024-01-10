import os
import Game
import Start
from colorama import Fore, Style
from tabulate import tabulate
import json


@staticmethod
def show():
    print(f"{Fore.GREEN}Stats:  {Style.RESET_ALL}", end="\n")
    read()
    input("\nPress ENTER to return to the main menu...")
    Start.Menu()

@staticmethod
def save(who_won):
    round_number = str(Game.round_number())

    with open('stats.json', 'r') as json_file:
        json_data = json_file.read()

    data = json.loads(json_data)

    data+= [
    [data[len(data)-1][0]+1, who_won, round_number]
    ]

    with open('stats.json', 'w') as json_file:
        json_file.write(json.dumps(data))
   
@staticmethod
def read():
    with open('C:/Users/spart/OneDrive/Pulpit/Statki_GIT/Statki/stats.json', 'r') as json_file:
        json_data = json_file.read()

    data = json.loads(json_data)
    headers = ["Index", "Who won", "Round"]
    table = tabulate(data, headers, tablefmt="grid")
    print(table)
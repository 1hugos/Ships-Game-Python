import Game
from tabulate import tabulate
from colorama import Fore, Style

def player_map_draw(player_map):
    print("\t<PLAYER MAP>")
    print("   A  B  C  D  E  F  G  H")
    print("—————————————————————————————")
    for i in range(len(player_map)):
        print(f"{i + 1}| ", end="")
        for j in range(len(player_map[i])):
            if player_map[i][j] == 'A':
                print(f"{Fore.GREEN}⛴  {Style.RESET_ALL}", end="")
            elif player_map[i][j] == 'B' or player_map[i][j] == 'C':
                print(f"{Fore.YELLOW}⛴  {Style.RESET_ALL}", end="")
            elif player_map[i][j] == 'D' or player_map[i][j] == 'E' or player_map[i][j] == 'F':
                print(f"{Fore.BLUE}⛴  {Style.RESET_ALL}", end="")
            elif player_map[i][j] == 'X':
                print(f"{Fore.RED}X  {Style.RESET_ALL}", end="")
            elif player_map[i][j] == 'O':
                print(f"{Fore.WHITE}O  {Style.RESET_ALL}", end="")
            else:
                print("•  ", end="")
        print(f"|{i + 1}")
    print("—————————————————————————————")
    print("   A  B  C  D  E  F  G  H\n")

def enemy_map_draw():
    print("\t<ENEMY MAP>")
    print("   A  B  C  D  E  F  G  H")
    print("—————————————————————————————")
    
    for i in range(len(Game.enemyMap)):
        print(f"{i + 1}| ", end="")
        for j in range(len(Game.enemyMap[i])):
            if Game.enemyMap[i][j] == '':
                print("•  ", end="")
            elif Game.enemyMap[i][j] in ['A', 'B', 'C', 'D', 'E', 'F']:
                print("•  ", end="")
            elif Game.enemyMap[i][j] == 'X':
                print(f"{Fore.RED}X  {Style.RESET_ALL}", end="")
            elif Game.enemyMap[i][j] == 'O':
                print(f"{Fore.WHITE}O  {Style.RESET_ALL}", end="")
        print(f"|{i + 1}")
    
    print("—————————————————————————————")
    print("   A  B  C  D  E  F  G  H\n")




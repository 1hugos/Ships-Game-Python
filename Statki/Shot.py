import random
import Game
import Map
import Ships
from colorama import Fore, Style, init

def get_coordinates():
    while True:
        choice = input("Enter the coordinates: [A-H][1-8]: ")
        if len(choice) == 2 and 'A' <= choice[0].upper() <= 'H' and '1' <= choice[1] <= '8':
            x = choice[0].upper()
            y = int(choice[1])
            return x, y

def convert_coordinates(x):
    return ord(x) - ord('A') + 1

def try_shot():
    print("————————————————————————————————————————\nTry to shoot the enemy's ship: ")
    shooted = False
    
    x, y = get_coordinates()
    z = convert_coordinates(x)
    
    if Game.playerShooted[y - 1][z - 1]:
        print("Choose another position!!!")
        try_shot()
    
    print("\n————————————————————————————————————————")
    
    temp = Game.enemyMap[y - 1][z - 1]
    if temp in ['A', 'B', 'C', 'D', 'E', 'F']:
        Game.enemyMap[y - 1][z - 1] = 'X'
        shooted = True
        print(Fore.GREEN + f"Player HIT at: {x}-{y}" + Style.RESET_ALL)
    else:
        Game.enemyMap[y - 1][z - 1] = 'O'
        print(Fore.RED + f"Player MISS at: {x}-{y}" + Style.RESET_ALL)
    
    Game.playerShooted[y - 1][z - 1] = True
    is_ship_sunk(temp, Game.enemyMap)
    
    print("————————————————————————————————————————")
    
    Map.enemy_map_draw()
    
    print("————————————————————————————————————————")
    if shooted and Ships.any_ship_exist(Game.enemyMap):
        try_shot()

def enemy_smart_shot():
    rand = random.Random()
    x = ' '
    hit = False
    miss = False
    direction = rand.randint(0, 3)
    ship_a, ship_b, ship_c, ship_d, ship_e, ship_f = False, False, False, False, False, False
    
    while not hit:
        row = rand.randint(0, 7)
        col = rand.randint(0, 7)
        
        x = chr(ord('A') + col)
        
        if Game.playerMap[row][col] not in ['X', 'O']:
            if Game.playerMap[row][col] in ['A', 'B', 'C', 'D', 'E', 'F']:
                print(Fore.GREEN + f"Enemy HIT at: {x}-{row + 1}" + Style.RESET_ALL)
                temp = Game.playerMap[row][col]
                Game.playerMap[row][col] = 'X'
                is_ship_sunk(temp, Game.playerMap)
                hit = True
                
                while hit and not miss:
                    if not any([ship_a, ship_b, ship_c, ship_d, ship_e, ship_f]):
                        if direction == 0 and row > 0:
                            row -= 1
                        elif direction == 1 and row < 7:
                            row += 1
                        elif direction == 2 and col > 0:
                            col -= 1
                        elif direction == 3 and col < 7:
                            col += 1
                        else:
                            direction = (direction + 1) % 4

                        x = chr(ord('A') + col)
                        
                        if Game.playerMap[row][col] not in ['X', 'O']:
                            if Game.playerMap[row][col] in ['A', 'B', 'C', 'D', 'E', 'F']:
                                print(Fore.GREEN + f"Enemy HIT at: {x}-{row + 1}" + Style.RESET_ALL)
                                temp1 = Game.playerMap[row][col]
                                Game.playerMap[row][col] = 'X'
                                is_ship_sunk(temp1, Game.playerMap)
                            else:
                                print(Fore.RED + f"Enemy MISS at: {x}-{row + 1}" + Style.RESET_ALL)
                                Game.playerMap[row][col] = 'O'
                                miss = True
                    else:
                        break
            else:
                print(Fore.RED + f"Enemy MISS at: {x}-{row + 1}" + Style.RESET_ALL)
                Game.playerMap[row][col] = 'O'
                hit = True

    print("————————————————————————————————————————")
    Map.player_map_draw(Game.playerMap)


def is_ship_sunk(ship_size, map):
    is_sunk = all(map[i][j] != ship_size for i in range(8) for j in range(8))
    
    if is_sunk:
        if ship_size == 'A':
            print(Fore.RED + "Ship of size 4 has been sunk!" + Style.RESET_ALL)
        elif ship_size in ['B', 'C']:
            print(Fore.RED + "Ship of size 3 has been sunk!" + Style.RESET_ALL)
        elif ship_size in ['D', 'E', 'F']:
            print(Fore.RED + "Ship of size 2 has been sunk!" + Style.RESET_ALL)

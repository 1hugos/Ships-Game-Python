import random
from colorama import Fore, Style

@staticmethod
def random_ships_on_map():
    map = [['' for _ in range(8)] for _ in range(8)]
    ship_sizes = [4, 3, 3, 2, 2, 2]
    ship_types = ['A', 'B', 'C', 'D', 'E', 'F']
    ship_count = 0
    for i in range(len(ship_sizes)):
        placed = False
        while not placed:
            row = random.randint(0, 7)
            col = random.randint(0, 7)
            is_horizontal = random.choice([True, False])
            if is_horizontal:
                if col + ship_sizes[i] <= 8:
                    can_place = all(map[row][j] == '' for j in range(col, col + ship_sizes[i]))
                    if can_place:
                        for j in range(col, col + ship_sizes[i]):
                            map[row][j] = ship_types[ship_count]
                        placed = True
                        ship_count += 1
            else:
                if row + ship_sizes[i] <= 8:
                    can_place = all(map[j][col] == '' for j in range(row, row + ship_sizes[i]))
                    if can_place:
                        for j in range(row, row + ship_sizes[i]):
                            map[j][col] = ship_types[ship_count]
                        placed = True
                        ship_count += 1
    print("   A  B  C  D  E  F  G  H")
    print("—————————————————————————————")
    for i in range(len(map)):
        print(f"{i + 1}| ", end="")
        for j in range(len(map[i])):
            if map[i][j] == 'A':
                print(f"{Fore.GREEN}⛴  {Style.RESET_ALL}", end="")
            elif map[i][j] == 'B' or map[i][j] == 'C':
                print(f"{Fore.YELLOW}⛴  {Style.RESET_ALL}", end="")
            elif map[i][j] == 'D' or map[i][j] == 'E' or map[i][j] == 'F':
                print(f"{Fore.BLUE}⛴  {Style.RESET_ALL}", end="")
            else:
                print("•  ", end="")
        print(f"|{i + 1}")
    print("—————————————————————————————")
    print("   A  B  C  D  E  F  G  H\n")
    return map

@staticmethod
def any_ship_exist(tablica):
    for i in range(len(tablica)):
        for j in range(len(tablica[i])):
            if tablica[i][j] in ['A', 'B', 'C', 'D', 'E', 'F']:
                return True
    return False
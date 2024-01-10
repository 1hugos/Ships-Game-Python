import Shot
import Ships
import Stats
import Game

playerMap = [[' ' for _ in range(8)] for _ in range(8)]
playerShooted = [[False for _ in range(8)] for _ in range(8)]  # tablica sprawdzająca czy strzelano w dane pole
enemyMap = [[' ' for _ in range(8)] for _ in range(8)]
roundNumber = 1

def round_number():
    return roundNumber - 1

def play_round():
    print("\t    ROUND\033[0;31m\n" +
          "\t  ▄███▄███▄\n" +
          f"\t  ███\033[0m {Game.roundNumber} \033[0;31m███\n" +
          "\t   ▀█████▀ \n" +
          "\t     ▀█▀\033[0m")
    Shot.try_shot()

    if Ships.any_ship_exist(Game.enemyMap):
        Shot.enemy_smart_shot()
    
    Game.roundNumber += 1

def play_game():
    print("\t<ENEMY MAP>")
    Game.enemyMap = Ships.random_ships_on_map()
    print("\t<PLAYER MAP>")
    Game.playerMap = Ships.random_ships_on_map()

    while True:
        play_round()
        if not Ships.any_ship_exist(Game.playerMap) or not Ships.any_ship_exist(Game.enemyMap):
            break

    if not Ships.any_ship_exist(Game.playerMap):
        Stats.save("Computer")
        print("Computer won the game!")
    elif not Ships.any_ship_exist(Game.enemyMap):
        Stats.save("Player")
        print("Player won the game!")
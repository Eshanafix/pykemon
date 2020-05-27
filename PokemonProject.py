#Hello :)

from random import randint
import sys

def run_game():
    print(input("Hi! Sorry to keep you waiting. "))
    print(input('Welcome to the World of Pokemon! '))
    print(input('My name is Birch, but everyone calls me the pokemon professor. '))
    print(input('This is what we call a Pokemon! '))
    print(input('*Birch pulls out a pokeball and there\'s a large flash of a light, three creatures pop out* '))
    print(input('These are Charmander, Squirtle, and Bulbasaur. They are what we call Starter Pokemon! '))
    print(input('Now, I\'m sure you are aware this reality is not real, so all you have to do is overcome every obstacle on route 1 and you will win! '))
    player = selectPokemon()
    route_1(player)


class pokemon:

    def __init__(self,name,health,damage):
        self.name = name
        self.health = health
        self.damage= damage
    def setHealth(self,health):
        self.health = health
    def setDamage(self,damage):
        self.damage = damage



class trainer:
    def __init__(self,name,pet):
        self.name = name
        self.pet = pet

def selectPokemon():
    pl_name = input('Before we continue, please tell me your name: ')
    print(input('Brilliant! From your name alone I can tell you have a bright future '))
    po_name = input('''And for the moment you have been waiting for, please tell me what pokemon you want!
    1) Charmander
    2) Bulbasaur
    3) Squirtle
    Choice: ''')

    if(int(po_name) == 1):
        new_player = trainer(pl_name,pokemon('Charmander', 20, randint(5,7)))
    elif(int(po_name) == 2):
        new_player = trainer(pl_name,pokemon('Bulbasaur', 20, randint(5,7)))
    elif(int(po_name) == 3):
        new_player = trainer(pl_name,pokemon('Squirtle', 20, randint(5,7)))
    else:
        print('You\'ve dissapointed me. goodbye...')
        sys.exit()
    print(input(f'So it\'s {new_player.pet.name}, congratulations {new_player.name}! Now go and beat route 1! '))
    print(input('*You travel to the entrance of route 1* '))

    return new_player

def createPokemon():
    enemy_list = [pokemon("Palkia", 10, randint(2,4)), pokemon("Dialga", 10, randint(2,4)), pokemon("Mewtwo", 10, randint(2,4)), pokemon("Rasputin", 10, randint(2,4)), pokemon("Ho-Oh", 10, randint(2,4))]
    return enemy_list

def route_1 (player):
    enemies = createPokemon()
    rounds_left = 4
    enemynum = 4
    
    while player.pet.health > 0 and rounds_left >= 1:
        choice = (input(""" What will you do...
        1) Go forward
        2) Be a Bitch and Go Home
        Choose:  """))
        
        if(int(choice) == 1):
            battleVar = randint(1,10)
            if(battleVar == 1):
                print(input('Congrats! You passed through tall grass successfully, move on '))
                rounds_left -= 1
            else:
                print(input('Oh no! You encountered a wild pokemon, get ready for battle! '))
                battleEnemy = enemies[randint(0,enemynum)]
                enemynum -= 1
                print(input(f'I choose {player.pet.name}! '))
                print(input('*intense battle music plays* '))
                while(player.pet.health > 0 and battleEnemy.health > 0):
                    print(input(f"{player.pet.name}, health: {player.pet.health} VS {battleEnemy.name}, health: {battleEnemy.health} "))
                    b_choice = input('''What will you do...
                    1) Tackle
                    2) Run 
                    Choice: ''')
                    if(int(b_choice) == 1):
                        battleEnemy.setHealth(battleEnemy.health - player.pet.damage)
                        print(input(f'{player.pet.name} used tackle! {battleEnemy.name} goes down to {battleEnemy.health} health! Nice Attack!'))
                        if(battleEnemy.health <= 0):
                            print(input(f'Congrats! You defeated {battleEnemy.name}. Move on '))
                            battleEnemy.setHealth(10) 
                            rounds_left -= 1
                            break
                    else:
                        run = randint(1,10)
                        if(run == 1):
                            print(input('Congrats! You successfully ran away! move on '))
                            break
                            #check if run is 1 for enemy attack, add text for defeating enemy
                        else:
                            print(input('You were unable to run away! '))
                    player.pet.setHealth(player.pet.health - battleEnemy.damage)        
                    print(input(f'{battleEnemy.name} used Hyper Beam! {player.pet.name} goes down to {player.pet.health} health! Be Careful!'))
                    if(player.pet.health <= 0):
                        print(input("Oh no! You lost, please retreat!"))
                        sys.exit()
                       
        else:
           print(input('coward...'))
           sys.exit()
    print(input("Congratulations! You completed route 1!! Please check back later to see if our simulation has been updated. Have a good day."))


run_game()

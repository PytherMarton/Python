from colorama import Fore, Back, Style
import time,sys,os
import random

os.system("cls")


def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)

def typingPrintFast(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.03) 

def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value 


print("      .--'''--.    ...----''''''------..........------''''''---...    .--''--.\n"
"     |         |  |     _   _   ___  ___    ___   ___   ___       |  |        |\n"
"     |         '--'    | |_| | | __| |  \  /   \ | __| / __|      '--'        |\n"
"     |         |  |    | |_| | | _|  |__/  |   | | _|  \___\      |  |        |\n"
"     |         |  |    |_| |_| |___| |   \ \___/ |___| |___/      |  |        |\n"
"     |         |  |                                               |  |        |\n"
"     |         |  |           Textbased RPG by @Team Us           |  |        |\n"
"     |.--''--. |  |...----''''''------..........------''''''---...|  |.--''--.|\n"
"      '      '.--.'                                             '.--.'      '\n"
)

time.sleep(2)

print(Fore.RED +"                    |--__\n"
"                    |\n"
"                    X\n"
"     |-___         / \           |-_\n"
"     |            ~~~~~          |\n "
"    X            | .:|          X\n"
"    / \___________| O |_________/ \ \n"
"   /~~~~         |:  . |       ~~~~\ \n"
"   |.: |________| .   : |______|: .|\n"
"   |  :|.       :  ...   :     |.  |\n"
"   | .          .  |||   .        :|\n"
"   WWW____________' ' '________WWWWW\n"
"   --         ____-      ____--_\n"
)

time.sleep(1)

typingPrintFast(Fore.GREEN +"As the darkness rises over the land of the hailvaara, the ancient will bring the demise and destruction to all light of the west and north, many have stood up and were a battle that a last hope, but that faded when there light overshadowed the darkness might they fought bravely and as shiny beacon they brought us time to find the destined hero that will light us through this era of crisis and darkness the light will shine again and keep the darkness away forever.\n")

print(Style.RESET_ALL)

time.sleep(1)
town_drunk_health = 20
warrior_health = 200
wolf_health = 35
ogre_health = 50
troll_health = 50

typingPrint(Back.BLUE +"Put inputs as the first letter of the action you wish to take.\n")
print(Style.RESET_ALL)

def tutorial():
    global town_drunk_health
    global warrior_health
    if town_drunk_health > 0:
        typingPrint("The Town Drunk is ready for battle?\n")
        attack = input("What action will you take?\nAttack\nDefend\n")
        attack = attack.lower()
        if attack == "a":
            print("                            _\n"
"                          .!=!.\n"
"                          \===/\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                         .-----.\n"
"                     /\__:-----:__/\ \n"
"                   ./ ._. \.-./ ._. \. \n"
"                 ./ ./  -.  V  .-  \. \.\n"
"                /__/      \   /      \__\ \n"
"                          |! !|\n"
"                          |! !|\n"
"                         / . . \ \n"
"                        |!.V V.!| \n"
"                         \. V ./ \n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                           \V/\n"
"                            '"
  )
            warrior_damage = random.randint(4,6)
            typingPrint("Town Drunk took ")
            typingPrint(Fore.RED +f"{warrior_damage} damage.\n")
            print(Style.RESET_ALL)
            time.sleep(1)
            town_drunk_health = town_drunk_health - warrior_damage
            if town_drunk_health < 0:
                town_drunk_health = 0
            else:
                town_drunk_health = town_drunk_health
            typingPrint("Town Drunk has ")
            typingPrint(Fore.GREEN +f"{town_drunk_health} HP remaining! ")
            print(Style.RESET_ALL)
            time.sleep(1)
            typingPrint("Town Drunk is confused.\n")
            time.sleep(1)
            coin_flip = random.randint(1,2)
            if coin_flip == 1:
                typingPrint("Town Drunk hit itself in confusion.\n")
                town_drunk_health -= 4
                if town_drunk_health < 0:
                    town_drunk_health = 0
                else:
                    town_drunk_health = town_drunk_health
                typingPrint("Town Drunk has ")
                typingPrint(Fore.GREEN +f"{town_drunk_health} HP remaining!\n")
                print(Style.RESET_ALL)
                typingPrint("Lucky!\n")
                print("--------------------")
                time.sleep(1)
                tutorial()
            else:
                town_drunk_attack = random.randint(10, 20)
                typingPrint("Town Drunk hits you in confusion!\n")
                typingPrint("Town Drunk deals ")
                typingPrint(Fore.RED + f"{town_drunk_attack} damage!\n")
                print(Style.RESET_ALL)
                warrior_health -= town_drunk_attack
                typingPrint("You have ")
                typingPrint(Fore.BLUE + f"{warrior_health} HP remaining!\n")
                print(Style.RESET_ALL)
                typingPrint("How Unlucky!\n")
                print("--------------------")
                time.sleep(1)
                tutorial()
        elif attack == "d":
            town_drunk_attack = random.randint(15,25)
            warrior_armour = 5
            print("           _____________________________________________\n"
  "           \-------------------------------------------/\n            "
"V_________________________________________V\n"
"            |                |         |              |\n"
"            |                |         |              |\n"
"            |                |         |              |\n"
"            |                |         |              |\n"
"             \_______________|         |_____________/ \n"
"             (                                       )\n"
"              (                                     )\n"
"               V                                   V\n"
"               (____________.          .___________)\n"
"                V           |          |         V\n"
"                  V         |          |        V\n"
"                   V        |          |       V\n"
"                    V       |          |      V\n"
"                     V      |          |     V\n"
"                      V     |          |    V\n"
"                       V____|__________|___V\n"
"                        \___[.________.]__/")
            typingPrint("Town Drunk attacks!\n")
            typingPrint("You defend skillfully!\n")
            time.sleep(1)
            town_drunk_attack -= warrior_armour
            typingPrint("Town drunk deals ")
            typingPrint(Fore.RED +f"{town_drunk_attack}!\n")
            print(Style.RESET_ALL)
            warrior_health = warrior_health - town_drunk_attack
            typingPrint("You have ")
            typingPrint(Fore.BLUE + f"{warrior_health} HP remaining!\n")
            time.sleep(1)
            print(Style.RESET_ALL)
            reflection = town_drunk_attack - 10
            typingPrint("You deal ")
            typingPrint(Fore.RED + f"{reflection} in reflection damage!\n")
            print(Style.RESET_ALL)
            town_drunk_health -= reflection
            if town_drunk_health <= 0:
                town_drunk_health = 0
            else:
                town_drunk_health = town_drunk_health    
            typingPrint("Town Drunk has ")
            typingPrint(Fore.GREEN + f"{town_drunk_health} Hp remaining!\n")
            print(Style.RESET_ALL)
            print("--------------------")
            time.sleep(1)
            tutorial()
        else:
            print(Back.RED +"Invalid Input")
            print(Style.RESET_ALL)

            time.sleep(1)
            tutorial()
    else:
        typingPrint("The Town Drunk has been defeated!\n")
        typingPrint("The adventure continues!\n")


tutorial()
time.sleep(2)

os.system("cls")

typingPrint(Fore.GREEN +"The Town Drunk has been defeated!\n The adventure continues!\n")
print(Style.RESET_ALL)
time.sleep(1)

print(" .------------------.  .-----------------.  .------------------.\n"
     "| .----------------. || .---------------. || .----------------.  |\n"
     "| |                | || |      --       | || |                 | |\n"
     "| |  V     V     V | || |     /  \      | || |    /\      /\   | |\n"
     "| |   V   V V   V  | || |    / /\ \     | || |   /  \    /  \  | |\n"
     "| |    V V   V V   | || |   / ---- \    | || |  /    \  /    \ | |\n"
     "| |     V     V    | || | _/ /    \ \_  | || | /      \/      \| |\n"
     "| |                | || ||___|    |___| | || |                 | |\n"
     "| |     Warrior    | || |    Archer     | || |      Mage       | |\n"
     "| '----------------' || '---------------' || '----------------'  |\n"
     " '------------------'  '-----------------'  '------------------'"
)

typingPrint("CHARACTER SELECTION:\n")
print('')
time.sleep(1)
typingPrintFast(Fore.GREEN + "Warrior\n"
    "Weapon type : Steel Sword and Shield\n"
    "max HP : 200\n"
    "DMG Range : 4-6\n"
    "Armor Rating : 5\n"
    "Bio - David the holy warrior of triene is a master of fighting\n"
    "the dark forces of hailvaara he holds no fear as he wields his sword\n"
    "and shield, he instills fear into his enemies that burns deep into\n"
    "their dark souls.\n")
time.sleep(1)
print('')
typingPrintFast(Fore.YELLOW + "Archer\n"
    "Weapon type : Elven Bow and arrows\n"
    "Max HP : 150\n"
    "DMG Range : 2-8\n"
    "Armor Rating : 3\n"
    "Bio - Clara the divine archer originates from the hidden village in the woods,\n"
    "she is a part of the rangers of the north and possesses a bow that gleams light\n"
    "of honour and justice, she never backs down from unimaginable danger,\n"
    "striking mercilessly from the shadows.\n")
time.sleep(1)
print('')
typingPrintFast(Fore.GREEN + "Mage\n"
    "Weapon type : Ash staff\n"
    "max HP : 100\n"
    "DMG Range : 4-10\n"
    "Armor rating : 1\n"
    "Bio - Merlin, the only mage in this region, he creates mostly mess and disfunction\n"
    "but occasionaly he will disply a feat of magic that reminds the locals why they rely\n"
    "on him on a regular basis, whereever he goes he feels compeled to try to help if he can.\n")
time.sleep(1)
print('')
print(Style.RESET_ALL)

def character_selection():
    player=typingInput("Which champion will face this perilous journey? (W/A/M)")
    player = player.lower()
    if player == "w":
        typingPrint("Are you sure you want to choose this character?")
        confirmation = input("YES or NO")
        if confirmation == "y":
            hero = "David, The Holy Knight"
            typingPrint(f"You have chosen {hero}, to face Lun'Kat, The Winged Terror of the Skies!")
        elif confirmation == "n":
            character_selection()
        else:
            typingPrint("Invalid selection, please try again")
            character_selection() 
    elif player == "a":
        typingPrint("Are you sure you want to choose this character?")
        confirmation = input("YES or NO")
        if confirmation == "y":
            hero = "clara, the divine archer"
            typingPrint("You need to complete the game to unlock this character\n")
            character_selection()
        elif confirmation == "n":
            character_selection()
        else:
            typingPrint("Invalid selection, please try again")
            character_selection()
    elif player == "m":
        typingPrint("Are you sure you want to choose this character?")
        confirmation = input("YES or NO")
        if confirmation == "y":
            hero = "Merlin, The Elemental Sage"
            typingPrint("You need to complete the game to unlock this character\n")
            character_selection()
        elif confirmation == "n":
            character_selection()
        else:
            typingPrint("Invalid selection, please try again")
            character_selection()
    else:
        typingPrint("Invalid input! Thats no champion!\n")
        character_selection()
 
character_selection()

time.sleep(2)
os.system("cls")
print("            /\             //\n"
"            \ \           _!_\n"
"             \ \         /___\ \n"
"              \ \        [+++]\n"
"               \ \    _ _\^^^/_ _\n"
"                \ \/ (    '-' ( )\n"
"                /( \/  | {&}  /\ \ \n"
"                  \   / \    /  > )\n"
"                   '''   >::; -''''''-.\n"
"                        /::: /         \ \n"
"                       /  /||    {&}   |\n"
"                      (  /  (\         /\n"
"                      / /    \*-.___.-'\n"
"                    _/ /      \ \ \n"
"                   /___|     /___|\n"
)
typingPrintFast(Fore.GREEN +"As Dave the holy knight enter the forest of dark oaths he sees the\n"
"treeline come into focus and the dark feeling of foreboding awaits him if he enters unprepared\n"
"so he readies him self to face any danger he may face he hears howls and clenches his sword.\n")
print('')
print('')
time.sleep(2)
typingPrint(Fore.GREEN +"There  is a sound from behind and in front of you hear what do you do...\n")
time.sleep(1)
typingPrint("An arrow flies past and you see a wolf fall down I lend you my bow warrior of light.\n")
print(Style.RESET_ALL)
typingPrint("Warrior meets Archer.\n")
typingPrint(Fore.GREEN +"I am Dave the holy night of trine these enemies dont stand a chance against our combined attack they both ready their weapons. I am Clara we wont fall here.\n")
time.sleep(1)
typingPrint("So we all will face this darkness together I dave the holy knight of trien pledge my self to the cause, I clara give my bow to this cause, I rinceword wants to go home but I offer my magic they form the heroes of trein as lightening forms in the sky we are ready.\n")
print(Style.RESET_ALL)
time.sleep(2)
print("                                        __\n"
"                                      .d$$b\n"
"                                    .' TO$;\ \n"
"                                   /  : TP._;\n"
"                                  / _.;  :Tb|\n"
"                                 /   /   ;j$j\n"
"                             _.-''      d$$$$\n"  
"                           .' ..       d$$$$;\n"
"                          /  /P'      d$$$$P.  |\ \n"
"                         /   ''      .d$$$P' |\^''1\n"
"                       .'            'T$P^''''''  :\n"
"                   ._.'      _.'                  ;\n"
"                '.-''.-'-' ._.       _.-''    .-''\n"    
"              '.-''_____  ._                .-''\n"
"            -(.g$$$$$$$b.                  .'\n"
"             ''''^^T$$$P^)               .(:\n"
"                 _/  -'' /.'            /:/;\n"
"              ._.'-''-' '')/            /;/;\n"
"           '-.-''..--''' ''/            /  ;\n"
"          .-'' ..--'''     -'              :\n"
"          ..--'''--.-''      (\         ..-(\ \n"
"            ..--'''            '-\(\/;''\n"
"              _.                     :\n"
"                                     ;'-\n"
"                                    :\ \n"
"                                    ;\n"
)

def fight_wolf():
    global warrior_health
    global wolf_health
    wolf_damage = random.randint(10,15)
    if wolf_health > 0 and warrior_health > 0:
        typingPrint("The Wolf Pack is ready for battle!\n")
        attack = typingInput("What action will you take?\nAttack\nDefend\n")
        attack = attack.lower()
        if attack == "a":
            print("                            _\n"
"                          .!=!.\n"
"                          \===/\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                         .-----.\n"
"                     /\__:-----:__/\ \n"
"                   ./ ._. \.-./ ._. \. \n"
"                 ./ ./  -.  V  .-  \. \.\n"
"                /__/      \   /      \__\ \n"
"                          |! !|\n"
"                          |! !|\n"
"                         / . . \ \n"
"                        |!.V V.!| \n"
"                         \. V ./ \n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                           \V/\n"
"                            '"
  )
            warrior_damage = random.randint(7,10)
            typingPrint("Wolf Pack took ")
            typingPrint(Fore.RED +f"{warrior_damage} damage!\n")
            print(Style.RESET_ALL)
            time.sleep(1)
            wolf_health -= warrior_damage
            if wolf_health < 0:
                wolf_health = 0
            else:
                wolf_health = wolf_health
            typingPrint("Wolf Pack has ")
            typingPrint(Fore.GREEN +f"{wolf_health} HP remaining!\n")
            print(Style.RESET_ALL)
            time.sleep(1)
            wolf_damage = random.randint(10,15)
            warrior_health -= wolf_damage
            if warrior_health < 0:
                warrior_health = 0
            else:
                warrior_health = warrior_health
            typingPrint("You have ")
            typingPrint(Fore.BLUE +f"{warrior_health} HP remaining!\n")
            print(Style.RESET_ALL)
            typingPrint("--------------------\n")
            time.sleep(1)
            fight_wolf()
        elif attack == "d":
            print("           _____________________________________________\n"
  "           \-------------------------------------------/\n            "
"V_________________________________________V\n"
"            |                |         |              |\n"
"            |                |         |              |\n"
"            |                |         |              |\n"
"            |                |         |              |\n"
"             \_______________|         |_____________/ \n"
"             (                                       )\n"
"              (                                     )\n"
"               V                                   V\n"
"               (____________.          .___________)\n"
"                V           |          |         V\n"
"                  V         |          |        V\n"
"                   V        |          |       V\n"
"                    V       |          |      V\n"
"                     V      |          |     V\n"
"                      V     |          |    V\n"
"                       V____|__________|___V\n"
"                        \___[.________.]__/")
            warrior_armour = 5
            typingPrint("The Wolf Packs Attacks!\n")
            typingPrint("You defend cautiosly!\n")
            time.sleep(1)
            wolf_damage = random.randint(10,15)
            wolf_damage -= warrior_armour
            warrior_health -= wolf_damage
            if warrior_health < 0:
                warrior_health = 0
            else:
                warrior_health = warrior_health
            typingPrint("You have ") 
            typingPrint(Fore.BLUE +f"{warrior_health} HP remaining!\n")
            print(Style.RESET_ALL)
            time.sleep(1)
            reflection = int(wolf_damage/2)
            typingPrint("You have dealt ")
            typingPrint(Fore.RED +f"{reflection} reflection damage!\n")
            print(Style.RESET_ALL)
            wolf_health -= reflection
            if wolf_health < 0:
                wolf_health = 0
            else:
                wolf_health = wolf_health
            typingPrint("The Wolf Pack have ") 
            typingPrint(Fore.GREEN +f"{wolf_health} HP remaining!\n")
            print(Style.RESET_ALL)
            typingPrint("You ") 
            typingPrint(Fore.GREEN +"heal 5 HP!")
            print(Style.RESET_ALL)
            warrior_health += 5
            typingPrint("You have ")
            typingPrint(Fore.BLUE +f"{warrior_health} HP remaining!\n")
            print(Style.RESET_ALL)
            typingPrint("--------------------\n")
            time.sleep(1)
            fight_wolf()
        else:
            print(Back.RED +"Invalid Input")
            print(Style.RESET_ALL)
            typingPrint("--------------------\n")
            time.sleep(1)
            fight_wolf()
    elif wolf_health == 0 and warrior_health > 0:
        typingPrint("The Wolf Pack have been defeated!\n")
        typingPrint("The adventure continues!\n")
        typingPrint("--------------------\n")
    else:
        typingPrint("You have been defeated by the mighty wolf pack!\n")
        typingInput("Press any button to get your revenge!\n")
        fight_wolf()

fight_wolf()  

time.sleep(3)
os.system("cls")

typingPrint(Fore.GREEN +"The warrior and the archer continues to walk through the forest...\nThey hear someting.\n")
time.sleep(1)   
typingPrint("Oh no! It's an Ogre!\n")
print(Style.RESET_ALL)
time.sleep(1)
print("                ______                   ______                 ______\n"  
"               ( O  o )                 ( O  o )               ( O  o )              \n"
"              /    0    \              /    0    \            /    0    \ \n"
"             / / |    |\ \            / / |    |\ \          / / |    |\ \ \n"
"            ///\  |  |  ('')         ///\  |  |  ('')       ///\  |  |  ('')\n"
"                   ||                       ||                     ||\n"
"                  /  \                     /  \                   /  \ \n"
"                 _|  |_                   _|  |_                 _|  |_\n"
)
time.sleep(1)
turn = 1
def fight_ogre():
    global warrior_health
    global ogre_health
    global turn
    turn += 1
    if turn%2 == 0:
        if ogre_health > 0 and warrior_health > 0:
            typingPrint("The Ogre Lord is ready for battle!\n")
            attack = typingInput("What action will you take?\nAttack\nDefend\n")
            attack = attack.lower()
            if attack == "a":
                print("                            _\n"
"                          .!=!.\n"
"                          \===/\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                         .-----.\n"
"                     /\__:-----:__/\ \n"
"                   ./ ._. \.-./ ._. \. \n"
"                 ./ ./  -.  V  .-  \. \.\n"
"                /__/      \   /      \__\ \n"
"                          |! !|\n"
"                          |! !|\n"
"                         / . . \ \n"
"                        |!.V V.!| \n"
"                         \. V ./ \n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                           \V/\n"
"                            '"
  )
                warrior_damage = random.randint(9,14)
                typingPrint("Ogre Lord took ")
                typingPrint(Fore.RED +f"{warrior_damage} damage!\n")
                print(Style.RESET_ALL)
                time.sleep(1)
                ogre_health -= warrior_damage
                if ogre_health < 0:
                    ogre_health = 0
                else:
                    ogre_health = ogre_health
                typingPrint("Ogre Lord has ")
                typingPrint(Fore.GREEN +f"{ogre_health} HP remaining!\n")
                print(Style.RESET_ALL)
                time.sleep(1)
                ogre_damage = random.randint(30,60)
                typingPrint("Ogre Lord deals ")
                typingPrint(Fore.RED +f"{ogre_damage} damage!\n")
                print(Style.RESET_ALL)
                warrior_health -= ogre_damage
                if warrior_health < 0:
                    warrior_health = 0
                else:
                    warrior_health = warrior_health
                typingPrint("You have ")
                typingPrint(Fore.BLUE +f"{warrior_health} HP remaining!\n")
                print(Style.RESET_ALL)
                print("--------------------\n")
                time.sleep(1)
                fight_ogre()
            elif attack == "d":
                print("           _____________________________________________\n"
  "           \-------------------------------------------/\n            "
"V_________________________________________V\n"
"            |                |         |              |\n"
"            |                |         |              |\n"
"            |                |         |              |\n"
"            |                |         |              |\n"
"             \_______________|         |_____________/ \n"
"             (                                       )\n"
"              (                                     )\n"
"               V                                   V\n"
"               (____________.          .___________)\n"
"                V           |          |         V\n"
"                  V         |          |        V\n"
"                   V        |          |       V\n"
"                    V       |          |      V\n"
"                     V      |          |     V\n"
"                      V     |          |    V\n"
"                       V____|__________|___V\n"
"                        \___[.________.]__/")
                warrior_armour = 10
                typingPrint("The Ogre Lord Attacks!\n")
                typingPrint("You defend desperately!\n")
                time.sleep(1)
                ogre_damage = random.randint(30,60)
                ogre_damage -= warrior_armour
                typingPrint("The Ogre Lord deals ")
                typingPrint(Fore.RED +f"{ogre_damage} damage!\n")
                print(Style.RESET_ALL)
                warrior_health -= ogre_damage
                if warrior_health < 0:
                    warrior_health = 0
                else:
                    warrior_health = warrior_health
                typingPrint("You have ")
                typingPrint(Fore.BLUE +f"{warrior_health} HP remaining!\n")
                print(Style.RESET_ALL)
                time.sleep(1)
                reflection = int(ogre_damage/2)
                typingPrint("You have dealt ")
                typingPrint(Fore.RED +f"{reflection} reflection damage!\n")
                print(Style.RESET_ALL)
                ogre_health -= reflection
                if ogre_health < 0:
                    ogre_health = 0
                else:
                    ogre_health = ogre_health
                typingPrint("Ogre Lord has ")
                typingPrint(Fore.GREEN +f"{ogre_health} HP remaining!\n")
                print(Style.RESET_ALL)
                typingPrint("You ")
                typingPrint(Fore.GREEN +"heal 5 HP!")
                print(Style.RESET_ALL)
                warrior_health += 5
                typingPrint("You have ")
                typingPrint(Fore.BLUE +f"{warrior_health} HP remaining!\n")
                print(Style.RESET_ALL)
                print("--------------------\n")
                time.sleep(1)
                fight_ogre()
            else:
                print(Back.RED +"Invalid Input")
                print(Style.RESET_ALL)
                print("--------------------\n")
                time.sleep(1)
                fight_ogre()
        elif ogre_health == 0 and warrior_health > 0:
            typingPrint("The Ogre Lord have been defeated!\n")
            typingPrint("The adventure continues!\n")
            print("--------------------\n")
        else:
            typingPrint("You have been defeated by the glorious Ogre Lord!\n")
            typingInput("Press any button to get your revenge!\n")
            fight_ogre()
    else:
        typingPrint("You attack the Ogre Lord!\n")
        warrior_damage = random.randint(9,14)
        typingPrint("Ogre Lord took ")
        typingPrint(Fore.RED +f"{warrior_damage} damage!\n")
        print(Style.RESET_ALL)
        time.sleep(1)
        ogre_health -= warrior_damage
        if ogre_health < 0:
            ogre_health = 0
        else:
            ogre_health = ogre_health
        typingPrint("Ogre Lord has ")
        typingPrint(Fore.GREEN +f"{ogre_health} HP remaining!\n")
        print(Style.RESET_ALL)
        typingPrint("The Ogre Lord is charging up his attack!\n")
        print("--------------------\n")
        fight_ogre()
        
fight_ogre()

time.sleep(3)
os.system("cls")

typingPrint(Fore.GREEN +"They fought bravely and win the fight against the Ogre.\n"
"But thats not the end...\n")
time.sleep(1)
typingPrint("The forest trolls comes out, and you roll out the way and guard yourself.\n")
print(Style.RESET_ALL)
time.sleep(1)
print("       ''''''''''''             ''''''''''''            ''''''''''''\n"
"        \(.\  /.)/               \(.\  /.)/              \(.\  /.)/\n"
"         \  ..  /                 \  ..  /                \  ..  /\n"
"          \ t--/                   \ t--/                  \ t--/\n"
"           \__/                     \__/                    \__/\n"
)

print("       ''''''''''''             ''''''''''''            ''''''''''''\n"
"        \(.\  /.)/               \(.\  /.)/              \(.\  /.)/\n"
"         \  ..  /                 \  ..  /                \  ..  /\n"
"          \ t--/                   \ t--/                  \ t--/\n"
"           \__/                     \__/                    \__/\n"
)

time.sleep(1)
def fight_forest_troll():
    global warrior_health
    global troll_health
    troll_damage = random.randint(10,15)
    if troll_health > 0 and warrior_health > 0:
        typingPrint("The Forest Trolls are ready for battle!\n")
        attack = typingInput("What action will you take?\nAttack\nDefend\n")
        attack = attack.lower()
        if attack == "a":
            print("                            _\n"
"                          .!=!.\n"
"                          \===/\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                         .-----.\n"
"                     /\__:-----:__/\ \n"
"                   ./ ._. \.-./ ._. \. \n"
"                 ./ ./  -.  V  .-  \. \.\n"
"                /__/      \   /      \__\ \n"
"                          |! !|\n"
"                          |! !|\n"
"                         / . . \ \n"
"                        |!.V V.!| \n"
"                         \. V ./ \n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                           \V/\n"
"                            '"
  )
            warrior_damage = random.randint(7,10)
            typingPrint("The Forest Trolls took ")
            typingPrint(Fore.RED +f"{warrior_damage} damage!\n")
            print(Style.RESET_ALL)
            time.sleep(1)
            troll_health -= warrior_damage
            if troll_health < 0:
                troll_health = 0
            else:
                troll_health = troll_health
            typingPrint("Forest Trolls have ")
            typingPrint(Fore.GREEN +f"{troll_health} HP remaining!\n")
            print(Style.RESET_ALL)
            time.sleep(1)
            troll_damage = random.randint(10,15)
            for i in range(2):
                typingPrint("Forest Trolls deal ")
                typingPrint(Fore.RED +f"{troll_damage} damage!\n")
                print(Style.RESET_ALL)
            troll_damage *= 2
            warrior_health -= troll_damage
            if warrior_health < 0:
                warrior_health = 0
            else:
                warrior_health = warrior_health
            typingPrint("You have ")
            typingPrint(Fore.BLUE +f"{warrior_health} HP remaining!\n")
            print(Style.RESET_ALL)
            print("--------------------")
            time.sleep(1)
            fight_forest_troll()
        elif attack == "d":
            print("           _____________________________________________\n"
  "           \-------------------------------------------/\n            "
"V_________________________________________V\n"
"            |                |         |              |\n"
"            |                |         |              |\n"
"            |                |         |              |\n"
"            |                |         |              |\n"
"             \_______________|         |_____________/ \n"
"             (                                       )\n"
"              (                                     )\n"
"               V                                   V\n"
"               (____________.          .___________)\n"
"                V           |          |         V\n"
"                  V         |          |        V\n"
"                   V        |          |       V\n"
"                    V       |          |      V\n"
"                     V      |          |     V\n"
"                      V     |          |    V\n"
"                       V____|__________|___V\n"
"                        \___[.________.]__/")
            warrior_armour = 7
            typingPrint("The Forest Trools Attacks!\n")
            typingPrint("You defend skeptically!\n")
            time.sleep(1)
            troll_damage = random.randint(10,15)
            troll_damage -= warrior_armour
            for i in range(4):
                typingPrint("Forest Trolls have dealt ")
                typingPrint(Fore.RED +f"{troll_damage} damage!\n")
                print(Style.RESET_ALL)
            troll_damage *= 4
            warrior_health -= troll_damage
            if warrior_health < 0:
                warrior_health = 0
            else:
                warrior_health = warrior_health
            typingPrint("You have ")
            typingPrint(Fore.GREEN +f"{warrior_health} HP remaining!\n")
            print(Style.RESET_ALL)
            time.sleep(1)
            reflection = int(troll_damage/2)
            typingPrint("You have dealt ")
            typingPrint(Fore.RED +f"{reflection} reflection damage!\n")
            print(Style.RESET_ALL)
            troll_health -= reflection
            if troll_health < 0:
                troll_health = 0
            else:
                troll_health = troll_health
            typingPrint("The Forest Trolls have ")
            typingPrint(Fore.GREEN +f"{troll_health} HP remaining!\n")
            print(Style.RESET_ALL)
            typingPrint("You ")
            typingPrint(Fore.GREEN +"heal 8 HP!")
            print(Style.RESET_ALL)
            warrior_health += 7
            typingPrint("You have ")
            typingPrint(Fore.BLUE +f"{warrior_health} HP remaining!\n")
            print(Style.RESET_ALL)
            print("--------------------")
            time.sleep(1)
            fight_forest_troll()
        else:
            print(Back.RED +"Invalid Input")
            print(Style.RESET_ALL)
            print("--------------------")
            time.sleep(1)
            fight_forest_troll()
    elif troll_health == 0 and warrior_health > 0:
        typingPrint("The Forest Trolls have been defeated!\n")
        typingPrint("The adventure continues!\n")
        print("--------------------")
    else:
        typingPrint("You have been defeated by the!\n")
        typingInput("Press any button to get your revenge!\n")

fight_forest_troll()

time.sleep(3)
os.system("cls")

typingPrint(Fore.GREEN +"The warrior come across a castle with a light trying to get your interest, but a massive shadow on the bridge of the souls which way will you go?")
print(Style.RESET_ALL)
print("                    |--__\n"
"                    |\n"
"                    X\n"
"     |-___         / \           |-_\n"
"     |            ~~~~~          |\n "
"    X            | .:|          X\n"
"    / \___________| O |_________/ \ \n"
"   /~~~~         |:  . |       ~~~~\ \n"
"   |.: |________| .   : |______|: .|\n"
"   |  :|.       :  ...   :     |.  |\n"
"   | .          .  |||   .        :|\n"
"   WWW____________' ' '________WWWWW\n"
"   --         ____-      ____--_\n"
"              \   \      \   \ \n"
"               \ - \      \ - \ \n"
"                \   \      \   \ \n"
"                 \ - \      \ - \ \n"
"                  \   \      \   \ \n"
"                    ^           ^\n"
"                   Left        Right\n"
)

def path_choice():
    typingPrint(Fore.GREEN +"You have come to fork in the road, which path will you choose? The path to the left leads to forboding bridge, the right path leads to a strangley alluring light.\n")
    print(Style.RESET_ALL)
    answer=typingInput("Will you go left (L) or right(R): \n")
    answer=answer.lower()
    if answer == "l":
       typingPrint("You take the left path towards the bridge.\n")
    elif answer == "r":
       typingPrint("You take the right path towards the light.\n")
path_choice()


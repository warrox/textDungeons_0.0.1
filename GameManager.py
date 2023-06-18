from colorama import Fore
import random
import time


class GameManager:
    chapel_dict = []
    bag_dict = []
    kurbz_dict = [0]

    def __init__(self, game_name: str = "Text Fiasco Dungeon", race: str = "", weapon=None, player_defense: int = 10):
        if weapon is None:
            weapon = []
        self.name = game_name  # Nom du jeu
        self.race = race  # Race pour le joueur
        self.weapon = weapon  # arme choisi
        self.defense_player = player_defense  # point de vie du joueur
        self.race_weapons(self.initialize_game())
        self.scenario(self.direction())

    def race_weapons(self, player):
        if player == 1:
            self.race = "Human"
        if player == 2:
            self.race = "Undead"
        if player == 1 or player == 2:
            weapon_choice = input(Fore.LIGHTGREEN_EX + "type 'knife' to equip or 'Else' ")
        else:
            return
        if weapon_choice.upper() == "knife".upper():
            weapon_choice = "knife"
            self.weapon = weapon_choice
            print("This knife is very sharpe, your attack up to 10 !")
            return weapon_choice
        elif weapon_choice.upper() == "Else".upper():
            weapon_choice = "Banana"
            self.weapon = weapon_choice
            print(Fore.LIGHTYELLOW_EX + "Yous just equipped a banana," + Fore.LIGHTGREEN_EX +
                  " god damn it, pick the good one, next time")
            return weapon_choice
        else:
            print(Fore.RED + "Enter a right command!")
        #  next methode(function)
        self.race_weapons(player)

    def initialize_game(self):
        # Initialize the game
        print("----")
        print(Fore.LIGHTGREEN_EX + f"Welcome in {self.name}")
        print()
        time.sleep(0.7)
        print(
            "This world is dark as you can't see anything in this dungeon, \nyou've heard sometimes a voice far away, this is your only sign ")
        print("----")
        # Race choice
        time.sleep(0.7)
        player_choice = input(f"Choose a race press 1 for human or press 2 for undead ?")
        try:
            int_player_choice = int(player_choice)
        except:
            print("Choose a number")
            print(Fore.RED + "You didn't choose between 1 or 2, Try again")
            return self.initialize_game()
        if int_player_choice == 1:
            time.sleep(0.7)
            print(
                Fore.LIGHTWHITE_EX + "Human specs: Humans are versatile and adaptable, making them ideal for a variety of roles in combat and exploration.\n They are physically strong and quick, with above-average endurance and agility.\n Additionally, humans are known for their quick wit and resourcefulness, making them excellent problem solvers and strategists.")  # INFO : tu dois preciser les specs de cette race
            return int_player_choice
        elif int_player_choice == 2:
            time.sleep(0.7)
            print(
                Fore.LIGHTWHITE_EX + "Undead specs: The undead have several strengths that make them formidable opponents in combat.\n For one, they are immune to many types of attacks that affect living creatures, such as poison and disease.\n Additionally, they have enhanced strength and endurance, \nallowing them to withstand more damage than most other races. \nThe undead also have unique abilities, such as the power to drain the life force of their enemies and the ability to control the dead.")  # INFO : tu dois preciser les specs de cette race
            return int_player_choice
        else:
            print(Fore.RED + "You didn't choose between 1 or 2, Try again")
            self.race_weapons(player_choice)
            return self.initialize_game()  # Retourne la fonction si le user entre en chiffre non compris

    def direction(self):
        d = ['North', 'South', 'East', 'West']
        direction_str = ""
        print()
        time.sleep(1.2)
        if self.kurbz_dict.index([0][0]):
            self.defense_player += 10
        else:
            pass
        print("Back to this dark room, gotta choose a direction")
        print("life remaining " + str(self.defense_player) + " ,Weapon equipped " + self.weapon)
        direction = input("Choose a direction between " + str(d).upper())
        if direction.upper() in str(d).upper():
            direction_str = direction.upper()
        else:
            print("Game over, t'es trop un kassos")
            quit()
        return direction_str


    def scenario(self, b):
        global chapel_dict
        chapel_dict = [{'Name': "Spider", 'Damage': 2, 'Health': 10}, {'Name': "Skull", 'Damage': 2, 'Health': 10}]
        forest_dict = [{'Name': "Gobelin", 'Damage': 1, 'Health': 6}, {'Name': "Gobelin", 'Damage': 1, 'Health': 6},
                       {'Name':
                            "Gobelin", 'Damage': 1, 'Health': 6}, {'Name': "Troll", 'Damage': 4, 'Health': 20}]
        action_choice_int = 0
        # First scenario
        if b == "North".upper():
            print()
            print()
            time.sleep(1.2)
            print(f"You entered into the spider chapel and find a {chapel_dict[0]['Name']} "
                  f"and {chapel_dict[1]['Name']}")
            print()
            time.sleep(0.7)
            print(f"Use your {self.weapon} against {chapel_dict[0]['Name']} and {chapel_dict[1]['Name']}")
            print()
            r = random.randint(0, 1)
            if self.weapon == "Banana":
                try:
                    time.sleep(0.7)
                    action_choice = input("Press 1 to eat the banana or press 2 to throw it into the enemies")
                    action_choice_int = int(action_choice)
                except:
                    print("Choose a number")
            if action_choice_int == 1:
                time.sleep(0.7)
                print("You ate the banana without removing the skin, you're an animal")  # Todo
                time.sleep(0.4)
                print("You're starting to feel a pain into your stomach... want to vomit ?")
                self.defense_player += 15  # boost vie player avec la banana
                print("You boosted your life by 15")
                self.combat_manager(chapel_dict[r]['Damage'], self.defense_player, 1, chapel_dict[r]['Health'],
                                           chapel_dict[r]['Name'])
                self.scenario(self.direction())

            if action_choice_int == 2:
                time.sleep(1.4)
                print(f"{chapel_dict[r]['Name']} is graping and eating the Banana, it increase it life by 15 omg ...")
                print()  # Replace by timer look the egg timer project to import the library
                print()
                print()
                print()
                print()
                # self.chapel_dict[0].__getitem__(2)  # Want to increase health of ennemiy but don't know how to manipulate dictonary
                self.combat_manager(chapel_dict[r]['Damage'], self.defense_player, 1, 25,
                                           chapel_dict[r]['Name'])
                self.scenario(self.direction())

            elif self.weapon == "knife":
                while action_choice_int != 1:
                    try:
                        time.sleep(1.2)
                        action_choice = input(Fore.LIGHTGREEN_EX + "Press 1 to attack with your knife")
                        action_choice_int = int(action_choice)
                    except:
                        print("Choose a number")
                    if action_choice_int == 1:
                        self.combat_manager(chapel_dict[r]['Damage'], self.defense_player, 10, chapel_dict[r]['Health'],
                                            chapel_dict[r]['Name'])  # 2,10,4,8,"Spider"
                        self.scenario(self.direction())
                    else:
                        print(Fore.RED + "Unknown command")
            elif self.weapon == 'BLACKED HEART':
                while action_choice_int != 1:
                    try:
                        time.sleep(1.2)
                        action_choice = input(Fore.LIGHTGREEN_EX + f"Press 1 to attack with your {self.weapon}")
                        action_choice_int = int(action_choice)
                    except:
                        print("Choose a number")
                    if action_choice_int == 1:
                        self.combat_manager(chapel_dict[r]['Damage'], self.defense_player, 15, chapel_dict[r]['Health'],
                                            chapel_dict[r]['Name'])  # 2,10,4,8,"Spider"
                        self.scenario(self.direction())
        #  Second scenario
        if b.upper() == "South".upper():
            time.sleep(1.2)
            print(f"As you set out on your journey to the south, you enter a dense forest.\n "
                  "You hear strange noises coming from the trees, and your instincts tell you to be cautious."
                  "\n Suddenly, a group of goblins jumps out from behind the bushes, wielding sharp weapons and "
                  f"looking fierce.You draw your {self.weapon} and prepare for battle.")
            if self.weapon == "Banana":
                time.sleep(0.4)
                print(f"I can't defeat those enemy with my {self.weapon}, i should come back")
                return self.scenario(self.direction())
            while action_choice_int != 1:
                try:
                    time.sleep(0.7)
                    action_choice = input(Fore.LIGHTGREEN_EX + "Press 1 to attack with your knife")
                    action_choice_int = int(action_choice)
                except:
                    print("Choose a number")
                if action_choice_int == 1:
                    r = random.randint(0, 3)
                    self.combat_manager(forest_dict[r]['Damage'], self.defense_player, 10, forest_dict[r]['Health'],
                                        forest_dict[r]['Name'])
                    self.scenario(self.direction())
                else:
                    print(Fore.RED + "Uknown command")

        # third scenario
        shop = [{'Name': 'BLACKED HEART','Damage': 15},{'Name': 'KURBZ','Power': 'Full regen in the dark room'},
                {'Name': 'BAG','SLOTS': 5}]
        if b.upper() == "East".upper():
            print("After walking hours, you're in the front of  the no face village ")
            print("The No Face Village is cursed, and those who enter it are never seen again. Will you turn back now, "
                  "\n or will you face the horrors that lurk within?")
            c = input("Enter *Go* to enter or *Leave* to go back ?")
            if c.upper() == "Go".upper():
                print(Fore.LIGHTYELLOW_EX + "As you enter the No Face Village, a mysterious figure approaches you with an unsettling grin."
                      "\nGreetings, adventurer. Are you in need of stuff ? "
                      "\n**they ask, their eyes gleaming in the dim light.**")


            elif c.upper() == "Leave".upper():
                return self.scenario(self.direction())
            #  c1 here to not indent the code
            c1 = input("Type yes or no ?")
            if c1.upper() == "yes".upper():
                print("Alright, alright, here is the list of weapons available ")
                time.sleep(0.5)
                print("Blacked heart : 15 damages|price : Free")
                time.sleep(0.5)
                print("Press 1")
                time.sleep(0.5)
                print("Kurbz : regen your health after going back to the dark room |price : Free")
                time.sleep(0.5)
                print("Press 2")
                time.sleep(0.5)
                print("Bag 5 slots|price : Free")
                time.sleep(0.5)
                print("Press 3")
                c2 = input("Enter a command to buy an article")
            elif c1.upper() == "no".upper():
                return self.scenario(self.direction())
            match c2.upper():
                case "1":  # Blacked heart
                    n = self.weapon
                    self.weapon = shop[0]['Name']
                    print(Fore.LIGHTGREEN_EX + f"{n} was replaced by {self.weapon} in your inventory")

                case "2":  # kurbz
                    print(Fore.LIGHTGREEN_EX + f"{shop[1]['Name']} has been equipped")
                    self.kurbz_dict.append(shop[1])
                    self.kurbz_dict[0], self.kurbz_dict[1] = self.kurbz_dict[1], self.kurbz_dict[0]

                case "3":  # Bag 5 slots #todo a finir ...
                    print(Fore.LIGHTGREEN_EX + f"{shop[2]['Name']} has been equipped")
                    self.bag_dict.append(shop[2])
            return self.scenario(self.direction())
        if b.upper() == "West".upper():
            print("You entering into a ominous labyrinth, after a few meters"
                  "\nyou feel lost and can't go back to your previous path, you must choose a way ...")
            c = input("Choose a way to go ? (Left,right,forward,backward)")
        match c.lower():
                case "left":
                    print("you turn left and find yourself in a maze of twisting corridors and darkened chambers. Here, "
                          "\nthey will face off against a pack of snarling werewolves. "
                          "\nThese fierce beasts are strong and ferocious,")
                    c = input("Tap 1 to start the fight")
                    if c == "1":
                        self.combat_manager(10, self.defense_player, 10, 15,
                                            "werewolves")
                        self.combat_manager(10, self.defense_player, 10, 15,
                                            "werewolves")
                        self.combat_manager(10, self.defense_player, 10, 15,
                                            "werewolves")
                        self.scenario(self.direction())
                    else:
                        return self.scenario(self.direction())
                case "right":
                    print("you walk a few meters and found a group of bloodthirsty goblins,"
                          "\narmed with sharp blades and deadly traps")
                    self.combat_manager(2, self.defense_player, 10, 10,
                                        "Bloodthirsty goblins")
                    self.combat_manager(2, self.defense_player, 10, 10,
                                        "Bloodthirsty goblins")
                    self.combat_manager(2, self.defense_player, 10, 10,
                                        "Bloodthirsty goblins")
                    self.combat_manager(2, self.defense_player, 10, 10,
                                        "Bloodthirsty goblins")
                    self.scenario(self.direction())
                case "forward":
                    print("group of twisted and corrupted humans. These humans were once normal, "
                          "\nbut have been transformed by dark magic into something far more sinister. "
                          "\nThey are armed with dark spells and curses, and the user must use their magic and wits to "
                          "\ncounter their attacks and defeat them.")
                    c = input("Tap 1 to start the fight")
                    if c == "1":
                        self.combat_manager(6, self.defense_player, 10, 7,
                                            "Corrupted human")
                        self.combat_manager(6, self.defense_player, 10, 7,
                                            "Corrupted human")
                        self.combat_manager(6, self.defense_player, 10, 7,
                                            "Corrupted human")
                        self.scenario(self.direction())
                    else:
                        return self.scenario(self.direction())
                case "backward":
                    print("they will discover a hidden passage leading to a secret room. "
                          "In the center of the room sits a chest, filled with ancient treasures and powerful artifacts."
                          "\nBut beware: the room is guarded by a fearsome dragon, "
                          "\nand the user must defeat it to claim the chest as their own.")
                    c = input("Tap 1 to start the fight")
                    if c == "1":
                        self.combat_manager(100, self.defense_player, 10, 100,
                                            "Dragon of the abysse")
                        self.scenario(self.direction())
                    else:
                        return self.scenario(self.direction())

    def combat_manager(self, attack_enemy: int, defense_player: int, attack_player: int, defense_enemy: int
                       , enemy_name: str) -> tuple:
        for _ in range(0, defense_player) or range(0, defense_enemy):
            defense_player -= attack_enemy
            self.defense_player = defense_player
            defense_enemy -= attack_player
            print(f" {enemy_name} damage you {attack_enemy}")
            time.sleep(0.3)
            print(f"Health remaining {defense_player}")
            time.sleep(1.4)
            print(f"Your damage: {attack_player} on {enemy_name}")
            time.sleep(0.3)
            print(f"Ennemies health :{defense_enemy}")
            if defense_player <= 0:
                print(Fore.LIGHTRED_EX + "GameOver")
                print(Fore.LIGHTRED_EX + "Try again")
                quit()
            if defense_enemy <= 0:
                print(f"You defeated {enemy_name}, Well done")

                break
        return self.defense_player, defense_enemy

    def eat_manager(self, e):
        print()  # Todo
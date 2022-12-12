class Player:
    def __init__(self, name):
        self.name = name
        self.items_use = True
        self.potions = 1
        if name == "Human":
            self.hp = 75
            self.maxhp = 75
            self.attack = 4
            self.defense = 3
            self.speed = 3
            self.items_use = True
            self.experience = 0
            self.gold = 0
        elif name == "Dwarf":
            self.hp = 120
            self.maxhp = 120
            self.attack = 6
            self.defense = 4
            self.speed = 3
            self.items_use = False
            self.experience = 0
            self.gold = 0
        elif name == "Elf":
            self.hp = 80
            self.maxhp = 80
            self.attack = 5
            self.defense = 2
            self.speed = 4
            self.items_use = False
            self.experience = 0
            self.gold = 0
        elif name == "Hobbit":
            self.hp = 65
            self.maxhp = 65
            self.attack = 3
            self.defense = 2
            self.speed = 4
            self.items_use = True
            self.experience = 0
            self.gold = 0

    def __str__(self):
        return f"Hp: {self.hp}/{self.maxhp}, attack: {self.attack}, defense: {self.defense}, speed: {self.speed}. You have {self.gold} gold and {self.experience} experience points to spend\n"

    def attack_enemy(self, mon):
        if self.attack - mon.defense <= 1:
            hp_loss = 1 * mon.speed
            mon.hp = mon.hp - hp_loss
            print(f"You hit {mon.name} for {hp_loss}")
        else:
            hp_loss = (self.attack - mon.defense) * self.speed
            mon.hp = mon.hp - hp_loss
            print(f"You hit {mon.name} for {hp_loss}")

    def wear_item(self, items, number_of_items):
        no_item_type = True
        if number_of_items > 1:
            for i in range(number_of_items):
                if items[-1].item_type == items[i].item_type and items[-1].item_grade > items[i].item_grade:
                    self.maxhp = self.maxhp + items[-1].hp_bonus - items[i].hp_bonus
                    self.hp = self.hp + items[-1].hp_bonus - items[i].hp_bonus
                    self.attack = self.attack + items[-1].attack_bonus - items[i].attack_bonus
                    self.defense = self.defense + items[-1].defense_bonus - items[i].defense_bonus
                    self.speed = self.speed + items[-1].speed_bonus - items[i].speed_bonus
                    no_item_type = False
                    break
                elif items[-1].item_type == items[i].item_type and items[-1].item_grade < items[i].item_grade:
                    print("You already have a stronger item")
                    no_item_type = False
                    break
        if no_item_type:
            self.maxhp = self.maxhp + items[-1].hp_bonus
            self.hp = self.hp + items[-1].hp_bonus
            self.attack = self.attack + items[-1].attack_bonus
            self.defense = self.defense + items[-1].defense_bonus
            self.speed = self.speed + items[-1].speed_bonus

    def spend_experience(self):
        if self.experience < 1:
            print("\nYou don't have any expierence points to spend!\n")
        else:
            print("\n\nYou can spend your experience points here!\n",
                  "+10 hp costs 2 expierence points\n",
                  "+1 attack costs 4 experience points\n",
                  "+1 defense costs 4 experience points\n",
                  "+1 speed costs 15 experience points\n")
            choice = ""
            while (choice != 'exit' and self.experience > 1):
                while (choice not in ['hp', 'att', 'def', 'sp', 'exit']):
                    print(f"You have {self.experience} experience points left")
                    choice = input("Choose between hp, att, def, sp to increase choosen stat. Write exit to leave instead: ")
                if choice == "exit":
                    break
                elif choice == "hp":
                    self.hp = self.hp + 10
                    self.maxhp = self.maxhp + 10
                    self.experience = self.experience - 2
                    print(self)
                    choice = ""
                elif choice == "att" and self.experience > 3:
                    self.attack = self.attack + 1
                    self.experience = self.experience - 4
                    print(self)
                    choice = ""
                elif choice == "def" and self.experience > 1:
                    self.defense = self.defense + 1
                    self.experience = self.experience - 4
                    print(self)
                    choice = ""
                elif choice == "sp" and self.experience > 14:
                    self.speed = self.speed + 1
                    self.experience = self.experience - 15
                    print(self)
                    choice = ""
            print()

    def use_potion(self):
        if self.potions > 0:
            if self.hp + 25 > self.maxhp:
                self.hp = self.maxhp
            else:
                self.hp = self.hp + 25
                self.potions = self.potions - 1
            print(f"Replenished health. Your currently have {self.hp} hp")
            print(f"You currently have {self.potions} potions")
        else:
            print("You don't have any potions!")
        print()
        
    def find_potion(self):
        self.potions = self.potions + 1
##        color.write("You have found a potion!", "STRING")
        print("You have found a potion!")
                            
class Monster:
    def __init__(self, name):
        self.name = name
        if name in ["Goblin1", "Goblin2", "Goblin3"]:
            self.hp = 10
            self.attack = 2
            self.defense = 1
            self.speed = 2
        if name == "Big goblin1" or name == "Big goblin2" or name == "Big goblin3":
            self.hp = 20
            self.attack = 3
            self.defense = 2
            self.speed = 3
        if name == "Orc1" or name == "Orc2" or name == "Orc3":
            self.hp = 50
            self.attack = 6
            self.defense = 3
            self.speed = 3
        if name in ["Ogre1", "Ogre2", "Ogre3"]:
            self.hp = 90
            self.attack = 10
            self.defense = 5
            self.speed = 3
        if name == "Dragon":
            self.hp = 300
            self.attack = 20
            self.defense = 5
            self.speed = 3
            
    def __str__(self):
        return f"{self.name}. His stats: hp: {self.hp}, attack: {self.attack}, defense: {self.defense}, speed: {self.speed}"

    def attack_enemy(self, player):
        if self.attack - player.defense <= 1:
            hp_loss = 1 * player.speed
            player.hp = player.hp - hp_loss
            #color.write(f"{self.name} hits you for {hp_loss}\n", "COMMENT")
            print(f"{self.name} hits you for {hp_loss}\n")
        else:
            hp_loss = (self.attack - player.defense) * self.speed
            player.hp = player.hp - hp_loss
            #color.write(f"{self.name} hits you for {hp_loss}\n", "COMMENT")
            print(f"{self.name} hits you for {hp_loss}\n")

class Item:
    def __init__(self, name, hp_bonus, attack_bonus, defense_bonus, speed_bonus, item_type, item_grade):
        self.name = name
        self.hp_bonus = hp_bonus
        self.attack_bonus = attack_bonus
        self.defense_bonus = defense_bonus
        self.speed_bonus = speed_bonus
        self.item_type = item_type
        self.item_grade = item_grade
##        color.write(f"You have found a {self.name}!\n", "STRING")
        print(f"You have found a {self.name}!")

        #testing colors
##        color.write(f"You have found a {self.name}!\n", "STRING")
##        color.write(f"You have found a {self.name}!\n", "SYNC")
##        color.write(f"You have found a {self.name}!\n", "stdin")
##        color.write(f"You have found a {self.name}!\n", "BUILTIN")
##        color.write(f"You have found a {self.name}!\n", "console")
##        color.write(f"You have found a {self.name}!\n", "COMMENT")
##        color.write(f"You have found a {self.name}!\n", "stdout")
##        color.write(f"You have found a {self.name}!\n", "TODO")
##        color.write(f"You have found a {self.name}!\n", "stderr")
##        color.write(f"You have found a {self.name}!\n", "hit")
##        color.write(f"You have found a {self.name}!\n", "DEFINITION")
##        color.write(f"You have found a {self.name}!\n", "KEYWORD")
##        color.write(f"You have found a {self.name}!\n", "ERROR")
##        color.write(f"You have found a {self.name}!\n", "sel")
        print(self)

    def __str__(self):
        return(f"{self.name} adds to your stats:\nhp: {self.hp_bonus}, attack: {self.attack_bonus}, defense: {self.defense_bonus}, speed: {self.speed_bonus}")

class Room:
    def __init__(self, name):
        self.name = name
        self.monsters = []
        self.items = []
        if name == "room1":
            self.monsters.append(Monster("Goblin1"))
            self.experience_to_gain = 1
            self.gold_to_gain = 25
        if name == "room2":
            self.monsters.append(Monster("Goblin1"))
            self.monsters.append(Monster("Goblin2"))
            self.experience_to_gain = 2
            self.gold_to_gain = 50
        if name == "room3":
            self.monsters.append(Monster("Big goblin1"))
            self.experience_to_gain = 3
            self.gold_to_gain = 75
        if name == "room4":
            self.monsters.append(Monster("Goblin1"))
            self.monsters.append(Monster("Big goblin1"))
            self.experience_to_gain = 4
            self.gold_to_gain = 100
        if name == "room5":
            self.monsters.append(Monster("Big goblin1"))
            self.monsters.append(Monster("Big goblin2"))
            self.experience_to_gain = 5
            self.gold_to_gain = 125
        if name == "room6":
            self.monsters.append(Monster("Orc1"))
            self.experience_to_gain = 6
            self.gold_to_gain = 150
        if name == "room7":
            self.monsters.append(Monster("Orc1"))
            self.monsters.append(Monster("Goblin1"))
            self.experience_to_gain = 7
            self.gold_to_gain = 200
        if name == "room8":
            self.monsters.append(Monster("Orc1"))
            self.monsters.append(Monster("Orc2"))
            self.experience_to_gain = 8
            self.gold_to_gain = 225
        if name == "room9":
            self.monsters.append(Monster("Big goblin1"))
            self.monsters.append(Monster("Orc1"))
            self.monsters.append(Monster("Goblin1"))
            self.experience_to_gain = 9
            self.gold_to_gain = 250
        if name == "room10":
            self.monsters.append(Monster("Orc1"))
            self.monsters.append(Monster("Orc2"))
            self.monsters.append(Monster("Orc3"))
            self.experience_to_gain = 10
            self.gold_to_gain = 300
        if name == "room11":
            self.monsters.append(Monster("Ogre1"))
            self.experience_to_gain = 11
            self.gold_to_gain = 350
        if name == "room12":
            self.monsters.append(Monster("Orc1"))
            self.monsters.append(Monster("Ogre1"))
            self.experience_to_gain = 12
            self.gold_to_gain = 400
        if name == "room13":
            self.monsters.append(Monster("Big goblin1"))
            self.monsters.append(Monster("Ogre1"))
            self.experience_to_gain = 13
            self.gold_to_gain = 450
        if name == "room14":
            self.monsters.append(Monster("Ogre1"))
            self.monsters.append(Monster("Ogre2"))
            self.experience_to_gain = 14
            self.gold_to_gain = 500
        if name == "room15":
            self.monsters.append(Monster("Ogre1"))
            self.monsters.append(Monster("Ogre2"))
            self.monsters.append(Monster("Dragon"))
            self.experience_to_gain = 15
            self.gold_to_gain = 1000

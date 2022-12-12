from pathlib import Path
import time
from textgame_classes import Player, Monster, Item, Room

def player_choice():
    print()
    player = "none"
    while (player not in ["Human", "Dwarf", "Elf", "Hobbit"]):
        player = input("Please choose between Human, Dwarf, Elf or Hobbit: ")
    player = Player(player)
    return player

def lost():
##    color.write("You die with all your treasures...\n\n", "ERROR")
    print("You die with all your treasures...\n\n")

#Works now, fights all monsters from the list one by one. Not simultaneously yet
def fight(player, mob):
    print("--------------------------------------")
    while mob:
        print(f"***Current monster is {mob[0]}***\n")
        while (mob[0].hp > 0 and player.hp > 0):
            print("HP STATUS")
            print(f"{mob[0].name} hp is {mob[0].hp}")
            print(f"Your hp is {player.hp}")
            print(">>")
            if (mob[0].speed > player.speed):
                mob[0].attack_enemy(player)
                if player.hp <=0:
                    print("Player dies!")
                    lost()
                    break
                else:
                    player.attack_enemy(mob[0])
                    if (mob[0].hp <=0):
##                        color.write(f"{mob[0].name} dies\n\n", "BUILTIN")
                        print(f"{mob[0].name} dies\n")
                        break
            else:
                player.attack_enemy(mob[0])
                if mob[0].hp <=0:
##                    color.write(f"{mob[0].name} dies\n\n", "BUILTIN")
                    print(f"{mob[0].name} dies\n")
                    break
                else:
                    mob[0].attack_enemy(player)
                    if player.hp <= 0:
                        ("Player dies!")
                        lost()
                        break
            time.sleep(0.8)
        mob.pop(0)

def load_intro():
    file_path = Path.home() / "textgameIntro.txt"
    with open(file_path, mode="r", encoding = "utf-8") as file:
        for line in file.readlines():
            print(line, end="")

def create_rooms():
    rooms = [Room("room1"), Room("room2"), Room("room3"), Room("room4"), Room("room5"), Room("room6"), Room("room7"), Room("room8"),
             Room("room9"), Room("room10"), Room("room11"), Room("room12"), Room("room13"), Room("room14"), Room("room15")]
    return rooms

def show_menu():
        print("What do you want to do?")
        print(" m - go to another room\n",
          "x - spend experience points\n",
          "p - use a potion to replenish up to 25 health\n",
          #"s - spend gold in the shop\n",
          "c - check your stats\n",
          "exit - quit game")

def make_choice(player, rooms):
        items = []
        number_of_items = 0
        show_menu()
        choice = input("Your choice: ")
        if (choice in ['m', 'x', 'p', 's', 'c']):
            if choice == "exit":
                print("Thanks for playing!")
                quit()
            elif choice == "x":
                player.spend_experience()
                make_choice(player, rooms)
            elif choice == "p":
                player.use_potion()
                make_choice(player, rooms)
            elif choice == 'c':
                print(player)
                make_choice(player, rooms)
            elif choice == "m":
                fight_room(player, rooms, items, number_of_items)
            else:
                make_choice(player, rooms)

def room_after(player, room):
    player.experience = player.experience + room.experience_to_gain
    player.gold = player.gold + room.gold_to_gain
    print(f"You have found {room.gold_to_gain} gold!")
    room.gold_to_gain = 0
    room.experience_to_gain = 0

def fight_room(player, rooms, items, number_of_items):
    proceed = ""
    while (proceed != "yes" and player.hp > 0):
        room_number = ""
        while (room_number not in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]):
            try:
                room_number = int((f"{input('Which number of room do you want to proceed to? Choose from 1 to 15: ')}"))
            except ValueError:
                print("Choose from 1 to 15!")
        room_number = room_number - 1
        if room_number in [0, 1, 3, 6, 7, 10, 11, 14]:
            fight(player, rooms[room_number].monsters)
            room_after(player, rooms[room_number])
##            player.experience = player.experience + rooms[0].experience_to_gain
##            player.gold = player.gold + rooms[0].gold_to_gain
##            print(f"You have found {rooms[0].gold_to_gain} gold!")
##            rooms[0].gold_to_gain = 0
##            rooms[0].experience_to_gain = 0
        if room_number == 2:
            fight(player, rooms[room_number].monsters)
            room_after(player, rooms[room_number])
            if player.items_use and rooms[room_number].gold_to_gain > 0:
                items.append(Item("Dagger", 0, 1, 0, 0, "weapon", 1))
                number_of_items = number_of_items + 1
                player.wear_item(items, number_of_items)
        if room_number == 4:
            fight(player, rooms[room_number].monsters)
            room_after(player, rooms[room_number])
            if player.items_use and rooms[room_number].gold_to_gain > 0:
                items.append(Item("Wooden Shield", 0, 0, 1, 0, "shield", 1))
                number_of_items = number_of_items + 1
                player.wear_item(items, number_of_items)
            player.find_potion()
        if room_number == 5:
            fight(player, rooms[room_number].monsters)
            room_after(player, rooms[room_number])
            if player.items_use and rooms[room_number].gold_to_gain > 0:
                items.append(Item("Rusty Sword", 0, 2, 0, 0, "weapon", 2))
                number_of_items = number_of_items + 1
                player.wear_item(items, number_of_items)
        if room_number == 8:
            fight(player, rooms[room_number].monsters)
            room_after(player, rooms[room_number])
            if player.items_use and rooms[room_number].gold_to_gain > 0:
                items.append(Item("Fine shield", 0, 0, 2, 0, "shield", 2))
                number_of_items = number_of_items + 1
                player.wear_item(items, number_of_items)
        if room_number == 9:
            fight(player, rooms[room_number].monsters)
            room_after(player, rooms[room_number])
            if player.items_use and rooms[room_number].gold_to_gain > 0:
                items.append(Item("Leather armor", 10, 0, 1, 0, "armor", 1))
                number_of_items = number_of_items + 1
                player.wear_item(items, number_of_items)
            player.find_potion()
        if room_number == 12:
            fight(player, rooms[room_number].monsters)
            room_after(player, rooms[room_number])
            if player.items_use and rooms[room_number].gold_to_gain > 0:
                items.append(Item("Mail armor", 15, 0, 2, 0, "armor", 2))
                number_of_items = number_of_items + 1
                player.wear_item(items, number_of_items)
            player.find_potion()
        if room_number == 13:
            fight(player, rooms[room_number].monsters)
            room_after(player, rooms[room_number])
            player.find_potion()
        if player.hp >0:
##                    color.write("\nCongratulations! You won this fight\n\n", "STRING")
            print("Congratulations! You won this fight\n\n")
        room_number = ""
        make_choice(player, rooms)
    play_again = ""
    while (play_again.lower() != 'y' or play_again.lower() != "n"):
        play_again = input("Do you want to play again? y/n: ")
        if play_again.lower() == "y":
            play_game()
        elif play_again.lower() == "n":
            quit()

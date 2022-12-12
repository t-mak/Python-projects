import sys
import textgame_helper

#used this for colors in text, wasn't working when I turned game in executable file outside of IDLE
##try:
##    color = sys.stdout.shell
##except AttributeError:
##    raise RuntimeError("Use IDLE")       

def play_game():
    textgame_helper.load_intro()
    player = textgame_helper.player_choice()
    rooms = textgame_helper.create_rooms()
    textgame_helper.make_choice(player, rooms)

play_game()

#add turns into the fight - can use potions... but then cant fight
#add stat buffing potions for 1-2 turns
#add room descriptions to be loaded from a file
#add save_game
#add graphics/Gui
#add merchant for gold
#add companions
#add other "castles"

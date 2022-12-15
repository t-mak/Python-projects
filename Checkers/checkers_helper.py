#TODO
#DONE - can't beat if no landing possible anymore. Player beating enemy pieces movement - this still needs to check if there are no blocking pieces that don't allow the beating!
#DONE enemy movement
#DONE enemy beating
#DONE player needs to beat when player has a beating possible
#DONE changing to king piece after reaching last line
#DONE changing to king piece for enemy too after reaching first line
#DONE win condition successfully being checked

#DONE player king now can beat pieces across the board
#DONE player king can move across the board
#DONE implemented checking if no player pieces are in the way of a queen - if there are some, queen cannot jump over them
#TBD computer king movement and beating
# -ISSUE with beating -> king doesnt check if there is a piece standing on a field behind, meaning it might land on a field where another piece is standing as of now
# - beating simply check fields from possible moves and whether there is free field after enemy piece, landing there and then recheck if more beatings possible. Dont complicate it further

#separate player and computer methods
#remove unneccesary, duplicated code and simplify it
#if player has beatigns with 2 different pieces, implement choice which player can use instead of choosing one randomly
#add visuals, colors, highlight last moved piece from where to where
#add different fields colors

#ISSUES
#FIXED computer moves instead of beating, when it can beat
#FIXED computer used his piece at field b6 to beat my piece at field a5... Which should not be possible. Computer beats player, even if players piece is at the first or last column
#FIXED player can beat through the wall
#FIXED computer doesn't beat more than once even when it can
#FIXED for player after choosing already taken field for movement and then selecting not taken one, it keeps prompting "where do you want ot move it"
#FIXED if player chooses a piece that has no moves, player cannot quit the loop asking for a move
#FIXED if player choose a correct piece name e.g. 'aa' that cannot move anywhere, and later when prompted write wrong peice name e.g. 'ab43' there is an error
#FIXED player now choosing correct piece to move results in 'this piece cannot move nor beat' and prompt again for selecting a piece
#FIXED when player uses 'change' command to change selected piece, new piece would move but program would keep prompting for different field choice

#ISSUE king lists all pieces on it's way as beatable, as long as they have space behind them, even if there are 2 pieces next to each other. 
#Below shows that king AA can beat both 06 and 10. But it doesnt show 05. It should show that king AA cannot beat at all.
#also king shouldnt be able to move over 2 pieces, nor over 1. if there is 1, it must beat like other normal pieces.
#   A   B   C   D   E   F   G   H
#   -------------------------------
# 8| --  AA  --  02  --  03  --  04  |8
# 7| 05  --  06  --  07  --  08  --  |7
# 6| --  09  --  10  --  11  --  --  |6
# 5| --  --  --  --  --  --  12  --  |5
# 4| --  II  --  --  --  --  --  --  |4
# 3| --  --  JJ  --  KK  --  LL  --  |3
# 2| --  EE  --  FF  --  GG  --  HH  |2
# 1| 01  --  BB  --  CC  --  DD  --  |1
#   -------------------------------
#    A   B   C   D   E   F   G   H

#ISSUE WITH BEATING OVER OWN PIECES
#below shows that AA can beat 01, but I shouldnt be able to go over JJ
#   A   B   C   D   E   F   G   H
#   -------------------------------
# 8| --  AA  --  02  --  03  --  04  |8
# 7| 05  --  JJ  --  --  --  --  --  |7
# 6| --  09  --  --  --  11  --  08  |6
# 5| --  --  --  --  01  --  12  --  |5
# 4| --  --  --  --  --  --  --  --  |4
# 3| --  --  --  --  --  --  --  --  |3
# 2| --  --  --  --  --  --  --  --  |2
# 1| --  --  --  --  --  --  --  --  |1
#   -------------------------------
#    A   B   C   D   E   F   G   H

import random, time
from pickle import FALSE
from checkers_classes import Board
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class Helper:
    def __init__(self):
        # self.player = Player()
        self.game_in_progress = 0
        self.game_board = Board()
        self.pieces_number = 0
        self.turn = 0
        self.kings = []
        # self.kings.append("AA")

    def return_key(self, val):
        for key, value in self.game_board.placement.items():
            if value==val:
                return key
        return('Key Not Found')


## GAME METHODS

    ## PRINT BOARD
    def print_board(self):
        cls()
        print("\nCurrent board:")
        row_index = 0
        row_print = 8
        field_type = 0
        self.pieces_number = len(self.game_board.placement)
        print ('   A   B   C   D   E   F   G   H')
        print ('  -------------------------------')
        for row in self.game_board.board:
            position_index = 0
            print('' + str(row_print) + '|', end=' ')
            for position in row:
                piece_index = 0
                for piece in self.game_board.placement:
                    if self.game_board.placement[piece] == self.game_board.board[row_index][position_index]: #check if for each board position there is a piece there #list index out of range
                        print(piece +' ', end=' ')
                        piece_index = piece_index + 1
                        break
                    elif piece_index >= self.pieces_number - 1:
                        print("-- ", end=' ')
                        break         
                    piece_index = piece_index + 1
                position_index = position_index + 1
            row_index = row_index + 1
            print('|' + str(row_print), end=' ')
            row_print = row_print -1
            print()
        print ('  -------------------------------')
        print ('   A   B   C   D   E   F   G   H')

    ## CHECK IF GAME IS STILL IN PROGRESS
    def check_pieces_left(self):
        black_pieces_count = 0
        white_pieces_count = 0
        for key in self.game_board.placement:
            if (key in self.available_pieces_player()):
                white_pieces_count = white_pieces_count + 1
            else:
                black_pieces_count = black_pieces_count + 1
        # print('Player pieces left: ' + str(white_pieces_count))
        # print('Computer pieces left: ' + str(black_pieces_count))
        self.add_kings()
        self.print_kings()
        print()
        if black_pieces_count == 0:
            print("*****************")
            print("* You have won! *")
            print("*****************")
            time.sleep(2)
            self.game_in_progress = 0
            return 1
        if white_pieces_count == 0:
            print("********************")
            print("* Computer has won *")
            print("********************")
            time.sleep(2)
            self.game_in_progress = 0
            return 1
        return 0 
    
    def available_pieces_player(self):
        white_available_pieces = []
        for key in self.game_board.placement:
            if key in ['AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH', 'II', 'JJ', 'KK', 'LL']:
                white_available_pieces.append(key)
        return white_available_pieces

    ## SHOW MENU 
    def show_menu(self):
        if (self.game_in_progress == 0):
            print("Welcome to Checkers!")
            print("Play new game - n")
            print("Rules - r")
            print("Quit - q")
            # print("Test kings movement - t")
            choice = input("Your choice: ")
            if (choice in ['n', 'q', 'r']):
                if choice == "q":
                    print("Thanks for playing!")
                    quit()
                elif choice == "r":
                    print()
                    print("Piece becomes a queen after reaching row 8 for player or row 1 for computer")
                    print("Queens can move across the whole board in all directions and beat in the same manner")
                    print("Normal pieces cannot beat backwards")
                    print("Pieces must beat if a beating is possible")
                    print("Multiple beatings are possible")
                    print()
                    self.show_menu()
                elif choice == "n":
                    #new game
                    self.game_in_progress = 1
                    self.game_board.initialize_game()
                    self.show_menu()
                # elif choice == "t":
                #     self.game_board.initialize_game()
                #     self.kings_possible_moves('JJ', check_for=1)
                #     self.kings_possible_moves('09', check_for=1)
                else:
                    self.show_menu()
        elif (self.game_in_progress == 1): 
            if self.turn  == 0:
                self.print_board()
            self.turn = self.turn + 1
            choice = ''
            while choice not in ['m', 's', 'n', 'q', 'r']:
                print()
                print("Make a move - m")
                print("Show board - s")
                print("New game - n")
                print("Rules - r")
                print("Quit - q")
                choice = input("Your choice: ")
                print()
                if (choice in ['s', 'm', 'n', 'q', 'r']):
                    if choice == "q":
                        print("Thanks for playing!")
                        quit()
                    elif choice == "n":
                        self.game_board.initialize_game()
                        self.show_menu()
                    elif choice == 's':
                        self.print_board()
                        self.show_menu()
                    elif choice == "r":
                        print("Pieces become queen after reaching row 8 for player or row 1 for computer")
                        print("Queens can move across the whole board in all directions and beat in the same manner")
                        print("Normal pieces cannot beat backwards")
                        print("Piece must beat if a beating is possible")
                        print("Multiple beating is possible")
                        self.show_menu()
                    elif choice == 'm':
                        self.player_piece_choice()
                        print()
                        if (self.check_pieces_left() == 1):
                            self.game_in_progress == 0
                            self.show_menu()
                        print("Computer's turn")
                        self.computer_piece_choice()
                        if (self.check_pieces_left() == 1):
                            self.game_in_progress == 0
                            self.show_menu()
                        self.show_menu()
                    else:
                        self.show_menu()
        print()

##PLAYER METHODS
    def player_beat_enemy(self, piece_choice, beating_choice):
        board_letter_player = self.game_board.placement[piece_choice][0]
        board_number_player = self.game_board.placement[piece_choice][1]    
        board_letter_computer = self.game_board.placement[beating_choice][0]
        board_number_computer = self.game_board.placement[beating_choice][1]   

        player_piece = self.return_key(self.game_board.placement[piece_choice])
        enemy_piece = self.return_key(self.game_board.placement[beating_choice])

        #check positions of player vs enemy piece. Only need to check horizontal positions, as beating is always forward for player
        if (ord(board_letter_player) < ord(board_letter_computer)):
            self.game_board.placement[player_piece] = chr(ord(board_letter_computer) + 1) + str(int(board_number_computer) + 1)
        else:
            self.game_board.placement[player_piece] = chr(ord(board_letter_computer) - 1) + str(int(board_number_computer) + 1)
        self.pieces_number = self.pieces_number - 1
        self.game_board.placement.pop(enemy_piece)  #changed from pop to remov
        if enemy_piece in self.kings:
            self.kings.pop(enemy_piece)
        return 

    def player_piece_choice(self):
        self.print_kings()
        piece_choice = ''
        if piece_choice in self.kings:
                # field_choice = self.kings_possible_moves(piece_choice, check_for=1)
                self.move_piece_king(piece_choice, field_choice="", beaten_enemy_already=0, computer_or_player=1)
                self.print_board()
                return
        for piece_beating_check in self.available_pieces_player():
            if len(self.possible_beatings_player(piece_beating_check)) > 0:
                piece_choice = piece_beating_check
                print("Player must beat!")
                self.move_piece_player(piece_choice, beaten_enemy_already = 0)
                return
        piece_choice = input("Please select a piece to move: ").upper()
        while piece_choice not in self.available_pieces_player():
            print("Wrong piece name")
            print()
            self.player_piece_choice()
        else: 
            print()
            #KINGS ADDED
            

                
            #KIGNS ADDEDplayer_beat_enemy
            self.move_piece_player(piece_choice, beaten_enemy_already = 0)


    def player_beating_enemy(self, piece_choice, possible_beatings):
        beating_choice = ''
        while beating_choice not in self.available_pieces_computer():
            print()
            beating_choice = input("Which piece do you want to beat?: ")
        self.player_beat_enemy(piece_choice, beating_choice)
        possible_beatings.remove(beating_choice)
        return 
        
    def move_piece_player(self, piece_choice, beaten_enemy_already): #works! For moving pieces alone, but works!
        #variable to check if I already beaten someone with this piece. If so, I can only beat again, cannot move
        if piece_choice in self.kings:
            self.move_piece_king(piece_choice, field_choice="", beaten_enemy_already=0, computer_or_player=1)
            return
        possible_beatings = []
        possible_beatings = self.possible_beatings_player(piece_choice)
        # print("Piece_choice in move_piece_player value is: " + str(piece_choice))
        if (len(possible_beatings) >0):
            print("Possible beatings: ", end='')
            for n in possible_beatings:
                print(n + " ", end='')
            self.player_beating_enemy(piece_choice, possible_beatings)
            beaten_enemy_already = 1
            self.move_piece_player(piece_choice, beaten_enemy_already)
        if beaten_enemy_already != 1:
            moved = 1
            taken = 0
            changed = 0
            while (moved == 1):
                taken = 0
                print("Write 'change' if you want to select a different piece")
                new_position = input("Where do you want to move it?: ")
                if new_position == 'change':
                    print()
                    changed = 1
                    self.player_piece_choice()
                if (new_position in self.possible_moves_player(piece_choice)): #checks if piece can move there and if there arent any other pieces on that field                    
                    for key in self.game_board.placement:
                        if (self.game_board.placement[key] == new_position):
                            taken = 1
                            print("Wrong destination, another piece is already on that position")
                            print()
                    if taken == 0:
                        self.game_board.placement[piece_choice] = new_position
                        moved = 0
                elif changed == 1:
                    break
                else:
                    print('You cannot move there')
                    self.print_board()
                    print()
        return 0


    def possible_beatings_player(self, choice): 
        player_possible_moves = self.possible_moves_player(choice) #this returns fields with possible moves, NOT enemy pieces (e.g a2, c2 not 01, 02). Need to find the key of the value
        
        #enemy_field_check is now a list of possible moves of the player. Now I need to check if there are any enemy pieces in those fields
        #check if in a field where player can move, there is an enemy piece
        beating = []
        for key in self.game_board.placement:
            if key in self.available_pieces_computer():
                if (self.game_board.placement[key] in player_possible_moves): # self.game_board.placement[key] is like self.game_board.placement['01'] which returns value (field like a1) 
                    if int(self.game_board.placement[key][1]) < 8 and str(self.game_board.placement[key][0]) !='a' and str(self.game_board.placement[key][0]) !='h': #check if there is space to move, if computer piece is not at row 8 
##                      checking here if I can land after beating enemy piece

                        #choice #this is player piece
                        #key #this is enemy piece
                        board_letter_player = self.game_board.placement[choice][0]
                        board_letter_computer = self.game_board.placement[key][0]
                        board_number_computer = self.game_board.placement[key][1] 

                        check_if_taken = 0  

                        #check positions of player vs enemy piece. Only need to check horizontal positions, as beating is always forward for player
                        #player at e1 wants to be enemy at d2 -> I need to check if c3 is free for landing
                        if (ord(board_letter_player) < ord(board_letter_computer)): #if enemy piece is further to the right on board
                            temp_value = chr(ord(board_letter_computer) + 1) + str(int(board_number_computer) + 1) #temp_value holds field for landing I would need free to beat
                            check_if_taken = self.return_key(temp_value)
                        #I need to get cordinates behind computer piece and then check if there is another piece there from the placement list
                        elif (ord(board_letter_player) > ord(board_letter_computer)):
                            temp_value = chr(ord(board_letter_computer) - 1) + str(int(board_number_computer) + 1)
                            check_if_taken = self.return_key(temp_value)
                        if check_if_taken in self.game_board.placement:
                            return beating
                        else:
                            beating.append(key)
        return beating


 
    def possible_moves_player(self, choice): #RECHECKED 15.12 20:00, looks good
        #BELOW SHOWS THAT AFTER 'CHANGE' THE SELECTED PIECE STAYS THE SAME!
        # print("possibloe moves player choice value is: " + choice)
        board_letter = self.game_board.placement[choice][0]
        board_number = self.game_board.placement[choice][1]
        moves = []

        if self.return_key(choice) in self.kings:
            moves = self.kings_possible_moves(choice, check_for=0) #ISSUE?
            return moves
        else:
            if board_letter == 'a': #if piece is in the first column
                temp_numb = int(board_number) + 1
                temp_letter = chr(ord(board_letter) + 1)
                combined = temp_letter + str(temp_numb)
                moves.append(combined) 
            elif board_letter == 'h': #if piece is in the last column
                temp_numb = int(board_number) + 1
                temp_letter = chr(ord(board_letter) - 1)
                combined = temp_letter + str(temp_numb)
                moves.append(combined) 
            else:
                temp_numb = int(board_number) + 1
                temp_letter = chr(ord(board_letter) + 1)
                combined = temp_letter + str(temp_numb)
                moves.append(combined)
                temp_numb = int(board_number) + 1
                temp_letter = chr(ord(board_letter) - 1)
                combined = temp_letter + str(temp_numb)
                moves.append(combined) 
        return moves


##COMPUTER METHODS
#First called computer_piece_choice() from show_menu() method above.

#TBD (move_piece_computer method), it needs to be changed to a big degree. First version is a copy of move_piece_player and comments apply to differences between these 2 methods
#I already have a piece choosen by computer
#I already have a beating I want it to do or a move I want it to do (if it can beat, beating. If it cannot, move)
#Same as for player, after a beating I need to recheck if a piece can do a beating from a new position. So computer can do multiple beatings in one turn
#But same as for player, it can only do additional beatings after a beating has been done. It canoot do a beating+move. It can only do beating+beating(+beating...)
#I need to call this method either for movement or beating: add argument for the method like beat_or_move with value 0 being beating, value 1 being move
#ATTENTION: possible_moves returns 1-2 list items. Possible_beatings only return 1 item. Either update possible_moves method or take it into consideration in move_piece_computer

    def computer_beat_player(self, piece_choice, beating_choice): 
        # print("Beating choice is: " + str(beating_choice)) 

        piece_choice = str(piece_choice)
        beating_choice = str(beating_choice[0]) #was otherwise giving KeyError: "['JJ']" at line board_letter_player = self.game_board.placement[piece_to_beat][0]. It was a list ['JJ'] instead of 'JJ' 

        #THESE SHOULD HOLD PIECE NAME (01, JJ ETC.)
        computer_piece = piece_choice
        piece_to_beat = beating_choice

        #THESE SHOULD HOLD BOARD FIELD VALUES (a1, g5 etc)
        board_letter_computer = self.game_board.placement[computer_piece][0]
        board_number_computer = self.game_board.placement[computer_piece][1]  
        board_letter_player = self.game_board.placement[piece_to_beat][0]  
        board_number_player = self.game_board.placement[piece_to_beat][1]  
        
        #check relative position of computer piece to player piece. Depending on it, reposition computer piece and remove player piece that is being beaten
        if (ord(board_letter_computer) < ord(board_letter_player)):
            self.game_board.placement[computer_piece] = chr(ord(board_letter_player) + 1) + str(int(board_number_player) - 1)
        else:
            self.game_board.placement[computer_piece] = chr(ord(board_letter_player) - 1) + str(int(board_number_player) - 1)
        self.pieces_number = self.pieces_number - 1
        self.game_board.placement.pop(piece_to_beat)
        return

    def move_piece_computer(self, piece_choice, field_choice, move_or_beat):
        if move_or_beat == 0: #if computer moves
            i = 0 
            #below checks if a piece has 1 or 2 possible moves. 
            #if there are 2 possible moves, randomly choose one of them.
            if len(field_choice) == 1:
                self.game_board.placement[piece_choice] = field_choice[i] #move piece to a new positon
                self.print_board()
                print("Computer moved piece " + piece_choice + " to field " + field_choice[i])
            else:
                i = random.randint(0, 1)
                self.game_board.placement[piece_choice] = field_choice[i]
                self.print_board()
                print("Computer moved piece " + piece_choice + " to field " + field_choice[i])
        else:
            self.computer_beat_player(piece_choice, field_choice)
            self.print_board()
            print("Computer uses piece " + piece_choice + " to beat players piece " + str(field_choice[0]))
            if piece_choice in self.kings:
                self.kings.pop(piece_choice)
            if self.computer_possible_beatings(piece_choice):
                possible_beatings = self.computer_possible_beatings(piece_choice)
                self.move_piece_computer(piece_choice, possible_beatings, move_or_beat=1)
        return

    def computer_piece_choice(self):
        print("Computer is choosing a piece...")
        time.sleep(0.5)
        piece_choice = ''
        piece_choice_beating = []
        black_available_pieces = self.available_pieces_computer() #works correctly, returns list of black pieces left
        piece_choice, piece_choice_beating = self.find_possible_beatings(black_available_pieces) #works correctly - checks if any of the black pieces can beat player

        if piece_choice == '':
            piece_choice, piece_choice_move = self.find_possible_moves(black_available_pieces)
            self.move_piece_computer(piece_choice, piece_choice_move, move_or_beat=0) #INSIDE ABOVE IF CHECK - caleld if computer cannot beat a player, but can move
        else:
            self.move_piece_computer(piece_choice, piece_choice_beating, move_or_beat=1) #called if computer can beat player with a piece
        
    ##Works correctly. For 10 gave e5, c5 as possible moves.
    def computer_possible_moves(self, choice, check_for): 
        #CHECK_FOR ARGUMENT: 
        #if check_for = 0: call of this method is for beatings (which just has a role to return nearby movable fields, without checking anything further - they can be blocked)
        #if check_For = 1: call of this method is for moves, need to check if these fields aren't obstructed/blocked/taken by ANY piece, if so can't move there.
        board_letter = self.game_board.placement[choice][0]
        board_number = self.game_board.placement[choice][1]
        moves = []

        taken_fields_list = list(self.game_board.placement.values())

        if board_letter == 'a': #if piece is in the first column
            temp_numb = int(board_number) - 1
            temp_letter = chr(ord(board_letter) + 1)
            combined = temp_letter + str(temp_numb)
            if check_for == 1 and combined not in taken_fields_list: 
                moves.append(combined) 
            elif check_for == 0: 
                moves.append(combined)
        elif board_letter == 'h': #if piece is in the last column
            temp_numb = int(board_number) - 1
            temp_letter = chr(ord(board_letter) - 1)
            combined = temp_letter + str(temp_numb)
            if check_for == 1 and combined not in taken_fields_list: 
                moves.append(combined) 
            elif check_for == 0:
                moves.append(combined)
        else:
            temp_numb = int(board_number) - 1
            temp_letter = chr(ord(board_letter) + 1)
            combined = temp_letter + str(temp_numb)
            if check_for == 1 and combined not in taken_fields_list: 
                moves.append(combined)
            elif check_for == 0:
                moves.append(combined)
            temp_numb = int(board_number) - 1
            temp_letter = chr(ord(board_letter) - 1)
            combined = temp_letter + str(temp_numb)
            if check_for == 1 and combined not in taken_fields_list: 
                moves.append(combined) 
            elif check_for == 0:
                moves.append(combined)

        return moves

    ##Works correctly. Correctly checks for possible beatings of player and if landing is possible
    def computer_possible_beatings(self, choice): #11.12TODO - this still needs to check if there are no blocking pieces that don't allow the beating!
            
            #HOW IT WORKS 
            #below line is used to find nearby, movable fields. Later it is used to check if player pieces are there. And if so, later checked if there 
            #is a field to land after beating. If yes, computer can beat player.
            computer_moves = self.computer_possible_moves(choice, check_for=0) #this returns fields with possible moves, NOT enemy pieces (e.g a2, c2 not 01, 02). Need to find the key of the value
            beating = []
            for key in self.game_board.placement:
                if key in self.available_pieces_player():
                    if (self.game_board.placement[key] in computer_moves): # self.game_board.placement[key] is like self.game_board.placement['01'] which returns value (field like a1) 
                        if (int(self.game_board.placement[key][1]) > 1 and str(self.game_board.placement[key][0]) !='a' and str(self.game_board.placement[key][0]) !='h'): #check if there is space to move, if computer piece is not at row 1 

    ##                      checking here if I can land after beating enemy piece

                            #choice - this is player piece
                            #key - this is enemy piece

                            board_letter_computer = self.game_board.placement[choice][0]
                            board_number_computer = self.game_board.placement[choice][1] 
                            board_letter_player = self.game_board.placement[key][0]
                            board_number_player = self.game_board.placement[key][1]
                            check_if_taken = 0  

                            #check positions of player vs enemy piece. Only need to check horizontal positions, as beating is always forward for player
                            #player at e1 wants to be enemy at d2 -> I need to check if c3 is free for landing
                            if (ord(board_letter_computer) < ord(board_letter_player)): #if player piece is further to the right on board
                                temp_value = chr(ord(board_letter_player) + 1) + str(int(board_number_player) - 1) #temp_value holds field for landing I would need free to beat
                                check_if_taken = self.return_key(temp_value)
                            #I need to get cordinates behind computer piece and then check if there is another piece there from the placement list
                            else:
                                temp_value = chr(ord(board_letter_player) - 1) + str(int(board_number_player) - 1)
                                check_if_taken = self.return_key(temp_value)
                            if check_if_taken in self.game_board.placement:
                                return beating
                            else:
                                beating.append(key)
            return beating

    def available_pieces_computer(self):
        black_available_pieces = []
        for key in self.game_board.placement:
            if key in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
                black_available_pieces.append(key)
        return black_available_pieces

    def find_possible_beatings(self, black_available_pieces):
        possible_beatings = []
        piece_choice = '' 
        random.shuffle(black_available_pieces)
        for piece in black_available_pieces:
            possible_beatings = self.computer_possible_beatings(piece) #this uses method possible moves too
            if len(possible_beatings) > 0:
                piece_choice = piece
                break
            possible_beatings.clear()
        return piece_choice, possible_beatings

#HOW IT WORKS find_possible_moves() method
#This method checks for each computer piece if it has possible moves (not beatings).
#It returns as soon as it finds a piece that can move somewhere. 
#But list order is shuffled -> meaning it will randomize order first, so 01 isn't always checked first and computer is less predictable.
#meaning if 01 has possible moves, it won't always be chosen as a piece to move by computer thanks to randomizing the order of the list. 
#Computer might move 09 or 05 instead since random.shuffle() put it as a first element in the list after shuffle instead of 01
#If a piece has possible move, it is stored together with field that it can move to and method breaks and returns these value
    def find_possible_moves(self, black_available_pieces):
        possible_moves = []
        piece_choice = ''
        random.shuffle(black_available_pieces)
        for piece in black_available_pieces:
            possible_moves = self.computer_possible_moves(piece, check_for=1)
            if len(possible_moves) > 0:
                piece_choice = piece
                break
            possible_moves.clear()
        return piece_choice, possible_moves

#KING METHODS
    def add_kings(self):
        for piece in self.game_board.placement:
            if piece not in self.kings:
                if piece in self.available_pieces_computer() and self.game_board.placement[piece][1] == '1':
                    self.kings.append(piece)
                    print("Piece " + piece + " is now a king.")
                elif piece in self.available_pieces_player() and self.game_board.placement[piece][1] == '8':
                    self.kings.append(piece)
                    print("Piece " + piece + " is now a king.")

    def print_kings(self):
        print('The following pieces are kings: ', end='')
        print(self.kings)

    def possible_beatings_playerking(self, choice, computer_or_player): #this just checks if enemy pieces are nearby and checks if field behind them is free or not
        if computer_or_player == 1:
            king_possible_moves = self.kings_possible_moves(choice, check_for=0) #this returns fields with possible moves, NOT enemy pieces (e.g a2, c2 not 01, 02). Need to find the key of the value
            print("Kings possible moves are: " + str(king_possible_moves))
            #enemy_field_check is now a list of possible moves of the player. Now I need to check if there are any enemy pieces in those fields
            #check if in a field where player can move, there is an enemy piece
            beating = []
            for key in self.game_board.placement:
                # print("in for loop")
                # print("For key: " + key)
                if key in self.available_pieces_computer():
                    # print("in first if")
                    if (self.game_board.placement[key] in king_possible_moves): # self.game_board.placement[key] is like self.game_board.placement['01'] which returns value (field like a1) 
                        # print("in second if")
                        if int(self.game_board.placement[key][1]) < 8 and int(self.game_board.placement[key][1]) > 1 and str(self.game_board.placement[key][0]) !='a' and str(self.game_board.placement[key][0]) !='h': #check if there is space to move, if computer piece is not at row 8 
                            # print("in third if")
    # checking here if I can land after beating enemy piece

                            #choice #this is player piece
                            #key #this is enemy piece
                            board_letter_king = self.game_board.placement[choice][0]
                            board_number_king = self.game_board.placement[choice][1]
                            board_letter_enemy = self.game_board.placement[key][0]
                            board_number_enemy = self.game_board.placement[key][1] 
                            print("Position for: " + str(key) + " is " + board_letter_enemy + "" + board_number_enemy)
                            check_if_taken = 0  
                            check_if_taken_behind = ''
                            temp_value2 = 0
                            finish_loop = 0
                            print("CHOICE VALUE IS: " + choice)
                            # check positions of player vs enemy piece. Only need to check horizontal positions, as beating is always forward for player
                            # player at e1 wants to beat an enemy at d2 -> I need to check if c3 is free for landing
                            while finish_loop == 0:
                                if (ord(board_letter_king) < ord(board_letter_enemy) and int(board_number_king) < int(board_number_enemy)): #if enemy piece is to the top right
                                    temp_value = chr(ord(board_letter_enemy) + 1) + str(int(board_number_enemy) + 1) #temp_value holds position of the field after the beating target (if beating target is at c7, it will hold d8)
                                    temp_value2 = chr(ord(board_letter_enemy) - 1) + str(int(board_number_enemy) - 1) #temp_value2 position of the field before the beating target, (if beating target is at c7, it will hold b6)
                                    # temp_value3 = #this holds position of piece used for beating,
                                    # above temp_value and temp_value 2 are to make sure there are no 2 pieces next to each other, as well to make sure there is a place to land for piece that beats
                                    check_if_taken = self.return_key(temp_value)
                                    # print("temp value is: " + temp_value + " and temp_value2 is: " + temp_value2)
                                    # print("self.return_key(temp_value2): " + self.return_key(temp_value2) + " self.return_key(choice) " + self.return_key(choice))
                                    check_if_taken_behind = self.return_key(temp_value2)

                                    #CHECKING IF ANY PLAYER PIECES ARE IN THE WAY
                                    for i, j in zip(range(ord(board_letter_king)+1, ord(board_letter_enemy)), range(int(board_number_king)+1, int(board_number_enemy))):
                                        value_to_key = chr(i) + str(j)
                                        if self.return_key(value_to_key) in self.available_pieces_player():
                                            finish_loop = 1
                                            break
                                #I need to get cordinates behind computer piece and then check if there is another piece there from the placement list
                                elif (ord(board_letter_king) > ord(board_letter_enemy) and int(board_number_king) < int(board_number_enemy)): #if enemy piece is to the top left
                                    temp_value = chr(ord(board_letter_enemy) - 1) + str(int(board_number_enemy) +1)
                                    temp_value2 = chr(ord(board_letter_enemy) + 1) + str(int(board_number_enemy) -1)
                                    check_if_taken = self.return_key(temp_value)
                                    check_if_taken_behind = self.return_key(temp_value2)
                                    # print("temp value is: " + temp_value + " and temp_value2 is: " + temp_value2)
                                    # print("self.return_key(temp_value2): " + self.return_key(temp_value2) + " self.return_key(choice) " + self.return_key(choice))

                                    #CHECKING IF ANY PLAYER PIECES ARE IN THE WAY
                                    for i, j in zip(range(ord(board_letter_king)-1, ord(board_letter_enemy), -1), range(int(board_number_king)+1, int(board_number_enemy))):
                                        value_to_key = chr(i) + str(j)
                                        if self.return_key(value_to_key) in self.available_pieces_player():
                                            finish_loop = 1
                                            break
                                elif (ord(board_letter_king) > ord(board_letter_enemy) and int(board_number_king) > int(board_number_enemy)): #if enemy piece is to the bottom left
                                    temp_value = chr(ord(board_letter_enemy) - 1) + str(int(board_number_enemy) -1)
                                    temp_value2 = chr(ord(board_letter_enemy) +1) + str(int(board_number_enemy) +1)
                                    # temp_value3 = 
                                    check_if_taken = self.return_key(temp_value)
                                    check_if_taken_behind = self.return_key(temp_value2)
                                    # print("temp value is: " + temp_value + " and temp_value2 is: " + temp_value2)
                                    # print("self.return_key(temp_value2): " + self.return_key(temp_value2) + " self.return_key(choice) " + self.return_key(choice))
                                    #here checking for 06

                                    #CHECKING IF ANY PLAYER PIECES ARE IN THE WAY
                                    for i, j in zip(range(ord(board_letter_king)-1, ord(board_letter_enemy), -1), range(int(board_number_king)-1, int(board_number_enemy), -1)):
                                        value_to_key = chr(i) + str(j)
                                        if self.return_key(value_to_key) in self.available_pieces_player():
                                            finish_loop = 1
                                            break
                                elif (ord(board_letter_king) < ord(board_letter_enemy) and int(board_number_king) > int(board_number_enemy)): #if enemy piece is to the bottom right
                                    temp_value = chr(ord(board_letter_enemy) + 1) + str(int(board_number_enemy) - 1)
                                    temp_value2 = chr(ord(board_letter_enemy) -1) + str(int(board_number_enemy) +1)
                                    check_if_taken = self.return_key(temp_value)
                                    check_if_taken_behind = self.return_key(temp_value2)
                                    # print("temp value is: " + temp_value + " and temp_value2 is: " + temp_value2)
                                    # print("self.return_key(temp_value2): " + self.return_key(temp_value2) + " self.return_key(choice) " + self.return_key(choice))

                                    #CHECKING IF ANY PLAYER PIECES ARE IN THE WAY
                                    for i, j in zip(range(ord(board_letter_king)+1, ord(board_letter_enemy)), range(int(board_number_king)-1, int(board_number_enemy), -1)):
                                        value_to_key = chr(i) + str(j)
                                        if self.return_key(value_to_key) in self.available_pieces_player():
                                            finish_loop = 1
                                            break
                                if finish_loop == 1:
                                    break
                                if check_if_taken in self.game_board.placement or check_if_taken_behind in self.game_board.placement and check_if_taken_behind != choice: #checks if there are pieces behind or in front of the beating target
                                # if (check_if_taken in self.game_board.placement):
                                    print()
                                else:
                                    beating.append(key)
                                print(str(beating))
                                break
        # print("Beating contents before returned to move_piece_playerking: " + str(beating))
        return beating

    def king_beating(self, piece_choice, possible_beatings, computer_or_player):
        if computer_or_player == 1:
            beating_choice = ''
            while beating_choice not in self.available_pieces_computer():
                print()
                beating_choice = input("Which piece do you want to beat?: ")
            self.king_beat_enemy(piece_choice, beating_choice)
            possible_beatings.remove(beating_choice)
        return 

    def king_beat_enemy(self, piece_choice, beating_choice):
        board_letter_king = self.game_board.placement[piece_choice][0]
        board_number_king = self.game_board.placement[piece_choice][1]    
        board_letter_enemy = self.game_board.placement[beating_choice][0]
        board_number_enemy = self.game_board.placement[beating_choice][1]   

        king_piece = self.return_key(self.game_board.placement[piece_choice])
        enemy_piece = self.return_key(self.game_board.placement[beating_choice])

        #REPOSITION KING PIECE
        if (ord(board_letter_king) < ord(board_letter_enemy) and int(board_number_king) < int(board_number_enemy)): #if enemy piece is to the top right
            new_pos = chr(ord(board_letter_enemy) + 1) + str(int(board_number_enemy) - 1)
            # print("New position for king is: " + str(new_pos))
            # temp_value = chr(ord(board_letter_enemy) + 1) + str(int(board_number_enemy) + 1) #temp_value holds field for landing I would need free to beat
            # check_if_taken = self.return_key(temp_value)
            self.game_board.placement[king_piece] = chr(ord(board_letter_enemy) + 1) + str(int(board_number_enemy) + 1)
        #I need to get cordinates behind computer piece and then check if there is another piece there from the placement list
        if (ord(board_letter_king) > ord(board_letter_enemy) and int(board_number_king) < int(board_number_enemy)): #if enemy piece is to the top left
            new_pos = chr(ord(board_letter_enemy) - 1) + str(int(board_number_enemy) + 1)
            # print("New position for king is: " + str(new_pos))
            # temp_value = chr(ord(board_letter_enemy) - 1) + str(int(board_number_enemy) +1)
            # check_if_taken = self.return_key(temp_value)
            self.game_board.placement[king_piece] = chr(ord(board_letter_enemy) - 1) + str(int(board_number_enemy) + 1)
        if (ord(board_letter_king) > ord(board_letter_enemy) and int(board_number_king) > int(board_number_enemy)): #if enemy piece is to the bottom left
            new_pos = chr(ord(board_letter_enemy) - 1) + str(int(board_number_enemy) - 1)
            # print("New position for king is: " + str(new_pos))
            self.game_board.placement[king_piece] = chr(ord(board_letter_enemy) - 1) + str(int(board_number_enemy) - 1)
            # temp_value = chr(ord(board_letter_enemy) - 1) + str(int(board_number_enemy) -1)
            # check_if_taken = self.return_key(temp_value)
        elif (ord(board_letter_king) < ord(board_letter_enemy) and int(board_number_king) > int(board_number_enemy)): #if enemy piece is to the bottom right
            new_pos = chr(ord(board_letter_enemy) + 1) + str(int(board_number_enemy) - 1)
            # print("New position for king is: " + str(new_pos))
            self.game_board.placement[king_piece] = chr(ord(board_letter_enemy) + 1) + str(int(board_number_enemy) - 1)
            # temp_value = chr(ord(board_letter_enemy) + 1) + str(int(board_number_enemy) - 1)
            # check_if_taken = self.return_key(temp_value)
        #check positions of player vs enemy piece. Only need to check horizontal positions, as beating is always forward for player
        # if (ord(board_letter_king) < ord(board_letter_enemy)):
        #     self.game_board.placement[player_piece] = chr(ord(board_letter_enemy) + 1) + str(int(board_number_enemy) + 1)
        # else:
        #     self.game_board.placement[player_piece] = chr(ord(board_letter_enemy) - 1) + str(int(board_number_enemy) + 1)
        # self.pieces_number = self.pieces_number - 1
        self.pieces_number = self.pieces_number - 1
        self.game_board.placement.pop(enemy_piece)  #changed from pop to remov
        if enemy_piece in self.kings:
            self.kings.pop(enemy_piece)
        return 

    def move_piece_king(self, piece_choice, field_choice, beaten_enemy_already, computer_or_player):
        move_or_beat = 0 #TO BE CHANGED, FOR TESTING its hardcoded value
        if computer_or_player == 1: #if it's player making a move
            possible_beatings = [] 
            possible_beatings =  self.possible_beatings_playerking(piece_choice, computer_or_player=1)
            print("King piece " + piece_choice + " can beat " + str(possible_beatings))
            self.print_board()
            print(self.game_board.placement)
            # print("Piece_choice in move_piece_king for player value is: " + str(piece_choice))
            if (len(possible_beatings) >0):
                print("Possible beatings: ", end='')
                for n in possible_beatings:
                    print(n + " ", end='')
                self.king_beating(piece_choice, possible_beatings, computer_or_player=1)
                beaten_enemy_already = 1
                self.move_piece_king(piece_choice, field_choice="", beaten_enemy_already=1, computer_or_player=1) #field_choice is empty, since I dont need it for player
            if beaten_enemy_already != 1:
                moved = 1
                taken = 0
                changed = 0
                while (moved == 1):
                    taken = 0
                    print("Write 'change' if you want to select a different piece")
                    new_position = input("Where do you want to move it?: ")
                    if new_position == 'change':
                        print()
                        changed = 1
                        self.player_piece_choice()
                    if (new_position in self.kings_possible_moves(piece_choice, check_for=1)): #checks if piece can move there and if there arent any other pieces on that field                    
                        for key in self.game_board.placement:
                            if (self.game_board.placement[key] == new_position):
                                taken = 1
                                print("Wrong destination, another piece is already on that position")
                                print()
                        if taken == 0:
                            self.game_board.placement[piece_choice] = new_position
                            moved = 0
                    elif changed == 1:
                        break
                    else:
                        print('You cannot move there')
                        self.print_board()
                        print()
        if computer_or_player == 0: #if it's computer making a move
            if move_or_beat == 0: #if computer moves
                i = 0 
                #below checks if a piece has 1 or 2 possible moves. 
                #if there are 2 possible moves, randomly choose one of them.
                if len(field_choice) == 1:
                    self.game_board.placement[piece_choice] = field_choice[i] #move piece to a new positon
                    self.print_board()
                    print("Computer moved piece " + piece_choice + " to field " + field_choice[i])
                else:
                    i = random.randint(0, len(field_choice))
                    self.game_board.placement[piece_choice] = field_choice[i]
                    self.print_board()
                    print("Computer moved piece " + piece_choice + " to field " + field_choice[i])
        return
#TBD for king
        # else: 
        #     self.computer_beat_player(piece_choice, field_choice)
        #     self.print_board()
        #     print("Computer uses piece " + piece_choice + " to beat players piece " + str(field_choice[0]))
        #     if self.computer_possible_beatings(piece_choice):
        #         possible_beatings = self.computer_possible_beatings(piece_choice)
        #         self.move_piece_computer(piece_choice, possible_beatings, move_or_beat=1)
        # return

    def kings_possible_moves(self, choice, check_for): #THIS WORKS 100% CORRECTLY
        #if check_for = 0: call of this method is for beatings (which just has a role to return nearby movable fields, without checking anything further - they can be blocked)
        #if check_For = 1: call of this method is for moves, need to check if these fields aren't obstructed/blocked/taken by ANY piece, if so can't move there.
        print(self.game_board.placement[choice]) #was returning None. because... no board was made!
        board_letter = self.game_board.placement[choice][0]
        board_number = self.game_board.placement[choice][1]

        taken_fields_list = list(self.game_board.placement.values())

        # print("Board letter is: " + board_letter)
        # print("Board number is: " + board_number)

        moves = []
        #x1 is top left quarter, x2 top right, x3 bottom left, x4 bottom right

        #doesnt work correctly yet check possible movement towards x1 quarter. 
        moves_x1 = []
        temp_letter = chr(ord(board_letter))
        temp_numb = int(board_number)
        for i in range(1, 8): 
            if temp_letter == 'a' or temp_numb == 8:
                break
            temp_letter = chr(ord(board_letter) - i)
            temp_numb = int(board_number) + i 
            combined = temp_letter + str(temp_numb)
            if check_for == 1 and combined not in taken_fields_list:
                moves.append(combined)
                moves_x1.append(combined)
            elif check_for == 0:
                moves.append(combined)
                moves_x1.append(combined)
    #    print("x1 quarter: " + str(moves_x1))   

        #WORKS CORRECTLY check possible movement towards x2 quarter. 
        moves_x2 = []
        temp_letter = chr(ord(board_letter))
        temp_numb = int(board_number)
        for i in range(1, 8): 
            if temp_letter == 'h' or temp_numb == 8:
                break
            temp_letter = chr(ord(board_letter) + i)
            temp_numb = int(board_number) + i 
            combined = temp_letter + str(temp_numb)
            if check_for == 1 and combined not in taken_fields_list:
                moves.append(combined)
                moves_x2.append(combined)
            elif check_for == 0:
                moves.append(combined)
                moves_x2.append(combined)

    #    print("x2 quarter: " + str(moves_x2))   

        # WORKS, seems like it. Check possible movement towards x3 quarter. 
        moves_x3 = []
        temp_letter = chr(ord(board_letter))
        temp_numb = int(board_number)
        for i in range(1, 8): 
            if temp_letter == 'a' or temp_numb == 1:
                break
            temp_letter = chr(ord(board_letter) - i)
            temp_numb = int(board_number) - i 
            combined = temp_letter + str(temp_numb)
            if check_for == 1 and combined not in taken_fields_list:
                moves.append(combined)
                moves_x3.append(combined)
            elif check_for == 0:
                moves.append(combined)
                moves_x3.append(combined)

     #   print("x3 quarter: " + str(moves_x3))  

        moves_x4 = []
        temp_letter = chr(ord(board_letter))
        temp_numb = int(board_number)
        for i in range(1, 8): 
            if temp_letter == 'h' or temp_numb == 1:
                break
            temp_letter = chr(ord(board_letter) + i)
            temp_numb = int(board_number) - i #if helper_numb is on minus, it will add it instead
             #if helper_letter is on minus, it will add it instead
            combined = temp_letter + str(temp_numb)
            if check_for == 1 and combined not in taken_fields_list:
                moves.append(combined)
                moves_x4.append(combined)
            elif check_for == 0:
                moves.append(combined)
                moves_x4.append(combined)

      #  print("x4 quarter: " + str(moves_x4))  

        moves = moves_x1 + moves_x2 + moves_x3 + moves_x4
        # print("Possible moves for king piece " + choice + ": " + str(moves))  

        return moves
            #damka w a1 moze isc do b2, c3, d4, e5, f6, g7, h8 -> all higher letter + higher number by 1 combined
            #damka w a3 moze do b4, c5, d7, e8 ORAZ b2, c1 -> all high letter + higher number by 1 combined AND lower leter and lower number by 1 combined
            #damka w e3 moze isc do f2, g1 ORAZ d2, c1 ORAZ d4, c5, b6, a7 ORAZ f4, g5, h6
            #damka w h8 moze isc do a1, b2, c3, d4, e5, f6, g7 -> all lower letter + lower number by 1 combined
            #damka w h4 moze isc do g3, f2, e1 ORAZ g5, f6, e7, d8 
#TODO
#DONE - can't beat if no landing possible anymore. Player beating enemy pieces movement - this still needs to check if there are no blocking pieces that don't allow the beating!
#DONE enemy movement
#DONE enemy beating
#player NEEDING to beat when player has a beating
#changing to queen piece after reaching last line and movement for it -> basically more rules
#changing to queen piece for enemy too after reaching first line

#ISSUES
#FIXED computer moves instead of beating, when it can beat

import random
from pickle import FALSE
from checkers_classes import Board
import player, computer
# from player import Player

class Helper:
    def __init__(self):
        # self.player = Player()
        self.game_in_progress = 0
        self.game_board = Board()
        self.pieces_number = 24

    def return_key(self, val):
        for key, value in self.game_board.placement.items():
            if value==val:
                return key
        return('Key Not Found')


## GAME METHODS

    ## PRINT BOARD
    def print_board(self):
        print("\nCurrent board:")
        row_index = 0
        row_print = 8
        print ('   A   B   C   D   E   F   G   H')
        print ('  -------------------------------')
        for row in self.game_board.board:
            position_index = 0
            print('' + str(row_print) + '|', end=' ')
            for position in row:
                piece_index = 0
                for piece in self.game_board.placement:
                    #print(self.game_board.placement[piece])
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
            if (key in ['AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH', 'II', 'JJ', 'KK', 'LL']):
                white_pieces_count = white_pieces_count + 1
            else:
                black_pieces_count = black_pieces_count + 1
        print('White pieces left: ' + str(white_pieces_count))
        print('Black pieces left: ' + str(black_pieces_count))
        if black_pieces_count == 0:
            print("You have won!")
            self.game_in_progress = 0
        if white_pieces_count == 0:
            print("Computer has won")
            self.game_in_progress = 0
        return 0 
    
    # def initialize_game(self):
    #     return 0

    ## SHOW MENU 
    def show_menu(self):
        self.check_pieces_left()
        print()
        if (self.game_in_progress == 0):
            print("Welcome to Checkers!")
            print("Play new game - n")
            print("Quit - q")
            choice = input("Your choice: ")
            if (choice in ['n', 'q']):
                if choice == "q":
                    print("Thanks for playing!")
                    quit()
                elif choice == "n":
                    #new game
                    self.game_in_progress = 1
                    self.game_board.initialize_game()
                    self.show_menu()
                else:
                    self.show_menu()
        elif (self.game_in_progress == 1):
            print("Show board - s")
            print("Make a move - m")
            print("New game - n")
            print("Quit - q")
            choice = input("Your choice: ")
            if (choice in ['s', 'm', 'n', 'q']):
                if choice == "q":
                    print("Thanks for playing!")
                    quit()
                elif choice == "n":
                    #new game
                    print('Here I want to reinitialize the board and clean it from any movement')
                    self.game_board.initialize_game()
                    self.show_menu()
                elif choice == 's':
                    self.print_board()
                    self.show_menu()
                elif choice == 'm':
                    self.player_piece_choice()
                    self.computer_piece_choice()
                    self.show_menu()
                else:
                    self.show_menu()

##PLAYER METHODS
    def player_beat_enemy(self, piece_choice, beating_choice):
        board_letter_player = self.game_board.placement[piece_choice][0]
        board_number_player = self.game_board.placement[piece_choice][1]    
        board_letter_computer = self.game_board.placement[beating_choice][0]
        board_number_computer = self.game_board.placement[beating_choice][1]   

        # print("board letter player: " + board_letter_player) 
        # print("board number player: " + board_number_player)         
        # print("board letter enemy: " + board_letter_computer)   
        # print("board number enemy: " + board_number_computer)

        player_piece = self.return_key(self.game_board.placement[piece_choice])
        enemy_piece = self.return_key(self.game_board.placement[beating_choice])
        # print("Player piece used for beating: " + player_piece)
        # print("Enemy piece used for beating: " + enemy_piece)

        #check positions of player vs enemy piece. Only need to check horizontal positions, as beating is always forward for player
        if (ord(board_letter_player) < ord(board_letter_computer)):
            self.game_board.placement[player_piece] = chr(ord(board_letter_computer) + 1) + str(int(board_number_computer) + 1)
            print(chr(ord(board_letter_computer) + 1) + str(int(board_number_computer) + 1))
        else:
            self.game_board.placement[player_piece] = chr(ord(board_letter_computer) - 1) + str(int(board_number_computer) + 1)
        self.pieces_number = self.pieces_number - 1
        self.game_board.placement.pop(enemy_piece)  #changed from pop to remov
        return 

    def player_piece_choice(self):
            piece_choice = input("Please select piece to move: ")
            if (piece_choice in ['AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH', 'II', 'JJ', 'KK', 'LL']):
                print("You are about to move piece " + piece_choice)
                # beating = []
                # beating = self.possible_beatings_player(piece_choice)
                self.move_piece_player(piece_choice, beaten_enemy_already = 0)

    def player_beating_enemy(self, piece_choice, possible_beatings):
        beating_choice = input("Which piece do you want to beat?: ")
        self.player_beat_enemy(piece_choice, beating_choice)
        possible_beatings.remove(beating_choice)
        # self.enemy_beating(piece_choice, beating)
        return 
        

    def move_piece_player(self, piece_choice, beaten_enemy_already): #works! For moving pieces alone, but works!
        #variable to check if I already beaten someone with this piece. If so, I can only beat again, cannot move
        possible_beatings = []
        possible_beatings = self.possible_beatings_player(piece_choice)
        if (len(possible_beatings) >0):
            print("You must beat the enemy piece")
            print("Possible beatings: ")
            for n in possible_beatings:
                print(n)
            self.player_beating_enemy(piece_choice, possible_beatings)
            beaten_enemy_already = 1
            self.move_piece_player(piece_choice, beaten_enemy_already)
        if beaten_enemy_already != 1:
            new_position = input("Where do you want to move it?: ")
            if (new_position in self.possible_moves_player(piece_choice)): #checks if piece can move there and if there arent any other pieces on that field.
                for key in self.game_board.placement:
                    if (self.game_board.placement[key] == new_position):
                        print("Wrong destination, another piece is already on that position")
                        return 0
                self.game_board.placement[piece_choice] = new_position
            else:
                print('You cannot move there')
                self.show_menu() 
        #self.enemy_piece_choice() #enemy turn     #HERE ERROR    
        return 0


    def possible_beatings_player(self, choice): #11.12TODO - this still needs to check if there are no blocking pieces that don't allow the beating!
        player_possible_moves = self.possible_moves_player(choice) #this returns fields with possible moves, NOT enemy pieces (e.g a2, c2 not 01, 02). Need to find the key of the value
        
        #enemy_field_check is now a list of possible moves of the player. Now I need to check if there are any enemy pieces in those fields
        #check if in a field where player can move, there is an enemy piece
        beating = []
        for key in self.game_board.placement:
            if key in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
                if (self.game_board.placement[key] in player_possible_moves): # self.game_board.placement[key] is like self.game_board.placement['01'] which returns value (field like a1) 
                    if int(self.game_board.placement[key][1]) < 8: #check if there is space to move, if computer piece is not at row 8 

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
                            print(self.return_key(temp_value)) 
                            check_if_taken = self.return_key(temp_value)
                        #I need to get cordinates behind computer piece and then check if there is another piece there from the placement list
                        else:
                            temp_value = chr(ord(board_letter_computer) - 1) + str(int(board_number_computer) + 1)
                            print(self.return_key(temp_value)) 
                            check_if_taken = self.return_key(temp_value)
                        # if return_key(): #now I need to check if no pieces are behind computer piece. 
                        if check_if_taken in self.game_board.placement:
                            print("Can't land after beating, beating impossible")
                        else:
                            print("Possible beating of enemy piece in field: " + self.game_board.placement[key])
                            beating.append(key)
        return beating


    def possible_moves_player(self, choice):
        print("Inside possible moves player")
        # print(choice)
        # print(self.game_board.placement[choice][0]) #take first value from board numbering (a,b,c,d,e,f,g,h)
        # print(self.game_board.placement[choice][1]) #take second value from board numbering (1,2,3,4,5,6,7,8)
        board_letter = self.game_board.placement[choice][0]
        board_number = self.game_board.placement[choice][1]
        moves = []

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
        print("Beating choice is: " + str(beating_choice)) 

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
            print(chr(ord(board_letter_player) + 1) + str(int(board_number_player) - 1))
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
                print("Computer moved piece " + piece_choice + " to field " + field_choice[i])
            else:
                i = random.randint(0, 1)
                self.game_board.placement[piece_choice] = field_choice[i]
                print("Computer moved piece " + piece_choice + " to field " + field_choice[i])
        else:
            print("do a beating") #if computer beats player
            self.computer_beat_player(piece_choice, field_choice)

            # self.game_board.placement[piece_choice] = choosen_move_beating
        return


    def move_piece_player(self, piece_choice, beaten_enemy_already): #works! For moving pieces alone, but works!
        #variable to check if I already beaten someone with this piece. If so, I can only beat again, cannot move
        possible_beatings = []
        possible_beatings = self.possible_beatings_player(piece_choice)
        if (len(possible_beatings) >0):
            print("You must beat the enemy piece")
            print("Possible beatings: ")
            for n in possible_beatings:
                print(n)
            self.player_beating_enemy(piece_choice, possible_beatings)
            beaten_enemy_already = 1
            self.move_piece_player(piece_choice, beaten_enemy_already)
        if beaten_enemy_already != 1:
            new_position = input("Where do you want to move it?: ")
            if (new_position in self.possible_moves_player(piece_choice)): #checks if piece can move there and if there arent any other pieces on that field.
                for key in self.game_board.placement:
                    if (self.game_board.placement[key] == new_position):
                        print("Wrong destination, another piece is already on that position")
                        return 0
                self.game_board.placement[piece_choice] = new_position
            else:
                print('You cannot move there')
                self.show_menu() 
        #self.enemy_piece_choice() #enemy turn     #HERE ERROR    
        return 0

    def computer_piece_choice(self):
        print("Computer is choosing a piece...")
        piece_choice = ''
        piece_choice_beating = []
        black_available_pieces = self.available_pieces() #works correctly, returns list of black pieces left
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

        print()
        print("Inside possible moves computer")
        print("Check for value is: " + str(check_for))
        # print(choice)
        # print(self.game_board.placement[choice][0]) #take first value from board numbering (a,b,c,d,e,f,g,h)
        # print(self.game_board.placement[choice][1]) #take second value from board numbering (1,2,3,4,5,6,7,8)
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
            

            # for move in computer_moves:
            #     print("Computer piece " + choice + " can move to field: " + move)
            
            beating = []
            for key in self.game_board.placement:
                if key in ['AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH', 'II', 'JJ', 'KK', 'LL']:
                    if (self.game_board.placement[key] in computer_moves): # self.game_board.placement[key] is like self.game_board.placement['01'] which returns value (field like a1) 
                        if int(self.game_board.placement[key][1]) > 1: #check if there is space to move, if computer piece is not at row 1 

    ##                      checking here if I can land after beating enemy piece

                            #choice #this is player piece
                            #key #this is enemy piece

                            board_letter_computer = self.game_board.placement[choice][0]
                            board_number_computer = self.game_board.placement[choice][1] 
                            board_letter_player = self.game_board.placement[key][0]
                            board_number_player = self.game_board.placement[key][1]
                            
                            check_if_taken = 0  

                            #check positions of player vs enemy piece. Only need to check horizontal positions, as beating is always forward for player
                            #player at e1 wants to be enemy at d2 -> I need to check if c3 is free for landing
                            if (ord(board_letter_computer) < ord(board_letter_player)): #if player piece is further to the right on board
                                temp_value = chr(ord(board_letter_player) + 1) + str(int(board_number_player) - 1) #temp_value holds field for landing I would need free to beat
                                # print(self.return_key(temp_value)) 
                                check_if_taken = self.return_key(temp_value)
                            #I need to get cordinates behind computer piece and then check if there is another piece there from the placement list
                            else:
                                temp_value = chr(ord(board_letter_player) - 1) + str(int(board_number_player) - 1)
                                # print(self.return_key(temp_value)) 
                                check_if_taken = self.return_key(temp_value)
                            # if return_key(): #now I need to check if no pieces are behind computer piece. 
                            if check_if_taken in self.game_board.placement:
                                print("Can't land after beating, beating impossible")
                            else:
                                print("Possible beating of enemy piece in field: " + self.game_board.placement[key])
                                beating.append(key)
            return beating

    def available_pieces(self):
        black_available_pieces = []
        for key in self.game_board.placement:
            if key in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
                black_available_pieces.append(key)
            #print("Black pieces available: " + str(black_available_pieces))
        print("Black pieces available: " + str(black_available_pieces))
        return black_available_pieces

    def find_possible_beatings(self, black_available_pieces):
        #added list shuffle, so computer doesn't always choose 01, 02, 03... as first choice if they have possible beatings, making it less predictable
        #what move computer will do. Now even if 01 can beat player, computer might choose piece 05 instead.
        possible_beatings = []
        piece_choice = '' #temp, placeholder
        print("Unshuffled black_available_pieces in find possible beatings: " + str(black_available_pieces))
        random.shuffle(black_available_pieces)
        print("Shuffled black_available_pieces using random.shuffle in find possible beatings: " + str(black_available_pieces)) 
        for piece in black_available_pieces:
            possible_beatings = self.computer_possible_beatings(piece) #this uses method possible moves too
            print("Possible beatings for piece " + piece + " are: " + str(possible_beatings))
            if len(possible_beatings) > 0:
                piece_choice = piece
                break
            possible_beatings.clear()
        if len(possible_beatings) < 1:
            print("Computer has no possible beatings")
        else:
            print("Piece: " + piece_choice + " has possible beating in " + str(possible_beatings))
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
        print("Unshuffled black_available_pieces: " + str(black_available_pieces))
        random.shuffle(black_available_pieces)
        print("Shuffled black_available_pieces using random.shuffle: " + str(black_available_pieces)) 
        print("Shuffled black_available_pieces: " + str(random.sample(black_available_pieces, len(black_available_pieces))))
        for piece in black_available_pieces:
            possible_moves = self.computer_possible_moves(piece, check_for=1)
            print("Possible moves for piece " + piece + " are: " + str(possible_moves))
            if len(possible_moves) > 0:
                piece_choice = piece
                break
            possible_moves.clear()
        if len(possible_moves) < 1:
            print("Computer has no possible moves")
        else:
            print("Piece: " + piece_choice + " can move to " + str(possible_moves))
        return piece_choice, possible_moves
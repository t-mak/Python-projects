#Dla uproszczenia niech komputer zamiast pionków ma cyfry, a gracz litery. Tutaj nie chodzi o zabawę z tworzeniem grafiki na ekranie, niech to będzie prosty interfejs tekstowy.

#class Board:
    #board 8x8, each player has 12 pieces. Pieces can move only on black board fields. Fields are white and black

    #board as a tuple is better, I do not need to update it, I need it to be iterable and have an order. I won't be changing any data about board. It's static there.
    #pieces also won't be changing, they are just there
    #placement will be changing though
    #can use some special placement like [black piece[0], "beaten"] to have a way to know if piece is unusable
    
    #initialize putting pieces on a board using indexes, or at start I can do it even manually

class Board:
    def __init__(self):
        self.board = ()
            # a tylko do b
            # b do a c
            # c do b d
            # d do c e
            # e do d f
            # f do e g
            # g do f h
        self.placement = {}


    def initialize_game(self):
        
        self.board = (
            ('a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'),
            ('a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'),
            ('a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'),
            ('a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'),
            ('a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'),
            ('a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'),
            ('a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'),
            ('a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'))

        self.placement = {
            "AA" : "a1",
            "BB" : "c1",
            "CC" : "e1",
            "DD" : "g1",
            "EE" : "b2",
            "FF" : "d2",
            "GG" : "f2",
            "HH" : "h2",
            "II" : "a3",
            "JJ" : "c3",
            "KK" : "e3",
            "LL" : "g3",
            "01" : "b8",
            "02" : "d8",
            "03" : "f8",
            "04" : "h8", 
            "05" : "a7", 
            "06" : "c7", 
            "07" : "e7", 
            "08" : "g7", 
            "09" : "b6", 
            "10" : "d6", 
            "11" : "f6", 
            "12" : "h6",
        }        
        # self.black_pieces = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

        # self.white_pieces = ['AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH', 'II', 'JJ', 'KK', 'LL']

        # black_pieces_two = [
        #     [1, board[0][1]], [2, board[0][3]], [3, board[0][5]], [4, board[0][7]],
        #     [5, board[1][0]], [6, board[1][2]], [7, board[1][4]], [8, board[1][6]],
        #     [9, board[2][1]], [10, board[2][3]], [11, board[2][5]], [12, board[2][7]]
        #     ]

        # self.placement = [
        #     [self.white_pieces[0], self.board[7][0]], [self.white_pieces[1], self.board[7][2]], [self.white_pieces[2], self.board[7][4]], [self.white_pieces[3], self.board[7][6]],
        #     [self.white_pieces[4], self.board[6][1]], [self.white_pieces[5], self.board[6][3]], [self.white_pieces[6], self.board[6][5]], [self.white_pieces[7], self.board[6][7]],
        #     [self.white_pieces[8], self.board[5][0]], [self.white_pieces[9], self.board[5][2]], [self.white_pieces[10], self.board[5][4]], [self.white_pieces[11], self.board[5][6]],
        #     [self.black_pieces[0], self.board[0][1]], [self.black_pieces[1], self.board[0][3]], [self.black_pieces[2], self.board[0][5]], [self.black_pieces[3], self.board[0][7]],
        #     [self.black_pieces[4], self.board[1][0]], [self.black_pieces[5], self.board[1][2]], [self.black_pieces[6], self.board[1][4]], [self.black_pieces[7], self.board[1][6]],
        #     [self.black_pieces[8], self.board[2][1]], [self.black_pieces[9], self.board[2][3]], [self.black_pieces[10], self.board[2][5]], [self.black_pieces[11], self.board[2][7]]
        # ]



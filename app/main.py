class Piece():
    def __init__(self, type, color):
        self.type = type
        self.color = color
    
    def __eq__(self, other):
        if not isinstance(other, Piece):
            raise NotImplementedError(f'Wrong type of objects compare: {other} is not Piece')
        return other.type == self.type and other.color == self.color

    def __repr__(self):
        return f'< tipo: [{self.type}] - cor: [{self.color}]>'

    def __str__(self):
        return self.type


class Board():
    white = 'white'
    black = 'black'

    __init_p1_board = [
        ('P', '2a'),('P', '2b'),('P', '2c'),('P', '2d'),('P', '2e'),('P', '2f'),('P', '2g'),('P', '2h'),
        ('T', '1a'),('C', '1b'),('B', '1c'),('Q', '1d'),('K', '1e'),('B', '1f'),('C', '1g'),('T', '1h'),
    ]

    __init_p2_board = [
        ('P', '7a'),('P', '7b'),('P', '7c'),('P', '7d'),('P', '7e'),('P', '7f'),('P', '7g'),('P', '7h'),
        ('T', '8a'),('C', '8b'),('B', '8c'),('Q', '8d'),('K', '8e'),('B', '8f'),('C', '8g'),('T', '8h'),
    ]

    def __init__(self):
        '''
            Init game like this:

            1 [T][C][B][Q][K][B][C][T]
            2 [P][P][P][P][P][P][P][P]
            3 [ ][ ][ ][ ][ ][ ][ ][ ]
            4 [ ][ ][ ][ ][ ][ ][ ][ ]
            5 [ ][ ][ ][ ][ ][ ][ ][ ]
            6 [ ][ ][ ][ ][ ][ ][ ][ ]
            7 [P][P][P][P][P][P][P][P]
            8 [T][C][B][Q][K][B][C][T]
            -- a  b  c  d  e  f  g  h
        '''

        self.length = 8
        self.height = 8
        self.board = [[None for _ in range(self.length)] for _ in range(self.height)]

        for piece, cord in self.__init_p1_board:
            self.setP(Piece(piece, self.white), cord)
        
        for piece, cord in self.__init_p2_board:
            self.setP(Piece(piece, self.black), cord)

    def setP(self, piece: Piece, cord: str):
        cordsTranlated = self.__getTranslateCords(cord)
        self.board[cordsTranlated[0]][cordsTranlated[1]] = piece


    def __getTranslateCords(self, cords:str):
        result = []

        tableChars = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        tableNums = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7}
        splitedCords = [c for c in cords]

        result.append(tableNums[splitedCords[0]])
        result.append(tableChars[splitedCords[1]])
        return result


    def getCordPiece(self, cord: str):
        cordsT = self.__getTranslateCords(cord)
        piece = self.board[cordsT[0]][cordsT[1]]
        return piece


    def __str__(self):
        result =  ''
        for index, board in enumerate(self.board):

            if index:
                result += f'\n'
            result += f'{index + 1} '
            for l in board:
                if l:
                    result += f'[{l}]'
                else:
                    result += f'[ ]'

        result += '\n' + ''.join([f'{l}' for l in ['--',' a ',' b ',' c ',' d ',' e ',' f ',' g ',' h']])
        return result
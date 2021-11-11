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

        self.setP(Piece('P', self.white), '2a')
        self.setP(Piece('P', self.white), '2b')
        self.setP(Piece('P', self.white), '2c')
        self.setP(Piece('P', self.white), '2d')
        self.setP(Piece('P', self.white), '2e')
        self.setP(Piece('P', self.white), '2f')
        self.setP(Piece('P', self.white), '2g')
        self.setP(Piece('P', self.white), '2h')

        self.setP(Piece('T', self.white), '1a')
        self.setP(Piece('C', self.white), '1b')
        self.setP(Piece('B', self.white), '1c')
        self.setP(Piece('Q', self.white), '1d')
        self.setP(Piece('K', self.white), '1e')
        self.setP(Piece('B', self.white), '1f')
        self.setP(Piece('C', self.white), '1g')
        self.setP(Piece('T', self.white), '1h')

        self.setP(Piece('P', self.white), '7a')
        self.setP(Piece('P', self.white), '7b')
        self.setP(Piece('P', self.white), '7c')
        self.setP(Piece('P', self.white), '7d')
        self.setP(Piece('P', self.white), '7e')
        self.setP(Piece('P', self.white), '7f')
        self.setP(Piece('P', self.white), '7g')
        self.setP(Piece('P', self.white), '7h')

        self.setP(Piece('T', self.white), '8a')
        self.setP(Piece('C', self.white), '8b')
        self.setP(Piece('B', self.white), '8c')
        self.setP(Piece('Q', self.white), '8d')
        self.setP(Piece('K', self.white), '8e')
        self.setP(Piece('B', self.white), '8f')
        self.setP(Piece('C', self.white), '8g')
        self.setP(Piece('T', self.white), '8h')


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
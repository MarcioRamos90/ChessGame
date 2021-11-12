from chess import Board, Piece, Game


def testGameStart(capsys):
    game = Game()
    game.start()
    captured = capsys.readouterr()

    assert '1 [T][C][B][Q][K][B][C][T]' in captured.out
    assert '8 [T][C][B][Q][K][B][C][T]' in captured.out
    assert '\njogador 1: qual peça deseja mover?: ' in captured.out


def testBoard():
    board = Board()
    assert board.length == 8
    assert board.height == 8


def testPeoesDasBrancas():
    board = Board()
    piece = Piece('P', 'white')

    # peoes
    assert board.getCordPiece('2a') == piece
    assert board.getCordPiece('2b') == piece
    assert board.getCordPiece('2c') == piece
    assert board.getCordPiece('2d') == piece
    assert board.getCordPiece('2e') == piece
    assert board.getCordPiece('2f') == piece
    assert board.getCordPiece('2g') == piece
    assert board.getCordPiece('2h') == piece
    

def testGerentesDasBrancas():
    board = Board()

    # gerentes
    assert board.getCordPiece('1a') == Piece('T', 'white')
    assert board.getCordPiece('1b') == Piece('C', 'white')
    assert board.getCordPiece('1c') == Piece('B', 'white')
    assert board.getCordPiece('1d') == Piece('Q', 'white')
    assert board.getCordPiece('1e') == Piece('K', 'white')
    assert board.getCordPiece('1f') == Piece('B', 'white')
    assert board.getCordPiece('1g') == Piece('C', 'white')
    assert board.getCordPiece('1h') == Piece('T', 'white')


def testStrBoard():
    expected = '''1 [T][C][B][Q][K][B][C][T]
2 [P][P][P][P][P][P][P][P]
3 [ ][ ][ ][ ][ ][ ][ ][ ]
4 [ ][ ][ ][ ][ ][ ][ ][ ]
5 [ ][ ][ ][ ][ ][ ][ ][ ]
6 [ ][ ][ ][ ][ ][ ][ ][ ]
7 [P][P][P][P][P][P][P][P]
8 [T][C][B][Q][K][B][C][T]
-- a  b  c  d  e  f  g  h'''
    print(expected)

    board = Board()

    result = str(board)

    assert expected == result

"""
Environment for chess board and pieces
"""


class ChessBoard:
    """
    Object for chess environment
    """
    def __init__(self):
        """
        Initialize attributes
        """
        self.pieces = ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']
        self.letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.board = self.set_board()

    def set_board(self):
        """
        Method for initializing the board. Uses a dictionary to manage columns, rows and pieces.
        :return:
        """
        # Set letters
        board = dict()
        for rows in range(len(self.letters)):
            for letter in self.letters:
                board[letter+str(rows+1)] = 'Unoccupied'
        return board



    def set_chess_pieces(self):
        """
        Method for initializing a normal game of chess
        :return:
        """
        # Set white pieces
        self.board['A1'] = 'white', 'rook'
        self.board['B1'] = 'white', 'knight'
        self.board['C1'] = 'white', 'bishop'
        self.board['D1'] = 'white', 'queen'
        self.board['E1'] = 'white', 'king'
        self.board['F1'] = 'white', 'bishop'
        self.board['G1'] = 'white', 'knight'
        self.board['H1'] = 'white', 'rook'

        self.board['A2'] = 'white', 'pawn'
        self.board['B2'] = 'white', 'pawn'
        self.board['C2'] = 'white', 'pawn'
        self.board['D2'] = 'white', 'pawn'
        self.board['E2'] = 'white', 'pawn'
        self.board['F2'] = 'white', 'pawn'
        self.board['G2'] = 'white', 'pawn'
        self.board['H2'] = 'white', 'pawn'


        # Set black pieces
        self.board['A8'] = 'black', 'rook'
        self.board['B8'] = 'black', 'knight'
        self.board['C8'] = 'black', 'bishop'
        self.board['D8'] = 'black', 'queen'
        self.board['E8'] = 'black', 'king'
        self.board['F8'] = 'black', 'bishop'
        self.board['G8'] = 'black', 'knight'
        self.board['H8'] = 'black', 'rook'

        self.board['A7'] = 'black', 'pawn'
        self.board['B7'] = 'black', 'pawn'
        self.board['C7'] = 'black', 'pawn'
        self.board['D7'] = 'black', 'pawn'
        self.board['E7'] = 'black', 'pawn'
        self.board['F7'] = 'black', 'pawn'
        self.board['G7'] = 'black', 'pawn'
        self.board['H7'] = 'black', 'pawn'


    def move_piece(self, piece):
        """
        Method for moving pieces
        :param piece:
        :return:
        """

    def create_8_queen_problem(self):
        """
        place 8 queens randomly on the board
        :return:
        """


    def __repr__(self):
        """
        Prints the current state of the board
        :return:
        """
        return str(self.board)

class Pawn:
    """

    """
    def init(self):
        """

        :return:
        """
    def rules(self):
        """
        Method that checks the rules for the various pieces
        :return:
        """

class Rook:
    """
    """

    def init(self):
        """

        :return:
        """
    def rules(self):
        """
        Method that checks the rules for the various pieces
        :return:
        """

class Bishop:
    """

    """

    def init(self):
        """

        :return:
        """
    def rules(self):
        """
        Method that checks the rules for the various pieces
        :return:
        """

class Knight:
    """

    """

    def init(self):
        """

        :return:
        """
    def rules(self):
        """
        Method that checks the rules for the various pieces
        :return:
        """

class Queen:
    """

    """

    def init(self):
        """

        :return:
        """
    def rules(self):
        """
        Method that checks the rules for the various pieces
        :return:
        """

class King:
    """

    """

    def init(self):
        """

        :return:
        """
    def rules(self):
        """
        Method that checks the rules for the various pieces
        :return:
        """


if __name__ == '__main__':
    board = ChessBoard()
    board.set_chess_pieces()
    print(board)



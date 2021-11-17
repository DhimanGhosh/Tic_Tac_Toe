import numpy as np
import pandas as pd


class Game:
    def __init__(self):
        self.__O = 'O'
        self.__X = 'X'
        self.__symbol = {'O': self.__X, 'X': self.__O}
        self.__next_symbol = self.__O
        self.__init_board_value = '-'
        self.__board = self.__init_board()

    def __init_board(self):
        mat = np.zeros((3, 3), dtype="U1")
        mat[:] = self.__init_board_value
        df = pd.DataFrame(data=mat, index=[1, 2, 3], columns=['A', 'B', 'C'])
        return df

    def __display_board(self):
        print(self.__board)

    def __get_cell_value(self, cell: str):
        s = self.__board[cell[0]]
        return s[int(cell[-1])]

    def __insert_symbol(self, cell: str, symbol: str):
        col = cell[0]
        row = int(cell[-1])
        s = self.__board[col]
        s[row] = symbol
        self.__board[col] = s

    def __check_result(self):
        a = self.__board['A'].to_list()
        b = self.__board['B'].to_list()
        c = self.__board['C'].to_list()

        r1 = self.__board.iloc[0].to_list()
        r2 = self.__board.iloc[1].to_list()
        r3 = self.__board.iloc[2].to_list()

        d1 = [
            self.__get_cell_value('A1'),
            self.__get_cell_value('B2'),
            self.__get_cell_value('C3')
        ]
        d2 = [
            self.__get_cell_value('C1'),
            self.__get_cell_value('B2'),
            self.__get_cell_value('A3')
        ]

        res = [str, list]
        if a == [self.__O] * 3 or a == [self.__X] * 3:
            res[-1] = ['A1', 'A2', 'A3']
            res[0] = self.__O if self.__O in a else self.__X
            return res
        elif b == [self.__O] * 3 or b == [self.__X] * 3:
            res[-1] = ['B1', 'B2', 'B3']
            res[0] = self.__O if self.__O in b else self.__X
            return res
        elif c == [self.__O] * 3 or c == [self.__X] * 3:
            res[-1] = ['C1', 'C2', 'C3']
            res[0] = self.__O if self.__O in c else self.__X
            return res
        elif r1 == [self.__O] * 3 or r1 == [self.__X] * 3:
            res[-1] = ['A1', 'B1', 'C1']
            res[0] = self.__O if self.__O in r1 else self.__X
            return res
        elif r2 == [self.__O] * 3 or r2 == [self.__X] * 3:
            res[-1] = ['A2', 'B2', 'C2']
            res[0] = self.__O if self.__O in r2 else self.__X
            return res
        elif r3 == [self.__O] * 3 or r3 == [self.__X] * 3:
            res[-1] = ['A3', 'B3', 'C3']
            res[0] = self.__O if self.__O in r3 else self.__X
            return res
        elif d1 == [self.__O] * 3 or d1 == [self.__X] * 3:
            res[-1] = ['A1', 'B2', 'C3']
            res[0] = self.__O if self.__O in d1 else self.__X
            return res
        elif d2 == [self.__O] * 3 or d2 == [self.__X] * 3:
            res[-1] = ['C1', 'B2', 'A3']
            res[0] = self.__O if self.__O in d2 else self.__X
            return res
        elif self.__init_board_value not in self.__board.values:
            res = ['Draw']
            return res
        else:
            return None

    def __next_player(self, cell: str):
        if self.__get_cell_value(cell) not in ['X', 'O']:
            self.__next_symbol = self.__symbol[self.__next_symbol]
            self.__insert_symbol(cell=cell, symbol=self.__next_symbol)
            result = self.__check_result()
            self.__display_board()
            return result if result else self.__board
        print(f'Cell "{cell}" is not Empty!')
        self.__display_board()
        return None

    def play(self):
        self.__display_board()
        player1 = input('Player 1 Name: ')
        print(f'{player1} is {self.__X}')
        player2 = input('Player 2 Name: ')
        print(f'{player2} is {self.__O}')
        
        def player1_entry():
            res = None
            while True:
                cell = input(f'{player1} Enter Cell: ').upper()
                if cell[0] not in ['A', 'B', 'C'] or 1 > int(cell[-1]) > 3:
                    print('Invalid Cell!')
                    continue
                res = self.__next_player(cell)
                if res is None:
                    continue
                break
            return res
        
        def player2_entry():
            res = None
            while True:
                cell = input(f'{player2} Enter Cell: ').upper()
                if cell[0] not in ['A', 'B', 'C'] or 1 > int(cell[-1]) > 3:
                    print('Invalid Cell!')
                    continue
                res = self.__next_player(cell)
                if res is None:
                    continue
                break
            return res
        
        while not self.__check_result():
            res = player1_entry()
            if type(res) is not list:
                res = player2_entry()
            if type(res) is list:
                if self.__X in res:
                    print(f'{player1} wins!\nMatched: {res[-1]}')
                elif self.__O in res:
                    print(f'{player2} wins!\nMatched: {res[-1]}')
                else:
                    print('Game Draw!')
                break


if __name__ == '__main__':
    game = Game()
    game.play()

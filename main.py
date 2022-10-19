class ConnectFour():
    def __init__(self):
        self.board = [[" " for row in range(8)] for column in range(8)]
        self.turn = 2

    def turns(self):
        if self.turn == 2:
            self.turn = 1
        else:
            self.turn = 2
        return self.turn 

    def check_position(self,column):
        for row in range(7,-1,-1):
            if self.board[row][column] == 0:
                self.board[row][column] == self.turn
                return self.board
    
    def checking(self):
        if self.check_draw() == 3:
            self.check_draw()
        if self.horizontal() != 0:
            return self.horizontal()
        if self.vertical() != 0:
            return self.vertical()
        if self.right_diagonal() != 0:
            return self.right_diagonal()
        if self.left_diagonal() != 0:
            return self.left_diagonal()
        return 0 
        
    def horizontal(self):
        for row in range(8):
            for column in range(8):
                try:
                    if self.tablero[row][column] != 0:
                        if self.tablero[row][column] == 1:
                            if self.tablero[row][column + 1] == 1:
                                if self.tablero[row][column + 2] == 1:
                                    if self.tablero[row][column + 3] == 1:
                                        return 1

                    if self.tablero[row][column] != 0:
                        if self.tablero[row][column] == 2:
                            if self.tablero[row][column + 1] == 2:
                                if self.tablero[row][column + 2] == 2:
                                    if self.tablero[row][column + 3] == 2:
                                        return 2
                except(Exception):
                    return 0
        return 0

    def vertical(self):
        for row in range (8):
            for column in range(8):
                try:
                    if self.tablero[row][column] != 0:
                        if self.tablero[row][column] == 1:
                            if self.tablero[row + 1][column] == 1:
                                if self.tablero[row + 2][column] == 1:
                                    if self.tablero[row + 3][column] == 1:
                                        return 1
                    
                    if self.tablero[row][column] != 0:
                        if self.tablero[row][column] == 2:
                            if self.tablero[row + 1][column] == 2:
                                if self.tablero[row + 2][column] == 2:
                                    if self.tablero[row + 3][column] == 2:
                                        return 2
                except(Exception):
                    return 0
        return 0

    def right_diagonal(self):
        for row in range (8):
            for column in range(8):
                try:
                    if self.tablero[row][column] != 0:
                        if self.tablero[row][column] == 1:
                            if self.tablero[row + 1][column + 1] == 1:
                                if self.tablero[row + 2][column +2] == 1:
                                    if self.tablero[row + 3][column + 3] == 1:
                                        return 1
                    
                    if self.tablero[row][column] != 0:
                        if self.tablero[row][column] == 2:
                            if self.tablero[row + 1][column + 1] == 2:
                                if self.tablero[row + 2][column +2] == 2:
                                    if self.tablero[row + 3][column + 3] == 2:
                                        return 2
                except(Exception):
                    return 0
        return 0

    def left_diagonal(self):
        for fila in range (8):
            for column in range(7, -1, -1):
                try:
                    if self.tablero[fila][column] != 0:
                        if self.tablero[fila][column] == 1:
                            if self.tablero[fila + 1][column - 1] == 1:
                                if self.tablero[fila + 2][column - 2] == 1:
                                    if self.tablero[fila + 3][column - 3] == 1:
                                        return 1
                    
                    if self.tablero[fila][column] != 0:
                        if self.tablero[fila][column] == 2:
                            if self.tablero[fila + 1][column - 1] == 2:
                                if self.tablero[fila + 2][column - 2] == 2:
                                    if self.tablero[fila + 3][column - 3] == 2:
                                        return 2
                except(Exception):
                    return 0
        return 0

    def check_draw(self):
        if not any(' ' in _ for _ in self.board):
            return 3
        return 0

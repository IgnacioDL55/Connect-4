
from main import ConnectFour


class visual():
    def game(self):
        game = ConnectFour()
        while True:
            self.print_board()
            self.player_pick()


    def print_board(self):
        game = ConnectFour()
        board= ""
        print("\n")
        for r in range(8):
            print(f"  ({r+1}) ", end="")
        print("\n")
        for r in game.board:
            for indice, c in enumerate(r):
                board += str(c) + "| - |" 
                if indice == 7:
                    board += "\n"
        print(board)
            
    
    
    def player_pick(self):
        game = ConnectFour()
        turn = game.turns()
        choice = int(input(f"Elije una columna para colocar tu ficha (1-8)\nEs tu turno jugador {turn}: "))
        game.check_position(choice-1)
        winner = game.checking()
        if winner == 3:
            self.print_board()
            print("Han Empatado")
            exit()
        if winner != 0 :
            self.print_board()
            print(f"Ha ganado el jugador {winner}")
            exit()

    def start(self):
        self.game()


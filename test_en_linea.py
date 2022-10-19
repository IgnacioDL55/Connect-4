import unittest
from main import ConnectFour

class test_ConnectFour(unittest.TestCase):
    def test_board(self):
        game = ConnectFour()
        self.assertEqual(len(game.board), 8)
        self.assertEqual(len(game.board[0]), 8)

    def test_definir_turnos(self):
        objeto = ConnectFour()
        objeto.turns()
        self.assertEqual(objeto.turn, 1)
        objeto.turns()
        self.assertEqual(objeto.turn, 2)
    
    def test_vertical(self):
        game = ConnectFour()
        game.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', '1', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', '1', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', '1', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', '1', ' ', ' ', ' ', ' ', ' ', ' ']]
        self.assertEqual(game.vertical(),0)
    
    def test_horizontal(self):
        game = ConnectFour()    
        game.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', '2', '2', '2', '2', ' ']]
        self.assertEqual(game.horizontal(),0)

    def test_diagonal1(self):
        game = ConnectFour()    
        game.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                           [' ', ' ', ' ', '1', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', '1', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', '1', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', '1', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
        self.assertEqual(game.right_diagonal(),0)
    
    def test_diagonal2(self):
        game = ConnectFour()    
        game.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                           [' ', ' ', ' ', '2', ' ', ' ', ' ', ' '],
                           [' ', ' ', '2', ' ', ' ', ' ', ' ', ' '],
                           [' ', '2', ' ', ' ', ' ', ' ', ' ', ' '],
                           ['2', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
        self.assertEqual(game.left_diagonal(),0)

    





if __name__ == "__main__":
    unittest.main()

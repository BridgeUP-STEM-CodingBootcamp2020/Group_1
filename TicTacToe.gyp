class Game:
    # Represents the visual representation of the game
    board_layout = """
      |     |      
   7  |  8  |  9   
      |     |      
 ----------------- 
      |     |      
   4  |  5  |  6   
      |     |      
 ----------------- 
      |     |      
   1  |  2  |  3   
      |     |      
"""
# Represents the list model of the game. (abstract)

    board_game = board_layout
    player1= 'X'
    player2= 'O'
    win = False 
    fullBoard = False 

    print("Welcome to Terminal Tic Tac Toe!")
    
    name = input("X or O?")
    print("Good luck, Player " + name + ", Player X moves first!")
    player= 'X'

    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    move = input("Player X, where will you move? ")

    # Set the board game equal to the initial board_layout
    def display_board(self):
        self.board_game = self.board_layout

    def space_check(self, position):
        availability = True
        if self.board[position] == "#": #acceseing the location in borad to check if avalable
            availability = True
        else:
            availability = False
        return availability

        #Player moves marker
    def place_marker(self, marker, position):
        self.board[position] = marker
        return self.board 

    def win_check(self):
        win = False 
        if self.board[7] == self.board[8] == self.board[9]:
            win = True  
            print("You won!")
        elif self.board[6] == self.board[5] == self.board[4]:
            win = True 
            print("You won!")
        elif self.board[3] == self.board[2] == self.board[1]:
            win = True
            print("You won!")
        elif self.board[9] == self.board[6] == self.board[3]:
            win = True 
            print("You won!")
        elif self.board[8] == self.board[5] == self.board[2]:
            win = True 
            print("You won!")
        elif self.board[7] == self.board[4] == self.board[1]:
            win = True 
            print("You won!")
        elif self.board[9] == self.board[5] == self.board[1]:
            win = True 
            print("You won!")
        elif self.board[7] == self.board[5] == self.board[3]:
            win = True
            print("You won!") 
        else:
            win = False 
            print("You lost :(")
        return win 

    def full_board_check(self):
        fullBoard = False
        for i in self.board:
            if i == '#':
                fullBoard = False 
            else:
                fullBoard = True
            print("The board is full?" + fullBoard)
            
    def replay(self):
        playAgain = input("Do you want to play again? y/n")
        if playAgain.lower() == 'y':
            return True
        elif playAgain.lower() == 'n':
            return False
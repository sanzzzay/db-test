import random
from redis_manager.base import RedisManager
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        r = RedisManager.get_client()
        while True:
            try:
                position = int(input(f"{self.name}, enter your move (1-9): ")) - 1
                if 0 <= position <= 8 and board.cells[position] == " ":
                    r.publish('tic-tac-toe', position)
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter a number between 1 and 9.")

class Board:
    def __init__(self):
        self.cells = [" " for _ in range(9)]

    def display(self):
        """
        Displays the current state of a tic-tac-toe board.
        Parameters:
            - self: Instance of the class containing the 'cells' attribute, which is a list representing the board state.
        Returns:
            - None: This function does not return a value.
        Example:
            - board.display() would print a 3x3 tic-tac-toe board using the 'cells' attribute of the board instance.
        """
        r = RedisManager.get_client()
        p = r.pubsub()
        p.subscribe('tic-tac-toe')
        for i in range(0, 9, 3):
            print(f" {self.cells[i]} | {self.cells[i+1]} | {self.cells[i+2]} ")
            if i < 6:
                print("-----------")

    def is_full(self):
        return " " not in self.cells

    def check_winner(self, symbol):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]
        return any(all(self.cells[i] == symbol for i in combo) for combo in winning_combinations)

class Game:
    def __init__(self):
        self.board = Board()
        self.players = [
            Player("Player X", "X"),
            Player("Player O", "O"),
            Player("Player Z", "Z")
        ]
        random.shuffle(self.players)

    def play(self):

        current_player_index = 0
        while True:
            self.board.display()
            current_player = self.players[current_player_index]
            position = current_player.make_move(self.board)
            self.board.cells[position] = current_player.symbol

            if self.board.check_winner(current_player.symbol):
                self.board.display()
                print(f"{current_player.name} wins!")
                break

            if self.board.is_full():
                self.board.display()
                print("It's a tie!")
                break

            current_player_index = (current_player_index + 1) % 3

if __name__ == "__main__":
    game = Game()
    game.play()
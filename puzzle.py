class PuzzleState:
    def __init__ (self, board, size, parent = None, move = None, cost = 0):
        self.board = board
        self.size = size
        self.parent = parent
        self.move = move
        self.cost = cost

    # Finds the position of the blank tile 0
    def find_blank (self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return i, j
        return None
    
    # Gets the possible moves from the current state, and returns the new states that result from those moves
    def get_neighbors (self):
        neighbors = []
        blank_pos = self.find_blank()
        row = blank_pos[0]
        col = blank_pos[1]

        # Possible moves
        moves = [(-1, 0, 'up'),
                 (1, 0, 'down'),
                 (0, -1, 'left'),
                 (0, 1, 'right')]
        
        for row_change, col_change, direction in moves:
            new_row = row + row_change
            new_col = col + col_change

            # Makes sure we are inside the board
            if new_row >= 0 and new_row < self.size and new_col >= 0 and new_col < self.size:
                new_board = []

                for rows in self.board:
                    new_board.append(rows.copy())
                
                # Swaps the blank tile with the tile in the direction of the move to create the new board configuration
                new_board[row][col] = new_board[new_row][new_col]
                new_board[new_row][new_col] = 0
                
                # The new state has the new board, the same size, the current state as its parent, the move that was made to get to it, and a cost that is one more than the current state's cost
                new_state = PuzzleState(new_board, self.size, parent = self, move = direction, cost = self.cost + 1)
                neighbors.append(new_state)

        return neighbors
    
    # This checks if the current state is the goal state
    def is_goal (self, goal):
        return self.board == goal
    
    # Converts each row of the board to a tuple and returns a tuple of those tuples, so that the state can be stored in a set for visited states since lists can't be stored in sets but tuples can
    def to_tuple (self):
        result = []
        for row in self.board:
            result.append(tuple(row))
        return tuple(result)
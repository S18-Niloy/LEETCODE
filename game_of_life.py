class Solution:
    def gameOfLife(self, board):
        m = len(board)
        n = len(board[0])

        # Define the eight possible neighbors' directions
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        # Copy the board to create the next state
        next_state = [[board[i][j] for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                live_count = 0

                # Count the live neighbors
                for direction in directions:
                    row, col = i + direction[0], j + direction[1]
                    if 0 <= row < m and 0 <= col < n and board[row][col] == 1:
                        live_count += 1

                # Apply the rules of the game to determine the next state
                if board[i][j] == 1 and (live_count < 2 or live_count > 3):
                    next_state[i][j] = 0
                elif board[i][j] == 0 and live_count == 3:
                    next_state[i][j] = 1

        # Update the original board with the next state
        for i in range(m):
            for j in range(n):
                board[i][j] = next_state[i][j]

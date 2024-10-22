from random import randint

# A utility function that configures the 2D array "board" with a given state.
def configureBoard(board, state):
    for i in range(4):
        board[state[i]][i] = 1  # Place the queen

# A utility function that prints the 2D array "board".
def printBoard(board):
    for row in board:
        print(*row)
    print()  # Print an empty line for better readability

# A utility function to calculate the number of attacking pairs of queens.
def calculateObjective(board, state):
    attacking = 0
    for i in range(4):
        row = state[i]

        # Check left
        for col in range(i):
            if state[col] == row:
                attacking += 1
            if abs(state[col] - row) == abs(col - i):
                attacking += 1

    return attacking

# A utility function to generate a board configuration given the state.
def generateBoard(board, state):
    for i in range(4):
        for j in range(4):
            board[i][j] = 0
    for i in range(4):
        board[state[i]][i] = 1

# This function gets the neighbor of the current state with the least objective value.
def getNeighbour(board, state):
    best_state = state[:]
    best_objective = calculateObjective(board, state)

    for i in range(4):
        original_row = state[i]
        for j in range(4):
            if j != original_row:  # Try moving to a different row
                state[i] = j
                generateBoard(board, state)
                objective = calculateObjective(board, state)

                # Print the current state and neighbor's cost
                print(f"Current state: {state}, Cost: {objective}")

                if objective < best_objective:
                    best_objective = objective
                    best_state = state[:]

        state[i] = original_row  # Restore original row

    return best_state, best_objective

def hillClimbing(board, state):
    while True:
        generateBoard(board, state)
        current_objective = calculateObjective(board, state)
        print(f"Current state: {state}, Cost: {current_objective}")

        if current_objective == 0:
            print("Goal configuration reached!")
            printBoard(board)
            break

        next_state, next_objective = getNeighbour(board, state)

        if next_objective >= current_objective:
            print("No better neighbor found, stopping.")
            printBoard(board)
            break

        state[:] = next_state  # Update state to best neighbor

# Driver code
N = 4  # Fixed for 4-queens
state = [0] * N
board = [[0 for _ in range(N)] for _ in range(N)]

# User input for starting state
print("Enter the starting positions of the queens (0 to 3) for each column (0-based index):")
for i in range(N):
    while True:
        try:
            pos = int(input(f"Column {i}: "))
            if pos < 0 or pos >= N:
                print(f"Please enter a number between 0 and {N-1}.")
            else:
                state[i] = pos
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Configure the board with the user's starting state
configureBoard(board, state)

# Do hill climbing on the board obtained
hillClimbing(board, state)
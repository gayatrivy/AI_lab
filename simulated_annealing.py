import random
import math

def calculate_conflicts(state):
    n = len(state)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def n_queens_simulated_annealing(n, max_iterations=1000, initial_temp=100, cooling_rate=0.99):
    state = [random.randint(0, n - 1) for _ in range(n)]

    def get_neighbor(state):
        neighbor = state[:]
        row = random.randint(0, n - 1)
        new_col = random.randint(0, n - 1)
        while new_col == neighbor[row]:
            new_col = random.randint(0, n - 1)
        neighbor[row] = new_col
        return neighbor

    current_conflicts = calculate_conflicts(state)
    temperature = initial_temp

    for iteration in range(max_iterations):
        if current_conflicts == 0:
            return state, iteration

        neighbor = get_neighbor(state)
        neighbor_conflicts = calculate_conflicts(neighbor)
        delta = neighbor_conflicts - current_conflicts

        if delta < 0 or random.random() < math.exp(-delta / temperature):
            state = neighbor
            current_conflicts = neighbor_conflicts

        temperature *= cooling_rate

    return state, max_iterations

n = 8
solution, iterations = n_queens_simulated_annealing(n)
if calculate_conflicts(solution) == 0:
    print(f"Solution found in {iterations} iterations: {solution}")
else:
    print(f"No solution found after {iterations} iterations. Best state: {solution}")
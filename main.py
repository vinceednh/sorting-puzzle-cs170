from puzzle import PuzzleState
from search import uniform_cost_search

# This makes the size of the board so it can be run with multiple different sizes
def make_goal(size):
    goal = []
    value = 1

    for i in range(size):
        row = []
        for j in range(size):
            row.append(value)
            value += 1
        goal.append(row)

    goal[size - 1][size - 1] = 0
    return goal

def main():
    size = int(input("Enter puzzle size: "))

    print("Enter board rows(use 0 for blank tile):")
    board = []

    for i in range(size):
        row = list(map(int, input().split()))
        board.append(row)

    goal = make_goal(size)
    start_state = PuzzleState(board, size)

    # Uniform Cost Search
    result, nodes_expanded, max_queue_size = uniform_cost_search(start_state, goal)

    if result is None:
        print("No solution found.")
    else:
        print("Goal reached!")
        print(f"Solution depth was {result.cost}")
        print(f"Nodes expanded: {nodes_expanded}")
        print(f"Max queue size: {max_queue_size}")

if __name__ == "__main__":
    main()
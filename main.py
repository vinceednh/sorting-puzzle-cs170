import time
from puzzle import PuzzleState
from search import uniform_cost_search, a_star_search

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
    size = int(input("Enter puzzle size (For example 3 for a 3x3 puzzle): "))

    print("Enter the initial board row by row, and use 0 for the blank tile (For example, 1 2 3 enter):")
    board = []

    for i in range(size):
        row = input().split()
        row_ints = []
        for x in row:
            row_ints.append(int(x))
        board.append(row_ints)

    goal = make_goal(size)
    start_state = PuzzleState(board, size)

    choice = input("Select algorithm to see traces for: (1) Uniform Cost Search, (2) A* Search with Misplaced Tiles Heuristic, (3) A* Search with Manhattan Distance Heuristic: \n")

    if choice == "1":
        show_output_ucs = True
        show_output_misplaced = False
        show_output_manhattan = False
    elif choice == "2":
        show_output_ucs = False
        show_output_misplaced = True
        show_output_manhattan = False
    elif choice == "3":
        show_output_ucs = False
        show_output_misplaced = False
        show_output_manhattan = True
    else:
        print("Invalid choice, Showing no steps.")
        show_output_ucs = False
        show_output_misplaced = False
        show_output_manhattan = False

    # All of these algorithms use time() to measure the time taken
    # Uniform Cost Search
    start_time = time.time()
    result, nodes_expanded, max_queue_size = uniform_cost_search(start_state, goal, show_output_ucs)
    end_time = time.time()
    duration = end_time - start_time

    # A* Search with Misplaced Tiles Heuristic
    start_time = time.time()
    result, nodes_expanded, max_queue_size = a_star_search(start_state, goal, 'misplaced', show_output_misplaced)
    end_time = time.time()
    duration = end_time - start_time

    # A* Search with Manhattan Distance Heuristic
    start_time = time.time()
    result, nodes_expanded, max_queue_size = a_star_search(start_state, goal, 'manhattan', show_output_manhattan)
    end_time = time.time()
    duration = end_time - start_time


if __name__ == "__main__":
    main()
import time
import matplotlib.pyplot as plt
from puzzle import PuzzleState
from search import uniform_cost_search, a_star_search_misplaced, a_star_search_manhattan

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

    algorithms = ["UCS", "A* Misplaced", "A* Manhattan"]
    nodes_expanded_list = []
    max_queue_size_list = []
    times = []

    # All of these algorithms use time() to measure the time taken
    # Uniform Cost Search
    start_time = time.time()
    result_ucs, nodes_expanded_ucs, max_queue_size_ucs = uniform_cost_search(start_state, goal, show_output_ucs)
    end_time = time.time()
    duration = end_time - start_time
    nodes_expanded_list.append(nodes_expanded_ucs)
    max_queue_size_list.append(max_queue_size_ucs)
    times.append(duration)

    if show_output_ucs:
        print(f"Execution time: {duration:.2f} seconds")

    # A* Search with Misplaced Tiles Heuristic
    start_time = time.time()
    result_misplaced, nodes_expanded_misplaced, max_queue_size_misplaced = a_star_search_misplaced(start_state, goal, show_output_misplaced)
    end_time = time.time()
    duration = end_time - start_time
    nodes_expanded_list.append(nodes_expanded_misplaced)
    max_queue_size_list.append(max_queue_size_misplaced)
    times.append(duration)

    if show_output_misplaced:
        print(f"Execution time: {duration:.2f} seconds")

    # A* Search with Manhattan Distance Heuristic
    start_time = time.time()
    result_manhattan, nodes_expanded_manhattan, max_queue_size_manhattan = a_star_search_manhattan(start_state, goal, show_output_manhattan)
    end_time = time.time()
    duration = end_time - start_time
    nodes_expanded_list.append(nodes_expanded_manhattan)
    max_queue_size_list.append(max_queue_size_manhattan)
    times.append(duration)

    if show_output_manhattan:
        print(f"Execution time: {duration:.2f} seconds")

    if result_ucs is None and result_misplaced is None and result_manhattan is None:
        print("No solution found.")

    #matplotlib nodes expanded by algorithm
    plt.figure(figsize=(9, 3))
    plt.bar(algorithms, nodes_expanded_list)
    plt.xlabel('Algorithm')
    plt.ylabel('Nodes Expanded')
    plt.title('Nodes Expanded by Algorithm')
    plt.tight_layout()
    plt.show()

    #matplotlib max queue size by algorithm
    plt.figure(figsize=(9, 3))
    plt.bar(algorithms, max_queue_size_list)
    plt.xlabel('Algorithm')
    plt.ylabel('Max Queue Size')
    plt.title('Max Queue Size by Algorithm')
    plt.show()

if __name__ == "__main__":
    main()
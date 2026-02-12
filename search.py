import heapq

def uniform_cost_search(start_state, goal_state, show_output = True):
    # Using a priority queue with the start state
    frontier = []
    visited = set()
    nodes_expanded = 0
    max_queue_size = 0
    counter = 0

    heapq.heappush(frontier, (0, counter, start_state))
    counter += 1

    while frontier:
        max_queue_size = max(max_queue_size, len(frontier))

        # Pop the state with the lowest cost
        item = heapq.heappop(frontier)
        current = item[2]

        # Makes sure we don't revisit states we've already seen
        if id(current) in visited:
            continue

        # Prints the output if the user selected to see it
        if show_output:
            print(f"The best state to expand with g(n) = {current.cost} and h(n) = 0 is...")
            for row in current.board:
                print(row)
            print()
        
        # Checks if we've reached the goal state
        if current.is_goal(goal_state):
            if show_output:
                print("Goal reached!")
                print(f"Solution depth was {current.cost}")
                print(f"Number of nodes expanded: {nodes_expanded}")
                print(f"Max queue size: {max_queue_size}")
            return current, nodes_expanded, max_queue_size

        # Expands the neighbors of the current state and adds them to the frontier
        neighbors = current.get_neighbors()
        for n in neighbors:
            heapq.heappush(frontier, (n.cost, counter, n))
            counter += 1

    return None, nodes_expanded, max_queue_size
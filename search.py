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
        state_tuple = current.to_tuple()
        if state_tuple in visited:
            continue

        visited.add(state_tuple)
        nodes_expanded += 1

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

def misplaced_tiles_heuristic(state, goal_state):
    count = 0
    for i in range(state.size):
        for j in range(state.size):

            # Skips the blank tile
            if state.board[i][j] != 0:
                if state.board[i][j] != goal_state[i][j]:
                    count += 1

    return count

def manhattan_distance_heuristic(state, goal_state):
    distance = 0
    for i in range(state.size):
        for j in range(state.size):
            value = state.board[i][j]

            if value != 0:

                target = goal_state[value]
                goal_row = target[0]
                goal_col = target[1]

                distance += abs(i - goal_row) + abs(j - goal_col)

    return distance

def a_star_search(start_state, goal_state, heuristic, show_output = True):
    frontier = []
    visited = set()
    nodes_expanded = 0
    max_queue_size = 0
    counter = 0

    heapq.heappush(frontier, (0, counter, start_state))
    counter += 1

    goal_positions = {}
    for i in range(len(goal_state)):
        for j in range(len(goal_state)):
            value = goal_state[i][j]
            goal_positions[value] = (i, j)

    while frontier:
        max_queue_size = max(max_queue_size, len(frontier))
        item = heapq.heappop(frontier)
        current = item[2]
        
        state_tuple = current.to_tuple()
        if state_tuple in visited:
            continue

        visited.add(state_tuple)
        nodes_expanded += 1

        if heuristic == 'misplaced':
            h_val = misplaced_tiles_heuristic(current, goal_state)
        elif heuristic == 'manhattan':
            h_val = manhattan_distance_heuristic(current, goal_positions)
        else:
            h_val = 0
        
        if show_output:
            print(f"The best state to expand with g(n) = {current.cost} and h(n) = {h_val} is...")
            for row in current.board:
                print(row)
            print()

        if current.is_goal(goal_state):
            if show_output:
                print("Goal reached!")
                print(f"Solution depth was {current.cost}")
                print(f"Number of nodes expanded: {nodes_expanded}")
                print(f"Max queue size: {max_queue_size}")
            return current, nodes_expanded, max_queue_size
        
        neighbors = current.get_neighbors()
        for n in neighbors:
            if heuristic == 'misplaced':
                h = misplaced_tiles_heuristic(n, goal_state)
            elif heuristic == 'manhattan':
                h = manhattan_distance_heuristic(n, goal_positions)
            else:
                h = 0

            priority = n.cost + h
            heapq.heappush(frontier, (priority, counter, n))
            counter += 1

    return None, nodes_expanded, max_queue_size
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

def a_star_search_misplaced(start_state, goal_state, show_output = True):
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

        # Pop the state with the lowest cost + heuristic
        item = heapq.heappop(frontier)
        current = item[2]

        # Makes sure we don't revisit states we've already seen
        state_tuple = current.to_tuple()
        if state_tuple in visited:
            continue

        visited.add(state_tuple)
        nodes_expanded += 1

        # Calculate the misplaced tiles for the current state
        h_val = 0
        for i in range(current.size):
            for j in range(current.size):
                if current.board[i][j] != 0:
                    if current.board[i][j] != goal_state[i][j]:
                        h_val += 1

        # Prints the output if the user selected to see it
        if show_output:
            print(f"The best state to expand with g(n) = {current.cost} and h(n) = {h_val} is...")
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

        # Calculate the misplaced tiles for the neighbors and add them to the frontier
        neighbors = current.get_neighbors()
        for n in neighbors:
            h = 0
            for i in range(n.size):
                for j in range(n.size):
                    if n.board[i][j] != 0:
                        if n.board[i][j] != goal_state[i][j]:
                            h += 1

            priority = n.cost + h
            heapq.heappush(frontier, (priority, counter, n))
            counter += 1

    return None, nodes_expanded, max_queue_size

def a_star_search_manhattan(start_state, goal_state, show_output = True):
    # Using a priority queue with the start state
    frontier = []
    visited = set()
    nodes_expanded = 0
    max_queue_size = 0
    counter = 0

    heapq.heappush(frontier, (0, counter, start_state))
    counter += 1

    # Computes the positions of each tile in the goal state
    goal_positions = {}
    for i in range(len(goal_state)):
        for j in range(len(goal_state)):
            value = goal_state[i][j]
            goal_positions[value] = (i, j)

    while frontier:
        max_queue_size = max(max_queue_size, len(frontier))

        # Pop the state with the lowest cost + heuristic
        item = heapq.heappop(frontier)
        current = item[2]

        # Makes sure we don't revisit states we've already seen
        state_tuple = current.to_tuple()
        if state_tuple in visited:
            continue

        visited.add(state_tuple)
        nodes_expanded += 1

        # Calculate the Manhattan distance for the current state
        h_val = 0
        for i in range(current.size):
            for j in range(current.size):
                value = current.board[i][j]
                if value != 0:
                    goal_position = goal_positions[value]
                    goal_row = goal_position[0]
                    goal_col = goal_position[1]
                    h_val += abs(i - goal_row) + abs(j - goal_col)

        # Prints the output if the user selected to see it
        if show_output:
            print(f"The best state to expand with g(n) = {current.cost} and h(n) = {h_val} is...")
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

        # Calculate the Manhattan distance for the neighbors and add them to the frontier
        neighbors = current.get_neighbors()
        for n in neighbors:
            h = 0
            for i in range(n.size):
                for j in range(n.size):
                    value = n.board[i][j]
                    if value != 0:
                        goal_position = goal_positions[value]
                        goal_row = goal_position[0]
                        goal_col = goal_position[1]
                        h += abs(i - goal_row) + abs(j - goal_col)

            priority = n.cost + h
            heapq.heappush(frontier, (priority, counter, n))
            counter += 1

    return None, nodes_expanded, max_queue_size
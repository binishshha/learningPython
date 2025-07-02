def dfs_depth_limited(a, b, target_x, target_y, max_depth, initial_state):
    # Visited set for the current depth-limited DFS run
    visited = set()

    def dfs_recursive(current_state, path, current_depth):
        x, y = current_state

        # Check depth limit
        if current_depth > max_depth:
            return None  # Reached depth limit, don't go deeper

        # Add to visited for this path
        visited.add(current_state)

        # Check if the target is reached
        if (target_x is not None and x == target_x) and \
           (target_y is not None and y == target_y):
            return path  # Goal achieved, return the current path

        next_possible_states = []

        # Rules (same as your 8 rules)
        # 1. Fill jug A
        if x < a:
            new_state = (a, y)
            if new_state not in visited:  # Important: only add if not visited IN THIS PATH
                next_possible_states.append(new_state)

        # 2. Fill jug B
        if y < b:
            new_state = (x, b)
            if new_state not in visited:
                next_possible_states.append(new_state)

        # 3. Empty jug A
        if x > 0:
            new_state = (0, y)
            if new_state not in visited:
                next_possible_states.append(new_state)

        # 4. Empty jug B
        if y > 0:
            new_state = (x, 0)
            if new_state not in visited:
                next_possible_states.append(new_state)

        # 5. Pour B into A until A is full
        space_in_a = a - x
        amount_to_pour_b_to_a = min(y, space_in_a)
        if amount_to_pour_b_to_a > 0:
            new_state = (x + amount_to_pour_b_to_a, y - amount_to_pour_b_to_a)
            if new_state not in visited:
                next_possible_states.append(new_state)

        # 6. Pour A into B until B is full
        space_in_b = b - y
        amount_to_pour_a_to_b = min(x, space_in_b)
        if amount_to_pour_a_to_b > 0:
            new_state = (x - amount_to_pour_a_to_b, y + amount_to_pour_a_to_b)
            if new_state not in visited:
                next_possible_states.append(new_state)

        # 7. Pour all B into A
        if x + y <= a and y > 0:
            new_state = (x + y, 0)
            if new_state not in visited:
                next_possible_states.append(new_state)

        # 8. Pour all A into B
        if x + y <= b and x > 0:
            new_state = (0, x + y)
            if new_state not in visited:
                next_possible_states.append(new_state)

        for next_s in next_possible_states:
            solution_path = dfs_recursive(next_s, path + [next_s], current_depth + 1)
            if solution_path:
                return solution_path
        
        # Backtrack: Remove current state from visited set
        visited.remove(current_state)
        
        return None

    return dfs_recursive(initial_state, [initial_state], 0)

def iterative_deepening_dfs(a, b, target_x, target_y, initial_state=(0, 0), max_total_steps=20):
    for depth_limit in range(max_total_steps + 1):
        path = dfs_depth_limited(a, b, target_x, target_y, depth_limit, initial_state)
        if path:
            print(f"\nSolution found at depth {depth_limit}:")
            for state in path:
                print(state)
            print(f"Total steps: {len(path) - 1}")
            return path
    print("No solution found within the maximum allowed steps.")
    return None

# --- Run the IDDFS example ---
if __name__ == "__main__":
    a_capacity = 3 # Jug 1 capacity
    b_capacity = 5 # Jug 2 capacity
    target_x_val = 1
    target_y_val = 5

    print(f"Jug 1 Capacity: {a_capacity}, Jug 2 Capacity: {b_capacity}")
    print(f"Target State: ({target_x_val}, {target_y_val})")

    # --- Manual user input for initial state ---
    while True:
        try:
            initial_x = int(input(f"Enter initial water in Jug A (0 to {a_capacity}): "))
            initial_y = int(input(f"Enter initial water in Jug B (0 to {b_capacity}): "))
            if 0 <= initial_x <= a_capacity and 0 <= initial_y <= b_capacity:
                user_initial_state = (initial_x, initial_y)
                break
            else:
                print("Invalid initial amounts. Please enter values within jug capacities.")
        except ValueError:
            print("Invalid input. Please enter integers.")
    # --- End manual user input ---

    print(f"Starting from Initial State: {user_initial_state}")

    shortest_path_iddfs = iterative_deepening_dfs(a_capacity, b_capacity, target_x_val, target_y_val, initial_state=user_initial_state, max_total_steps=15)

    if not shortest_path_iddfs:
        print("Could not find a solution for this target.")
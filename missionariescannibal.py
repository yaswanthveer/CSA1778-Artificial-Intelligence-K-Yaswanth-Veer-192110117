from collections import deque

def is_valid_state(state):
    missionaries, cannibals, boat = state
    if missionaries < 0 or cannibals < 0 or missionaries > 3 or cannibals > 3:
        return False
    if missionaries != 0 and missionaries < cannibals:
        return False
    if missionaries != 3 and missionaries > cannibals:
        return False
    return True

def generate_next_states(state):
    next_states = []
    missionaries, cannibals, boat = state

    if boat == "left":
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    next_state = (missionaries - m, cannibals - c, "right")
                    if is_valid_state(next_state):
                        next_states.append(next_state)
    else:
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    next_state = (missionaries + m, cannibals + c, "left")
                    if is_valid_state(next_state):
                        next_states.append(next_state)

    return next_states

def bfs_missionaries_cannibals():
    start_state = (3, 3, "left")
    goal_state = (0, 0, "right")

    visited = set()
    queue = deque([(start_state, [])])

    while queue:
        current_state, path = queue.popleft()
        visited.add(current_state)

        if current_state == goal_state:
            return path + [current_state]

        next_states = generate_next_states(current_state)
        for next_state in next_states:
            if next_state not in visited:
                queue.append((next_state, path + [current_state]))

    return None

def print_solution(path):
    if path:
        for state in path:
            missionaries, cannibals, boat = state
            print(f"Missionaries: {missionaries}, Cannibals: {cannibals}, Boat: {boat}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    solution_path = bfs_missionaries_cannibals()
    print_solution(solution_path)
from collections import deque

def water_jug_problem(x, y, target):
    visited = set()
    queue = deque([(0, 0)])
    
    while queue:
        jug1, jug2 = queue.popleft()
        
        if (jug1, jug2) in visited:
            continue
        
        visited.add((jug1, jug2))
        
        if jug1 == target or jug2 == target:
            return jug1, jug2
        
        # Fill jug1
        if jug1 < x:
            queue.append((x, jug2))
        
        # Fill jug2
        if jug2 < y:
            queue.append((jug1, y))
        
        # Empty jug1
        if jug1 > 0:
            queue.append((0, jug2))
        
        # Empty jug2
        if jug2 > 0:
            queue.append((jug1, 0))
        
        # Pour from jug1 to jug2
        pour_amount = min(jug1, y - jug2)
        if pour_amount > 0:
            queue.append((jug1 - pour_amount, jug2 + pour_amount))
        
        # Pour from jug2 to jug1
        pour_amount = min(jug2, x - jug1)
        if pour_amount > 0:
            queue.append((jug1 + pour_amount, jug2 - pour_amount))
    
    return None

if __name__ == "__main__":
    jug1_capacity = 4
    jug2_capacity = 3
    target_amount = 2
    
    result = water_jug_problem(jug1_capacity, jug2_capacity, target_amount)
    
    if result:
        jug1_amount, jug2_amount = result
        print(f"Solution found: ({jug1_amount}, {jug2_amount})")
    else:
        print("No solution found.")
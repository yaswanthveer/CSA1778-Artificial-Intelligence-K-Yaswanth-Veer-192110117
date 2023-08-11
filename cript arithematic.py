from itertools import permutations

def solve_cryptarithmetic(puzzle):
    words = puzzle.split()
    unique_letters = set("".join(words))
    if len(unique_letters) > 10:
        return None

    for perm in permutations(range(10), len(unique_letters)):
        digit_map = {letter: digit for letter, digit in zip(unique_letters, perm)}
        
        if all(digit_map[word[0]] != 0 for word in words):
            expression = " + ".join("".join(str(digit_map[letter]) for letter in word) for word in words[:-1])
            if eval(expression) == int("".join(str(digit_map[letter]) for letter in words[-1])):
                return digit_map

    return None

if __name__ == "__main__":
    puzzle = "send + more = money"
    
    solution = solve_cryptarithmetic(puzzle)
    
    if solution:
        print("Solution found:")
        for letter, digit in solution.items():
            print(f"{letter}: {digit}")
    else:
        print("No solution found.")
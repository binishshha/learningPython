import itertools
import re

def solve_cryptarithmetic(puzzle):
    """
    Efficiently solves a cryptarithmetic puzzle like "SEND + MORE = MONEY".
    Returns a valid mapping of letters to digits, or None if no solution exists.
    """
    # Remove spaces and split expression
    puzzle = puzzle.replace(" ", "")
    if '=' not in puzzle:
        raise ValueError("Invalid format. Expected 'EXPRESSION = RESULT'.")

    lhs, rhs = puzzle.split('=')

    # Extract all words and operators
    words = re.split(r'[+\-*/]', lhs) + [rhs]
    operators = re.findall(r'[+\-*/]', lhs)

    # Get unique letters
    letters = sorted(set(filter(str.isalpha, puzzle)))
    if len(letters) > 10:
        print("Too many unique letters (max 10).")
        return None

    # Identify leading letters (cannot be zero)
    leading = set(word[0] for word in words)

    # Precompute word to function: word → lambda mapping: SEND -> lambda m: 1000*m['S'] + 100*m['E'] + ...
    def word_to_number(word):
        return lambda m: sum((10**i) * m[ch] for i, ch in enumerate(reversed(word)))

    word_funcs = [word_to_number(word) for word in words]

    # Main search over permutations
    for perm in itertools.permutations(range(10), len(letters)):
        letter_digit = dict(zip(letters, perm))

        # Skip if any leading letter is mapped to 0
        if any(letter_digit[ch] == 0 for ch in leading):
            continue

        # Compute numeric values
        numbers = [func(letter_digit) for func in word_funcs]
        lhs_value = numbers[:-1]
        rhs_value = numbers[-1]

        # Evaluate expression using integer math
        result = lhs_value[0]
        for op, val in zip(operators, lhs_value[1:]):
            if op == '+':
                result += val
            elif op == '-':
                result -= val
            elif op == '*':
                result *= val
            elif op == '/':
                if val == 0 or result % val != 0:
                    break
                result //= val

        if result == rhs_value:
            return letter_digit

    return None

# --- Run Example ---
if __name__ == "__main__":
    puzzles = ["SEND + MORE = MONEY"]

    for puzzle in puzzles:
        print(f"\nSolving: {puzzle}")
        try:
            solution = solve_cryptarithmetic(puzzle)
            if solution:
                print("Solution found:")
                for letter in sorted(solution):
                    print(f"  {letter} = {solution[letter]}")

                # Verification
                verified = puzzle
                for letter, digit in solution.items():
                    verified = verified.replace(letter, str(digit))
                print(f"Verification: {verified}")
            else:
                print("No solution found.")
        except Exception as e:
            print(f"Error: {e}")

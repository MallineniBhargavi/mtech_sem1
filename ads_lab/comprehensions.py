# 04. Comprehensions

# ------ For Execution --------
# cd ads_lab 
# pwd
# python comprehensions.py


def list_comprehension_demo(numbers):
    
    return [n ** 2 for n in numbers]

def dict_comprehension_demo(numbers):
    """Return a dict mapping each number to its square using a
    dictionary comprehension.
    Args:
    numbers (list[int]): Input numbers.
    Returns:
    dict[int, int]: Mapping of number -> square.
    """
    return {n: n ** 2 for n in numbers}

def set_comprehension_demo(numbers):
    """Return the set of remainders (mod 3) using a set comprehension.
    (A set automatically removes duplicate values.)
    Args:
    numbers (list[int]): Input numbers.
    Returns:
    set[int]: Unique remainders when each number is divided by 3.
    """
    return {n % 3 for n in numbers}

def generator_comprehension_demo(numbers):
    """Return a generator that lazily yields the cube of each number.
    Args:
    numbers (list[int]): Input numbers.
    Returns:
    generator: A generator object; values are computed on demand
    when iterated (e.g., with next() or a for-loop).
    """
    return (n ** 3 for n in numbers)

def main():
    """Demonstrate all four comprehension types on the same input data."""
    numbers = [1, 2, 3, 4, 5, 6]
    print(f"Input numbers: {numbers}\n")
    # a) List comprehension
    squares = list_comprehension_demo(numbers)
    print(f"a) List Comprehension (squares) : {squares}")
    # b) Dictionary comprehension
    square_map = dict_comprehension_demo(numbers)
    print(f"b) Dictionary Comprehension (n -> n^2): {square_map}")
    # c) Set comprehension
    remainders = set_comprehension_demo(numbers)
    print(f"c) Set Comprehension (n % 3, unique) : {remainders}")
    # d) Generator comprehension
    cubes_gen = generator_comprehension_demo(numbers)
    print("d) Generator Comprehension (cubes) : ", end="")
    # A generator can only be iterated once; convert to a list to display it
    # (in real use, you'd typically loop over it directly to save memory).
    print(list(cubes_gen))

if __name__ == "__main__":
    main()

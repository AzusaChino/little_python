"""
Generates an array, containing the Fibonacci sequence, up until the nth term.

Starting with 0 and 1, use list.append() to add the sum of the last two numbers of the list to the end of the list, until the length of the list reachesn. Ifnis less or equal to0, return a list containing0`.
"""


def fibonacci(n):
    if n <= 0:
        return [0]

    sequence = [0, 1]
    while len(sequence) <= n:
        sequence.append(sequence[len(sequence) - 1] + sequence[len(sequence) - 2])

    return sequence


print(fibonacci(7))

def even_filter(nums):
    for num in nums:
        if num % 2 == 0:
            yield num


def multiply_by_three(nums):
    for n in nums:
        yield n * 3


def convert_to_string(nums):
    for n in nums:
        yield 'The number : %s' % n


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pipeline = convert_to_string(multiply_by_three(even_filter(nums)))

for n in pipeline:
    print(n)

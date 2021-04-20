def process(num):
    if num % 2 != 0:
        return
    num = num * 3
    num = 'The number : %s' % num
    return num


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in nums:
    print(process(n))

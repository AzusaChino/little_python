'''
Bubble_sort uses the technique of comparing and swapping
'''


def bubble_sort(lst):
    for pass_num in range(len(lst) - 1, 0, -1):
        for i in range(pass_num):
            if lst[i] > lst[i + 1]:  # compare
                temp = lst[i]  # swap
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
    return lst


if __name__ == '__main__':
    lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(bubble_sort(lst))

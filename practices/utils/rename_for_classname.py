def rename(input_str: str):
    str_list = input_str.split(' ')

    print(''.join(map(lambda x: x.capitalize(), str_list)))
    print('-'.join(map(lambda x: x.casefold(), str_list)))


if __name__ == '__main__':
    rename(input("please input: "))
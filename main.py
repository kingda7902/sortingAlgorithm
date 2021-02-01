from sorting import quick_sort
from utils import timer, read_the_numbers


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    file = 'numbers.txt'
    raw_data = read_the_numbers(file)
    data = list(map(int, raw_data))

    # data = timer(sorted)(data)
    timer(quick_sort)(data, 0, len(data) - 1)
    print(data[:10])

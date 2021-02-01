from sorting import quick_sort, quicksort
from utils import timer, read_the_numbers


if __name__ == '__main__':

    file = 'numbers.txt'
    raw_data = read_the_numbers(file)
    data = list(map(int, raw_data))

    # data = timer(sorted)(data)
    # timer(quick_sort)(data, 0, len(data) - 1)
    timer(quicksort)(data, 0, len(data) - 1)
    print(data[:10])

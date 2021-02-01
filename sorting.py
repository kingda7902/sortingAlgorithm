

def quick_sort(numbers_data, left, right):
    if left >= right:
        return

    i = left
    j = right
    key = numbers_data[left]

    while i != j:
        while numbers_data[j] > key and i < j:
            j -= 1
        while numbers_data[i] <= key and i < j:
            i += 1
        if i < j:
            numbers_data[i], numbers_data[j] = numbers_data[i], numbers_data[j]

    quick_sort(numbers_data, left, i - 1)
    quick_sort(numbers_data, i + 1, right)


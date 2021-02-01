def swap(a, left, right):
    a[left], a[right] = a[right], a[left]


def partition(a, left, right, pivot_index) -> int:
    pivot_value = a[pivot_index]
    swap(a, pivot_index, right)
    store_index = left
    for i in range(left, right):
        if a[i] <= pivot_value:
            swap(a, store_index, i)
            store_index += 1

    swap(a, right, store_index)
    return store_index


def quicksort(a, left, right):
    """
    The inplace version from the wikipedia
    """
    if right > left:
        pivot_index = left
        pivot_new_index = partition(a, left, right, pivot_index)
        quicksort(a, left, pivot_new_index-1)
        quicksort(a, pivot_new_index+1, right)


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
    #
    # quick_sort(numbers_data, left, i - 1)
    # quick_sort(numbers_data, i + 1, right)


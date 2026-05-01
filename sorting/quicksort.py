def quicksort(array : list) -> list:
    """ Best: O(nlogn) Average: O(nlogn) Worst: O(n^2) | O(nlogn) """
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    small, equal, big = [], [], []

    for num in array:
        if num < pivot:
            small.append(num)
        elif num > pivot:
            big.append(num)
        else:
            equal.append(num)

    return quicksort(small) + equal + quicksort(big)
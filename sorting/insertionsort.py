def insertion_sort(arr):
    """ Best: O(n) Average: O(n^2) Worst: O(n^2) | O(n) """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
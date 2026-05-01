def bubblesort(arr):
    """ Best: O(n^2) Average: O(n^2) Worst: O(n^2) | O(n) """
    for _ in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
def bubble_sort(arr):
    """
    Bubble sort implementation to sort a list in ascending order.

    Args:
        arr (list): The list of integers to sort.

    Returns:
        list: The sorted list.
    """
    def swap(i, j):
        """
        Swap two elements in the list at indices i and j.

        Args:
            i (int): Index of the first element.
            j (int): Index of the second element.
        """
        arr[i], arr[j] = arr[j], arr[i]

    # TODO: Implement the bubble sort algorithm below.
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:  # Swap if greater
                swap(j, j + 1)
                swapped = True
        if not swapped:  # sorted if no swaps
            break

    return arr

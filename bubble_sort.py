def bubble_sort(arr, ascending=True):
    """
    Sorts a list in place using bubble sort.
    
    Parameters:
        arr (list): The list to be sorted.
        ascending (bool): If True (default), sort in ascending order.
                          If False, sort in descending order.
    
    Returns:
        None (the list is modified in place)
    """
    n = len(arr)
    # Outer loop: number of passes
    for i in range(n):
        swapped = False
        # Inner loop: compare adjacent elements
        # After each pass, the largest (or smallest) element bubbles to the end
        for j in range(0, n - i - 1):
            # Determine swap condition based on order
            if ascending:
                # Swap if current > next (ascending)
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            else:
                # Swap if current < next (descending)
                if arr[j] < arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
        # If no swaps were made, the list is already sorted
        if not swapped:
            break
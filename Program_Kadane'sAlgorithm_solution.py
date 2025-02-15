def max_subarray_sum(arr):
    if not arr:  # Handle edge case where the array is empty
        return None  

    max_sum = arr[0]  # Initialize with the first element
    current_sum = arr[0]  

    for i in range(1, len(arr)):  # Start loop from the second element
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(arr))  # Output: 6 (subarray: [4, -1, 2, 1])

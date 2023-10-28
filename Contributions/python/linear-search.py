def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index where the target is found
    return -1  # If the target is not found, return -1


# Example
arr = [4, 2, 1, 7, 5, 3]
target = 5
result = linear_search(arr, target)
if result != -1:
    print(f"Element found at index {result}.")
else:
    print("Element not found in the array.")

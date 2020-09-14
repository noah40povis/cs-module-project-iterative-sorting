def linear_search(arr, target):
    for i in range(len(arr)): 
        if arr[i] == target: 
            return i 
        
    return -1   # not found


#Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # find the midpoint element 
    # length // 2
    left = 0
    right = len(arr) - 1
    # keep iterating so long as left <= right
    while left <= right:
        midpoint = (right + left) // 2
        if arr[midpoint] == target:
            return midpoint
        elif arr[midpoint] > target:
            # toss out the left side of the array 
            # toss out the midpoint element itself as well 
            right = midpoint - 1
        else:
            left = midpoint + 1
    # we didn't find what we're looking for 
    return -1

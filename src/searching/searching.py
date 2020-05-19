def linear_search(arr, target):
    for i in range(0,len(arr)): 
  
        if arr[i] == target: 
            return i 

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    #size of the array
    l = 0
    r = len(arr) - 1

    while l <= r: 
  
        mid = l + (r - l) // 2

        # Check if x is present at mid 
        if arr[mid] == target: 
            return mid 
  
        # If target is greater, ignore left half 
        elif arr[mid] < target: 
            l = mid + 1
  
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1
      
    # If we reach here, then the element 
    # was not present 

    return -1  # not found

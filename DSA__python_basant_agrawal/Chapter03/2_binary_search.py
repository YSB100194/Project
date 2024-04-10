'''The binary search algorithm is based on the divide-and-conquer design technique. This algorithm 
is used to find a given element from a sorted list of elements. It first compares the search element 
with the middle element of the list; if the search element is smaller than the middle element, then 
the half of the list of elements greater than the middle element is discarded; the process repeats 
recursively until the search element is found or we reach the end of the list. It is important to note 
that in each iteration, half of the search space is discarded, which improves the performance of 
the overall algorithm because there are fewer elements to search through.'''


def binary_search(arr, start, end, key):
    while start <= end:  
        mid = start + (end - start)//2
        if arr[mid] == key:  
            return mid  
        elif arr[mid] < key:  
            start = mid + 1  
        else:  
            end = mid - 1  
    return -1  


arr = [ 4, 6, 9, 13, 14, 18, 21, 24, 38] 

x = a=int(input("Enter the number to search :")) # input from User
result = binary_search(arr, 0, len(arr)-1, x)  
print(result) 



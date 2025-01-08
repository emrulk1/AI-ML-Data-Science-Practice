def binary_search(arr , key):
    start_pos = 0
    end_pos = len(arr) - 1
    lower = -1
    upper = -1
    while(start_pos <= end_pos):
        mid_pos = (start_pos + end_pos)//2
        value = arr[mid_pos]
        lower = mid_pos if value < key else mid_pos - 1
        upper = mid_pos if value > key else mid_pos + 1

def smallest_val_greater_than_key(arr, key):
    n = len(arr)
    start = 0
    end = n-1
    res = -1
    while start <= end:
        mid = (start+end)//2
        # if arr[mid] == key:
        #     res = mid
        #     end = mid - 1
        if arr[mid] <= key:
            start = mid + 1
        else:
            end = mid - 1
    
    
    return arr[start] if start < n else 'X'

def largest_val_less_than_key(arr, key):
    start = 0
    end = len(arr)-1
    res = -1
    while start <= end:
        mid = (start+end)//2
        # if arr[mid] == key:
        #     start = mid + 1
        if arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
     
    return arr[end] if end >= 0 else 'X'
        
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().split()) )
    
    number_of_query = int(input().strip())
    qeries = list(map(int, input().split()) )
    for key in qeries:
        # print(key)
        largest_less_than_key = largest_val_less_than_key(arr, key)
        
        
        smallest_greater_than_key = smallest_val_greater_than_key(arr, key)
        
        print(largest_less_than_key , smallest_greater_than_key)
        
        
        
        
        
    
            

        
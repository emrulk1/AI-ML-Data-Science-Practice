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

def binary_search_lower_bound(arr, key):
    start = 0
    end = len(arr)-1
    
    while start < end:
        mid = (start+end)//2
        if arr[mid] == key:
            end = mid
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    
    return end if arr[end] == key else -1


def binary_search_upper_bound(arr, key):
    start = 0
    end = len(arr)-1
    
    while start < end:
        mid = (start+end)//2
        if arr[mid] == key:
            start = mid + 1
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    
    #extra logic for end-1 element as there is a chance we can skip x as start = mid+1
    out = end if arr[end] == key else -1
    if out != -1:
        return out
    if end > 0:
        return end-1 if arr[end-1] == key else -1
    return -1    
        
if __name__ == '__main__':
    lower_pos = binary_search_lower_bound(arr, key)
    upper_pos = binary_search_upper_bound(arr, key)
    
    if(lower_pos != -1):
        print("{} found form index {} to {} in arr".format(key, lower_pos, upper_pos))
    else:
        print("{} not found in arr".format(key))
    
    key = 4
    lower_pos = binary_search_lower_bound(arr, key)
    upper_pos = binary_search_upper_bound(arr, key)
    
    if(lower_pos != -1):
        print("{} found form index {} to {} in arr".format(key, lower_pos, upper_pos))
    else:
        print("{} not found in arr".format(key))
    
    #https://gist.github.com/RahilRehan/8bb8a541ff4a072e050046feb08404d6

    
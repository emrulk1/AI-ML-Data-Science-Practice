# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def is_valid_mobile_number(number_str):
    result = re.search(r'^[7-9]\d{9}$', number_str)
    return result
    
if __name__ == "__main__":
    n = int(input().strip())
    for i in range(n):
        number_str = input()
        status = is_valid_mobile_number(number_str)
        if status:
            print("YES")
        else:
            print("NO")

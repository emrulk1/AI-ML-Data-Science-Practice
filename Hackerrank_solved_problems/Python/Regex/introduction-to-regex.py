# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def is_valid_float(number_str):
    result = re.search('^[+-]?[0-9]*\.[0-9]+$', number_str)
    return bool(result)
    
if __name__ == "__main__":
    n = int(input().strip())
    for i in range(n):
        number_str = input()
        status = is_valid_float(number_str)
        print(status)

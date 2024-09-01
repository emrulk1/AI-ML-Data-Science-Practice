# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def is_valid(regex_str) :
    try :
        re.compile(regex_str)
        return True
    except re.error:
        # print("Non valid regex pattern")
        return False
    
T = int(input().strip())

for t in range(T) :
    regex_str = input()
    res = is_valid(regex_str)
    print(res)

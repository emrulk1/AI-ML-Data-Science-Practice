# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input().strip())

for t in range(T) :
    try :
        num1 , num2 = map(int, input().split())
        
        try :
            res = num1 // num2
            print(res) 
    
        except ZeroDivisionError as e :
            print("Error Code:", e)
            
    except ValueError as e :
        print("Error Code:", e)
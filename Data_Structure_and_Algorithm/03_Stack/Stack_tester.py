from Stack import Stack

if __name__ == '__main__':
    s=Stack()

    print("s.isEmpty() is {} because there are no element in Stack!\n\n".format(s.isEmpty())) if s.isEmpty() == True else print("Stack is not empty.\n\n") 
    
    val = 4
    s.push(val)
    print("Pushed {} to Stack\n".format(val))
    
    val = 'dog'
    s.push(val)
    print("Pushed {} to Stack\n".format(val))
    print("Current top element of stack is : {}\n".format(s.peek()) )
    
    val = True
    s.push(val)
    print("Pushed {} to Stack\n".format(val))
    
    print("Number of elements in the stack : {}\n".format(s.size()) )
    
    
    print("s.isEmpty() is {} because there are no element !\n\n".format(s.isEmpty())) if s.isEmpty() == True else print("Stack is not empty.\n\n") 
    
    val = 8.4
    print("Pushed {} to Stack\n".format(val))
    
    val = s.pop()
    print("Removed {} from Stack\n".format(val))
    
    val = s.pop()
    print("Removed {} from Stack\n".format(val))
    
    print("Number of elements in the stack : {}\n".format(s.size()) )
    
    print("Current top element of stack is : {}\n".format(s.peek()) )
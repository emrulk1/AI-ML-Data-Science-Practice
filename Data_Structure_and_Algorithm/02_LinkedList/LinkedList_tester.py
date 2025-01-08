from LinkedList import Node,UnorderedList

def print_search_result(num, mylist):
    found = mylist.search(num)
    if found :
        print("{} found in my list".format(num))
    else:
        print("{} not found in my list".format(num))

if __name__ == '__main__':
            
    mylist = UnorderedList()

    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)

    print("Number of elements in my list:" ,mylist.size())
    
    print_search_result(93,mylist)
    
    mylist.add(100)
    print_search_result(100, mylist)
    print("\n\n")

    print("Number of elements in my list after adding {}:".format(100) ,mylist.size())
    print("mylist after adding {} : ".format(100))
    mylist.print_list()

    print("\n\n")

    mylist.remove(54)
    print("Number of elements in my list after removing {}:".format(54) ,mylist.size())
    print("mylist after removing {} : ".format(54))
    mylist.print_list()

    print("\n\n")

    mylist.remove(93)
    print("Number of elements in my list after removing {}:".format(93) ,mylist.size())
    mylist.print_list()

    print("\n\n")
    
    mylist_reversed = mylist
    print("mylist Original : ")
    mylist_reversed.print_list()
    
    mylist_reversed.reverse()
    print("mylist reversed : ")
    mylist_reversed.print_list()
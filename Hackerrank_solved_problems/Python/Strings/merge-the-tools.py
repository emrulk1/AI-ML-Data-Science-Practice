
#problem link : https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

def remove_consecutive(substr) :
    i = 0 
    sublen = len(substr)
    res = ""
    freq = dict()
    # res = str(substr[0])
    for i in range(0,sublen) :
        # while(i+1 < sublen and substr[i+1] == substr[i]) :
        #     i+=1
        # print(i,substr[i])
        # res+=substr[i]
        
        if substr[i] not in freq :
            res += substr[i] 
            freq[substr[i]] = 1
        
    return res        

def merge_the_tools(string, k) :
    n = len(string)
    
    # print(type(s))
    # print(type(k))
    
    substring_len = n//k
    
    for i in range(0,k) :
        startpos = i*substring_len
        endpos = startpos + substring_len 
        substr = string[startpos : endpos] 
        print(remove_consecutive(substr))



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
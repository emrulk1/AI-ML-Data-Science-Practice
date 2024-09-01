def minion_game(s):
    vowels = 'AEIOU'
    str_len = len(s)
    kevin_score, stuart_score = 0, 0

    for i , char in enumerate(s):
        if char in vowels:
            kevin_score += (str_len - i)
        else:
            stuart_score += (str_len - i)

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
        
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    
    else:
        print("Draw")


    
if __name__ == '__main__':
    s = input()
    minion_game(s)
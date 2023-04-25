def exist(board,word):
    i=0
    j=0
    count1=0
    count2=0
    for items in board:
        count1+=len(items)
    word1=""
    left=0
    right=1
    down=0
    up=0
    while count1!=count2:
        if word1==word:
            return True
        word1+=board[i][j]
        count2+=1
        if word1 not in word:
            word1=word1.replace(word1[-1],"",1)
            if right==1 and left==0 and down==0:
                right=0
                down=1
                j-=1
            if left==1 and right==0 and down==0:
                j-=1
                i-=1
                down=0
                right=0        
        if down==1:
            i+=1
            if i==3:
                i-=1
                left=1
            else:
                right=0
                left=0
        if left==1:
            j-=1
            right=0
            down=0
        if right==1:
            j+=1
            down=0
            left=0    
    return false         
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))    
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE"))

def longestcommonprefix(strs):
    l=len(strs)
    longestprefix=""
    previousletter=""
    words=0
    letters=0
    l=[]
    w=strs[0]
    strs=strs[1:]
    for index,letters in enumerate(w):
        for words in strs:
            flag=0
            if w.find(letters,index)==words.find(letters,index):
                previousletter=letters
                flag=1
            else:
                flag=0
        if flag==1:
            longestprefix+=previousletter
    return longestprefix   
            
            
print(longestcommonprefix(["flower","flow","flight"]))                
#print(longestcommonprefix(["aaa","aa","aaa"]))                
print(longestcommonprefix(["dog","racecar","car"]))

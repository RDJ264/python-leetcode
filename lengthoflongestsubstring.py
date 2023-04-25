def lengthofLongestSubstring(s):
    word=""
    flag=1
    listofsubstring={}
    for i in s:
        if i not in word:
            flag=1
            word+=i
        else:
            listofsubstring[word]=len(word)
            flag=0
            word=""
    if flag==1:
        listofsubstring[word]=len(word)
    return listofsubstring
def lengthofLongestSubstring2(s):
    word=""
    flag=1
    listofsubstring={}
    i=0
    while i<len(s):
        if s[i] not in word:
            word+=s[i]
            flag=1
        else:
            listofsubstring[word]=len(word)
            flag=0
            word=""
        if flag==1:
            i+=1
    if flag==1:
        listofsubstring[word]=len(word)
    return listofsubstring
def lengthofLongestSubstring4(s):
    word=""
    flag=1
    listofsubstring={}
    i=0
    word2=""
    while i<len(s):
        j=i+1
        while j<len(s):
            if s[j] not in word:
                word+=s[j]
                flag=1
            else:
                flag=0
                if s[i] not in word:
                    listofsubstring[s[i]+word]=len(s[i]+word)
                word=""
                break
            j+=1
        if flag==1:
            listofsubstring[word]=len(word)
        i+=1
    return listofsubstring    
    #return len(max(listofsubstring,key=listofsubstring.get))   
                
def lengthofLongestSubstring3(s):
    listofsubstring={}
    i=0
    flag=0
    while i<len(s):
        j=i+1
        while j<=len(s):
            for items in s[i:j]:
                if s[i:j].count(items)>=2:
                    flag=0
                    break
                else:
                    flag=1
            if flag==1:
                listofsubstring[s[i:j]]=len(s[i:j])
            j+=1
        i+=1
    return len(max(listofsubstring,key=listofsubstring.get))
def lengthofLongestSubstring4(s):
    i=0
    d={}
    while i<len(s):
        j=i+1 if i+1<len(s) else i
        while s[j]!=s[i]:
            j+=1
        d[s[i:j]]=len(s[i:j])
        print(d)
        i=j+1
    print(d)    
    #return len(max(listofsubstring,key=listofsubstring.get))
print(lengthofLongestSubstring4("abcabcbb"))
print(lengthofLongestSubstring4("bbbbb"))
print(lengthofLongestSubstring4("pwwkew"))

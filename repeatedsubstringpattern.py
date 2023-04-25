def repeatedSubstringPattern(s):
    word=""
    for nums,items in enumerate(s):
        word+=items
        if len(word)>=2:
            if word in s[nums+1:]:
                return "true"
    return "false"
def repeatedSubstringPattern2(s):
    word=""
    index=0
    for items in s:
        word+=items
        if len(word)>=2:
            if word in s[s.index(items)+1:]:
                return "true"
        index+=1
    return "false"
def repeatedSubstringPattern4(s):
    word=""
    index=0
    while index<len(s):
        word+=s[index]
        if len(word)>=2:
            if word in s[index+1:]:
                return "true"
        index+=1    
    return "false"        
        
print(repeatedSubstringPattern4("abab"))    
print(repeatedSubstringPattern4("aba"))         
print(repeatedSubstringPattern4("abcabcabcabc"))

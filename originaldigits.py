def originaldigits(s):
    l=["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"]
    d={"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    numtoletters=""
    orgnum=""
    counter=1
    for elements in d.keys():
        numtoletters=""
        index=0
        while index<len(elements):
            if elements[index] in s:
                numtoletters+=elements[index]
                s=s.replace(elements[index],"",1)
                #print(numtoletters)   
            index+=1
        if numtoletters in list(d):
            orgnum=orgnum+str(d[numtoletters])
    print(orgnum)         


def originaldigits2(s):
    i=0
    d={"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    li=[]
    tempindex=0
    index=0
    flag=True
    numtoletters=""
    while i<len(list(d)):
        li.append(list(d)[i][0:2])
        i+=1                
    print(li)                    
    while len(s)!=0:
        for elements in li:
            while index<len(d):
                for contents in elements:
                    if contents in list(d)[index]:
                        numtoletters=numtoletters+contents
                index+=1    
def originaldigits3(s):
    i=0
    d={"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    d1={}
    while i<len(d):
        letters=list(d.keys())[i]
        flag=0
        for j in letters:
            if j not in s:
                flag=1
                break
        if flag==0:
            d1[letters]=d[letters]
        i+=1
    l=""    
    for i in d1:
        l+=str(d1[i])
    return l
def originaldigits4(s):
    d={"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    i=0
    l=""
    while len(s)!=0:
        flag=0
        word=list(d.keys())[i]#individual words
        for letters in word:
            if letters not in s:
                flag=1
                break
        if flag==0:
            l+=str(d[word])
            for letter in word:
                s=s.replace(letter,"",1)
        else:
            i+=1
    return l        
            
        
                
        
print(originaldigits4("owoztneoer"))
print(originaldigits4("zerozero"))        
print(originaldigits4("fviefuro"))
"""print(originaldigits4("owoztneoer"))
print(originaldigits4("zerozero"))"""

"""def romantoint(s):
    i=0
    j=0
    num=0
    d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    while i<=len(s):
        if (i+1)<=len(s):
            if s[i-1]=="I" and s[i]=="V":
                num+=4
            elif s[i-1]=="I" and s[i]=="X":
                num+=9
            elif s[i-1]=="X" and s[i]=="L":
                num+=40
            elif s[i-1]=="X" and s[i]=="C":
                num+=90
            elif s[i-1]=="C" and s[i]=="D":
                num+=400
            elif s[i-1]=="C" and s[i]=="M":
                num+=900
            else:
                num+=d[s[i]]
            print(num)    
        i+=1        
    return num
def romantoint2(s):
    d={"I":1,"IV":4,"V":5,"IX":9,"X":10,"XL":40,"L":50,"XC":90,"C":100,"CD":400,"D":500,"CM":900,"M":1000}
    i=0
    j=1
    nums=0
    for elements in s:
        #print(s[i:j])
        if s[i:j] in d.keys():
            nums+=d[s[i:j]]
        else:
            for num in s[i:j]:
                nums+=d[num]
        i=j
        j=i+2
    return nums"""    
def romantoint3(s):
    d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    d1={"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
    i=0
    j=2
    s1=0
    for elements in s:        
        if s[i:i+2] in d1.keys():    
            s1+=d1[s[i:i+2]]  s1=1
            if i==len(s)-2:
                break
            i=i+2
        else:
            if i==len(s):
                break
            if s[i] in d.keys():
                s1+=d[s[i]]
                i+=1
        #print(s1)    
    return s1    
print(romantoint3("III"))
print(romantoint3("LVIII"))
print(romantoint3("MCMXCIV"))
print(romantoint3("MMCDXXV"))

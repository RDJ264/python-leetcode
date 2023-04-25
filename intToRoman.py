def romantoint(num):
    d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    i=0
    s=0
    if len(num)==0:
        return 0
    while i<len(num):
        if i+1<=len(num)-1:
            if d[num[i]]<d[num[i+1]]:
                s=s-d[num[i]]
            else:
                s=s+d[num[i]]
        i+=1
    s=s+d[num[i-1]]    
    return s    
            


def inttoroman(num):
    d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    repetition={"X":3,"I":3}
    diff={}
    s=""
    attached={"I":["V","X"],"X":["L","C"]}
    if len(str(num))==1 or num%10==0:
        for i in d:
            if num==d[i]-1 or num==d[i]-10 or num==d[i]-100:
                for j in d:
                    if d[i]-d[j]==num:
                        s=s+j+i
        return s
def inttoromansub(num):
    d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    repetition={"X":3,"I":3}
    diff={}
    count=0
    s=""
    attached={"I":["V","X"],"X":["L","C"]}
    while romantoint(s)!=num:
        for i in d:
            if d[i]<=num:
                diff[i]=abs(d[i]-num)
        l=[i for i in diff if diff[i]==min(diff.values())]
        s=s+l[-1]
        if l[-1]!="I" and l[-1]!="X":
            del d[l[-1]]
            del diff[l[-1]]
        else:
            count+=1
            if count==3:
                del d[l[-1]]
                del diff[l[-1]]        
    return s
def inttoromansub1(num):
    d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    repetition={"X":3,"I":3}
    diff={}
    count=0
    s=""
    num2=str(num)
    flag=0
    num3=num
    for i in d:
        if num==d[i]-1 or num==d[i]-10 or num==d[i]-100:
            flag=1
            break
    if flag==1:
        for i in d:
            for j in d:
                if d[i]-d[j]==num:
                    s=s+j+i
    else:
        while romantoint(s)!=num3:
            for i in d:
                if d[i]<=num:
                    diff[i]=abs(d[i]-num)
            print("diff=",diff)        
            l=[i for i in diff if diff[i]==min(diff.values())]
            s=s+l[-1]
            if romantoint(s)>int(num2):
                break
            if l[-1]!="I" and l[-1]!="X" and l[-1]!="C":
                del d[l[-1]]
                del diff[l[-1]]
            else:
                count+=1
                print("s=",s)
                if count==int(num2[-len(str(num))]):
                    del d[l[-1]]
                    del diff[l[-1]]
            num=num-romantoint(l[-1])
            print(num)
    return s
def inttoromansub2(num):
    s=""
    d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    diff={}
    num2=str(num)
    count=0
    while int(num2)!=0:
        counter=0
        k=1
        while counter<len(num2)-1:
            k=k*10
            counter+=1
        flag=0
        for i in d:
            if d[i]-k==k*int(num2[-len(num2)]):
                flag=1
                break
        if flag==1:
            for i in d:
                for j in d:
                    if d[i]-d[j]==k*int(num2[-len(num2)]):
                        s=s+j+i
        else:
            for i in d:
                if d[i]<=k*int(num2[-len(num2)]):
                    diff[i]=abs(d[i]-int(num2))
            l=[i for  i in diff if diff[i]==min(diff.values())]
            s=s+l[-1]
        num2=str(int(num-romantoint(s)))
    return s     
"""print(inttoroman(4))
print(inttoroman(5))
print(inttoroman(9))
print(inttoroman(40))
print(inttoroman(90))
print(inttoroman(50))
print(inttoroman(100))"""
#print(inttoroman(90))
#print(inttoromansub(6))
#print(inttoromansub1(4))
#print(inttoromansub1(9))
#print(inttoromansub1(11))
#print(inttoromansub1(116))
print(inttoromansub2(1994))

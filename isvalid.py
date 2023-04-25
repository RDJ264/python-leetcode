def isValid(s):
    stack=[]
    d={"(":")","[":"]","{":"}"}
    for i in s:
        if i in ['(','{','[']:
            stack.append(i)
        else:
            if i in [')',']','}']:
                if i==")":
                    if stack[-1]=="(":
                        stack.pop(-1)
                elif i=="}":
                    if stack[-1]=="{":
                        stack.pop(-1)
                elif i=="]":
                    if stack[-1]=="[":
                        stack.pop(-1)
    if len(stack)==0:
        return len(stack)
    else:
        return False

def isValid2(s):
    try:
        stack=[]
        flag=0
        for i in ['(','{','[']:
            if i not in list(s):
                flag=1
            else:
                flag=0
                break
        if flag==1:
            return False
        for i in s:
            if i in ['(','{','[']:
                stack.append(i)
            else:
                if i in [')',']','}']:
                    stack.append(i)
                    if stack[-1]==")":
                        if stack[-2]=="(" and len(stack)!=0:
                            for i in range(2):
                                stack.pop(-1)
                    elif stack[-1]=="]":
                        if stack[-2]=="[":
                            for i in range(2):
                                stack.pop(-1)
                    elif stack[-1]=="}":
                        if stack[-2]=="{":
                            for i in range(2):
                                stack.pop(-1)
        if len(stack)==0:
            return True
        else:
            return stack
    except IndexError:
        return False
                    
    
                

print(isValid2("]"))
print(isValid2(")(){}"))

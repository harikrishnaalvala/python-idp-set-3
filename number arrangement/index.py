s=input()
num=""
for i in s:
    if i.isdigit():
        num+=i 
    else:
        num+=" "
num=num.split()
num=list(map(int,num))
number=sorted(num,reverse=True)
if len(num)==0 or len(num)==1:
    print(s)
else:
    res=""
    i=0
    j=0
    k=len(s)
    while j<k:
        if s[j].isdigit():
            if s[j].isdigit() and (j==0 or (not s[j-1].isdigit())):
                res+=str(number[i])
                m=len(str(number[i]))
                i+=1 
                j+=1 
            else:
                j+=1 
        else:
            res+=s[j]
            j+=1 
    print(res)
            

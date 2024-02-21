def read_sentence(n):
    s=[]
    for i in range(n):
        a=input().split()
        s.append(a)
    return s 
def find_word(s,word):
    for i in range(len(s)):
        if word in s[i]:
            p=i+1 
            return p 
    return -1 
word=input()
n=int(input())
s=read_sentence(n)
p=find_word(s,word)
print(p)
            

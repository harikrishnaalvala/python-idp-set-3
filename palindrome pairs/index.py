def get_palindrome(sentence):
    p=[]
    for i in range(len(sentence)):
        for j in range(len(sentence)):
            if i!=j:
                pair=sentence[i]+sentence[j]
                if pair==pair[::-1]:
                    palindrome_pair=str(i)+" "+str(j)
                    p.append(palindrome_pair)
    return p
def get_palindrome_pair(p):
    if len(p)>0:
        for i in p:
            print(i)
    else:
        print(-1)
def main():
    sentence=input().split()
    p=get_palindrome(sentence)
    get_palindrome_pair(p)
main()

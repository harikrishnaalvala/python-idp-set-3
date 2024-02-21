def get_length(s):
    maximum=0
    for i in s:
        if (len(i)>maximum):
            maximum=len(i)
    return maximum
def find_word(s,maximum):
    for i in range(1,maximum+1):
        word=""
        for j in s:
            if(i<=len(j)):
                word+=j[i-1]
            else:
                word+=" "
        print(word)  
def main():
    s=input().split()
    maximum=get_length(s)
    find_word(s,maximum)
main()

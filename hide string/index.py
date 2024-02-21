def hide_string(sentence):
    new_string=[]
    for i in sentence:
        new_word=""
        for j in i:
            if (j=="a"):
                new_word+="z"
            elif (j=="A"):
                new_word+="Z"
            else:
                l=ord(j)
                p=l-1
                new_word+=chr(p)
        new_string.append(new_word)
    return new_string

sentence=input().split()
result=hide_string(sentence)
print(*result)
                

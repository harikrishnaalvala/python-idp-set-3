def read_input(number):
    sentence_list=[]
    for i in range(number):
        sentence=input().split()
        sentence_list.append(sentence)
    return sentence_list
def max_lengths(sentence_list):
    max_length=0
    for i in sentence_list:
        if(len(i)>max_length):
            max_length=len(i)
    return max_length
def concated_lists(sentence_list,max_length):
    concated_list=[]
    for i in range(max_length):
        word=""
        for j in sentence_list:
            if len(j)>i:
                word+=j[i]
        concated_list.append(word)
    return concated_list
def print_word(words):
    for i in words:
        print(i)
def main():
    number=int(input())
    sentence_list=read_input(number)
    max_length=max_lengths(sentence_list)
    concated_list=concated_lists(sentence_list,max_length)
    print_word(concated_list)
main()

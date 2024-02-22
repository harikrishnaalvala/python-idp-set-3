def print_result(non_adj_list):
    if (len(non_adj_list)==0):
        print("No Combinations")
    for non_adj_words in non_adj_list:
        print(non_adj_words)
def check_words(words_list,word1,word2):
    are_words=False
    for i in range(len(words_list)-1):
        if(words_list[i]==word1 and words_list[i+1]==word2):
            are_words=True
        elif(words_list[i+1]==word1 and words_list[i]==word2):
            are_words=True
    return are_words
    
def non_adjacent_words(words_list):
    non_adj_list=[]
    for i in range(len(words_list)-1):
        for j in range(i,len(words_list)):
            are_words=check_words(words_list,words_list[i],words_list[j])
            if (i+1<j and not are_words):
                non_adj_words=[words_list[i],words_list[j]]
                non_adj_words.sort()
                non_adj_words=" ".join(non_adj_words)
                if (non_adj_words not in non_adj_list):
                    non_adj_list.append(non_adj_words)
    non_adj_list.sort()
    return non_adj_list

def main():
    words_list=input().split()
    non_adj_list=non_adjacent_words(words_list)
    print_result(non_adj_list)
main()
    
  

number_dict={
    "0":"zero",
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
}
consecutive_nums={2:"double", 3:"triple", 4: "quadruple"}
def get_number_seperation(number):
    nums_list=[]
    nums_list.append(number[:4])
    nums_list.append(number[4:7])
    nums_list.append(number[7:])
    return nums_list
def convert_nums_readaable(number):
    human_reads=""
    i=0
    while i<len(number):
        repeats=1 
        j=i+1 
        while (j<len(number) and number[i]==number[j]):
            repeats+=1 
            j+=1 
        if repeats==1:
            human_reads+=number_dict[number[i]]+" "
        else:
            human_reads+=consecutive_nums[repeats]+" "+number_dict[number[i]]+" "
        i+=repeats
    return human_reads
    
def get_human_nums(nums_list):
    readable_nums=""
    for num in nums_list:
        readable_nums+=convert_nums_readaable(num)
    return readable_nums

def main():
    number=input()
    nums_list=get_number_seperation(number)
    result=get_human_nums(nums_list)
    print(result)
main()
    
    

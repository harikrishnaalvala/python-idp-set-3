def find_first_sum(number):
    num=0
    for i in str(number):
        num+=int(i)
    return num
def find_second_sum(number):
   while True:
       if len(str(number))==1:
           break
       number=find_first_sum(number)
   return number
number=int(input())
find_first_sum=find_second_sum(number)
print(find_first_sum)
    

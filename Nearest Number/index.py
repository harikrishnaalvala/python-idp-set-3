def check_even(number):
    number=str(number)
    if number[0]=="-":
        number=number[1:]
    for each_digit in number:
        if int(each_digit)%2 !=0:
            return False
    return True
def get_lower_even(number):
    while True:
        is_even=check_even(number)
        if (is_even):
            return number
        number-=1 
def get_higher_even(number):
    while True:
        is_even_digit=check_even(number)
        if (is_even_digit):
            return number
        number+=1 
        
def get_close_even_numbers(number):
    lower=get_lower_even(number)
    higher=get_higher_even(number)
    difference=number-lower
    higher_difference=higher-number
    
    if (difference<=higher_difference):
        return lower
    else:
        return higher
def main():
    number=int(input())
    result=get_close_even_numbers(number)
    print(result)
main()
        
      

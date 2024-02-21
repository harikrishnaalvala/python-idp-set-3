def get_rotated_number(number):
    rotated_number=number 
    for i in range(len(number)):
        digit=int(number[i])
        if (digit%2==1):
            rotated_number=number[i:]+number[:i]
            break 
    return rotated_number
def get_rotate_number_list(numbers):
    R=[]
    for i in numbers:
        rotated_number=get_rotated_number(i)
        R.append(rotated_number)
    return R 
def main():
    numbers=input().split()
    result=get_rotate_number_list(numbers)
    print(*result)
main()

R=[(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]
def get_quotient_reminder(number,deviser):
    quotient=number//deviser
    reminder=number%deviser
    return quotient,reminder
def find_numerals(number):
    numeral=""
    for i in R:
        quotient,reminder=get_quotient_reminder(number,i[0])
        numeral+=i[1]*quotient
        number-=(i[0]*quotient)
        if number<=0:
            break 
    return numeral
def main():
    number=int(input())
    result=find_numerals(number)
    print(result)
main()
        

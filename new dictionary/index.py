Alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def get_the_word(number):
    word=""
    while number>0:
        remainder=number%26
        if remainder==0:
            alphabet=Alphabets[25]
            number=number-26
        else:
            alphabet=Alphabets[remainder-1]
            number=number-remainder 
        word=alphabet+word
        number=number//26
    return word 
def main():
    number=int(input())
    word=get_the_word(number)
    print(word)
main()
            
            

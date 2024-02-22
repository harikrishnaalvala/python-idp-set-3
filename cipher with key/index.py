lowercase_letters="abcdefghijklmnopqrstuvwxyz"
def get_alphabet_mapping(alphabets):
    a={}
    for i in range(len(lowercase_letters)):
        a[lowercase_letters[i]]=alphabets[i]
    return a 
def remove_letters(word):
    new=""
    letters_set=set()
    for letter in word:
        if letter not in letters_set:
            new+=letter
            letters_set.add(letter)
    return new 
def remove_letters_from_word(word,letters_to_remove):
    new=""
    letters_set=set()
    for letter in word:
        if letter not in letters_to_remove:
            new+=letter
    return new 
def get_cipher_alphabet(key):
    key=remove_letters(key)
    remaining=remove_letters_from_word(lowercase_letters,key)
    return key+remaining
def get_ouput(word,alphabet):
    message=''
    for i in word:
        message+=alphabet[i]
    return message
def main():
    key,message=input().split()
    key,message=key.lower(),message.lower()
    alpha=get_cipher_alphabet(key)
    a=get_alphabet_mapping(alpha)
    result=get_ouput(message,a)
    print(result)
main()
    

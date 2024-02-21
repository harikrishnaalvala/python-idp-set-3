def number_of_books(book_price_list,pocket_money):
    no_of_books_buy=0
    book_price_list.sort()
    for i in book_price_list:
        if i<=pocket_money:
            no_of_books_buy+=1 
            pocket_money-=i
    return no_of_books_buy
def main():
    m=int(input())
    for i in range(m):
        no_of_books,pocket_money=map(int,input().split())
        book_price_list=list(map(int,input().split()))
        result=number_of_books(book_price_list,pocket_money)
        print(result)
main()
        

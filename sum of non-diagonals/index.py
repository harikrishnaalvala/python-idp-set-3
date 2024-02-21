def read_matrix(m):
    matrix=[]
    for i in range(m):
        row=list(map(int,input().split()))
        matrix.append(row)
    return matrix
def sum_of_non_diagonals(matrix,m):
    sum_of_elements=0
    for i in range(m):
        for j in range(m):
            if ((i!=j) and (i+j)!=(m-1)):
                sum_of_elements+=matrix[i][j]
    return sum_of_elements
def main():
    m=int(input())
    matrix=read_matrix(m)
    result=sum_of_non_diagonals(matrix,m)
    print(result)
main()
    

import numpy as np

def swap(A,i,j):
    temp=A[j]
    A[j]=A[i]
    A[i]=temp

def search_small(A,j,size):
    for i in range(j,size):
        if A[i] > A[j]:
            j=i
    value=j
    return value
    

def select(A,n):
    for i in range(n-1):
        j=search_small(A,i,n)
        swap(A,i,j)
          

def main():  
    A=np.array([1,10,15,5,6,4,98])
    size=len(A)
    print(A)
    select(A,size)
    print(A)

main()
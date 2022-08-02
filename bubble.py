import numpy as np

#function for interchange 2 positions
def swap(A,i,j):
    temp=A[j]
    A[j]=A[i]
    A[i]=temp

#Detection for disorder
def bubble(A,size):
    for i in range(size,0,-1):
        if A[i]>A[i-1]:
            swap(A,i,i-1)
            

def comp(A,size):
    for i in range(size):
        bubble(A,i)

def main():
    A=np.array([31,15,105,46,1,64,84])
    size=len(A) 
    print(A)
    comp(A,size) 
    
    print(A)




main()
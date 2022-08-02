import numpy as np  
import random

tam=6
#main
def app():
    #Write an array and check it
    #A=np.array([6,5,4,8,9,10])
    A=np.array([])
    #gen(tam,A)
    for i in range(tam):
        val=random.randint(0,100)
        A=np.append(A,[val])
    asc(A)
    print(A)


    

#Ordenar la matriz
def asc(mati):
    for i in range(len(mati)):
        for j in range(i+1,len(mati)):
            #"<" para orden descendente
            #">" para orden ascendente
            if mati[i] < mati[j]:
                tempe=mati[j]
                mati[j]=mati[i]
                mati[i]=tempe                
                print(i,j)



app()
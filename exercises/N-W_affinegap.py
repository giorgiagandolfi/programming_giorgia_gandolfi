#import from math module infinite value
from math import inf

#create the dictionary to calculate the scores
f=open("./matrix.txt","r")
matrix=[]
score_matrix={}
for line in f:
    line=line.rstrip()
    line=line.split()
    matrix.append(line)
for i in range(len(matrix[0])):
    for j in range(1,len(matrix)):
        score_matrix[matrix[0][i]+matrix[j][0]]=int(matrix[i+1][j])
mat=score_matrix
seq1="ACACT"
seq2="AAT"

#define a function that takes five arguments: the two strings, the matrix, the gap opening and gap extension penalities
def score_aff(s1,s2,S,h,g):
    #create the three empty (and then zero matrices) matrices of n*m dimension
    M=[]
    Ix=[]
    Iy=[]
    #trace back matrix
    t=[]
    m=len(s1)+1
    n=len(s2)+1
    M=[[0]*m for x in range(n)]
    Ix=[[0]*m for x in range(n)]
    Iy=[[0]*m for x in range(n)]
    t=[[0]*m for x in range(n)]
    #initialization of three matrices M[0][0]=0 
    Ix[0][0]=h
    Iy[0][0]=h
    #first row of M,Ix and t 
    for i in range(len(M[0][:-1])):
        M[0][i+1]=-inf
        Ix[0][i+1]=-inf
        t[0][i+1]="L"
    #first column of M,Iy and t    
    for i in range(len(M[:-1])):
        M[i+1][0]=-inf
        Iy[i+1][0]=-inf
        t[i+1][0]="U"
    #first row of Iy    
    for j in range(len(Iy[0][:-1])):
        Iy[0][j+1]=h+((j+1)*g)
    #first column of Ix
    for i in range(len(Ix[:-1])):
        Ix[i+1][0]=h+((i+1)*g)
    #iteration
    for i in range(1,n):
        for j in range(1,m):
            #match
            m1=M[i-1][j-1]+S[s1[j-1]+s2[i-1]]
            #opening of a gap in first sequence
            ix1=M[i-1][j]+h+g
            #opening of a gap in second sequence
            iy1=M[i][j-1]+h+g
            m2=Ix[i-1][j-1]+S[s1[j-1]+s2[i-1]]
            m3=Iy[i-1][j-1]+S[s1[j-1]+s2[i-1]]
            #gap extension in first sequence
            ix2=Ix[i-1][j]+g
            #gap extension in second sequence
            iy2=Iy[i][j-1]+g
            #take the maximum value in each of the three matrices
            M[i][j]=max(m1,m2,m3)
            Ix[i][j]=max(ix1,ix2)
            Iy[i][j]=max(iy1,iy2)
            #the bottom right value will be the highest among the three
            start=max(M[i][j],Ix[i][j],Iy[i][j])
            #trace back matrix
            if start==M[i][j]:
                t[i][j]="D"
            elif start==Ix[i][j]:
                t[i][j]="U"
            elif start==Iy[i][j]:
                t[i][j]="L"
    al1=""
    al2=""
    j=len(s1)
    i=len(s2)
    while j>0 or i>0:
       if t[i][j]=="D":
           al1+=s1[j-1]
           al2+=s2[i-1]
           j-=1
           i-=1
       elif t[i][j]=="U":
           al1+="-"
           al2+=s2[i-1]
           i-=1
       elif t[i][j]=="L":
           al1+=s1[j-1]
           al2+="-"
           j-=1
    al1=al1[::-1]
    al2=al2[::-1]
            
    return al1,al2,
fin=score_aff(seq1,seq2,mat,-3,-1)
print(fin[0])
print(fin[1])

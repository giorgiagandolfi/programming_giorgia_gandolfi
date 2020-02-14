import input_data

def matrix (s1,s2,S,d):
    m=len(s1)+1
    n=len(s2)+1
    F=[]
    P=[]
    F=[[0]*m for x in range(n)]
    P=[[0]*m for x in range(n)]
    for i in range(len(F[0][:-1])):
        F[0][i+1]=F[0][i]+d
        P[0][i+1]="L"
    for i in range(len(F[:-1])):
        F[i+1][0]=F[i][0]+d
        P[i+1][0]="U"
    for i in range(1,n):
        for j in range(1,m):
            diag=F[i-1][j-1]+S[s1[j-1]+s2[i-1]]
            left=F[i][j-1]+d
            up=F[i-1][j]+d
            F[i][j]=max(diag,left,up)
            if F[i][j]==diag:
                P[i][j]="D"
            elif F[i][j]==up:
                P[i][j]="U"
            elif F[i][j]==left:
                P[i][j]="L"
    return F,P
gap=-2
final_matrices=matrix(input_data.seq1,input_data.seq2,input_data.BLOSUM52,gap)

def global_al(s1,s2,F,P):
    al1=""
    al2=""
    j=len(s1)
    i=len(s2)
    while j>0 or i>0:
        if P[i][j]=="D":
            al1+=s1[j-1]
            al2+=s2[i-1]
            j-=1
            i-=1
        elif P[i][j]=="U":
            al1+="-"
            al2+=s2[i-1]
            i-=1
        elif P[i][j]=="L":
            al1+=s1[j-1]
            al2+="-"
            j-=1
    final_score=F[i+1][j+1]
    return al1[::-1],al2[::-1],final_score
final_result=global_al(input_data.seq1,input_data.seq2,final_matrices[0],final_matrices[1])
print("The best global alignment is:"+"\n"+final_result[0]+"\n"+final_result[1]+"\n"+"The score of the best global alignment is :"+str(final_result[2]))



f=open("./matrix_nucl.txt","r") #create the dictionary for the score
diz={}
matrix=[]
for line in f:
    line=line.rstrip()
    line=line.split()
    matrix.append(line)
for i in range(len(matrix[0])):
    for j in range(1,len(matrix)):
        diz[matrix[0][i]+matrix[j][0]]=int(matrix[i+1][j])
mat=diz
#remove the gaps for the first row and the first column in order to have only zeros
#find the highest value in the last column an the highest value in the last row and find the highest one of these two
#this value will be the starter point in the trace back process
seq1="ACTGG"
seq2="ACCA"
def score(s1,s2,S,d):
    F=[]
    trace_back=[]
    m=len(s1)+1
    n=len(s2)+1
    F=[[0]*m for x in range(n)]
    trace_back=[[0]*m for x in range(n)]
    for i in range(len(F[0][:-1])):
        trace_back[0][i+1]="L"
    for i in range(len(F[:-1])):
        trace_back[i+1][0]="U"
    for i in range(1,n):#iteration based on the maximization of the value
        for j in range(1,m):
            diag=F[i-1][j-1]+S[s1[j-1]+s2[i-1]]#match
            left=F[i][j-1]+d #gap in the second sequence
            up=F[i-1][j]+d#gap in the first sequence
            F[i][j]=max(diag,left,up)
#(2)crate trace back matrix
            if F[i][j]==diag:
                trace_back[i][j]="D"
            elif F[i][j]==left:
                trace_back[i][j]="L"
            elif F[i][j]==up:
                trace_back[i][j]="U"
    max_row=max(F[n-1])#find the highest value of the last row
    col=[]
    for i in range(n):#append all values of the last column in a new list 
        col.append(F[i][m-1])
    max_col=max(col)#find the highest value of the list that is the max value of the row
    best_score=max(max_row,max_col)
    if best_score in F[n-1]:
        i_max=n-1
        j_max=F[n-1].index(best_score)
    else:
        i_max=m-1
        j_max=col.index(best_score)
    al1=""
    al2=""
    c=""
    j=j_max
    i=i_max
    while F[i][j]>0:
        if trace_back[i][j]=="D":
            al1+=s1[j-1]
            al2+=s2[i-1]
            j-=1
            i-=1
        elif trace_back[i][j]=="U":
            al1+="-"
            al2+=s2[i-1]
            i-=1
        elif trace_back[i][j]=="L":
            al1+=s1[j-1]
            al2+="-"
            j-=1

            
    al1=al1[::-1]
    al2=al2[::-1]
    for i in range(len(al1)):
        if al1[i]=="-" or al2[i]=="-":
            c+=" "
        elif al1[i]==al2[i]:
            c+="|"
        elif al1[i]!=al2[i]:
            c+="*"
    return al1,c,al2

final_alignment=score(seq1,seq2,mat,-2)

print(final_alignment[0])
print(final_alignment[1])
print(final_alignment[2])

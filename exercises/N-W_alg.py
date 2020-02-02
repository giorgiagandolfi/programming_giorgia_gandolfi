
f=open("./matrix.txt","r") #create the dictionary for the score
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


seq1="ACACT"
seq2="AAT"
def score(s1,s2,S,d):
    F=[]
    trace_back=[]
    m=len(s1)+1
    n=len(s2)+1
    F=[[0]*m for x in range(n)]
    trace_back=[[0]*m for x in range(n)]
    for i in range(len(F[0][:-1])):#initialize first row of the zero matrix with gaps (dall'inizio fino al penultimo)
        F[0][i+1]=F[0][i]+d
        trace_back[0][i+1]="L"
    for i in range(len(F[:-1])):#initialize first column of the zero matrix with gaps (dall'inizio fino al penultimo)
        F[i+1][0]=F[i][0]+d
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
    al1=""
    al2=""
    c=""
    j=len(s1)#5
    i=len(s2)#4
    while j>0 and i>0:
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
    return al1,al2,F[len(s2)][len(s1)],c,F

final_alignment=score(seq1,seq2,mat,-2)
print("The best alignment is:")
print(final_alignment[0])
print(final_alignment[4])
print(final_alignment[1])
print("The score of the alignment is: ",final_alignment[2])

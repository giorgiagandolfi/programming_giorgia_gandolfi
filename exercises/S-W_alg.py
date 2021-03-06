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
seq1="ACTCT"
seq2="ATTAA"
def score(s1,s2,S,d,t):
    F=[]
    trace_back=[]
    m=len(s1)+1
    n=len(s2)+1
    #initialize the two matrices as zero matrices
    F=[[0]*m for x in range(n)]
    trace_back=[[0]*m for x in range(n)]
    #edit first row of trace back matrix 
    for i in range(len(F[0][:-1])):
        trace_back[0][i+1]="L"
    #edit first column of trace back matrix
    for i in range(len(F[:-1])):
        trace_back[i+1][0]="U"
    for i in range(1,n):#iteration based on the maximization of the value
        for j in range(1,m):
            diag=F[i-1][j-1]+S[s1[j-1]+s2[i-1]]#match
            left=F[i][j-1]+d #gap in the second sequence
            up=F[i-1][j]+d#gap in the first sequence
            #fill up the matrix according to the highest value between zero, diag, left and up
            #negative values are avoided
            F[i][j]=max(diag,left,up,0)
            #fill up trace back matrix
            if F[i][j]==diag:
                trace_back[i][j]="D"
            elif F[i][j]==left:
                trace_back[i][j]="L"
            elif F[i][j]==up:
                trace_back[i][j]="U"
    #the starting point for the trace back is the highest value in the matrix of scores
    #put all values of the F matrix into a list
    #assign to a variable the highest value
    #find the value into the row of F matrix (F[i]) in order to retrive i index (the position in the row)
    #find the value with its i index into F columns (F[i_max][j]) and retrive j index (the position in the column)
    values=[]
    for i in range(n):
        for j in range(m):
            values.append(F[i][j])
    start=max(values)
    for i in range(n):
        if start in F[i]:
            i_max=i
    for j in range(m):
        if start==F[i_max][j]:
            j_max=j
    al1=""
    al2=""
    j=j_max
    i=i_max
    #trace back until a value equal to zero is found
    while F[i][j]!=0:
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
    
    return al1,al2
final=score(seq1,seq2,mat,-2,2)
print(final[0])
print(final[1])


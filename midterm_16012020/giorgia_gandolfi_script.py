import input_data

def matrix(name):
    if name=="blosum62":
        f=open("./BLOSUM62_square.txt","r")
    else:
        f=open("./PAM250_square.txt","r")
    dict={}
    mat=[]
    for line in f:
        line=line.rstrip()
        line=line.split()
        mat.append(line)
    #print(mat)
    for i in range(len(mat[0])):
        for j in range(1,len(mat)):
            dict[mat[0][i]+mat[j][0]]=mat[i+1][j]
    return dict

mat=matrix(input())

def al(seq,d):
    seq1=seq[0]
    seq2=seq[1]
    score=0
    for i in range(len(seq1)):
        if seq1[i]=="-" or seq2[i]=="-":
            score+=d
        elif seq1[i]!="-" and seq2[i]!="-":
            score+=int(mat[seq1[i]+seq2[i]])
    return score
print("The score of the alignment is", al(input_data.align1,-2))
print("The score of the alignment is", al(input_data.align2,-2))
print("The score of the alignment is", al(input_data.align3,-2))




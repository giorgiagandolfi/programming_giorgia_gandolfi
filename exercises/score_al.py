seq1=input()
seq2=input()
def score(str1,str2):
    s=0
    for i in range(len(seq1)):
        if seq1[i]==seq2[i]:
            s+=1
    return s
print(score(seq1,seq2))

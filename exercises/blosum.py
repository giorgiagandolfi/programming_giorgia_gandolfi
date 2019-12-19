f=open("./blosum.txt","r")
blosum50={}
blosum=[]
for line in f:
    line=line.rstrip()
    line=line.split()
    blosum.append(line)
#print(blosum)
for i in range(len(blosum[0])):
    for j in range(1,len(blosum)):
        blosum50[blosum[0][i]+blosum[j][0]]=blosum[i+1][j]
#print(blosum50)
seq1="ALASVLIRLITRLYP"    
seq2="ASAVHLNRLITRLYP"
def score(s1,s2):
    s=0
    for i in range(len(seq1)):
        s+=int(blosum50[s1[i]+s2[i]])
    return s
print(score(seq1,seq2))
f.close()

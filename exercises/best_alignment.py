#create dictionary of the matrix
o=open("./matrix", "r")
l=o.readline()
l=l.rstrip()
base=l.split()
nucleotide_matrix={}
for i in range(len(base)):
    line=o.readline()
    line=line.rstrip()
    line=line.split()
    for j in range(len(base)):
        nucleotide_matrix[base[i]+base[j]]=int(line[j+1])

seq1="TCA"
seq2="GA"
#create sequence 1 with gaps
for i in range(len(seq2)):
    seq1="-"+seq1
    seq1=seq1+"-"
all_sequences=[]#will contain all possible sequence 2 according with the program
all_scores=[]#will contain all possible scores of the possible alignment
for i in range(len(seq1)-2):
    seq2=(i*"-")+seq2+((len(seq1)-(len(seq2))-i)*"-")#creation of sequence2 with gaps>the sequence GA will shift of one each times of the for loop
    score=0 
    for j in range(len(seq1)):
        score += nucleotide_matrix[seq1[j]+seq2[j]]#call the dictionary
    all_scores.append(score)
    all_sequences.append(seq2)
    seq2="GA"  
best_alignment=all_scores.index(max(all_scores))#the index of the maximun score value
print("BEST ALIGNMENT:")
print(seq1)
print(all_sequences[best_alignment])#the index in the list of the scores will correspond to the sequence2 that has the best score
print("The score of the best alignment is ",max(all_scores))

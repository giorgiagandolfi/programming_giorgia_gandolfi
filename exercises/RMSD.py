fh1=open("./model1.pdb","r")
fh2=open("./model2.pdb","r")

l=[]
for line in fh1:
    line=line.rstrip()
    l.append(line.split())#splitta ogni elemento per lo spazio indip dalla lugnhezza dello spazio: l'output sarà una lista con tuple ognuno contenente una riga del file pdb
car_a=[]
for i in l[1:-1]:
    if "CA" in i:
        car_a.append(i)#lista con tuple conteneti le righe del file relative unicamente al CA
dist=[]
for j in car_a:
    dist.append((float(j[6]),float(j[7]),float(j[8])))#fare una nuova lista che contiene le coordinate dell'atomo con CA in base all'indice nalla lista
print(dist)
l1=[]
for line2 in fh2:
    line2=line2.rstrip()
    l1.append(line2.split())
car_a2=[]
for x in l1[1:-1]:
    if "CA" in x:
        car_a2.append(x)
dist1=[]
for y in car_a2:
    dist1.append((float(y[5]),float(y[6]),float(y[7])))
print(dist1)
from math import *
def rmsd(lista1,lista2):
    Dz=[]#la lista che contiene ogni differenza **2 di ogni coppia di tuple (con le tre coord)che aumenta per ogni elemento della lista
    sum=0.0
    for z in range(len(lista1)):
        d=((lista1[z][0]-lista2[z][0])**2+(lista1[z][1]-lista2[z][1])**2+(lista1[z][2]-lista2[z][2])**2)
        Dz.append(d)
    RMSD=sqrt((1/len(lista1))*fsum(Dz))
    return RMSD
print(rmsd(dist,dist1))
    
fh1.close()
fh2.close()
#controllare altra risoluzione su github

def SearchMin(V):
    mn=100
    indmn=0
    for i in range (0,len(V)):
        if (i not in completed and V[i]<mn):
            indmn=i
            mn=V[i]
    A=''
    B = Maplegend[indmn]
    for j in range (0,len(Map)):
        if Map[indmn][j]==mn:
            A=Maplegend[j]
    print(A,B,mn)
    return indmn

Map=[[0, 1.97,21.6,10.7,22.3,10.4],
     [1.97,0,22.3,11.4,23,11.1],
     [21.6,22.3,0,11.5,5.2,12],
     [10.7,11.4,11.5,0,13.4,0.68],
     [22.3,23,5.2,13.4,0,13.8],
     [10.4,11.1,12,0.68,13.8,0]]


V=[0,500,500,500,500,500]
Maplegend=['v78','v86','s20','mp1','sg22','u7']
completed=[]
length=0

while (len(completed)<6):
    ind=SearchMin(V)
    for i in range (0,len(Map)):
        if (Map[ind][i]!=0 and Map[ind][i]<V[i] and i not in completed):
            V[i]=Map[ind][i]
    completed.append(ind)

for i in V:
    length+=i

print(length)


#Baiyifei
##
#
#
d=int(input())
n=int(input())
lis=[]
lis1=[]
for i in range(n):
   x,y,k=map(int,input().split())
   lis.append([x,y,k])
   
for i in range(129):
    for j in range(129):
        x1=i
        x2=j
        pub=0
        for item in lis:
            if x1-d<=item[0]<=x1+d and x2-d<=item[1]<=x2+d:
                pub+=item[2]
        lis1.append(pub)
z=max(lis1)
print(lis1.count(z),z)
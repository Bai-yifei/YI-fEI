        for item in lis:
            if x1-d<=item[0]<=x1+d and x2-d<=item[1]<=x2+d:
                pub+=item[2]
        lis1.append(pub)
z=max(lis1)
print(lis1.count(z),z)
#
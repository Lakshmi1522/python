n=int(input("enter the number"))
for i in range(1,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if(k**2==i**2+j**2):
                print((i,j,k))


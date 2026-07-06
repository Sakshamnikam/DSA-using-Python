n=6 #rows
m=6 #columns

for i in range(0,n):
    for j in range(0,m):
        if(i==0 or i==n-1 or j==0 or j==m-1):
            print('*',end='')
        else:
            print(' ',end='')
    print()
        
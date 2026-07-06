def display(n): #5
    if n==0:
        return
    else:
        display(n-1)
        print(n,end=' ')

n=5
display(n)
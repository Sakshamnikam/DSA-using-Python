def check(str):

    left=0
    n=len(str)
    right=n-1

    for i in range(0,len(str)):
        if str[right]!=str[left]:
            return -1
        left+=1
        right-=1

    
str='101'
res=check(str)
if res==-1:
    print('Not a palindrome ')
else:
    print(str,'Is a palindrome!')

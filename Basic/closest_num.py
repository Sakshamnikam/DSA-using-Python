n=13
m=4

rmd=n%m
val1=n-rmd
val2=val1+m

num1=abs(n-val1)
num2=abs(n-val2)

if(num1<num2):
    print(num1)
else:
    print(num2)
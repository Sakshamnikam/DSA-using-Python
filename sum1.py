import time

start = time.time()

# Your code
sum = 0
for i in range(1000000):
    sum += i

end = time.time()

print("Execution Time:", end - start, "seconds")

n=10
sum=0
for i in range(1,n+1):
    sum=sum+i
    if(sum==n):
        break
    else:
        continue

if(sum==n):
    print("true",sum)

else:
    print('False')
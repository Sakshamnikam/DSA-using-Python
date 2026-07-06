import time

start = time.time()

# Your code
sum = 0
for i in range(1000000):
    sum += i

end = time.time()

print("Execution Time:", end - start, "seconds")

n=int(input('Input:'))

for i in range(1,n):
    sum=0
    for j in range(i,n):
        sum=sum+j

        if(sum==n):
            print("true")
            exit()
        if(sum>n):
            break

print('False')


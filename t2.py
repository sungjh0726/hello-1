i, sum = 0, 0
while(i < 100) :
    i = i +1
    if (i % 2 == 1):
        sum += i

print("sum=", sum)

sum2 = 0
for i in range(101) :
    if (i % 2 == 1) :
        sum2 += i


print("sum2=", sum2)

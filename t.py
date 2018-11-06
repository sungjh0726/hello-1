i, sum = 0, 0
while (i >= 0):
    i += 1
    if (i < 2 or (i != 100 and i % 2 == 0)):
        continue

    isPrime = True
    for j in range(2, i):
        if (i % j == 0):
            isPrime = False
            break

    if (isPrime):
        sum += i;
        print(i, " is prime number!!")
    
    if (i == 100):
        print("End!!", sum)
        break
import timeit

def run_string_code(code):
    print( timeit.timeit(code, number=100) )

# run_string_code('"-".join(str(n) for n in range(10))  ')


def fn():
    sum = 0
    print("fn!!")
    for i in range(1000):
        for j in range(1000):
           sum += i + j 

    return sum


# print(timeit.Timer(fn).timeit(10) )
print("---------------------------")
# q = min(timeit.Timer(fn).repeat(10,1))  # 10번반복인데, 돌때(반복)마다 1번만 수행
q = min(timeit.Timer(fn).repeat(2,10))  # 2번반복인데, 돌때(반복)마다 10번씩 수행
print(q)

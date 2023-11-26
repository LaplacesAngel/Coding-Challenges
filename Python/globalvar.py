import time

start_time = time.perf_counter()

globalvar = 10

def func():
    ans = 0
    localvar = globalvar
    for x in range(100000):
        ans += localvar * x
    return ans

print(func())

end_time = time.perf_counter()

perf_time = end_time - start_time

print(f"The execution time is {perf_time} seconds")
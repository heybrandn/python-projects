def fib(x):
    if x < 1:
        return None
    if x < 3:
        return 1
    el1 = el2 = 1
    sum = 0
    for i in range(3, x+1):
        sum = el1+el2
        el1, el2 = el2, sum
    return sum
for x in range(1, 20):
    print(fib(x))
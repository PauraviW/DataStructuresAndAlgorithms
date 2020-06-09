# Uses python3
def calc_fib(n):
    # if (n <= 1):
    #     return n
    #
    # return calc_fib(n - 1) + calc_fib(n - 2)

    if n <= 1:
        return n
    f = []
    f.append(0)
    f.append(1)
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    # print(f)
    return f[-1]



n = int(input())
print(calc_fib(n))




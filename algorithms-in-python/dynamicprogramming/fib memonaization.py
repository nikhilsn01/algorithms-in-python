# memonization

memo = [0 for i in range(1000)]
def fib(n,memo):
    if memo[n]!=0:
        return memo[n]
    if n<=2:
        return 1
    memo[n] = fib(n-1,memo)+fib(n-2,memo)
    return memo[n]

print(fib(6,memo))
print(fib(7,memo))
print(fib(50,memo))

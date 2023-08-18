def fib(n):
    return n if n<=1 else fib(n-1) + fib(n-2)
i=0
while i<50:
    print(fib(i),end=",")
    i-=-1
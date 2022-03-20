fib1 = 0
fib2 = 1
fib3 = 1
print(fib1)
print(fib2)
print(fib3)

while fib3 < 100:
    fib1 = fib2
    fib2 = fib3
    fib3 = fib1 + fib2
    print(fib3)

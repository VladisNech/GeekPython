import random

X = random.uniform(0, 1)
print("X / 2 =", X / 2)
n = 0
while True:
    Y = random.uniform(0, 1)
    print(f"Y{n + 1}", "=", Y)
    n += 1
    if Y <= X / 2:
        continue
    else:
        print("En =", n)
        break

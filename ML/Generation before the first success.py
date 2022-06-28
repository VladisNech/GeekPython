from random import uniform
import numpy as np

X = uniform(0, 1)
n = 0
Y_list = []
print("X / 2 =", X / 2)

while True:
    Y = uniform(0, 1)
    Y_list.append(Y)
    print(f"Y{n + 1}", "=", Y)
    n += 1
    if Y <= X / 2:
        continue
    else:
        print("Mат. ожидание (En) =", round(np.mean(Y_list), 2))
        break

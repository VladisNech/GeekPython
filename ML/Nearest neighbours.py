import numpy as np
from random import uniform
from scipy.spatial.distance import cdist


def nearest_neighbours(data: list) -> dict:
    dists = cdist(data, data).round(8)
    ids = np.argsort(dists)[:, 1]
    neighbours_dict = dict()
    for i in range(len(data)):
        neighbours_dict[i] = ids[i], dists[i, ids[i]]

    return neighbours_dict


# Тестирование на заданных значениях из примера
resulting_dict = nearest_neighbours(
    data=[[1], [2], [5], [7], [100], [130]]
)

for key, value in resulting_dict.items():
    print("{0}: {1}".format(key, value))
print("")

data = [
    [1.14, 0.9, 3.87, 4.55, 1.65],
    [2.55, 1.1, 4.31, 1.04, 3.09],
    [3.82, 4.5, 4.26, 4.76, 3.01],
    [4.52, 0.2, 1.14, 0.05, 0.32],
    [4.11, 4.24, 0.77, 2.04, 0.56],
    [0.44, 1.92, 4.32, 4.06, 4.4],
    [1.13, 3.42, 4.98, 1.6, 2.03],
    [3.45, 3.5, 2.75, 4.32, 2.65],
    [3.18, 4.0, 4.46, 4.18, 0.31],
    [0.74, 1.06, 0.39, 4.33, 2.34]
]

for key, value in nearest_neighbours(data).items():
    print("{0}: {1}".format(key, value))
print("")


# Тестирование на сгенерированных произвольно значениях
def random_list():
    list = []
    for i in range(10):
        temp_list = []
        for j in range(0, 5):
            numbers = uniform(0, 10).__round__(2)
            temp_list.append(numbers)
        list.append(temp_list)
    return list


for key, value in nearest_neighbours(random_list()).items():
    print("{0}: {1}".format(key, value))

def my_sort(input_list: list, ascending: bool = True):
    sorted_list = input_list.copy()
    for i in range(0, len(sorted_list)):
        for j in range(i, len(sorted_list)):
            if sorted_list[i] > sorted_list[j]:
                sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]

    if not ascending:
        sorted_list = sorted_list[::-1]

    return sorted_list


input_list = [-3, 1, 1, 2, 8, 5]
sorted_list = my_sort(input_list, ascending=False)
print(sorted_list)

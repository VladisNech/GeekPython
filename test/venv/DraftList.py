import random

my_list = []
i = 0

for i in range(10):
    number = random.randint(1, 100)
    my_list.append(number)
print(sum(my_list), max(my_list), min(my_list))

# -------------------------------------------------------------------------------------------------------------------


def print_sep(my_sep, sep_len):
    return my_sep * sep_len


sep = print_sep('-', 10)
text = f'Hello {sep} fans {sep}'

print(text)

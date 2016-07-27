import random

random.seed(1)


@profile
def sort_fast():
    number_list = range(500)
    random.shuffle(number_list)
    sorted(number_list)

sort_fast()

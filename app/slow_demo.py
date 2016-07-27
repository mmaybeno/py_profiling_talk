import random

random.seed(1)


@profile
def sort_slow():
    number_list = range(500000)
    random.shuffle(number_list)
    sorted(number_list)


sort_slow()

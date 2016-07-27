import random
import cProfile

random.seed(1)

number_list = range(50000)
random.shuffle(number_list)


def sort_fast():
    number_list = range(500)
    random.shuffle(number_list)
    sorted(number_list)


def sort_slow():
    number_list = range(500000)
    random.shuffle(number_list)
    sorted(number_list)

if __name__ == '__main__':

    cProfile.run('sort_fast()')
    cProfile.run('sort_slow()')

from random import randint


def pick_one_many_times(item):
    while True:
        if type(item) not in [tuple, list]:
            return item
        else:
            item=item[randint(0, len(item)-1)]

def pick_one(item):
    item = item[randint(0, len(item)-1)]
    return item
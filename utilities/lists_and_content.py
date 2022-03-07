from random import randint, shuffle
import copy

def ip_address(length = 4):
    return '.'.join([str(randint(0, 255)) for i in range(length)])

names = ('Boris', 'Charles', 'Angela', 'Jeremy', 'Dianne', 'Xandra', 'Xavier', 'Rasputin', 'Olga', 'Helga', 'Niamh')
filenames = ('todo', 'shopping', 'people', 'artichokes', 'videos', 'shoes')
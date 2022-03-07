from random import randint, shuffle, sample
from ceh.utilities import utilities as utl

def uk_government_data_classifications_in_order():
    """official, secret, top secret
    decide whether most-least or least-most
    """
    num_choices=4
    question_text='What are the UK government\'s data classifications ordered from PLACEHOLDER?'
    ascending_order, descending_order='least to most', 'most to least'
    correct_list=['official','secret','top secret']#least to most default
    fillers=['official-secret','official top-secret','classified','unclassified','sensitive','unofficial']
    return utl.generic_correct_order(num_choices, question_text, ascending_order, descending_order, correct_list, fillers)

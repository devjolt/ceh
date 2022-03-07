from random import randint, shuffle

from ceh.utilities import utilities as utl


def aaa_in_order():
    """official, secret, top secret
    decide whether most-least or least-most
    """
    num_choices=4
    question_text='Which of the following is ordered correctly from PLACEHOLDER?'
    ascending_order, descending_order='first to last', 'last to first'
    correct_list=['identification','authentication','authorisation']#least to most default
    fillers=[]
    return utl.generic_correct_order(num_choices, question_text, ascending_order, descending_order, correct_list, fillers)
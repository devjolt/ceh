from random import randint, shuffle

from ceh.utilities import utilities as utl

def bcp_in_order():
    num_choices=4
    question_text='What are the stages of developing a BCP ordered PLACEHOLDER?'
    ascending_order, descending_order='first to last', 'last to first'
    correct_list=['identify','analyse','create','measure']#least to most default
    fillers=['physical','locate','act','implement','manage']
    return utl.generic_correct_order(num_choices, question_text, ascending_order, descending_order, correct_list, fillers)

def dr_plan_in_order():
    num_choices=4
    question_text='What are the stages of developing a DR plan ordered PLACEHOLDER?'
    ascending_order, descending_order='first to last', 'last to first'
    correct_list=['BIA','design','implement','test', 'review', 'maintain']#least to most default
    fillers=['physical','locate','act','manage']
    return utl.generic_correct_order(num_choices, question_text, ascending_order, descending_order, correct_list, fillers)


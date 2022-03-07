from random import randint, shuffle, choice
from ceh.utilities import utilities as utl

def cyber_killchain_order():
    """official, secret, top secret
    decide whether most-least or least-most
    """
    num_choices=4
    question_text='What are the stages in the cyber killchain from PLACEHOLDER?'
    ascending_order, descending_order='first to last', 'last to first'
    correct_list=['reconnaisance','weaponisation','delivery','exploitation', 'installation', 'command and control', 'actions on objectives']#least to most default
    fillers=[]
    return utl.generic_correct_order(num_choices, question_text, ascending_order, descending_order, correct_list, fillers)

def cyber_killchain_order_descriptions():
    """official, secret, top secret
    decide whether most-least or least-most
    """
    num_choices=4
    question_text='What are the stages in the cyber killchain from PLACEHOLDER?'
    ascending_order, descending_order='first to last', 'last to first'
    correct_list=[
        'gather data on the target to probe for weak points',
        'create a deliverable malicious payload using and exploit and a backdoor',
        'send weaponsised bundle to the victim',
        'exploit a vulnerability by executing code on the victim\'s system',
        'install malware on the target system',
        'create a command and control channel to communicate and pass data back and forth', 
        f"perform actions to achieve intended {choice(['goals','objectives'])}"
        ]#least to most default
    fillers=[]
    return utl.generic_correct_order(num_choices, question_text, ascending_order, descending_order, correct_list, fillers)



from random import randint, shuffle

from ceh.utilities import utilities as utl

def osi_model_layers_in_order():
    """official, secret, top secret
    decide whether most-least or least-most
    """
    num_choices=4
    question_text='What are the layers in the OSI model ordered PLACEHOLDER?'
    ascending_order, descending_order='lowest to highest', 'highest to lowest'
    correct_list=['physical','datalink','network','transport','session','presentation','application']#least to most default
    fillers=['secret','classified', 'queue', 'MAC', 'SOHO', 'NFC', 'bluetooth']
    return utl.generic_correct_order(num_choices, question_text, ascending_order, descending_order, correct_list, fillers)

def tcp_ip_model_layers_in_order():
    num_choices=4
    question_text='What are the layers in the TCP IP model ordered PLACEHOLDER?'
    ascending_order, descending_order='lowest to highest', 'highest to lowest'
    correct_list=['network interface','internet','network','transport','application']#least to most default
    fillers=['physical','datalink','session','presentation','secret','classified', 'queue', 'MAC', 'SOHO', 'NFC', 'bluetooth']
    
    return utl.generic_correct_order(num_choices, question_text, ascending_order, descending_order, correct_list, fillers)

def rings_of_security():
    num_choices=4
    question_text='What are the rings of security from PLACEHOLDER?'
    ascending_order, descending_order='innermost to outermost', 'outermost to innermost'
    correct_list=['kernel','device drivers','applications']#least to most default
    fillers=['physical','datalink','session','presentation','secret','classified', 'queue', 'MAC', 'SOHO', 'NFC', 'bluetooth']
    return utl.generic_correct_order(num_choices, question_text, ascending_order, descending_order, correct_list, fillers)
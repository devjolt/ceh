from random import randint, shuffle

from ceh.utilities import utilities as utl

def ca_certificates():
    num_choices=4
    question_text='What are the stages in obtaining a certificate from PLACEHOLDER?'
    ascending_order, descending_order='first to last', 'last to first'
    correct_list=[
        'client requests certificate from CA, providing public key and proof of id',
        'CA validates the client identity',
        'CA produces and signs with CA private key',
        'certificate is issued to the client',
        'the cetificate can be validated by any other client'
        ]
    fillers=['certificate updated by CA', 'certificate signed by client']
    return utl.generic_correct_order(num_choices, question_text, ascending_order, descending_order, correct_list, fillers)

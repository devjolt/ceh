from random import randint
from ._5_logic import *

def ip_address(length = 4):
    return '.'.join([str(randint(0, 255)) for i in range(length)])

questions = {
    'aaa_in_order':aaa_in_order,
    'terms': {
        'question_with_0':'Which best describes the following: PLACEHOLDER?',
        'question_with_1':'What best describes the following: PLACEHOLDER?',
        'type':'pairs',
        'course_code':'',
        'pairs':(
            ('An awareness campaign', 'The most cost-effective way of stopping the sharing of passwords by users'),
            ('employees', 'the leading source of computer crime losses'),
            ('Authorization', 'determines who is trusted for a given purpose'),
            ('audit trails ', 'required in order to provide accountability'),
            ('people', 'weakest link in a security system'),
            ('Errors','Most security breaches caused by employees are through'),
            ('security policy','sets out the organisation\’s formal stance on security for staff and contractors to see'),
            ('Objective evidence', 'Information which can be proved true through observation, documents, records, orpersonal interview'),
            ('Classification labelling of information', 'a control which helps to protect against unintentional disclosure ofinformation'),
            ('the major purpose of information security in an organisation','supporting the effective and efficient achievement of the organisation\’s businessobjectives'),
            ('seperation of duties', 'the principle that no user should be given enough privileges to misuse the system on their own'),
            ('assurance', 'the amount of confidence that an organisation has that its controls satisfy necessary security requirements'),
            ('non-repudiation', 'the ability to prove that an event occurred'), 
            ('fail secure', 'disconnecting a system if an event occurs'),
            ('an accidental threat', ['human error', 'malfunctions', 'fire','flood']),
            ('a deliberate threat', ['ransomeware', 'malware', 'shoulder surfing']),
            ('Privacy', ['the protection of personal data','restrictions on monitoring, surveillance and communications interception']),
            (['Intellectual Property', 'IP'], ['the legal rights which result from activity in the industrial, scientific, literary and artistic fields']),
            (['DevSecOps'], ['an approach to culture, automation, and platform design that integrates security as a shared responsibility throughout the entire IT lifecyclemm']),
            (['need to know basis'], ['preventing staff from attaining skills accross an entire process and thereby rendering it vulnerable']),
            ('Links to vendor agnostic websites specific to information security', 'Useful additions to a security training programme for all staff members'),
            ('All the agreed security requirements of each party', 'a third party connection contract should specify this'),
    
        ),
        
        'fillers': (
            (['sales', 'marketing', 'Pre-exploit vulnerability management','PE/VM'], ['arpa testing', 'yellow box testing', 'red box testing', 'dns testing'])
        )
    },
    
    'acceptable use policy':{
        'question':'which of the following is PLACEHOLDER part of the process flow on building an acceptable usage policy?',
        'type':'correct incorrect',
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            'define the target audience, readership, buisness or organisation',
            'consider the impact of the policy',
            'establish rules, compliance and legal concerns',
            'gather feedback from shareholders and review previous policy',
            'review and update existing policy or set up a new template',
            'decide which devides and types of access should be included',
            'find a template',
            'download a template',
        ),
        'incorrect': (
            f'define punishments',
            f'implement the policy regardless of impact for safety',
            'consider how to enforce the policy on stakeholders',
            'generate your own template to avoid copyright concerns',
            'share template with GDPR',
            'share template with OSEC',
            'obtain template from GDPR',
            f'only desktops located on-site should be included'
        ),
    },
    'acceptable use policy':{
        'question':'which of the following is an example of PLACEHOLDER?',
        'type':'correct incorrect',
        'positive':'enabling',
        'negative':'authentication',
        'course_code':'',
        'correct':(
            'specifying user access rights to a folder',
            'specifying user access privileges to part of a system',
            'specifying user access rights to an application',
            'granting access rights to edit a web page',
        ),
        'incorrect': (
            f'using a password to access an application',
            f'using a smartcard to access a server room',
            'requiring a pin number and RFID tag to access data on a USB drive',
            'needing to complete a capcha and enter a secret phrase to access part of a system'
        ),
    },
    'accountability, authorisation and authentication': {
        'question_with_0':'When a user PLACEHOLDER, which of the following aspects is the system ensuring?',
        'question_with_1':'Which of the following demonstrates PLACEHOLDER?',
        'type':'pairs',
        'course_code':'',
        'pairs':(
            ('accountability',['has to sign a price of equipment out', 'notifies stores that they are borrowing a laptop']),
            ('authorisation',['is granted access rights to part of a network', 'is granted access rights to a directory', 'is granted access rights to an application', 'determines who is trusted for a given purpose']),
            ('authentication',['logs onto a computer system and is asked for their mother’s maiden name','completes a capcha', 'is required to scan an id card to gain access']),
        ),
        
        'fillers': (
            (['integrity','confidentiality','availability'],['wears safety shores whilst on site', 'uses their computer to check personal emails', 'ensures that their laptop is charged with the correct charger']),
        )
    },
    'controls':{
        'question':'Controls are PLACEHOLDER implemented to:',
        'type':'correct incorrect',
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            'Mitigate risk',
            'Reduce the potential for loss',
        ),
        'incorrect': (
            f'Eliminate risk',
            f'Eliminate the potential for loss',
            'Mitigate likelihood',
            'Mitigate a threat',
            'Eliminate a threat'
        ),
    },
    'controls classifications':{
        'question':'Which of the following security controls is classified by PLACEHOLDER?',
        'type':'correct incorrect',
        'positive':'function',
        'negative':'type',
        'course_code':'',
        'correct':(
            'preventative',
            'protective',
            'detective'
            'deterrant',
            'recovery',
            'compensating'
        ),
        'incorrect': (
            'physical', 
            'technical', 
            'administrative'
        ),
    },

    'controls classifications':{
        'question':'Which of the following are PLACEHOLDER classified as security controls by function?',
        'type':'correct incorrect',
        'positive':'function',
        'negative':'type',
        'course_code':'',
        'correct':(
            'preventative',
            'protective',
            'detective'
            'deterrant',
            'recovery',
            'compensating'
        ),
        'incorrect': (
            'physical', 
            'technical', 
            'administrative'
            'nuclear',
            'software',
            'hardware',
        ),
    },

    'controls classifications':{
        'question':'Which of the following are PLACEHOLDER classified as security controls by type?',
        'type':'correct incorrect',
        'positive':'function',
        'negative':'type',
        'course_code':'',
        'correct':(
            'physical', 
            'technical', 
            'administrative',
        ),
        'incorrect': (
            'preventative',
            'protective',
            'detective'
            'deterrant',
            'recovery',
            'compensating',
            'nuclear',
            'software',
            'hardware',
        ),
    },
}

"""
5 proceedural and people security controls

network is two or more computers which are connected in order to share data or communications
CIA is an essential elemnt of any network
AAA is an essential element of any netowork authentication,  authorisation, accountability
threat, risk and vulnerability is an essential elemnt in the design on any network

open systems interconnection model (OSI) - primary model for networks

7 layers

department of defence - TCP IP model


firewall after router
firewall in line
antivirus on each machine
firewall at gateway
"""
from random import randint, choice

from ._2_logic import *

from ceh.utilities import utilities as utl



questions = {
    #google hacking commands
    #tools
    #counter measures
    #

    'nmap commands': {
        'question_with_0':'Which best describes the following: PLACEHOLDER?',
        'question_with_1':'What best describes the following: PLACEHOLDER?',
        'type':'old_pairs',
        'course_code':'',
        'pairs':(
            ('impact', 'the result of a security incident'),
            ('risk assessment','an essential first step in contingency planning'),
            ('risk management', 'process of reducing risk to an acceptable level'),
            ('very low risks', 'can be ignored'),
            ('threat', 'action or event with an unwanted consequence'),
            ('risk', 'likelihood multiplied by impact'),
            ('impact', ['measurement of the consequences of an event happening', 'measured in terms of CIA']),
            ('non-repudiation', 'the ability to prove that an event occurred'), 
            ('fail secure', 'disconnecting a system if an event occurs'),
            (['impact','likelihood'], 'one of the two terms used in combination to define levels of risk'),
            ('risk appetite', 'the amount and type of risk that an organisation is prepared to pursue, retain or take'),
            ('risk tolerance', 'the amount and type of risk that an organisation takes'),
            ('improved resilience against and recovery time from a harmful incident', 'the primary benefit of implementing appropriate information security within an organisation'),
            ('an accidental threat', ['human error', 'malfunctions', 'fire','flood']),
            ('a deliberate threat', ['ransomeware', 'malware', 'shoulder surfing']),
            (['Open Source Intelligence', 'OSINT'], 'the collection andanalysis of information that is gathered from public sources'),
            ('the MOST IMPORTANT role of senior management in regard to information security', 'Providing visible and material support for information security within the organisation'),
            ('Privacy', ['the protection of personal data','restrictions on monitoring, surveillance and communications interception']),
            ('need to know basis', 'preventing staff from attaining skills accross an entire process and thereby rendering it vulnerable'),
            (['ISMS','information security management system'], 'defines and manages controls that an organization needs to implement to ensure that it is sensibly protecting the confidentiality, availability, and integrity of assets from threats and vulnerabilities'),
            ('Business continuity and disaster recovery', 'a set of processes and techniques used to help an organization recover from a disaster and continue or resume routine business operations'),
            ('controls', 'protect against whatever risk is identified'),
            ('inherant risk','risks perculiar to a specific organisation'),
            ('PESTLE','analysis of political, social, economic and other environmental factors'),
            ('ISO 27002','a code of practise for security controls')
        ),
        
        'fillers': (
            (['sales', 'marketing', 'Pre-exploit vulnerability management','PE/VM'], ['arpa testing', 'yellow box testing', 'red box testing', 'dns testing'])
        )
    },

    'more terms': {
        'question_with_0':'Which best describes the following: PLACEHOLDER?',
        'question_with_1':'What best describes the following: PLACEHOLDER?',
        'type':'pairs',
        'course_code':'',
        'pairs':(
            ('seperation of duties', 'the principle that no user should be given enough privileges to misuse the system on their own'),
            ('vulnerability', 'absence of a safeguard that could be exploited'),
            ('assurance', 'the amount of confidence that an organisation has that its controls satisfy necessary security requirements'),
            ('non-repudiation', 'the ability to prove that an event occurred'), 
            ('fail secure', 'disconnecting a system if an event occurs'),
            (['impact','likelihood'], 'one of the two terms used in combination to define levels of risk'),
            ('risk appetite', 'the amount and type of risk that an organisation is prepared to pursue, retain or take'),
            ('risk tolerance', 'the amount and type of risk that an organisation takes'),
            ('improved resilience against and recovery time from a harmful incident', 'the primary benefit of implementing appropriate information security within an organisation'),
            ('an accidental threat', ['human error', 'malfunctions', 'fire','flood']),
            ('a deliberate threat', ['ransomeware', 'malware', 'shoulder surfing']),
            ('the MOST IMPORTANT role of senior management in regard to information security', 'Providing visible and material support for information security within the organisation'),
            ('Privacy', ['the protection of personal data','restrictions on monitoring, surveillance and communications interception']),
            ('need to know basis', 'preventing staff from attaining skills accross an entire process and thereby rendering it vulnerable'),
            (['ISMS','information security management system'], 'defines and manages controls that an organization needs to implement to ensure that it is sensibly protecting the confidentiality, availability, and integrity of assets from threats and vulnerabilities'),
            ('Business continuity and disaster recovery', 'a set of processes and techniques used to help an organization recover from a disaster and continue or resume routine business operations'),
            ('controls', 'protect against whatever risk is identified'),
            ('inherant risk','risks perculiar to a specific organisation'),
            ('PESTLE','analysis of political, social, economic and other environmental factors'),
            ('ISO 27002','a code of practise for security controls'),
            ('quantitative risk assessment','a numerical means to measure comparative risks')
        ),
        
        'fillers': (
            (['sales', 'marketing', 'Pre-exploit vulnerability management','PE/VM'], ['arpa testing', 'yellow box testing', 'red box testing', 'dns testing'])
        )
    },
    'terms': {
        'question_with_0':'Which best describes the following: PLACEHOLDER?',
        'question_with_1':'What best describes the following: PLACEHOLDER?',
        'type':'old_pairs',
        'course_code':'',
        'pairs':(
            (['impact','likelihood'], ['one of the two terms used in combination to define levels of risk']),
            ('risk appetite', ['the amount and type of risk that an organisation is prepared to pursue, retain or take']),
            ('risk tolerance', ['the amount and type of risk that an organisation takes']),
            ('an accidental threat', ['human error', 'malfunctions', 'fire','flood']),
            ('a deliberate threat', ['ransomeware', 'malware', 'shoulder surfing']),
            (['the MOST IMPORTANT role of senior management in regard to information security'], ['Providing visible and material support for information security within the organisation']),
            (['Privacy'], ['the protection of personal data','restrictions on monitoring, surveillance and communications interception']),
            ),
        'fillers': ()
    },
    'integrity availability': {
        'question':'Which of the following can be described as a PLACEHOLDER?',
        'type':'correct incorrect',
        'positive':'threat',
        'negative':'vulnerability',
        'course_code':'',
        'correct':(
            'malware',
            'phishing',
            'malicious code',
            'earthquake', 
            'power outage', 
            'terrorist attack',
            'loss of a laptop',
        ),
        'incorrect': (
            'system misconfiguration',
            'incorrect file system structures',
            'a firedoor which can be opened from the outside',
            'an easilly replicable smart car entry system', 
            'a common password',
            'out of date software'

        ),
    },
    'integrity availability': {
        'question':'Which of the following can be described as PLACEHOLDER?',
        'type':'correct incorrect',
        'positive':'mitigation',
        'negative':'acceptance',
        'course_code':'',
        'correct':(
            'installing new anti virus software',
            'implementing a clean desk policy',
            'purchasing a new firewall',
            'installing a man trap'
        ),
        'incorrect': (
            'leaving earthquake out of a risk assessment',
            'considering the risk of a terrorist attack as being insignificant and taking no action',
            'leaving an old firewall in place',
        ),
    },
    'threat types': {
        'question_with_0':'Which best describes the following: PLACEHOLDER?',
        'question_with_1':'What best describes the following: PLACEHOLDER?',
        'type':'pairs',
        'course_code':'',
        'pairs':(
            ('accidental interal threat', 'user spilling tea on a laptop'),
            ('deliberate internal threat', ['disgruntled employee', 'compromised employee stealing data']),
            ('accidental external threat', ['flood', 'cleaner forgetting to lock doors']),
            ('deliberate external threat', ['a hacker gaining entry to a system', 'malware']),
            
            ),
        'fillers': ()
    },
    'responses to risk': {
        'question_with_0':'Which best describes the following: PLACEHOLDER?',
        'question_with_1':'What best describes the following: PLACEHOLDER?',
        'type':'pairs',
        'course_code':'',
        'pairs':(
            ('avoid', 'elimination of hazards, events and exposures that can negatively affect an organization'),
            ('fallback', ['a resilience based approach','a redundancy based approach']),
            ('transfer', 'contractual shifting of a pure risk from one party to another'),
            ('share', 'reducing the likelihood and impact of uncertainty'),
            ('reduce', 'take steps to reduce the likelihood or impact of a loss'),
            ('exploit','taking advantage of an event which occurs'),
            ('accept', 'do nothing'),
            ('terminate', 'altering an inherently risky process or practice to remove the risk'),
            ),
        'fillers': ()
    },
    'responses to risk correct incorrect': {
        'question':'Which of the following is PLACEHOLDER a response to risk?',
        'type':'correct incorrect',
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            'avoid',
            'fallback', 
            'transfer',
            'share', 
            'reduce', 
            'exploit', 
            'accept',
            'terminate'
        ),
        'incorrect': (
            'mediate',
            'premedidate',
            'isolate',
            'push',
            'take', 
            'insure',
            'give away', 
            'minimise', 
            'advance', 
            'allow',
            'exterminate'
        ),
    },
    'risk assessment or risk response': {
        'question':'Which of the following is part of PLACEHOLDER?',
        'type':'correct incorrect',
        'positive':'risk assessment',
        'negative':'risk response',
        'course_code':'',
        'correct':(
            'idientification of risks',
            'idntification of assets', 
            'threat assessment',
            'vulnerability assessment', 
            'risk analysis', 
            'risk prioritisation', 
            'risk evaluation',
            'multiplying likelihood by impact'
            'examining existing controls',
            'consulting',
        ),
        'incorrect': (
            'residual risk calculation',
            'avoid',
            'fallback', 
            'transfer',
            'share', 
            'reduce', 
            'exploit', 
            'accept',
            'terminate'
        ),
    },
    'responses to risk correct incorrect': {
        'question':f"A conpany conducts a risk assessment and discovers that the key risks relate to {utl.pick_one(['confidential records','cloud data storage','processing customer data'])}? Part of BEST policy for managing this discovery is PLACHOLDER:",
        'type':'correct incorrect',
        'positive':'',
        'negative':'never',
        'course_code':'',
        'correct':(
            'decide what residual risk is acceptable',
            'implement controls to achieve acceptable risk level', 
            ),
        'incorrect': (
            'encrypt all records',
            'implement a solution based on the minium justified investment',
            'implement a solution based on ease of implementation',
            'report risk to ICO',
            'report risk to GDPR', 
            'fully implement ISO 27000 to mitigate risk',
            'fully implement ISO 27001 to mitigate risk',
            'fully implement ISO 27002 to mitigate risk',
            'fully implement ISO 27003 to mitigate risk',
            'fully implement GDPR to mitigate risk',
        ),
    },
    'the steering commitee should consist of': {
        'question':'What should a security policy be within an organisation?',
        'question_type':'correct incorrect',
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            'mandatory',
        ),
        'incorrect': (
            'discretionary',
            'optional',
            'advirosry',
            'implemented where possible',
        ),
    },
    'who is accountable': {
        'question_with_0':'Who is accountable for PLACEHOLDER?',
        'question_with_1':'PLACEHOLDER is accountable for:?',
        'type':'pairs',
        'course_code':'',
        'pairs':(
            (['information assets','deciding how often data is backed up'], 'data owner'),
            (['investing in security','providing visible and material support for information security within the organisation'], 'senior management'),
            ('managing threats and vulnerabilities', 'risk owner'),
            ('the day-to-day management of assets', 'asset owner'),
            ('writing a security policy', 'CISO'),
            ('every connection to a third party', 'connection owner'),
            ('organise security', 'department managers'),
        ),
        'fillers': (['ordering new equipment','maintaining a balance of expenditure'], ['the IT team', 'the IT manager']),
    },
    'third pary access': {
        'question':'Which of the folling is PLACEHOLDER why third party access should be controlled?',
        'question_type':'correct incorrect',
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            'they might introduce malicious code',
            'they might access critical buisness systems',
        ),
        'incorrect': (
            'they might use more than their allotted resources',
            'they may access their own data',
            'they may deny damaging your system',
        ),
    },
    
}

"""
context of different organisations

even diferent departments have different contexts

always start with a good understanding of context


strengths, weakness, oportunities and and strength of domain area
get a good understanding of interfaces

PESTLE

what is unique to that organisation

asset evaluation
risk classification

threat

number of controls

27001 114 controls for security management

27002 code of practise for controls

businesses processes used for prioritising risk throughout the organisation

asset based approach to identifation of risk



asset - by knowing asset and properties, you know which things can impact it
threat - what could have a negative impact
vulnerability - how vulnerable are we to these impacts
impact - the consequences to the business of something occurring
controls (countermeasures and safeguards)


"""
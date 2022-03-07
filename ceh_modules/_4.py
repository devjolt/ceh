from random import randint

from ._4_logic import *

def ip_address(length = 4):
    return '.'.join([str(randint(0, 255)) for i in range(length)])

questions = {
    'information_lifecycle_in_order':information_lifecycle_in_order,
    'activity_is_carried_out_at_the_stage':activity_is_carried_out_at_the_stage,
    'REST APIs': {
        'question':'Considering the information lifecycle, which of the following is PLACEHOLDER?',
        'type':'correct incorrect',
        'positive':'true',
        'negative':'false',
        'course_code':'',
        'correct':(
            ('it has been estimated that 1.7MB of data will be created for every person on Earth each second'),
            ('security is considered at each of the three stages'),
            ('cheaper storage arguably encourages poor information management'),
            ('the value of information is an important consideration for a custodian'),
            ('the need for security of information is an important consideration for a custodian'),
            ('availability of information is an important consideration for a custodian')
        ),
        'incorrect': (
            'due to more efficience storage and processing, the amount of data held by custodians is predicted to halve in four years',
            'security is only a consideration at the utilisation stage',
            'security is only a consideration at the acquisition stage',
            'security is only a consideration at the disposal stage stage',
        ),
    },


    'acquisition, utilisation and transfer definitions': {
        'question_with_0':'Which of the following relate to the PLACEHOLDER stage in the information life cycle?',
        'question_with_1':'What part of the data and information life cycle considers PLACEHOLDER?',
        'type':'pairs',
        'course_code':'',
        'pairs':(
            ('acquisition', ['planning','identification','classification','data source','how data comes into the posession of the custodian', 'creating data', 'sending data to a custodian via email','sending data to a custodian via letter', 'acquiring data using an API', 'generating data', 'the stage at which data is classified', 'planning a system to manage information', 'unique identification of information']),
            ('utilisation', ['storage','processing','sharing','transmission','validity','integrity', 'using data to educate an organisation','publishing data','encoding data into a website','making data available via an API','publishing data on an intranet', 'securely storing data', 'processing data', 'integrity', 'validity']),
            ('transfer', ['validity', 'disposal', 'transfer', 'auditing','disposing of information', 'archiving data', 'storing information so that it can be retrieved at a later date', 'auditing a data-wiping process']),
        ),
        'fillers': (
            ('ISO', 'marketing'),
            ('telemarketing', 'FIFO'),
            ('arbitage', 'cryptocurrency'),
        )
    },
    'information lifecycle': {
        'question':'Which of the following is PLACEHOLDER a part of the data and information life cycle?',
        'type':'correct incorrect',
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            ('acquisition'),
            ('utilisation'),
            ('disposal'),
        ),
        'incorrect': (
            'upscaling',
            'refactoring',
            'digestion',
            'sensitive',
            'unofficial'
        ),
    },
    
    'true false auditing testing': {
        'question':'Considering testing, aduiting and review, which of the following is PLACEHOLDER correct?',
        'type':'correct incorrect',
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            ('there is value in proving that a system is secure'),
            ('testing provides confidence in a system'),
            ('a single test after completion is not enough'),
            ('some testing must be done by expert testers'),
            ('contributions of individual consultants are valuable'),
            ('some testing must be done by expert testers'),
            ('poor patching policy is a major source of security weakness'),
            ('a report should contain an executive summary'),
            ('reports may have some level of protective marking to prevent unauthorised access'),
        ),
        'incorrect': (
            'a single test after completion of a system is often enough',
            'tests and reviews need to be completed only once if properly documented',
            'once tested, a system may be regarded as secure for years to come',
            'testing may be done by any employee',
            'an independant consultant should be part of every review', 
            'penetration tests are the only way to uncover vulnerabilities',
            'virus analysis is the only way to uncover vulnerabilities',
            'when discovered, organisations are legally obliged to follow a framework to address them',
            'penetration tests are the only way to uncover vulnerabilities',
            'all employees should have access to the executive summary of a test and review process'
        ),
    },
    'true false auditing testing': {
        'question':'Considering testing, aduiting and review, which of the following is an example of PLACEHOLDER practise?',
        'type':'correct incorrect',
        'positive':'good',
        'negative':'bad',
        'course_code':'',
        'correct':(
            ('following completion of a data processing system, carrying out an annual review of security for the lifecycle of the product'),
            ('employing a pentration testing company to find vulnerabilities in a system'),
            ('employing a specialist security consultant to assess system security on a bi-annual basis'),
            ('implementing a patching policy which insists on a monthly review'),
            ('when an audit is completed, producing a summary for decision makers'),
            ('when an audit is completed, marking an executive summary for only authorised access'),
            ('consider changes to security proceedures which are widely disregarded')
        ),
        'incorrect': (
            'certifying a system as secure following a single test',
            'following completion of a data processing system, carrying out a well documented test indended to suffice for the 10 year lifetime of the product',
            'undertaking vulnerability testing by having an emplyee extensively use the product',
            'relying mostly on virus analysis to uncover vulnerabilities',
            'making the executive summary of a test and review process publicly available'
            'sacking employees who disregard security processes'
        ),
    },
    'true false auditing testing': {
        'question':'Which of the following is an example of PLACEHOLDER practise when monitoring system and network access or usage?',
        'type':'correct incorrect',
        'positive':'good',
        'negative':'bad',
        'course_code':'',
        'correct':(
            ('logging data from a range of systems, appliances and devices'),
            ('monitoring network traffic'),
            ('monitoring traffic over external data links'),
            ('keeping six months worth of log data'),
            ('analysing data for unusual patterns of behaviour'),
            ('analysing data for signatures of known attacks'),
            ('employing specialists to gather evidence in the event of a security breach'),
            ('collecting and storing traffic data in a way that it is legally admissable in court'),
            ('using a security operations center to store and analyse data')
                
        ),
        'incorrect': (
            'monitoring network traffic at peak times',
            'monitoring only internal traffic',
            'monitoring only inbound traffic',
            'recycling log storage data weekly',
            'collecting and storing traffic data in the most cost effective way possible',
        ),
    },
    'true false security involvement in system and product assessment': {
        'question':'When considering security in system and product assessment, which of the following is PLACEHOLDER?',
        'type':'correct incorrect',
        'positive':'correct',
        'negative':'incorrect',
        'course_code':'',
        'correct':(
            ('all new systems should have to go through some form of appropriate testing'),
            ('all new products should have to go through some form of appropriate testing'),
            ('products developed in house should go through testing'),
            ('purchsed products should go through testing'),
            ('a product bought from a reputable supplier should be tested'),
            ('every product should be considered for it\'s effects on confidentiality, abailability and integrity'),
            ('how a product interacts with other assets should be tested'),
            ('it is advisable to use a test environment which replicates live systems'),
            ('testing on live systems may have an adverse impact'),
            ('use of a malware scanner in recommended for new code'),
                
        ),
        'incorrect': (
            ('some new systems should have to go through some form of appropriate testing'),
            ('some new products should have to go through some form of appropriate testing'),
            ('products developed in house can be trusted without testing'),
            ('purchsed products are regarded as already having been tested'),
            ('a product bought from a reputable supplier does not need to be tested'),
            ('each product should be tested only in isolation from other products to ensure a reliable result'),
            ('if a product is tested and secure, it does not matter if others parts of the system are compromised'),
            ('it is advisable to use a live system for valid testing'),
            ('test environments do not reflect the requirements of a live system'),
            ('it is preferable to always examine new code by eye'),
        )
    },
    'true false security issues with off the shelf products': {
    'question':'Which of the following is PLACEHOLDER?',
    'type':'correct incorrect',
    'positive':'correct',
    'negative':'incorrect',
    'course_code':'',
    'correct':(
        ('rogue code hidden in off the shelf products may be a threat'),
        ('bugs in off the shelf products may introduce vulnerabilities'),
        ('security updates are essential in securing commercial products'),
        ('low priced copies of products containing malware is a threat'),
        ('purchasing pirated products may leave a company open to prosecution'),
        ('prosectution may have an impact on operations and lead to loss of reputation'),            
    ),
    'incorrect': (
        ('off the shelf products may be regarded as completely secure'),
        ('off the shelf products do not contain bugs'),
        ('security updates should be regarded with suspicion'),
        ('security updates should be skipped in favour of thorough testing'),
        ('products from unreputable vendors are be fine if properly tested'),
        ('purchasing pirated products may result in prosecution under GDPR')
    )
    },
    'true false collaborative development': {
    'question':'Which of the following is PLACEHOLDER?',
    'type':'correct incorrect',
    'positive':'correct',
    'negative':'incorrect',
    'course_code':'',
    'correct':(
        ('collaborative development is beneficial'),
        ('a dev team should seek to involve other business functions which will use a deliverable'),
        ('end users should be consulted when a new product is developed'),
        ('involving end users helps them to buy in to security features'),
        ('involving end users in development is known as stakeholder engagement'),
        ('a current knowledge of new system architectures and technologies is important for security architects'),            
        ('a good security manager maintains good relationships with all other managers to gain trust')   
    ),
    'incorrect': (
        ('development is best undertaken in small, isolated teams to improve attention to detail'),
        ('a dev team should involve as few other buisness functions as possible'),
        ('end users should be consulted once at the start of the process'),
        ('the views of end users is secondary to security considerations'),
        ('a good security manager employs punishments to ensure compliance'),
    )
    },
    'controls': {
        'question_with_0':'Which of the following is an example of a PLACEHOLDER control?',
        'question_with_1':'What type of control is PLACEHOLDER?',
        'type':'pairs',
        'course_code':'',
        'pairs':(
            ('physical', ['a laptop lock','a door lock']),
            ('technical', ['an authentication system','a retinal scan','a fingerprint scan']),
            ('proceedural', ['an acceptable use policy', 'a disciplinary policy']),
        ),
        'fillers': (
            ('forceful', 'threats'),
            ('military', 'hypnosis'),
        )
    },
    'true false collaborative development': {
    'question':'Regarding security and awareness training, which of the following is PLACEHOLDER?',
    'type':'correct incorrect',
    'positive':'correct',
    'negative':'incorrect',
    'course_code':'',
    'correct':(
        ('should be part of a new joiner induction'),
        ('should be relevant and interesting'),
        ('it should be regular'),
        ('it should involve all employees'),
        ('training should be recorded'),
    ),
    'incorrect': (
        ('given after probationary period for new employees'),
        ('a dev team should involve as few other buisness functions as possible'),
        ('end users should be consulted once at the start of the process'),
        ('the views of end users is secondary to security considerations'),
        ('a good security manager employs punishments to ensure compliance'),
    )
    },
    'true false collaborative development': {
    'question':'Which of the following is PLACEHOLDER a security policy which affects employees?',
    'type':'correct incorrect',
    'positive':'',
    'negative':'not',
    'course_code':'',
    'correct':(
        'contracts of employment', 
        'codes of conduct', 
        'acceptable use policies', 
        'segregation', 
        'seperation of duties policy', 
        'mandatory vacation policy', 
        'BYOD/removable medial policy', 
        'disciplinary policy',
    ),
    'incorrect': (
        'gDPR', 
        'health and Safety Act',
        'copyright act',
        'safety signage policy',
        'laptop lock', 
        'multifactor authentication', 
        'bifactor authentication', 
        'type 1 authentication',
        'type 2 authentication',
        'type 4 authentication',
        'type 3 authentication',
        'username and password',
    )
    },
    'true false collaborative development': {
    'question':'Which of the following is PLACEHOLDER a user access control layer?',
    'type':'correct incorrect',
    'positive':'',
    'negative':'not',
    'course_code':'',
    'correct':(
        'username and password', 'smartcard','key phrase','pin number', 'NFC fob', 'fingerprint scan', 'retinal scan','captcha'
    ),
    'incorrect':(
        'GDPR', 'top secret', 'ISO27001', 'ISO27002', 'receptionist', 'security guard', 'laptop lock', 'firewall', 'static MAC address', 'dynamic IP'
    )
    },


    'controls': {
        'question_with_0':'Which of the following is an example of PLACEHOLDER?',
        'question_with_1':'What type of error is PLACEHOLDER?',
        'type':'pairs',
        'course_code':'',
        'pairs':(
            (['false acceptance','FAR' ], ['a finger print scan incorrectly identifies someone as authenticated','a retinal scan incorrectly grants permission to perform an action','a finger print scan incorrectly grants permission to perform an action','a retinal scan incorrectly authenticates someone']),
            (['false rejection','FRR'], ['a finger print scan incorrectly fails to authenticate someone','a retinal scan incorrectly fails to grant permission to perform an action','a finger print scan incorrectly fails to grant permission to an authorised person','a retinal scan incorrectly fails to authenticate someone']),
        ),
        'fillers': (
            (['type-4 authenication', 'false imprinsonment'], ['a lock is picked, enabling an authorised person to gain entry', 'a lock is picked, enabling an unauthorised person to gain entry']),
            (['type-3 threats', 'acceptable use policy'], ['an authorised person guesses their pasword after forgetting it']),
        )
    },
    
'controls': {
        'question_with_0':'Which of the following is an example of PLACEHOLDER access control?',
        'question_with_1':'What type of control is the following: PLACEHOLDER?',
        'type':'pairs',
        'course_code':'',
        'pairs':(
            ('type 1', ['username and password','key phrase','number pattern','pin number','something you know', 'easiest to replicate']),
            ('type 2', ['smartcard','key fob','key','NFC token', 'something you have']),
            ('type 3', ['finger print', 'retinal scan', 'something you are']),
            (['bi-factor','multi factor'], make_bifactor()),########custom question
        ),
        
        'fillers': (
            (['captcha','type 4', 'type 0'], make_single_factor()),########custom question
        )
    },


'controls': {
        'question_with_0':'Which of the following is true of PLACEHOLDER?',
        'question_with_1':'What type of control does the following describe: PLACEHOLDER?',
        'type':'pairs',
        'course_code':'',
        'pairs':(
            (['DAC','discressionary access control'], ['set arbitrarily','used in commercial settings']),
            (['role based', 'RBAC'], ['easiest to administer','most convenient to administer']),
            (['mandatory control','MAC'], ['set by head office', 'used in government settings', 'used in military settings']),
        ),
        
        'fillers': (
            (['captcha','type 4', 'type 0'],['most expensive', 'favoured by sporting organisations', 'only works in industrial settings', 'only works in commercial settings', 'only works in goverment settings', 'only works in miliary settings']),
        )
    },

    'software development lifecycle': {
        'question_with_0':'Which of the following would be considered at the PLACEHOLDER stage of the software development lifecycle?',
        'question_with_1':'What type of control is the following: PLACEHOLDER?',
        'type':'pairs',
        'course_code':'',
        'pairs':(
            ('requirements and security', ['legal aspects','regulations','contracts']), 
            ('specification', ['selecting authenitication layers','considering security to be build','key','NFC token', 'something you have']),
            ('design', ['diagram of architecture', 'sketch of architecture']),
            (['aquisition', 'development'], 'considering the build and security'),
            ('testing', ['black box','white box','grey box','unit testing','integrated testing','functional testing','system testing', 'alpha testing', 'beta testing']),
            ('implementation', ['configuration for security', 'baselining']),
            ('maintenance', ['patching', 'updates'])
        ),
        
        'fillers': (
            (['sales', 'marketing'], ['arpa testing', 'yellow box testing', 'red box testing', 'dns testing'])
        )
    },
    'choosing products':{''
        'When choosing a security critical product to protect sensitive information, it is PLACEHOLDER wise to choose one which is:'
         'type':'correct incorrect',
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            'certified against ISO/IEC 2700 series standard', 'proven secure by appropriately trained pentesting professionals'
        ),
        'incorrect':(
            'fully guaranteed', 'evaluated against common criteria', 'highlt rated by trade journals'
        )
    },
    

}

'''
    'acceptance testing': {
    'question':'Who should be involve in acceptance testing?',
    'type':'correct incorrect',
    'positive':'',
    'course_code':'',
    'correct':(
        'all '
    ),
    'incorrect':(
        'GDPR', 'top secret', 'ISO27001', 'ISO27002', 'receptionist', 'security guard', 'laptop lock', 'firewall', 'static MAC address', 'dynamic IP'
    )
    },



}

'true false software development': {
        'question':'Considering the software development lifecycle, which of the following is PLACEHOLDER?',
        'type':'correct incorrect',
        'positive':'correct',
        'negative':'incorrect',
        'course_code':'',
        'correct':(
            
                
        ),
        'incorrect': (
        ),
    },
}

permissions
permissions at the file, folder level
directory permissions are inheritable
directory permissions are cumulative
permisions are swet by the owner to individual or group accounts
permissions may be implicit
permissions may be explicit
can be set to read, write, 

need to know and hold principle
principle of least privilege - only giving as much access to people as they need to satisfy their function
classification of data - categorising data as 
handling caveats - rules about what can be done with the data can be included in the accpetable use policy
aplies to all types of media
applies to waste material

why are people the weakest link?
you can't socially engineer a machine
people may act out of revenge
people can make mistakes
people can act intentionally
people fit all areas of internal, external, intentional, unintentional
people on staff are trusted and have certain privileges
people are unpredictable

occording to ISO27003 
policy should use
categories
Which categories should x document have

defence against unauthorised access
only vaild and accurate data is processed
proper functional testing
backups - 
assurance of availability - a par of the application failing
comp[liace - legal aspects
security of data transmision/communications - 
auditiing and recording

who should be involved in acceptance testing?
project team
end users
managers
asurance team
acreditation team

changes to software must be formally manage to ensure the following:
benefits of the requested change
risk
accepted downtime
development time
training needs
recording changes

'true false changes to software': {
        'question':'Considering the software development lifecycle, which of the following is PLACEHOLDER?',
        'type':'correct incorrect',
        'positive':'true',
        'negative':'false',
        'course_code':'',
        'correct':(
            '3rd parties going out of buisness can be mitigated using Escrow',
            '3rd parties changing hands',
            'trade secrets can be protected through the data protection act',
            'intellectial property can be protected through the data protection act',
            'rogue code can be mitigated though testing',
            'trade secrets can be protected with NDAs',        
            'when making changes to software'
        ),
        'incorrect': (
            '',
            '',
            '',
            '',
            '',

        ),
    },
'''

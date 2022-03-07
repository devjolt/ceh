from random import randint
from cismp.utilities import utilities as utl
from ._8_logic import *

questions = {
    'true and false business recovery plan':{
    'question':'Regarding disaster recovery and business continuity management, which of the following is PLACEHOLDER?',
    'positive':'correct',
        'negative':'incorrect',
        'course_code':'8',
        'correct':(
            'business recovery plans are best developed in the way which suits the organisation',
            'disaster recovery plans are best developed in the way which suits the organisation', 
            'ensuring that a risk assessment has been completed effectively is essential',
            'considering the consequences of events is more important than comprehensively considering all possible events',
            'it is good practice to involve a number of key staff members in planning',
            'documentation is a vital part of DR',
            'involving professionals in testing documentation is recommended',
            'multiple copies of a DR plan should be kept on site',
            'change management should ensure that all copies are the latest version',
            'people should be the first consideration in a DR plain',
            'succession planning involves deciding who the decision maker is in case of non-availability',
            'succession planning identifies key personnel and their replacements in case of non-availability',
        ),
        'incorrect':(
            'business recovery plans are best developed following a strict framework',
            'disaster recovery plans are best developed following a strict framework', 
            'a risk assessment can be completing following completion of the BRP',
            'a risk assessment can be completing following completion of the DR plan',
            'a risk assessment can be completing following completion of the BRP and DR plan',
            'comprehensively considering all possible events is essential',
            'it is good practice for company leaders to make executive decision on the content of the BRP',
            'it is good practice for company leaders to make executive decision on the content of the DR plan'
            'one copy of a DR plan should be kept on site',
            'change management should ensure that one copy of the latest version is maintained',
            'equipment should be the first consideration in a DR plain',
            'data should be the first consideration in a DR plain',
            'succession planning involves deciding which systems should take over in case of failure. ',
            'succession planning identifies key systems and their replacements in case of non-availability',
        )
        
    },

    'Business continuity plan, disaster recovery': {
        'question_with_0':'Which of the following describes a PLACEHOLDER?',
        'question_with_1':'What is PLACEHOLDER?',
        'type':'pairs',
        'course_code':'8',
        'pairs':(
            (['BCP','business continuity plan'], ['thinking through events which might adversely impact a business, and writing down a method of continuing','plan to maintain continuity of business operations', 'plan to enable a business to keep running despite problems','planning for relatively small changes in normal operations', 'creating policies, plans and procedures to minimise impact of an event', 'active as long as organisation is able to perform is maintained']),
            (['DR', 'disaster recovery'], ['continuing to operate and attempting to get back to normal', 'defined in ISO 24672','functional if businesss continuity fails','active if continuity is broken', 'functional if businesss continuity plan is inadequate']),
            (['BIA','business impact analysis'], ['considering the implications of possible threats to a business', 'derived from a risk assessment']),
            (['business continuity'], ['the capability of the organisation to continue delivering products or services at acceptable predefined levels following a disruptive incident', 'defined in ISO 22301']),
        ),
        'fillers': (
            (['CIA','BCS','ISO', 'GDPR', 'NCSC', 'BLA'], ['security patrolling a sensitive building', 'working from home to not catch covid', 'providing fruit for employees', 'planning to clse the office on Sundays', 'enforced vacations']),
        )
    },
    'resilience and redundancy': {
        'question_with_0':'Which of the following is an example of PLACEHOLDER?',
        'question_with_1':'Which of the following describes PLACEHOLDER?',
        'type':'pairs',
        'course_code':'8',
        'pairs':(
            ('warm standby', ['a duplicate system requiring some configuration','a duplicate system which may have some data pre-loaded','a duplicate system which may have data loaded to a known backup point']),
            ('cold standby', ['a duplicate sytem requiring configuration from scratch', 'a duplicate system which may be in a remote location']),
            ('hot standby', ['the most costly form of duplicate system','a duplicate system which is fully loaded with with up to date data', 'a duplicate system which is fully configured', 'a duplicate system which can be brought into service quickly']),
            ('synchronous replication', 'duplicating a system, waiting for acknowledgement of reciept'),
            ('asynchronous replication', 'duplicating a system, without for acknowledgement of reciept'),
        ),
        'fillers': (
            (['steady standby','amorphous replication'], ['duplicating your operating system in a partition', 'keeping your system on all the time']),
        )       
    },
    'cold, warm hot and high availability': {        
        'type':'correct incorrect',
        'question':'Which of the following is an example of PLACEHOLDER?',
        'positive':'resilience',
        'negative':'redundancy',
        'course_code':'8',
        'correct':(
            'ensuring that there are no single points of failure',
            'ensuring that failure in one part of a system cannot bring everything to a standstill',
            'using multiple webservers with load balancing',
            'cross-training employees in vital skillsets', 
        ),
        'incorrect':(
            'having a duplicate system on cold standby',
            'having a duplicate system on warm standby',
            'having a duplicate system on hot standby',
            'having a high availability duplicate system',
        )        
    },
    'Stages of business impact analysis': {
        'question_with_0':'Which of the following is an example of the  PLACEHOLDER stage in developing a business continuity plan?',
        'question_with_1':'Which of the following stage in developing a business continuity plan relates to PLACEHOLDER?',
        'type':'pairs',
        'course_code':'8',
        'pairs':(
            ('identify', ['risk assessment']),
            ('analyse', ['BIA', 'business impact analysis']),
            ('create', ['strategy and BCP development']),
            ('measure', ['testing the BCP','training in relation to BCP', 'maintaining BCP']),

        ),
        'fillers': (
            (['implement', 'impact'], ['cost benefit analysis', 'non-repudiation', 'procurement', 'critical']),
        )       
    },
    'BCP metrics': {
        'question_with_0':'Which of the following defines PLACEHOLDER?',
        'question_with_1':'Which of the following is PLACEHOLDER?',
        'type':'pairs',
        'course_code':'8',
        'pairs':(
            (['MTD','maximum tolerable downtime', 'MTPD', 'MAO', 'maximum acceptable outage', 'maximum tolerable period of disruption'], ['the maximum length of time a business function can be inoperable without causing irreperable harm to the business']),
            (['recovery time objective','RTO'], ['must always be less than the maximum acceptable outage','the maximum tolerable length of time that a computer, system, network or application can be down after a failure or disaster occurs']),
            (['recovery point objective','RPO'], ['a measurement of how much loss can be accepted by the organisation when a disaster occurs','typically measured in time since last backup was taken', 'greater than RPO']),
            (['maximum tolerable data loss','MTDL'], ['the maximum loss of data an organisation can tolerate','calculated according to age or value of data', 'must be lower than MTDL']),
        ),
        'fillers': (
            (['MTO', 'RTPD', ], ['the policy stating how you will achieve maximum tolerable downtime', 'the policy stating how you will achieve recovery time objective']),
            (['MPO', 'RTDL', ], ['MTD must always be less than RTO', 'the policy stating how you will achieve recovery time objective']),
        )       
    },
    'Stages of business impact analysis': {
        'question_with_0':'Which of the following is an example of the  PLACEHOLDER stage in developing a business continuity plan?',
        'question_with_1':'Which of the following stage in developing a business continuity plan relates to PLACEHOLDER?',
        'type':'pairs',
        'course_code':'8',
        'pairs':(
            ('initial risk assessment', ['risk assessment']),
            ('BIA', ['BIA', 'business impact analysis']),
            ('Design', ['strategy and BCP development']),
            ('implement', ['testing the BCP','training in relation to BCP', 'maintaining BCP']),
            ('test', ['testing the BCP','training in relation to BCP', 'maintaining BCP']),
            ('review', ['testing the BCP','training in relation to BCP', 'maintaining BCP']),
            ('maintenance', ['testing the BCP','training in relation to BCP', 'maintaining BCP']),

        ),
        'fillers': (
            (['plan','assess','classify','quantify','formalise', 'impact'], ['backing up vulnerable data', 'publishing the BCP', 'making copies of the BCP']),
        )       
    },
    'bcp_in_order':bcp_in_order,
    'dr_plan_in_order':dr_plan_in_order,
    'parts of bcp': {        
        'type':'correct incorrect',
        'question':'Which of the following is PLACEHOLDER a stage in a BCP?',
        'positive':'',
        'negative':'not',
        'course_code':'8',
        'correct':(
            'identify',
            'analyse',
            'measure',
            'create', 
        ),
        'incorrect':(
            'implement',
            'plan',
            'assess',
            'classify',
            'quantify',
            'formalise',
        )        
    },
    'parts of dr plan': {        
        'type':'correct incorrect',
        'question':'Which of the following is PLACEHOLDER a stage in a BCP?',
        'positive':'',
        'negative':'not',
        'course_code':'8',
        'correct':(
            'initial risk assessment',
            'BIA',
            'business impact analysis',
            'design',
            'implement', 
            'test', 
            'review',
            'maintenance',  
        ),
        'incorrect':(
            'plan',
            'assess',
            'classify',
            'quantify',
            'formalise',
            'publish',
            'submit for review',
            'audit'
        )        
    },
    'types of backup': {
        'question_with_0':'Which of the following describes PLACEHOLDER backup?',
        'question_with_1':'Considering backup, which of the following PLACEHOLDER?',
        'type':'pairs',
        'course_code':'8',
        'pairs':(
            ('full', ['involves backup of all files on a system','has the slowest backup time', 'has the quickest retore time', 'has the largest storage requirement']),
            ('incremental', ['involves backup of all files which have changed since the last full or incremental backup', 'has the quickest backup time', 'has the slowest restore time', 'has minimal storage requirement']),
            ('differential', ['involves backup of all files which have changed since the last full backup','has progressively slower backup time', 'has progressively quicker backup time', 'has progressively larger storage requirement']),

        ),
        'fillers': (
            (['integral', 'cloud'], ['involves backup of essential files on a system', 'involves backup of critical files on a system', 'involves backup of all files which have changed since the last differential backup']),
        )       
    },
    'enabling data availability': {        
        'type':'correct incorrect',
        'question':'Which of the following is PLACEHOLDER a technique used to enable data availability? ',
        'negative':'not',
        'course_code':'8',
        'correct':(
            'replication',
            'distributed file systems',
            'restore points',
            'refresh points',
            'shadow copies',
            'snapshots',
            'checkpoints',
            'system image',

        ),
        'incorrect':(
            'multiple usb drives',
            'data protection policy',
            'clear desk policy',
            '2fa',
            'BIA',
            'access points',
            'availability points',
            'distributed access',
            'restoration',
            'system notes',
            'documentation',

        )        
    },

}

"""
replication
dist


redundant array of indipendant disks

risk assessment allows you to prioritise areas more at risk
consider system redundancey


perform assessment

systems monitoring and testing
recovery methods

ISO27001 - standarts for managing an information security management system
framework which helps 
ISMS
latest in sept sept 2013

'ISO27001': {
        'question':'Regarding IS027001, which of the following is PLACEHOLDER?',
        'type':'correct incorrect',
        'positive':'correct',
        'negative':'incorrect',
        'course_code':'',
        'correct':(
            'based on managing risk',
            'risk assessment',
            'risk treatment',
            'statement of applicability',
            'help you to identify and correct issues',
            'conduct internal audits',
            'ensure infosec team is confident to perform their roles',
            'reaction and response to alerts should be tested',
            'critical data should be backed up',
        ),
        'incorrect': (
            
        ),
    },




"""
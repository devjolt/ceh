from random import randint
from cismp.utilities import utilities as utl
from ._7_logic import *

questions = {
    
    'operational controls': {
        'question_with_0':'Which of the following describe PLACEHOLDER operational controls?',
        'question_with_1':'Which operational control is PLACEHOLDER?',
        'type':'pairs',
        'course_code':'5',
        'pairs':(
            ('procedural', ['checking references for job applicants', 'clean desk policy','background checks for job applicants','hiring policy','vetting staff','dismissal policy','special area access', 'clear desk policy']),
            (['product', 'technical'], ['use of encryption', 'use of passwords','firewalls','encryption', 'use of bitlocker','Writing random data to the same data file for at least seven cycles']),
            ('physical', ['signs','mantraps','IR detection systems','gates','fences doors','locks','CCTV','lighting systems', 'security guards patroling a perimeter','having a reception area','often the most cost effective','ensuring that unauthorised people don\'t have access',f'preventing mechanical harm from happening to people','ensuring that unauthorised people don\'t have access',f'preventing mechanical harm from happening to assets','ensuring that unauthorised people don\'t have access',f'preventing mechanical harm from happening to data', 'securing devices to a desk', 'locking windows', 'preventing shoulder surfing', 'being aware of tailgating', 'keeping desks clear', 'locking secure areas', 'securely disposing of waste', 'deactivating lost devices']),
            ('environmental', ['heating', 'ventilation', 'air conditioning', 'HVAC', 'humidity controls']),
        ),
        'fillers': (
            (['network', 'preventative'], ['never using a device', 'working from home to not catch covid']),
            
        )  
    },
    'physical security true false': {
        'question':'Regarding physical security, which of the following PLACEHOLDER good practise?',
        'type':'correct incorrect',
        'positive':'describes',
        'negative':'does not describe',
        'course_code':'',
        'correct':(
            'often the most cost effective',
            'usually the first line of defence',
            'having a properly staffed reception area', 'properly protecting back doors and fire escapes', 'use of locked doors for access to sensitive areas', 'keeping keys in safes', 'securing devices', 'accompanying visitors',
            'marking equipment', 'using a stand-by power generator',
            'having a backup generator',
            'use of transparent ducts to house network cabling'
        ),
        'incorrect': (
            'often the least cost effective',
            'usually one of the last lines of defence',
            'penetration testing software', 'having a strong password policy',
            'having a properly configured firewall', 'biometric authentication',       
        ),
    },
    'preventative, detective and reactive action':{
        'question_with_0':'Which of the following is an example of PLACEHOLDER action?',
        'question_with_1':'PLACEHOLDER is an example of which type of action?', 
        'type':'pairs',
        'course_code':'7',
        'pairs':(
            ('preventative', ['Checking references for job applicants','A staffed reception area','A non-disclosure agreement', 'Locking windows','Being aware of tailgating', 'Keeping desks clear', 'Locking sensitive areas', 'Securely disposing of waste', 'A Clean desk policy', 'Being wary of shoulder surfing', 'Securing devices to a desk', 'Antivirus not allowing malware to be downloaded', 'background checks for job applicants', 'clear desk policy', 'security guards patroling a perimeter']),
            ('detective', ['An intruder alarm', 'Use of smart water to spray people in sesitive areas', 'Antivirus running checks on a system to identify malware']),
            ('reactive', ['An electrified fences','Antivirus removing malware', 'Deactivating lost devices', 'taking legal action']),
            
        ),
        'fillers': (
            (['adaptive', 'network', 'environmental', 'penetrative', 'official', 'legal'], ['never using a device', 'working from home to not catch covid']),
            
        )
    },
    'preventative measures':{
        'question_with_0':'Which of the following might prevent PLACEHOLDER?',
        'question_with_1':'PLACEHOLDER might prevent which of the following?', 
        'type':'pairs',
        'course_code':'7',
        'pairs':(
            ('accidental damage', ['Checking references for job applicants','A staffed reception area','A non-disclosure agreement', 'Locking windows','Being aware of tailgating', 'Keeping desks clear', 'Locking sensitive areas', 'Securely disposing of waste', 'A Clean desk policy', 'Being wary of shoulder surfing', 'Securing devices to a desk', 'Antivirus not allowing malware to be downloaded', 'Background checks for job applicants', 'A clear desk policy', 'Security guards patroling a perimeter']),
            ('theft', ['An intruder alarm', 'Use of smart water to spray people in sesitive areas', 'Antivirus running checks on a system to identify malware']),
            ('loss of availability', ['Server clusters', 'Virtualisation', 'Use of the cloud','Network load balancers']),
            ('loss of data ', ['Failover','Server clusters', 'Virtualisation']),
            
        ),
        'fillers': (
            (),
            
        )
    },
    'preventative measures':{
        'question_with_0':'Which of the following might prevent PLACEHOLDER?',
        'question_with_1':'PLACEHOLDER is an example of which type of measure?', 
        'type':'pairs',
        'course_code':'7',
        'pairs':(
            ('accidental damage', ['user training','policies','cable tidies','cable covers','routine maintainance and cleaning','power surge protection','environmental controls','heating ventilation and air conditioning','humidity controls','fire suppression systems']),
            ('theft', ['user awareness and training','vetting policies','hiring policies','physical building security','mobile device security','passwords','tiem out settings','kensington locks','encryption','GPS tracking','GSM tracking','remote sanitisation','mobile device management system']),
            ('loss of availability', ['Failover','Server clusters', 'Virtualisation', 'Cloud','network load balancers']),
            ('loss of data', ['RAID', 'redundant array of independant disks']),
        ),
        'fillers': (
            (['forgetting password', 'loss of power supply', 'loss of keys', 'ransomware'], 'resilient array of independant disks'),
        )
    },
    'RAID levels':{
        'question_with_0':'Which of the following describes PLACEHOLDER?',
        'question_with_1':'PLACEHOLDER describes which of the following?', 
        'type':'pairs',
        'course_code':'7',
        'pairs':(
            ('RAID 0', ['striped array','min 2 discs', 'only advantage is speed']),
            ('RAID 1', ['mirror','only 2 discs', 'only example is fault tolerance']),
            ('RAID 3', ['stripe with fixed parity','min 3 discs']),
            ('RAID 5', ['stripe with parity','min 3 discs']),
            ('RAID 6', ['double parity','min 4 discs']),
            ('RAID 10', ['mirrored stripe','min 4 discs']),
        ),
        'fillers': (
            (['RAID 2', 'RAID 4', 'RAID 7', 'RAID 8', 'RAID 9', 'RAID 11'],['min 1 disc','only 1 disc','min 5 discs','min 6 discs','min 7 disca','mirrored parity', 'mirrored mirror', 'striped mirror']),      
        )
    },
}
    
"""
waste documents - 
magnetic media - optcal
magnetic media - hard drive
old equipment/devices - 
3rd part data removal - 

waste should always be handled in accordance with its security protective markings and handling policies
shredding
incinerating
deleted/wiped (data)
formatted (drives)
degaussed putting through magnetic field
destroyed
pulped
a combination of any of the above is generally the best option
"""
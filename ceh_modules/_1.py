from random import randint, choice

from ._1_logic import *

words = ['risk','threat', 'disruption','backdoor','confidentiality','integrity','availability','non-repudiation', 'authenticity','identity','classification','policy','communication']

"""
resource = {
    'question_with_0':'Which isPOSNEG an example of PLACEHOLDER?',
    'question_with_1':'What best describes the following: PLACEHOLDER?',
    'positive_negative':('',' not'),
    'question_order':'What best describes the killchain from PLACEHOLDER?',
    'ascending_descending':('first to last', 'last to first'),
    'type':['vanilla_pairs','posneg_pairs', 'multi_pairs', 'order_pairs'],
    'course_code':'',
    'pairs':[
        ('correct',['A','B','C','D']),
        ('incorrect',['1', '2', '3','4']),
        ('ambiguous',['0', '9', '8','7']),
        
    ],
    'fillers': (
        ('backwards',['z', 'y', 'x','w']),
    )
}
#posneg_pairs - at least two pairs, both containing 3 items


"""
questions = {
    'terms': {
        'question_with_0':'Which is POSNEGthe best description of PLACEHOLDER?',
        'question_with_1':'What best describes the following: PLACEHOLDER?',
        'positive_negative':('','not '),
        'type':['new_pairs','multi_option_pairs'],
        'course_code':'1',
        'pairs':(
            ('confidentiality','the assurance that information can only be accessed by authorized people'),
            ('integrity',['the trustworthiness of data or resources', 'prevention of improper and unauthorised changes', 'assurance that information is sufficiently accurate for its purpose']),
            ('availability','assurance that the systems responsible for delivering, storing and processing information are accessible when required'),
            ('authenticity', 'characteristic of data that ensures the quality of being genuine or uncorrupted'),
            ('non-repudiation', 'way to guarantee that the sender of a message cannot deny having recieved the message'),
            (['motive', 'goal'], ['depends on attacker\'s state of mind', 'depends on attackers resources and capabilities']),
            ('vulnerability', 'absence of a safeguard that could be exploited'),
            ('passive attack', ['involves monitoring network traffic and data flow', 'does not tamper with data','difficult to detect','allow capture of data without consent of a user']),
            ('active attack', ['involves tampering with data to bypass or break into secured systems','involves sending traffic actively that can be detected','exploits information in transit','penetrate or infect target\'s network and gain access to remote systems to compromise internal network']),
            ('close-in attack', 'performed in physical proximity to the target'),
            ('insider attack', ['performed by trusted persons who have physical access to critical assets', f"involves using privileged access to {choice(['intentionally cause a threat to information or information systems','violate rules'])}"]),
            ('distribution attacks', [f"tampering with {choice(['hardware','software','hardware or software'])} prior to installation", f"attackers tamper with hardware or software {choice(['at its source', 'in transit'])}"]),
            ('information warfare','use of information and communication technologies for competetive advantage over an opponent'),
            (['command and control warfare','C2 warfare'], 'the impact an attacker possesses over a compromised system or network'),
            ('intelligence-based warfare', ['sensor-based technology that directly corrupts technological systems','consists of the design, protection and denial of systems that seek sufficient knowledge to dominate the battlescape']),
            ('electronic warfare','uses radio-electronic and cryptographic techniques to degrade communication'),
            ('radio-electronic techniques', 'attacking the physical means of sending information'),
            ('cryptographic techniques', 'disrupting the means of sending information using bits and bytes'),
            ('psychological warfare', ['use of various techniques to demoralise an adversary','propaganda', 'terror']),
            ('hacker warfare','use of viruses, logic bombs, trojan horses and sniffers to achieve many different goals'),
            ('economic warfare', 'affecting the economy of a business using economic means'),
            ('cyberwarfare', ['use of information systems agains the virtual personas of individuals or groups', 'broadest of all information warfare']),
            ('semantic attacks', 'taking over a system while maintaining the perception that it is operating correctly'),
            ('simula-warfare', 'acquiring weapons for mere demonstration rather than actual use'),
            ('defensive information warfare', 'involves all strategies and actions to defend against attacks on ICT assets'),
            ('offensive information warfare', 'involves attacks against the ICT assets of an opponent'),
            ('cyber kill chain methodology',['component of intelligence driven defense for the identification and prevention of malicious intrusion attacks', 'framework for securing cyberspace based on the concept of military kill chains','equiped with seven phase protection mechanism to mitigate and reduce cyber threats']),
            (['APT groups', 'advanced persistent threat groups'], 'organizations that lead, attacks on a country\'s information assets of national security or strategic economic importance through either cyberespionage or cybersabotage'),
            ('TTPs','patterns of activity associated with specific threat actors or groups'),
            ('adversary behavioural identifcation', 'identification of the common methods or techniques followed by an adversary to launch attacks'),
            ('IoCs', ['act as a good source of information about threats', 'contain actionable threat intelligence which helps in enhancing incident-handling strategies', 'information about malicious activity collected from various establishments in a network\'s inrastructure']),
            ('risk', 'Threats x Vulnerabilities x Impact'),
            ('CTI', 'the collection and  analysis of information about threats and adversaries and the drawing up of patterns that provide an ability to make knowledgeable decisions for preparedness, prevention, and response actions against various cyberattacks'),

        ),
        'fillers': (
            []
        )
    },


    'elements of information security': {
        'question_with_0':'Which is POSNEGa description of PLACEHOLDER?',
        'question_with_1':'What best describes PLACEHOLDER?',
        'positive_negative':('','not '),
        'type':['new_pairs','multi_option_pairs'],
        'course_code':'1',
        'pairs':(
            ('confidentiality','the assurance that information can only be accessed by authorized people'),
            ('integrity',['the trustworthiness of data or resources', 'prevention of improper and unauthorised changes', 'assurance that information is sufficiently accurate for its purpose']),
            ('availability','assurance that the systems responsible for delivering, storing and processing information are accessible when required'),
            ('authenticity', 'characteristic of data that ensures the quality of being genuine or uncorrupted'),
            ('non-repudiation', 'way to guarantee that the sender of a message cannot deny having recieved the message'),
        ),
        
        'fillers': (
            (['sales', 'marketing', 'Pre-exploit vulnerability management','PE/VM'], ['arpa testing', 'yellow box testing', 'red box testing', 'dns testing'])
        )
    },


    'elements of information security two': {
        'question_with_0':'which of the following POSNEG PLACEHOLDER?',
        'positive_negative':('are','could not be described as'),
        'type':['posneg_pairs', 'multi_option_pairs'],
        'course_code':'1',
        'pairs':(
            ('CEH elements of information security',['confidentiality','integrity','availability','non-repudiation','authenticity']),
            ('something other than CEH elements of information security',['identity','classification','policy','communication']),
        ),
        'fillers': ([])  
    },

    'combo': {
        'question_with_0':'which of the following POSNEG PLACEHOLDER?',
        'positive_negative':('are','could not be described as'),
        'type':['posneg_pairs', 'multi_option_pairs'],
        'course_code':'1',
        'pairs':(
            ('CEH elements of information security',['confidentiality','integrity','availability','non-repudiation','authenticity']),
            ('elements of an attack', ['motive','goal','method','vulnerability']),
            ('motives for an attack',['disrupt business continuity','information theft','create fear and chaos','bring financial loss to target', f"propogate {choice(['religious', 'political'])} beliefs",'achieve state military objectives','damage repuation of target','take revenge','demand ransom']),
            ('a category of attack according to IATF',['passive','active','close-in','insider','distribution'])
        ),
        'fillers': ([])  
    },
    'definition of attack': {
        'question_with_0':'which of the following POSNEG PLACEHOLDER?',
        'positive_negative':('are','could not be described as'),
        'type':['posneg_pairs', 'multi_option_pairs'],
        'course_code':'1',
        'pairs':(
            ('elements of an attack', ['motive','goal','method','vulnerability']),
            ('something other than the elements of an attack', ['risk','threat','identification','disruption','backdoor']),
        ),
        'fillers': ([])  
    },

    'formula of attack': {
        'question':'Which of the following PLACEHOLDERcorrectly describes the formula of an attack?',
        'type':'correct_incorrect',
        'positive':'',
        'negative':'in',
        'course_code':'',
        'correct':(
            'attacks = motive + method + vulnerability',
            'attacks = goal + method + vulnerability',
            'attacks=goal+method+vulnerability',
        ),
        'incorrect': (
            f"attacks = goal + method + {choice(words)}",
            f"attacks = goal + {choice(words)} + vulnerability",
            f"attacks = {choice(words)} + method + vulnerability",
        ),
    },
    'motives for attacks': {
        'question':'Which of the following are PLACEHOLDER motives for security attacks?',
        'type':'correct_incorrect',
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            'disrupt business continuity',
            'information theft',
            'create fear and chaos',
            'bring financial loss to target', 
            f"propogate {choice(['religious', 'political'])} beliefs",
            'achieve state military objectives',
            'damage repuation of target',
            'take revenge',
            'demand ransom',
        ),
        'incorrect': (
            'ransomware',
            'malware',
            'backdoor',
            'use backdoor',
            'phishing',
            'send email',
            'DDoS',
            'Botnet',
        ),
    
    },
    'classification of attacks': {
        'question':'Which of the following, according to IATF, are PLACEHOLDER a category of attack?',
        'type':'correct_incorrect',
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            'passive','active','close-in','insider','distribution'
        ),
        'incorrect': (
            'redundant','malicious','hacking','state sponsored','national', 'financial','revenge','reputation','revenge','theft','disruptive'
        ),
    },
    'types of attacks': {
        'question_with_0':'Which best describes PLACEHOLDER?',
        'question_with_1':'What best describes the following: PLACEHOLDER?',
        'type':'old_pairs',
        'course_code':'',
        'pairs':(
            ('a passive attack', ['involves monitoring network traffic and data flow', 'does not tamper with data','difficult to detect','allow capture of data without consent of a user']),
            ('an active attack', ['involves tampering with data to bypass or break into secured systems','involves sending traffic actively that can be detected','exploits information in transit','penetrate or infect target\'s network and gain access to remote systems to compromise internal network']),
            ('a close-in attack', 'performed in physical proximity to the target'),
            ('an insider attack', ['performed by trusted persons who have physical access to critical assets', f"involves using privileged access to {choice(['intentionally cause a threat to information or information systems','violate rules'])}"]),
            ('a distribution attack', [f"tampering with {choice(['hardware','software','hardware or software'])} prior to installation", f"attackers tamper with hardware or software {choice(['at its source', 'in transit'])}"]),
        ),
        'fillers': ()
    },
    'types of attacks': {
        'question_with_0':'Which is an example of PLACEHOLDER?',
        'question_with_1':'What best describes the following: PLACEHOLDER?',
        'type':'old_pairs',
        'course_code':'',
        'pairs':(
            ('a passive attack', ['footprinting', 'sniffing','network traffic analysis','decryption of weakly encrypted traffic']),
            ('an active attack', ['DoS', 'modification of information', 'spoofing', 'replay attacks', 'viruses', 'worms','ransomware','bypassing protection mechanisms','password-based attacks','privilege escalation','session hijacking','backdoor access', 'man-in-the-middle attack','cryptography attacks','DNS poisoning', 'ARP poisoning','SQL injection','compromised-key attack','XSS attacks','firewals attack', 'IDS attack', 'directory traversal attack','profiling','exploitation of application software','exploitation of OS software','arbitrary code execution']),
            ('a close-in attack', ['eavesdropping','shoulder surfing','dumpster diving']),
            ('an insider attack', ['wiretapping','theft of physical devices','data theft and sploliation','pod slurping','planting keyloggers', 'planting backdoors', 'planting malware']),
            ('a distribution attack', [f"tampering with {choice(['hardware','software','hardware or software'])} prior to installation", f"tampering with hardware or software {choice(['at its source', 'in transit'])}"]),
        ),
        'fillers': ()
    },
    'types of warfare': {
        'question_with_0':'Which is an example of PLACEHOLDER?',
        'question_with_1':'What best describes the following: PLACEHOLDER?',
        'type':'old_pairs',
        'course_code':'',
        'pairs':(
            ('information warfare','use of information and communication technologies for competetive advantage over an opponent'),
            (['command and control warfare','C2 warfare'], 'the impact an attacker possesses over a compromised system or network'),
            ('intelligence-based warfare', ['sensor-based technolofy that directly corrupts technological systems','consists of the design, protection and denial of systems that seek sufficient knowledge to dominate the battlescape']),
            ('electronic warfare','uses radio-electronic and cryptographic techniques to degrade communication'),
            ('radio-electronic techniques', 'attacking the physical means of sending information'),
            ('cryptographic techniques', 'disrupting the means of sending information using bits and bytes'),
            ('psychological warfare', ['use of various techniques to demoralise an adversary','propaganda', 'terror']),
            ('hacker warfare','use of viruses, logic bombs, trojan horses and sniffers to achieve many different goals'),
            ('economic warfare', 'affecting the economy of a business using economic means'),
            ('cyberwarfare', ['use of information systems agains the virtual personas of individuals or groups', 'broadest of all information warfare']),
            ('semaintic attacks', 'taking over a system while maintaining the perception that it is operating correctly'),
            ('simula-warfare', 'acquiring weapons for mere demonstration rather than actual use'),
            ('defensive information warfare', 'involves all strategies and actions to defend against attacks on ICT assets'),
            ('offensive information warfare', 'involves attacks against the ICT assets of an opponent'),
        ),
        'fillers': ()
    },

    'information warfare': {
        'question':'Which of the following is asssociated with PLACEHOLDER warfare?',
        'type':'correct_incorrect',
        'positive':'defensive',
        'negative':'offensive',
        'course_code':'',
        'correct':(
            'prevention','deterrance','alerts','detection','emergency preparedness','response'
        ),
        'incorrect': (
            'web application attacks','web server attacks','malware attacks','MITM attacks','system hacking'
        ),
    },
    #'cyber_killchain_order':cyber_killchain_order,
    #'cyber_killchain_order_descriptions':cyber_killchain_order_descriptions,
    #'cyber_killchain_order_descriptions_combined':cyber_killchain_order_descriptions_combined,
    

    'cyber killchain order': {
        'question_with_0':'Which of the following POSNEGdescribe PLACEHOLDER in the cyber killchain?',
        'question_with_1':'Which stage in the cyber killchain best describes the following activity: PLACEHOLDER?',
        'question_order':'What best describes the killchain from PLACEHOLDER?',
        'ascending_descending':('first to last', 'last to first'),
        'positive_negative':('','do not '),
        'type':['posneg_pairs', 'new_pairs', 'multi_option_pairs', 'order_pairs'],
        'course_code':'1',
        'pairs':(
            ('reconnaisance',[ 'gather data on the target to probe for weak points','gathering information about the target through internet searches or social engineering','performing analysis of various online activities and public information','gathering information from social\networking sites and web services', 'obtaining information about websites visited','monitoring and analysing the target organisation\'s website','performing Whois, DNS and network footprinting', 'performing scanning to identify open port and services']),
            ('weaponisation',['create a deliverable malicious payload using and exploit and a backdoor','identifying appropriate malware payload based on the analysis','creating new malware payload or selecting, resusing modifying available malware based on vulnerabilities','creating phishing email campaign','leveraging exploit kits and botnets']),
            ('delivery', ['send weaponsised bundle to the victim','sending phishing emails to employees of the target organisation','distributing USB drives containing malicious payload to employees of the target', 'performing watering hold attacks on the compromised website', 'implementing hacking tools against OS, applications and servers']),
            ('exploitation', ['exploit a vulnerability by executing code on the victim\'s system','install malware on the target system','exploiting software valuerabilities to gain remote access to the target', 'exploiting hardware valuerabilities to gain remote access to the target']),
            ('command and control', ['create a command and control channel to communicate and pass data back and forth', 'establish a two-way communication channel between the victim\'s system and th adversary controlled server', 'leveraging channels such as web traffic, email communication and DNS messages', 'applying privilege excalation techniques', 'hiding any evidence of compromise using techniques such as encryption']),
            ('actions on objectives', [f"perform actions to achieve intended {choice(['goals','objectives'])}",'gaining access to confidential data', 'destroy operation capability', 'use as launching point to perform other attacks']),
        ),
        'fillers': ([])  
    },
    'Tactics Techniques Procedures': {
        'question_with_0':'Considering TTPs, which of the following POSNEGdescribe PLACEHOLDER?',
        'question_with_1':'What best describes the following: PLACEHOLDER?',
        'ascending_descending':('first to last', 'last to first'),
        'positive_negative':('','do not '),
        'type':['posneg_pairs'],
        'course_code':'1',
        'pairs':(
            ('tactics',['the way a threat actor operates during different phases of an attack','the way an actor gathers information on a target', 'the pattern of methods an actor follows for initial compromise', 'the number of entry points an actor uses while attempting to enter the target network']),
            ('techniques',['the specific methods used by a threat actor during different phases of an attack','the tools used at each stage in an attack','may be non-technical in the initial phases','tend to be more technical in the intermediate phase']),
            ('procedures', ['a sequence of actions performed by the threat actors','sending phishing emails to employees of the target organisation','distributing USB drives containing malicious payload to employees of the target', 'performing watering hold attacks on the compromised website', 'implementing hacking tools against OS, applications and servers']),
        ),
        'fillers': ([])
    },
    'Adversary behavioural identification': {
        'question_with_0':'Considering adversary behavioural identification, Which of the following POSNEGrelate to PLACEHOLDER?',
        'question_with_1':'Which best relates to the following: PLACEHOLDER?',
        'positive_negative':('','do not '),
        'type':['posneg_pairs', 'new_pairs', 'multi_option_pairs'],
        'course_code':'1',
        'pairs':(
            ('internal reconnaisance',['the methods and techniques used to carry out find out about a system',f"enumeration of {choice(['systems', 'hosts', 'processes'])}", f"the execution of various commands to find out {choice(['local user context', 'system configuration', 'hostname', 'IP address', 'active remote systems', 'programs running on the target systems'])}", 'monitored using packet capturing tools', 'monitored by checking commands executed in batch scripts']),
            ('use of Powershell',['automating data exfiltration and launching further attacks',f"misuse identified by checking {choice(['PS transcript logs', 'Windows Event logs'])}"]),
            ('unspecified proxy activities', ['creating and configuring multiple domains pointing to the same host to switch quickly and avoid detection','countered by checking data feeds generated by domains']),
            ('use of command-line interface', ["using the CLI to interact with the target system","using the CLI to browse files","using the CLI to modify file content","using the CLI to create new accounts","using the CLI to connect to the remote system","using the CLI to download and install malicious code",'can be identified by checking logs for process IDs', 'can be identified by processes having arbitrary letters and numbers']),
            ('use of HTTP user agent', ['modifying the user agent field to communicate with the compromised system and carry out further attacks','can be identified by checking the content of the user agent field']),
            ('use of command and control server', [f"used to communicate remotely with compromised systems through an encrypted session",'adversary can use encrypted channel to steal data, delete data or launch further attacks', 'detected by tracking network traffic for outbound connection attempts', 'detected by tracking network traffic for unwanted open ports']),
            ('use of DNS tunneling', ['used to obfuscate malicious traffic in legitimate traffic', 'allows malicious traffic to hide in common protocols', 'can be detected by analysing malicious DNS requests', 'can be detected by analysing DNS payload','can be detected by analysing unspecified domains','can be detected by analysing destination of DNS requests']),
            ('use of web Shell', ['used to manipulate web server','performed by creating a shell within a website','allows remote access to server functionality','identified by analysing server access', 'identified by analysing error logs', 'identified by suspicious strings that indicate encoding','identified by user agent strings']),
            ('data staging', ['collecting and combining as much data as possible', 'detected by monitoring netowrk traffic for malicious file transfers', 'detected through file integrity monitoring and log events']),
        ),
        'fillers': ([])  
    },
    'Indicators of Compromise': {
        'question_with_0':'Considering adversary behavioural identification, which of the following POSNEGrelate to PLACEHOLDER?',
        'question_with_1':'Which best relates to the following: PLACEHOLDER?',
        'positive_negative':('','do not '),
        'type':['posneg_pairs', 'new_pairs', 'multi_option_pairs'],
        'course_code':'1',
        'pairs':(
            ('internal reconnaisance',['the methods and techniques used to carry out find out about a system',f"enumeration of {choice(['systems', 'hosts', 'processes'])}", f"the execution of various commands to find out {choice(['local user context', 'system configuration', 'hostname', 'IP address', 'active remote systems', 'programs running on the target systems'])}", 'monitored using packet capturing tools', 'monitored by checking commands executed in batch scripts']),
            ('use of Powershell',['automating data exfiltration and launching further attacks',f"misuse identified by checking {choice(['PS transcript logs', 'Windows Event logs'])}"]),
            ('unspecified proxy activities', ['creating and configuring multiple domains pointing to the same host to switch quickly and avoid detection','countered by checking data feeds generated by domains']),
            ('use of command-line interface', ["using the CLI to interact with the target system","using the CLI to browse files","using the CLI to modify file content","using the CLI to create new accounts","using the CLI to connect to the remote system","using the CLI to download and install malicious code",'can be identified by checking logs for process IDs', 'can be identified by processes having arbitrary letters and numbers']),
            ('use of HTTP user agent', ['modifying the user agent field to communicate with the compromised system and carry out further attacks','can be identified by checking the content of the user agent field']),
            ('use of command and control server', [f"used to communicate remotely with compromised systems through an encrypted session",'adversary can use encrypted channel to steal data, delete data or launch further attacks', 'detected by tracking network traffic for outbound connection attempts', 'detected by tracking network traffic for unwanted open ports']),
            ('use of DNS tunneling', ['used to obfuscate malicious traffic in legitimate traffic', 'allows malicious traffic to hide in common protocols', 'can be detected by analysing malicious DNS requests', 'can be detected by analysing DNS payload','can be detected by analysing unspecified domains','can be detected by analysing destination of DNS requests']),
            ('use of web Shell', ['used to manipulate web server','performed by creating a shell within a website','allows remote access to server functionality','identified by analysing server access', 'identified by analysing error logs', 'identified by suspicious strings that indicate encoding','identified by user agent strings']),
            ('data staging', ['collecting and combining as much data as possible', 'detected by monitoring netowrk traffic for malicious file transfers', 'detected through file integrity monitoring and log events']),
        ),
        'fillers': ([])  
    },

    'Indicators of Compromise': {
        'question_with_0':'Which of the following POSNEGrelate to the PLACEHOLDER category of IoC indicators?',
        'question_with_1':'Which best relates to the following: PLACEHOLDER?',
        'positive_negative':('','do not '),
        'type':['posneg_pairs', 'new_pairs', 'multi_option_pairs'],
        'course_code':'1',
        'pairs':(
            ('atomic',['cannot be segmented into smaller parts','meaning is not changed in the context of an intrusion', 'an IP address', 'an Email address']),
            ('computed',['obtained from the data extracted from a security incident','a hash value', 'a regular expression']),
            ('behavioural', ['useful in identifying code injection','enable broad protection','grouping of both atomic and computed indicators','combined on the basis of some logic']),
            ('email', ["social engineering","easy to use","autonomous when set up","email address","subject line",'attachments', 'links']),
            ('network', ['URLS','domain names','IP addresses', f"useful for {choice(['command and control', 'malware delivery','identifying computer specific information','identifying browser type','identifying operating system'])}"]),
            ('host-based', ['filenames','file hashes','registry keys','DDLs','mutex','found by performing an analysis of the infected sytem within the network']),
        ),
        'fillers': ([])  
    },
    'hacker classes': {
        'question_with_0':'Which of the following POSNEGrelate to PLACEHOLDER?',
        'question_with_1':'Which best relates to the following: PLACEHOLDER?',
        'positive_negative':('','do not '),
        'type':['new_pairs', 'multi_option_pairs'],
        'course_code':'1',
        'pairs':(
            ('black hats',['use skills for illegal or malicious purposes', 'often involved in criminal activity','crackers']),
            ('white hats',['penetration testers','defensive', 'have permission from system owner']),
            ('grey hats', ['offensive and defensive', 'may work within and outside of the law']),
            ('suicide hackers', ["aim to bring down critical infrastructure","not worried about facing jail time","not concerned about consequences of their actions"]),
            ('script kiddies', ['unskilled','do not develop their own software','focus on volume of attacks']),
            ('cyber terrorists', ['aim to create fear','threaten large scale disruption of computer networks']),
            ('state sponsored', ['employed by the government', 'target other states', 'target other governments']),
            ('hacktivist', ['perform hacking as acts of protest', 'aim to inrease awareness of their cause', 'commonly deface or disable websites'])
        ),
        'fillers': ([])  
    },
    'hacking phases': {
        'question_with_0':'Considering the phases of hacking, which of the following POSNEGrelate to PLACEHOLDER?',
        'question_with_1':'Which best relates to the following: PLACEHOLDER?',
        'question_order':'What best describes the hacking phases from PLACEHOLDER?',
        'ascending_descending':('first to last', 'last to first'),
        'positive_negative':('','do not '),
        'type':['posneg_pairs', 'new_pairs', 'multi_option_pairs', 'order_pairs'],
        'course_code':'1',
        'pairs':(
            ('reconnaisance',['can be active','can be passive','preparatory phase','Whois','gathering as much information as possible about a target','dumpster diving','social engineering']),
            ('scanning',['immediately precedes attack','scanning a network for specific information','in-depth probing','port scanning','Traceroute', 'Cheops', 'network mappers', 'ping tools', 'vulnerability scanners']),
            ('gaining access', ['use identified vulnerabilities','unauthorised access','happens locally, overs a LAN or the internet', 'password cracking', 'stack-based uffer overflows', 'denial-of-service', 'session hijacking', 'spoofing', 'packet flooding', 'privilege escalation']),
            ('maintaining access', ['retaining ownership','could involve closing up vulnerabilities','install backdoors']),
            ('clearing tracks', ['PsTools', 'NetCat', 'erasing footprint', 'remaining unnoticed', 'tunnelling', 'steganography','hiding information', 'can turn into a reconnaissance phase']),
        ),
        'fillers': ([])  
    },
    'risk': {
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
    'risk management process': {
        'question_with_0':'Considering the risk management process, which of the following POSNEGrelate to PLACEHOLDER?',
        'question_with_1':'Which best relates to the following: PLACEHOLDER?',
        'question_order':'What best describes the risk management process from PLACEHOLDER?',
        'ascending_descending':('first to last', 'last to first'),
        'positive_negative':('','do not '),
        'type':['posneg_pairs', 'new_pairs', 'multi_option_pairs', 'order_pairs'],
        'course_code':'1',
        'pairs':(
            ('risk identification',['initial step','sources','causes','consequences']),
            ('risk assessment',['estimate likelihood and impact','ongoing iterative process','assign priorities for risk mitigation','make mitigation plans','determine quantitative and qualitative risk', 'determine likelihood and severity', 'happens when hazards are identified by not controlled']),
            ('risk treatment', ['selecting and implementing controls','modifying risks','handle risks outside of tolerance', f"requires knowledge of {choice(['costs','methods','people responsible','benefits','likelihood of success','ways to measure success'])}"]),
            ('risk tracking and review', ['determine measure and procedures adopted are appropriate','regular inspections','identify improvements','ensures that controls are in place', 'ensures that controls are understood and followed']),
        ),
        'fillers': ([])  
    },
    'Types of threat intelligence': {
        'question_with_0':'Which of the following POSNEGrelate to PLACEHOLDER?',
        'question_with_1':'Which best relates to the following: PLACEHOLDER?',
        'question_order':'What best describes the types of threat intelligence from PLACEHOLDER?',
        'positive_negative':('','do not '),
        'ascending_descending':('highest level to most granular', 'most granular to highest level'),
        'type':['posneg_pairs', 'new_pairs', 'multi_option_pairs','order_pairs'],
        'course_code':'1',
        'pairs':(
            ('strategic threat intelligence',['financial impact of cyber activity','attribution for intrusions and data breaches', 'threat actors and attack trends', 'high level information', 'consumed by high level executives', 'threat landscape', 'statistical data on breaches, theft and malware','cyber attacks in geopolitical conflicts', 'how adversary TTPs change over time', 'impacts of industry decisions']),
            ('tactical threat intelligence',['used by threat actors',f"consumed by cyber security professionals such as {choice(['IT service managers', 'security operations managers', 'NOC staff','architects'])}", f"derived from {choice(['campaign', 'incident', 'attack group'])} reports",f"derived from {choice(['human intelligence', 'malware', 'technical papers','purchasing intelligence'])}",'provides data to day operational support']),
            ('operational threat intelligence', ['information about specific threats','contextual information','helps in understanding threat actors',f"consumed by {choice(['heads of incident response', 'network defenders', 'security forensics teams', 'fraud detection teams'])}",'improves early stages detecting capability']),
            ('technical threat intelligence', ["provides information about resources an attacker uses to perform an attack","short lifespan","specific IP addresses used by malicious endpoints","phishing email headers","consumed by SOC staff",'consumed by IR teams', 'directly fed into security devices','collected from active campaigns']),
        ),
        'fillers': ([])  
    },



}
"""
    'cloud service contract': {
        'question':'When setting up a contract with a supplier for hosting cloud services, which of the following safeguards is PLACEHOLDER important?',
        'type':'correct incorrect',
        'positive':'most',
        'negative':'not',
        'course_code':'',
        'correct':(
            'The ability to recover all information from the cloud if the contract isterminated',
            'The confidentiality and integrity of downloading information from the cloud',
            'The service level requirement for availability of the information'
        ),
        'incorrect': (
            'The make of hardware used by the hosting supplier',
            'The make of software used by the hosting supplier',
            'The location of the servers of the hosting supplier',
        ),
    },
    'integrity, availability and accountability': {
        'question_with_0':'Which of the following best describes PLACEHOLDER?',
        'question_with_1':'If PLACEHOLDER is important, which of the following would be used to ensure this is covered effectively?',
        'type':'pairs',
        'course_code':'',
        'pairs':(
            ('integrity',['the accuracy of information', 'the completeness of information', 'guarantee that the message sent is the message received, and that the message was not intentionally or unintentionally altered']),
            ('confidentiality',['the privacy of information', 'information only being seen by those who are intended']),
            ('availability',['the accessibility of information','information being to hand when required']),
            
        ),
        'fillers': (
            (['applicability', 'security', 'scarcity','visiblity'], ['the safety of employees', 'the safety of servers', 'the speed of a processor', 'the size of storage'])
        )
    },
    'three pillars': {
        'question':'Which of the following is PLACEHOLDER one of the pillars of information security:',
        'type':'correct incorrect',
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            'confidentiality',
            'availability',
            'integrity'
        ),
        'incorrect': (
            'strategy',
            'discretionary',
            'usability',
            'strategy',
            'risk avoidance',
            'managability',
        ),
    },
    'Good security practise': {
        'question':'Which of the following PLACEHOLDER correctly describe “good” security practice?',
        'type':'correct incorrect',
        'positive':'',
        'negative':'does not',
        'course_code':'',
        'correct':(
            'Accounts should be monitored regularly',
            'You should have a procedure in place to verify password strength',
            'You should ensure that there are no accounts without passwords'
        ),
        'incorrect': (
            'Employees can create their own accounts',
            'You should ensure that employees passwords are memorable',
            'You should require users to manually record each use of an external network',
            'Accounts should be closed if not accessed for 24 hours'
        ),
    },
    



}

"""
"""


'Good security practise': {
        'question':'A business impact analysis should PLACEHOLDER:",
        'type':'correct incorrect',
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
        ),
        'incorrect': (
            'Employees can create their own accounts',
            'You should ensure that employees passwords are memorable',
            'You should require users to manually record each use of an external network',
            'Accounts should be closed if not accessed for 24 hours'
        ),
    },





('', 'The BEST way of protecting against the eavesdropping of email'),
('denial of service', ''),
('', 'role of the organisation's senior management in risk analysis'),
('', 'would require information security systems awareness training'),
('', 'Countermeasures are directly associated with'),
('', 'determines who is trusted for a given purpose'),
('', 'determines who is trusted for a given purpose'),
('', 'determines who is trusted for a given purpose'),
('', 'determines who is trusted for a given purpose'),
('', 'determines who is trusted for a given purpose'),

('', 'determines who is trusted for a given purpose'),
('', 'determines who is trusted for a given purpose'),
('', 'determines who is trusted for a given purpose'),
('', 'determines who is trusted for a given purpose'),
('', 'determines who is trusted for a given purpose'),
('', 'determines who is trusted for a given purpose'),

('', 'determines who is trusted for a given purpose'),
('', 'determines who is trusted for a given purpose'),
('', 'determines who is trusted for a given purpose'),
('', 'determines who is trusted for a given purpose'),
('', 'determines who is trusted for a given purpose'),
('', 'determines who is trusted for a given purpose'),
('Regular incremental and full backups', ''),
('A formal disciplinary process, ''),


('trapdoor ', 'structured programming technique'),
('A gate access control system requiring a security token', 'prevent unauthorised access, damage and interference to IT services'),



('business continuity plan test results', 'record of Information Security Management System operation'),



In addition to identification, the only way to ensure the accountability of users for the actions taken within a system or domain would be?

(a) Oversight

(b) Authentication

(c) Authorization

(d) Credentials


"""
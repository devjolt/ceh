from cismp.utilities import utilities as utl
from ._6_logic import *


questions = {
    'OSI model layers in order':osi_model_layers_in_order,
    'TCP IP model layers in order':tcp_ip_model_layers_in_order,
    'OSI model': {
        'question_with_0':'Which of the following describe the PLACEHOLDER layer in the OSI model?',
        'question_with_1':'Which layer of the OSI model is the PLACEHOLDER?',
        'type':'pairs',
        'course_code':'5',
        'pairs':(
            ('application', ['layer 7','first layer for a sending device', 'final layer for a recieving device', 'seventh layer for a recieving device', 'last layer for a recieving device', 'layer which shows what was used to create a message']),
            ('presentation', ['layer 6','second layer for a sending device', 'sixth layer for a recieving device', 'layer containing information about appearance of data']),
            ('session', ['layer 5','third layer for a sending device', 'fifth layer for a recieving device', 'layer which sets parameters for communication']),
            ('transport', ['layer 4','fourth layer for a sending device', 'fourth layer for a recieving device', 'layer which may use TCP', 'layer which may use UDP']),
            ('network', ['layer 3','fifth layer for a sending device', 'third layer for a recieving device', 'layer which uses IP', 'layer involved in routing', 'layer which routes data to an IP']),
            ('datalink', ['layer 2','sixth layer for a sending device', 'second layer for a recieving device', 'layer which converts IP to a MAC address', 'routes data to a device']),
            ('physical', ['layer 1','final layer for a sending device', 'seventh layer for a sending device','last layer for a sending device', 'first layer for a recieving device', 'layer which may use ethernet cable to get data to a device', 'layer which may use a wireless network to get data to a device']),
        ),
        'fillers': (
            ('multi-factor', ['layer 0', 'layer 1','eight layer for a sending device', 'eigth layer for a recieving device','the first, second and third layer for a sending device', 'the first, second and third layer for a recieving device']),
        )
    },
    'OSI model and IP TCP model': {
        'question_with_0':'Which IP TCP model layer contains the PLACEHOLDER OSI layer?',
        'question_with_1':'',
        'type':'pairs',
        'course_code':'5',
        'pairs':(
            (['application','presentation', 'session'], ['application']),
            ('transport', ['transport', 'host to host']),
            (['network','datalink'], ['internet']),
            ('physical', ['network interface']),
        ),
        'fillers': (
            (['firewall','b-router', 'security', 'perimeter'], ['layer 0', 'layer 5']),
        )
    },
    'Network devices': {
        'question':'which of the following is PLACEHOLDER?',
        'type':'correct incorrect',
        'positive':'true',
        'negative':'false',
        'course_code':'',
        'correct':(
            'a router is a layer 3 networking device',
            'a router routes network traffic between one IP subnet to another',
            'a router may route traffic from a private to a public network',
            'a switch connects using a physical mac address',
            'a switch may be managed or unmanaged',
            'modern swithces may also incorporate a router',
            'modern firewalls work at multiple layers of the OSI model',
            'firewalls may be physical',
            'firewalls may be software based',
            'firewalls allow or deny traffic based on rules and access control lists',
            'firewall rules may be based on application protocols',
            'firewall rules may be based on port number',
            'firewall rules may be based on content',
            'firewall rules may be based on IP address',
        ),
        'incorrect': (
            f'a router is a layer {randint(1,2)} networking device',
            f'a router is a layer {randint(4,7)} networking device',
            'a router routes network traffic between one MAC address and another',
            'a router only routes traffic from a public to a private network',
            'a switch connects using IP address',
            'all switches are managed',
            'all switches are unmanaged',
            f'modern firewalls work only at layer {randint(1,2)} of the OSI model',
            'firewalls are only physical',
            'firewalls are only software based',
            'firewalls allow or deny traffic based on AUP',
            'firewall rules are always based on application protocols',
            'firewall rules are always based on port number',
            'firewall rules are always based on content',
            'firewall rules are always based on IP address',
            'firewall rules can not be based on content',
        ),
    },
    'rings of security':rings_of_security,
    'types of virus': {
        'question_with_0':'What best describes a PLACEHOLDER virus?',
        'question_with_1':'What type of virus PLACEHOLDER?',
        'type':'pairs',
        'course_code':'6',
        'pairs':(
            ('polymorphic', 'alter themselves to avoid detection'),
            ('macro',['exploits scripts to hide in documents', 'exploits scripts to hide in files']),
            ('stealth','masks or hides activity to avoid detection'),
            ('armoured','is difficult to detect or remove'),
            ('retrovirus', 'attacks anti virus systems'),
            ('phage', 'infectf mutliple parts of the system to regenerate more easilly'),
            ('companion',['takes root filename of an executable','tries to launch itself instead of a legitimate program']),
            (['mutlipart','multipartite'], 'infects your boot sector as well as files')
        ),
        'fillers': (
        )
    },
    'types of malware': {
        'question_with_0':'What best describes a PLACEHOLDER?',
        'question_with_1':'What type of malware PLACEHOLDER?',
        'type':'pairs',
        'course_code':'6',
        'pairs':(
            ('virus',['requires user interaction', 'doesn\'t self propogate', 'requires a host']),
            ('worm',['self replicates without a triggering event', 'propogates itself through a network', 'can be uses to distribute viruses', 'can be uses to distribute lobic bombs']),
            ('trojan',['downloaded by a user as part of a desired piece of code', 'disguised as something legitimate', f"is introduced through {utl.pick_one(['illegal downloads', 'games', 'screensavers','system softeware'])}", 'used to install DDoS Zombies/Bots']),
            ('rootkit',['works beneath the level at which tools used to detect viruses operate', 'operates at the kernel level', 'may be detected using heuristics']), 
            ('back door',['also called a trap door', 'may be installed legitaimnately into code', 'may be installed maliciously through trojan, virus, code download or manually', 'enables remote access clients']),
            ('spyware',['gathers data from your machine using your machine\'s resources', 'may be used in identity theft', 'associated with key logging']),
            ('adware',['promotes goods or services at the expecse of machine\'s resources', 'displays unwanted pop-up advertisements based on user activity']),
            ('ransomware',['files encrypted by bad actors', 'used to extort money']), 
            ('logic bomb',['maliscious code triggered by an action or a date', 'normally associated with insider attacks']), 
            (['bot','botnet'],['machine taken over using malicous code', 'controlled by a bot herder', 'are associated with DDoS attacks']),
            ('zero day exploit',['takes advantage of software which has just been launched', 'takes advantage of the lack of known attack signatures']),
        ),
        'fillers': (
        )
    },

    'types of attack': {
        'question_with_0':'What best describes a PLACEHOLDER attack?',
        'question_with_1':'What type of attack PLACEHOLDER?',
        'type':'pairs',
        'course_code':'6',
        'pairs':(
            (['man in the middle','MitM'],[f"involves {utl.pick_one(['spoofing', 'poisoning'])} name resolution systems", f"may involve {utl.pick_one(['spoofing', 'poisoning'])} {utl.pick_one(['DNS', 'domain name server', 'ARP', 'NetBios','WINS'])}"]),
            (['DoS', 'DDos'],['involves flooding an address with messages', 'overwhelming an address with requests', 'unauthorised withholding of information or resources']),
            ('spoofing', ['falsifying network data to undermine a system', f"may be used for {utl.pick_one(['replay attacks', 'SPAM', 'WAP attacks'])}"]),
            ('spam', 'sending unsolicited communication'),
            ('spim', 'using SMS services to get people to displose their data'),
            ('phishing', 'using emails to get people to displose their data'),
            ('spear phishing', 'targeting specific individuals with emails designed to get data'),
            ('whaling','targeting people in positions of respnonsibility with fake emails to get data'),
            ('vishing', 'using voice calls under false pretences to get users to disclose data'),
            ('pharming', 'malicious redirects of websites to fake sites in order to conduct Phishing attacks'),
            ('DNS poisoning', ['falsifying domain name service data', 'can be used to redirect to malicious sites']),
            ('ARP posoning', ['falsify IP-mac resolution', 'ommonly used in active sniffing attacks and matn in the middle attacks']),
            ('insider', f"can be protected against by {utl.pick_one(['policies', 'auditing', 'background checks', 'prhibiting external devices', 'application whitelisting'])}"),
            ('password', [f"can be protected against using {utl.pick_one(['longer', 'complex', 'regularly updated'])}",'passwords','brute force', 'dictionary attack', 'birthday attack', 'rainbow attack'] ),
            ('transitive access', 'sharing data with someone on the basis that they are trusted by someone you trust' ),
            (['url hacking','typo squatting'], 'using commonly misspelt urls to lure people onto a malicious site'),
            ('social engineering', ['exploiting human nature', f"using {utl.pick_one(['authority', 'intimidation', 'scarcity', 'urgency', 'familiarity', 'trust', 'flattery'])} to gain access or information"]),
            ('watering hole attack', 'observing users\' behaviour to lure them to a malicious site'),
        ),
        'fillers': (
        )
    },
    'types of DoS attack': {
        'question_with_0':'What best describes a PLACEHOLDER attack?',
        'question_with_1':'What type of attack PLACEHOLDER?',
        'type':'pairs',
        'course_code':'6',
        'pairs':(
            ('Smurf','uses ping packets agains the broadcast address so the replies return to the victim'),
            ('fraggle','uses UDP packets so the ICMP reply returns to the victum'),
            ('land ',['sends packets to a victim containing identical source and destination addresses','causes a victim to become stuck in a loop sending packets to themself']),
            ('ping of death',['sends large packets to a victim', 'sends packets too large for a victim to handle']), 
            ('syn flood',['sends TCP packets to a victim', 'exploits the three way handshake'])
        ),
        'fillers': (
        )
    },

    'types of password attacks': {
        'question_with_0':'What best describes a PLACEHOLDER?',
        'question_with_1':'What type of attack involves PLACEHOLDER?',
        'type':'pairs',
        'course_code':'6',
        'pairs':(
            (['brute force'],'attempting all valid combinations'),
            ('rainbow','using large pre-calculated databased of hashes to crack captured password hashes'),
            ('dictionary','attempts to break passwords based on a dictionary or list of words'),
            ('birthday attack','based on probability theory'), 
        ),
        'fillers': (
        )
    },
    
    'types of password attacks': {
        'question_with_0':'Which of the following is a PLACHOLDER exploit?',
        'question_with_1':'What type of exploit is PLACEHOLDER?',
        'type':'pairs',
        'course_code':'6',
        'pairs':(
            ('DNS','rogue DNS server'),
            ('rainbow','using large pre-calculated databased of hashes to crack captured password hashes'),
            ('dictionary','attempts to break passwords based on a dictionary or list of words'),
            ('birthday attack','based on probability theory'), 
        ),
        'fillers': (
        )
    },
    'types of password attacks': {
        'question_with_0':'Which of the following is a PLACHOLDER exploit?',
        'question_with_1':'What type of exploit is PLACEHOLDER?',
        'type':'pairs',
        'course_code':'6',
        'pairs':(
            ('DNS','rogue DNS server'),
            ('rainbow','using large pre-calculated databased of hashes to crack captured password hashes'),
            ('dictionary','attempts to break passwords based on a dictionary or list of words'),
            ('birthday attack','based on probability theory'), 
        ),
        'fillers': (
        )
    },
    'types of network design elements': {
        'question_with_0':'Which of the following describes PLACHOLDER?',
        'question_with_1':'Which design element is a PLACEHOLDER?',
        'type':'pairs',
        'course_code':'6',
        'pairs':(
            (['a VLAN', 'virtualisation', 'a virtual network'],['segmenting switch ports on managed devices (layer 2) and allocating to diferent networks','allows to networks to remain seperate from each other whilst sharing other access to resources','traffic between each department is controlled through the switch and router']),
            (['a DMZ', 'a transitional subnet'],['acts as a buffer network between the internet and a private LAN', 'implemented between 2 firewalls', 'implemented between a multi honed device']),
            (['Honeypot','Honeynet'],['used to monitor intrusion and conduct intelligence gathering', 'used to deflect potential attacks', 'located in the DMZ', 'located in a transitional subnet']),
            (['IDS', 'intrusion detection system'], ['passive devices which detect malicious traffic', 'passive devices', 'can be host based to monitor local activity']),
            ('load balancers', ['provide fault tolerance', 'provide redundancy', 'support web servers', 'support remote desktop servers','support FTP servers','support VPN servers']),
            (['network address translation','NAT'], ['converts internal IP addresses into public', 'masquerades internal addressing systems from public viewing', 'serves as a basic firewall']),
            (['port address translation','PAT'], ['connect single internal IP addresses to internal port numbers']),
            (['network address translation transversal','NAT-T'], ['supports IPSEC', 'supports other tunnelling VPN protocols','allow IPv4-6 networks to used NAT in interim between becoming mainstream']),
            (['proxy servers'], ['caching NAT service', 'can filter activity based on content', 'can filter activity based on URL','can filter activity based on keywords']),
            (['remote access servers', 'RAS'], 'support VPN/Terminal Service connections'),
            (['NAC', 'network access control'],['examines the connecting device', 'reduces day zero attacks', 'enforces network security policies','device or software which can perform firewall, antivirus, updates and identity functions'])
        ),
        'fillers': (
        )
    },
    'types of IDS': {
        'question_with_0':'Which of the following describes PLACHOLDER?',
        'question_with_1':'Which design element is a PLACEHOLDER?',
        'type':'pairs',
        'course_code':'6',
        'pairs':(
            ('signature based IDS','has a database of signatures of known malicious traffic'),
            ('anomaly based IDS',['can be trained to know what is normal traffic', 'raises an alert when diferent traffic patterns are seen']),
            ('behaviour based IDS','reacts to activity above or below baseline activity'),
            ('heuristics', 'the ability to make an educated guess as to whether traffic is malicious or not'),
        ),
        'fillers': (
        )
    },
        
    'cloud computing types': {
        'question_with_0':'Which of the following describes PLACEHOLDER cloud use?',
        'question_with_1':'Which operational control is PLACEHOLDER?',
        'type':'pairs',
        'course_code':'5',
        'pairs':(
            ('public', ['on-demand computing services and infrastructure are managed by a third-party provider and shared with multiple organizations', 'on-demand computing services and infrastructure using the public Internet']),
            ('private', ['a cloud computing environment in which all hardware and software resources are dedicated exclusively to, and accessible only by, a single customer']),
            ('community', ['used and paid for a group of users','used by a group of users for shared benefit','suitabile for data exchange']),
            ('hybrid', ['combination of cloud and on-site infrastructure']),
        ),
        'fillers': (           
        )
   
    },
    
    'cloud computing services': {
        'question_with_0':'Which of the following describes PLACEHOLDER?',
        'question_with_1':'Which is the term given used to describe providing PLACEHOLDER?',
        'type':'pairs',
        'course_code':'10',
        'pairs':(
            ('sofware as a service', 'software is accessed online via a subscription','software does not need to be bought and installed on individual computers'),
            ('platform as a service', ['provision of an environment in which to develop code', 'provision of a computing environment and some applications']),
            ('storage as a service', ['providing storage on a rental basis by a provider']),
            ('security as a service', ['providing security on a subscription model']),
            ('monitoring as a service', ['providing monitoring on a subscription model']),
            ('infrastructure as a service', ['a cloud computing service that offers essential compute, storage and networking resources on demand']),
        ),
        'fillers': (
            (['network as a service', 'prevention as a service', 'elasticity as a service', 'scalability as a service'], [
                'purchasing software to download and install locally',
                'buying computers with a pre-installed development platform',
                'installing custom-made architecture on site',
                'training staff to provide local security',
                'purchasing monitoring software and hardware and training staff to use them',
                f"{utl.pick_one(['software', 'security', 'platform', 'storage', 'monitoring', 'infrastructure'])} in the cloud",
                f"{utl.pick_one(['software', 'security', 'platform', 'storage', 'monitoring', 'infrastructure'])} as a package"]
                ),
            
        )
    },
    'cloud computing services': {
        'question_with_0':'Which of the following describes PLACEHOLDER?',
        'question_with_1':'Which is the term given used to describe providing PLACEHOLDER?',
        'type':'pairs',
        'course_code':'10',
        'pairs':(
            ('sofware as a service', 'software is accessed online via a subscription','software does not need to be bought and installed on individual computers'),
            ('platform as a service', ['provision of an environment in which to develop code', 'provision of a computing environment and some applications']),
            ('storage as a service', ['providing storage on a rental basis by a provider']),
            ('security as a service', ['providing security on a subscription model']),
            ('monitoring as a service', ['providing monitoring on a subscription model']),
            ('infrastructure as a service', ['a cloud computing service that offers essential compute, storage and networking resources on demand']),
        ),
        'fillers': (
            (['network as a service', 'prevention as a service', 'elasticity as a service', 'scalability as a service'], [
                'purchasing software to download and install locally',
                'buying computers with a pre-installed development platform',
                'installing custom-made architecture on site',
                'training staff to provide local security',
                'purchasing monitoring software and hardware and training staff to use them',
                f"{utl.pick_one(['software', 'security', 'platform', 'storage', 'monitoring', 'infrastructure'])} in the cloud",
                f"{utl.pick_one(['software', 'security', 'platform', 'storage', 'monitoring', 'infrastructure'])} as a package"]
                ),
            
        )
    },
    'cloud computing services': {
        'question_with_0':'If an email message is PLACEHOLDER, this can be described as?',
        'question_with_1':'What does it mean if an email message is PLACEHOLDER?',
        'type':'pairs',
        'course_code':'6',
        'pairs':(
            ('masquerading', 'not from the person it claims to be from'),
            ('phishing', 'trying to extract information from non targeted recipients'),
            ('spear phishing', 'extracting information from a specific recipient'),
            ('whaling', 'attempting to get information from a high value target'),
        ),
        'fillers': ()
    },
}

"""


ESP



how is data stores for GDPR
where is data stored
responsibilities 
availability
data retention and destruction
backups/replication
auditing
exit strategy


CSA

cloud control matric and caiq
"""


"""
seperation of systems
physical seperation of systems - 
logical seperation of systems, virtualisation
firewalls
DMZ area of known trust
intrusion detection system
intrusion prevention system
load balancer proxies
noneypots
honeynets
load balancer
proxies

security layers
data - checksums
application - malware detection
host - 
internal - 
perimeter
physical - doors, fences
awareness
proceedures
policies

seperation may take many forms and may be incorporated:
to gement a secure compartment facility (standalone or controlled access)
zone specific security areas
to zone vulnerable areas from the internal network
to control network traffic between departments

DNS
exploits

Rogue DNS server
SND poisoning
IP configuration corruption
proxy corruption

shoulder surfing - looking over someone's shoulder
dumpster diving
hoax emails
impersonation

rogue access points
evil twin same ssid
interference - jamming with noise
war driving using monitoring software to look for the presence of wireless networks
war chalking
bluejacking
bluesnarfing

wireless attacks
xss/cross site scripting - exploits trust a browser has with the web server
may result in identity data theft
financial loss
key logging

sql injection
use unexpected input to gain unauthorised access
exploits vulnerabilities  between front and back end

protects against sql injection with 
input validation
limit account privileges

LDAP atacks directory services rather than SQL
directory traversal - tryig to get beyond web contect an dgain other parts of file system
buffer overflow
header manipulation - modify headers submitted to a web server to manipulate cookies

application attacjs

forms tampering - chaning hidden values
url tampering -chaning the paths in urls to gain access to unaun
cookie tampering - stealing or modifying cookies to gain session tokens to provide access

telephone systems WAR dialing

mitigation 

SCADA
supervisory control and data acquisition system
industrial control system

used for large scale DoS
state espionage
terrorism

mitigateion
segregation of business and real time networks
segregation from the internet
restricted access
VPN/remote access

CCTV feeds
cctv systems are extensively used in the security of industrial , government and domestic environments
unnauthorised access

risks from instant messaging



    'types of spoofing attacks': {
        'question_with_0':'What best describes a PLACEHOLDER?',
        'question_with_1':'What type of malware PLACEHOLDER?',
        'type':'pairs',
        'course_code':'6',
        'pairs':(
            (['DoS', 'DDoS'],'using packets agains the broadcast address so the replies return to the victim'),
            ('SPAM','UDP packets used so the ICMP reply returns to the victum'),
            ('WAP attack',[]),
            
        ),
        'fillers': (
        )
    },



countermeasures to web-activity hacking
user training
acceptable use policy
access controlls
authentication
enmcryption
pen testing


malware countermeasures
user training and awareness
content scanning
checking software
firewall
sheep dip software
networ intrusion detection systenms / intrusion prevention system (NIDS/NIPS)


what is checking software vs sheep dip


system logs

event logs - on an ms system these cover all aspects of the systems but the most important logs are
security logs
system lohs
application log
access logs

audit logs - log user/machine activity such as logons, object access and special privilege actions

SIEM vs UTM
SIEM is a detective control
unified thread managements is a control but also 


hardenning is conducted at OS, system, network and application level

all systems should have unnecessary systems removed


a security posture is the level at which an organisation canwithstand an attack
baselines should be taken of all it systems after hardeiung
continues  monitoring always on

assessment tools

pair

protocol analyser/sniffer - wireshark
vulnerability scanners - nessus
ids/honeypots/honeynets
port scanners

VIPD is identifying vulnerabilities
pen-testing is exploiting vulnerabilities

wireshark, nesus, nmap, snort
zenmap is a gui version

when carrying out security assessments it is important to consider the following
baseline - current implemtnation
code reviews - glaws in program code
physical architecture - physical security
attack surface - visible to outside workd
deisgn reviews - of secuiry implemtnatin

When carrying out security testing, PLACEHOLDER is considered. What is the meaning of PLACEHOLDER in this context?
What is the word used to describe

types of testing
black box testing - no knowledge external and internal testing
grey box testing - partial knowledge of the target, login and password for one user, 
white box testing - full knowledge, network diagram, full access

what type of penetration testing would give you the best idea of your security posture?
black box

"""



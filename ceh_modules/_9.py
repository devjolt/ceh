from random import randint
from cismp.utilities import utilities as utl
from ._9_logic import *

questions = {
    
    'operational controls': {
        'question_with_0':'Which of the following is an operational control related to PLACEHOLDER?',
        'question_with_1':'Which operational control is PLACEHOLDER?',
        'type':'pairs',
        'course_code':'5',
        'pairs':(
            ('digial forensics', [' preserving data for use in court', 'applied to data breaches and malware']),
            ('cryptography', ['allowing data to be transfered securely', 'involves encryption of a message using a key into ciphertext', 'using a decryption key to convert a message into plain text']),
            ('threat intelligence', ['ensuring that unauthorised people don\'t have access',f"preventing mechanical harm from happening to {utl.pick_one(['people','assets','data'])}", 'securing devices to a desk', 'locking windows', 'preventing shoulder surfing', 'being aware of tailgating', 'keeping desks clear', 'locking secure areas', 'securely disposing of waste', 'having a clean desk policy','deactivating lost devices']),
        ),
        'fillers': (
            ('network', ['never using a device', 'working from home to not catch covid']),
        )
    },
    

    'cryptography correct incorrect': {
        'question':'Regarding cryptography, which of the following is PLACEHOLDER?',
        'type':'correct incorrect',
        'positive':'correct',
        'negative':'incorrect',
        'course_code':'',
        'correct':(
            'symmetric key systems are faster and simpler',
            'the primary goal of cryptography is confidentiality',
            'crypto systems can verify integrity',
            'encryption is the process that changes the data to make it unreadable',
            'decryption is the process that changes the data to make it readable',
            'cipher is the algorithm that produces the encryption',
            'key is used to determine the encryption process is the process that changes the data to make it readable',
        ),
        'incorrect': (
            'the primary goal of cryptography is availability',
            'the primary goal of cryptography is integrity',
            'the primary goal of cryptography is safety',
            'hash functions are used to encrypt',
            'decryption is the process that changes the data to make it unreadable',
            'encryption is the process that changes the data to make it readable',
            'key is the algorithm that produces the encryption',
            'cipher is used to determine the encryption process is the process that changes the data to make it readable',
        ),
    },
    'cryptography pairs': {
        'question_with_0':'Which of the following describes PLACEHOLDER?',
        'question_with_1':'Which of the following is PLACEHOLDER?',
        'type':'pairs',
        'course_code':'5',
        'pairs':(
            ('cipher', ['the algorithm that produces the encryption']),
            ('cryptography', ['allows data to be transfered securely', 'involves encryption of a message using a key into ciphertext', 'using a decryption key to convert a message into plain text']),
            ('key', ['used to determine the encryption process is the process that changes the data to make it readable']),
            ('encryption', ['the process that changes the data to make it unreadable']),
            ('decryption', ['the process that changes the data to make it readable']),
            ('hashing', ['the process of producing a summary of data in the form of a fixed length digest']),
            ('symmetric encryption', ['uses a single shared key for encryption and decryption']),
            ('asymmtric encryption', ['uses a public and private key', 'enables non-repudiation']),
            ('block cipher', ['encrypts a block of data']),
            ('stream cipher', 'encrypts each character'),
            ('steganography', ['the concept of hiding data in plain sight'])

        ),
        'fillers': (
        )
    },
    'assymetric entription algorithms': {
        'question_with_0':'Which of the following describes PLACEHOLDER?',
        'question_with_1':'Which of the following PLACEHOLDER?',
        'type':'pairs',
        'course_code':'5',
        'pairs':(
            (['RSA', 'Rivest, Shamir and Adleman'], 'currently most widely used accross most systems'),
            (['Elliptic Curve Cryptography', 'ECC'], 'provides longer key legth and uses less compute power'),
            ('El Gamal', 'doubles size of encrypted messages'),
            ('Diffie-Hellman', ['uses series of one-way functions and non-shared secrets to generate shared symmetric key']),
        ),
        'fillers': (
        )
    },
    'transport encryption': {
        'question_with_0':'Which of the following describes PLACEHOLDER?',
        'question_with_1':'Which of the following is PLACEHOLDER?',
        'type':'pairs',
        'course_code':'5',
        'pairs':(
            ('VPN', ['technology that encrypts your internet traffic on unsecured networks','hides your IP address', 'can use point to point tunnelling protocol', 'can use IPSec']),
            (['SSL', 'TLS'], 'cryptographic protocol designed to provide communications security over a computer network'),
            ('SSH', ' secure remote login to a terminal'),
            (['PGP', 'pretty good privacy','secure multipurpose mail extensions','S/MIME'], 'secure email encryption with digital signatures'),

        ),
        'fillers': (
        )
    },
    'authentication methods': {
        'question_with_0':'Which of the following describes PLACEHOLDER?',
        'question_with_1':'Which of the following PLACEHOLDER?',
        'type':'pairs',
        'course_code':'5',
        'pairs':(
            ('PAP', 'sends passwords in plaintext'),
            ('SPAP', 'is acryptographic protocol designed to provide communications security over a computer network'),
            (['EAP','is extensible authentication protocol'],'is used by smartcards'),
            ('CHAP', 'is challenge handshake protocol'),

        ),
        'fillers': (
        )
    },

    'terms': {
        'question_with_0':'Which of the following describes PLACEHOLDER?',
        'question_with_1':'Which of the following is PLACEHOLDER?',
        'type':'pairs',
        'course_code':'5',
        'pairs':(
            (['AH','authentication header'],'provides message integrity, non rep, authentication and access control'),
            ('ESP',['encapsulation security payload','provides condientiality and integity of contents through encryption']),
            ('transport mode','only payload is encrypted (usually for internal)'),
            ('tunnel mode','entire packet, header inc, is encrypted for external or VPC communications'),
            ('SSL',['used to privide a secure connection for a client servier traffic over the internet', 'uses encrypted session over port 443']),
            ('SSH',['secure connection that provides end to end encryption', 'replaces insecure telnet']),
        ),
        'fillers': (
        )
    },
    'hashing algorithms': {
        'question_with_0':'Which of the following describes PLACEHOLDER?',
        'question_with_1':'Which of the following is PLACEHOLDER?',
        'type':'pairs',
        'course_code':'5',
        'pairs':(
            (['RSA', 'Rivest, Shamir and Adleman'], 'currently most widely used accross most systems'),
            (['Elliptic Curve Cryptography', 'ECC'], 'provides longer key legth and uses less compute power'),
            ('El Gamal', 'doubles size of encrypted messages'),
            ('Diffie-Hellman', ['uses series of one-way functions and non-shared secrets to generate shared symmetric key']),
        ),
        'fillers': (
        )
    },

    
    'threat intelligence': {
        'question':'Regarding threat intelligence, which of the following is PLACEHOLDER?',
        'type':'correct incorrect',
        'positive':'correct',
        'negative':'incorrect',
        'course_code':'',
        'correct':(
            'involves understanding what an adversary can do',
            'increases efficiency of security operations',
            'should be timely, relevant and actionable',
            'it is important to have a global reach',
            'it should be able to integrate with existing tools',
            
        ),
        'incorrect': (
            'involves understanding your own capabilities',
            'increases efficiency of security operations',
            'should be timely, relevant and actionable',
            'it is important to have a global reach',
            'it should be able to integrate with existing tools',
           
        ),
    },
    'cryptography correct incorrect': {
        'question':'Regarding hashes, which of the following is PLACEHOLDER correct?',
        'type':'correct incorrect',
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            'defined as something calculated from a set of numbers or bit strings',
            'input can be of any length',
            'output is always a fixed length',
            'a fixed block of data will always return the same value',
            'one character in a block will change the hash',
            'cannot be reversed',
            'functions are relatively simple to compute',
            'hashes should be collision free',
            'password cracking relies on trying to crack the stored hash of the plain text password',
            'hashes are cracked by birthday attacks',
            'hashes are cracked by dictionary attacks',
            'hashes are cracked by rainbow table',
            'hashes are cracked by brute force attacks'
        ),
        'incorrect': (
            'an encryption technique',
            'a type of malicious software',
            'input is always a fixed length',
            'output can be of any length',
            'any two blocks from the same document will always return the same ',
            'one character in a block will not change the hash',
            'can be reversed',
            'functions are relatively complex to compute',
            'hashes rely on collisions to function',
            'hashes are cracked by Christmas attacks',
            'hashes are cracked by Easter attacks',
            'hashes are cracked by anniversary attacks',
            'hashes are cracked by monochrome tables',
            'hashes are cracked by raw strength attacks',
            'hashes are cracked by soft touch attacks',
        )
    },
    'key escrow': {
        'question':'Regarding key escrow, which of the following is PLACEHOLDER correct?',
        'type':'correct incorrect',
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            'copies of private keys are retained by centralised management systems',
            'copies of private keys are retained by third parties',
            'allows key recovery',
            'a key recovery agent is able to recover an accounts private key',
            'a data recovery agent is able to recover an accounts encryption key',
        ),
        'incorrect': (
            'copies of public keys are retained by centralised management systems',
            'copies of public  keys are retained by third parties',
            'allows key generation only',
            'a key recovery agent is able to recover an accounts public key',
            'a data recovery agent is able to recover an accounts username and password',
            'copies of private keys are retained securely by the holder',
            'copies of private keys are retained in a safe place',
        )
    },
    'PKI': {
        'question':'Regarding PKI, which of the following is PLACEHOLDER correct?',
        'type':'correct incorrect',
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            'PKI is the framework for deploying asymmeric cryptograhy systems',
            'uses digital certificates as a means of authenticating public keys',
            'uses digital certificates as a means of distributing public keys',
            'certificates are issed by certificate authorities which are trusted third parties',
            'allows two users with certificates to trust each other',
            'basis of e-commerce',
            'heirarchical model',
            'bridge model',
            'certificates can be revoked if it is compromised',
            'certificates can be revoked if it is expired',
            'certificates can be revoked if it is no longer valid',
            'certificates can be revoked if it is updated',
            'revoked certificates are made public',
            'revoked certificates are placed on CRL',
            'OCSP allows direct query based on the reciept of a certificate'
            'OCSP is quicker than CRL'
        ),
        'incorrect': (
            'PKI is the framework for deploying symmeric cryptograhy systems',
            'uses digital certificates as a means of authenticating private keys',
            'uses digital certificates as a means of distributing private keys',
            'certificates are self generated using trusted hashes',
            'certificates are self generated using trusted algorithms'
            'allows two users with matching certificates to trust each other',
            'ecommerce sites to save your passwords for easier use',
            'certificates are valid until voluntarily ended',
            'certificates are revoked randomly',
            'certificates renewed by using a CRL',
            'OCSP allows renewal of a certificate'
            'CRL is quicker than OCSP'
        )
    },
    'ca_certificates':ca_certificates,

}


"""
'digital forensics': {
        'question':'Regarding digital forensics, which of the following is PLACEHOLDER?',
        'type':'correct incorrect',
        'positive':'correct',
        'negative':'incorrect',
        'course_code':'',
        'correct':(
            'applied to data breaches, malware',
            'involves preserving data for use in court',
            'digital evidence is recognised much more in court',
            'a forensic science encompassing the recovery and preservation of evidence from digital devices',
        
        ),
        'incorrect': (
            
        ),
    },

"""
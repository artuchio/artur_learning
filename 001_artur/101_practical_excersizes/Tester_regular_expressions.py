import re
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa HaHaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( ) #vse eti simvali nuznhno iskat s pomoshju \
example.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Jones
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
abc
example*com
exampledcom
example.company
ball mall hall wall tall
'''

sentence = 'Start a sentence and then bring it to an end '
emails = '''
SampleMaiL@example.com
john.sample@my-work.net
jack-125-production@colledge.edu
bob.Samples@example.co.uk
example@example.org
'''

urls = '''
https://www.google.com
http://www.wordpress.org
https://www.nasa.gov
https://example.net
www.example.net
example.net
'''
# print('\tab') 	#ab
# print(r'\tab') #\tab
# pattern = re.compile(r'examplecom') #s pomoshju escapa zakryvaetsa metacharackters
# pattern = re.compile(r'\s')
# pattern = re.compile(r'\S')
# pattern = re.compile(r'\BHa')
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
pattern = re.compile(r'')
matches = pattern.finditer(emails)
# print(matches)
for match in matches:
    print(match)
    # print(match.start(), match.end(), match.span(), match.group())
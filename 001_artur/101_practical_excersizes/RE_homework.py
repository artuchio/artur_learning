import re

# text = "#123ABC #DEF123 #12G456 #FFFFFF #008000 #0000FF"
#
# hex_compile = re.compile(r'#[0-9a-fA-A]{6}')
# matches = re.finditer(hex_compile, text)
#
# for match in matches:
#     print("Found:", match)


# text = "21*9+6*5 (3+5)-9*4 7+1"
# #
# plus_number = re.compile(r'\d(?![+])') # Regular expression pattern to match digits not followed by a plus sign
# # plus_number = re.compile(r'\d(?!\+)'
# matches = re.findall(plus_number, text)
# #
# for match in matches:
#     print("Found:", match)

# text = "Завтрак в 10:00, обед в 13:30, учеба в 18:00, некорректное время 97:98"
#
# pattern = r'\b(?:[01]\d|2[0-3]):[0-5]\d\b' # Regular expression pattern to match valid times in "hh:mm" format
# matches = re.findall(pattern, text)
# for match in matches:
#     print("Found valid time:", match)




# name_pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b' # Define a regular expression pattern for names
# address_pattern = r'\d{3} [A-Z][a-z] [S][t]+, [A-Z]+ [A-Z]{2} \d{5}'
#
# with open("people.txt", "r") as file:
#     text = file.read()
#
# names = re.findall(name_pattern, text)
# addresses = re.findall(address_pattern, text)
#
# # name_count = len(names)
# addresses_count = len(addresses)

# print("Names:")
#
# for name in names:
#     print(name)

# for address in addresses:
#     print(address)
#
# print("Addresses:")
#
# for address in addresses:
#     print(address)
# print("\nFound:", addresses_count)

name_pattern = re.compile(r'[A-Za-z-]+ [A-Z-a-z-]+)\n')
address_pattern = re.compile(r'\d{3} [A-Za-z-9-]+ St.\., [A-Za-z-\']+ [A-Z]{2} \d{5}')

with open("people.txt", "r") as file:
    data = file.read()


people_matches = re.findall(name_pattern, data)
people_matches = list(people_matches)
print(len(people_matches))
address_matches = re.findall(name_pattern, data)

for address in address_matches:
    print(address)

idcode + re.compile(r'[1-8]\d\d(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])\d{4}')
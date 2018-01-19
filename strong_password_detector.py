# Strong Password Detection (using Regex)
# Automate The Boring Stuff Ch.7
# Oscar Padilla

import re

print("Enter password to test: ")
password = input()

# Regex object of at least 8 characters
len_regex = re.compile(r'''
    [a-zA-Z0-9._%+-]{8,}
''', re.VERBOSE)

# Regex object of at least 1 lowercase character
lower_regex = re.compile(r'''(
    [a-z]+
)''', re.VERBOSE)

# Regex object of at least 1 uppercase character
upper_regex = re.compile(r'''
    [A-Z]+
''', re.VERBOSE)

# Regex object of at least 1 digit
digit_regex = re.compile(r'''
    [0-9]+
''', re.VERBOSE)


def check(word):
    if word == []:
        print("Password is WEAK.")
        exit()

pw = len_regex.findall(password)
check(pw)
pw = lower_regex.findall(password)
check(pw)
pw = upper_regex.findall(password)
check(pw)
pw = digit_regex.findall(password)
check(pw)

print("Password is STRONG.")

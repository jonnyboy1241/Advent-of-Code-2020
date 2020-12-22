'''
--- Part Two ---
The line is moving more quickly now, but you overhear airport security talking about how passports with invalid data are getting through. Better add some data validation, quick!

You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:

byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.

Your job is to count the passports where all required fields are both present and valid according to the above rules. Here are some example values:

byr valid:   2002
byr invalid: 2003

hgt valid:   60in
hgt valid:   190cm
hgt invalid: 190in
hgt invalid: 190

hcl valid:   #123abc
hcl invalid: #123abz
hcl invalid: 123abc

ecl valid:   brn
ecl invalid: wat

pid valid:   000000001
pid invalid: 0123456789
Here are some invalid passports:

eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
Here are some valid passports:

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719

Count the number of valid passports - those that have all required fields and valid values. Continue to treat cid as optional. In your batch file, how many passports are valid?
'''

import re

passports = []
current_passport = {}

with open('data/day4.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            passports.append(current_passport)
            break

        line = line.strip('\n')

        if line == '':
            passports.append(current_passport)
            current_passport = {}
        else:
            fields = line.split()

            for field in fields:
                [key, val] = field.split(':')
                current_passport[key] = val

def val_byr(value):
    try:
        value_int = int(value)
        return 1920 <= value_int and value_int <= 2002
    except ValueError:
        return False

def val_iyr(value):
    try:
        value_int = int(value)
        return 2010 <= value_int and value_int <= 2020
    except ValueError:
        return False

def val_eyr(value):
    try:
        value_int = int(value)
        return 2020 <= value_int and value_int <= 2030
    except ValueError:
        return False

def val_hgt(value):
    unit = value[-2:]
    val = value[:-2]

    try:
        val_int = int(val)

        if unit == 'in':
            return 59 <= val_int and val_int <= 76

        elif unit == 'cm':
            return 150 <= val_int and val_int <= 193
        
        return False
    
    except ValueError:
        return False

def val_hcl(value):
    pattern = re.compile('[#][0-9a-f]{6}')
    return pattern.fullmatch(value) != None

def val_ecl(value):
    pattern = re.compile('amb|blu|brn|gry|grn|hzl|oth')
    return pattern.fullmatch(value) != None

def val_pid(value):
    pattern = re.compile('[0-9]{9}')
    return pattern.fullmatch(value) != None

num_valid_passports = 0
for passport in passports:
    length = len(passport)

    if not (length == 7 or length == 8):
        continue

    keys = passport.keys()

    if 'byr' in keys and 'iyr' in keys and 'eyr' in keys and 'hgt' in keys and 'hcl' in keys and 'ecl' in keys and 'pid' in keys:
        if val_byr(passport['byr']) and val_iyr(passport['iyr']) and val_eyr(passport['eyr']) and val_hgt(passport['hgt']) and val_hcl(passport['hcl']) and val_ecl(passport['ecl']) and val_pid(passport['pid']):
            if len(keys) == 7:
                num_valid_passports += 1
            
            elif 'cid' in keys and len(keys) == 8:
                num_valid_passports += 1

print(num_valid_passports)
    
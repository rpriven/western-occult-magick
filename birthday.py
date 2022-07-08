# Numerology
# Core Traits

#############
# Functions #
#############

# Reduces down to one digit or notifies of master number
def reduce(n):
    if n == 11 or n == 22 or n == 33:
        master = n
        print('Master number found in Birthday!:', master)
        return master
    total = sum(int(digit) for digit in str(n))
    if total < 10:
        return total
    else:
        return reduce(total)

# Changes characters in name to digits and reduces or notifies of master number
def name_num(name):
    x = 0
    total = 0   # total
    r = 0       # reduced
    for chars in name:
        x = ord(chars) - 96
        if x >= 10:
            r = sum(int(digit) for digit in str(x))
            total = total + r
            # print('total, r',total, r)
        else:
            total = total + x
            # print('total, x',total, x)
    return total

# Checks for master number, then reduces further as necessary
def master_check(total):
    r = 0
    if total == 11 or total == 22 or total == 33 or total == 44 or total == 55:
        master = total
        print('Master found! Congtratulations, your name has a Master Number of', master)
        return master
    if total >= 10:
        r = sum(int(digit) for digit in str(total))
        total = r
        if total == 11 or total == 22 or total == 33 or total == 44 or total == 55:
            master = total
            print('Master found! Congtratulations, your name has a Master Number of', master)
            return master
        elif total >= 10:
            r = sum(int(digit) for digit in str(total))
            return r
        return total    # previously r
    else: 
        return total

###########
## Input ##
###########

# Asks for the person's full name
name_raw = input("Please enter the person's Full Name: \n")

# Makes sure something was entered
while not name_raw:
    print('Error:  Name cannot be blank.')
    name_raw = input("Please enter the person's Full Name: \n")

# Makes sure letters were entered and not numbers
while name_raw.isnumeric():
    print('Error:  Please enter your name, not numbers.')
    name_raw = input("Please enter the person's Full Name:  \n")

# [Removes any spaces and] makes the name lowercase
name = name_raw.lower() # .replace(' ','')

# Asks user for their birthdate
birth_raw = input('What is your full Date of Birth? (mm/dd/yyyy) [eg. 5/13/1982]  \n')

# Makes sure something was entered
while not birth_raw:
    print('Error:  Birth date cannot be blank.')
    birth_raw = input('What is your full Date of Birth? (mm/dd/yyyy) [eg. 5/13/1982]  \n')

##################
## Calculations ##
##################

#--------------#
#+# Birthday #+#
#--------------#

# Splits birthday into pieces [month, day, year]
pieces = birth_raw.split('/')
print(pieces)
month = int(pieces[0])      # month = reduce(int(pieces[0])) ??  Will this work?
day = int(pieces[1])
year = int(pieces[2])

print('reduce:')

birth_date = month + day + year
birth_date = reduce(birth_date)
print('Before:',birth_date)

birth_date = reduce(month) + reduce(day) + reduce(year)
birth_date = reduce(birth_date)
print('After:',birth_date)

# Life Path
life_path = birth_date
# Birthday
birthday = reduce(day)

#----------#
#+# Name #+#
#----------#

name_split = name.split(' ')

# Figure out how many names are in the name
if len(name_split) < 2:
    print('Error:  More information needed.  Please use at least your First and Last name.')
    name_raw = input("Please enter the person's Full Name [First, Middle, Last]: \n")

if len(name_split) == 2:
    # print('Before Master Check')
    first = name_num(name_split[0])
    # print(first)
    last = name_num(name_split[1])
    # print(last)
    # print('2 names:', first, last)

    # Master Check
    first = master_check(first)
    last = master_check(last)
    # print('After Master Check')
    # print('2 names:', first, last)

    # Rejoin and Add
    rejoined_name = first + last
    # print('Rejoined name:',rejoined_name)
    added_name = reduce(rejoined_name)
    # print('Added name:', added_name)

if len(name_split) == 3:
    # print('Before Master Check')
    first = name_num(name_split[0])
    # print(first)
    middle = name_num(name_split[1])
    # print(middle)
    last = name_num(name_split[2])
    # print(last)
    # print('3 names:', first, middle, last)

    # Master Check
    first = master_check(first)
    middle = master_check(middle)
    last = master_check(last)
    # print('After Master Check')
    # print('3 names:', first, middle, last)

    # Rejoin and Add
    rejoined_name = first + middle + last
    # print('Rejoined name:',rejoined_name)
    added_name = reduce(rejoined_name)
    # print('Added name:', added_name)

if len(name_split) == 4:
    # print('Before Master Check')
    first = name_num(name_split[0])
    middle = name_num(name_split[1])
    middle2 = name_num(name_split[2])
    last = name_num(name_split[3])
    # print('4 names:', first, middle, middle2, last)

    # Master Check
    first = master_check(first)
    middle = master_check(middle)
    middle2 = master_check(middle2)
    last = master_check(last)
    # print('After Master Check')
    # print('4 names:', first, middle, middle2, last)

    # Rejoin and Add
    rejoined_name = first + middle + middle2 + last
    # print('Rejoined name:',rejoined_name)
    added_name = reduce(rejoined_name)
    # print('Added name:', added_name)

if len(name_split) > 4:
    print('Error:  Too many names, please use up to four names [First, Middle, Middle, Last]')
    name_raw = input("Please enter the person's Full Name: \n")

# Soul's Urge
souls_urge = added_name

# Expression

#################
## Core Output ##
#################

print('\n[~-`*.] Core for', name_raw,'[.*`-~]\n')

# Core 1: Life Path (Birth Date)
print('1: Life Path:', life_path)

# Core 2: Soul's Urge (Name)
print("2: Soul's Urge:", souls_urge)

# Core 3: Expression (Vowels)

# Core 4: Birthday
print('4: Birthday:', birthday)

##################
## Explanations ##
##################

#----------------------#
#+# General Meanings #+#
#----------------------#



#-------------#
#+# Details #+#
#-------------#


#------------------------------------------------------------------#

######################
## No Longer Needed ##
######################

'''
# Rejoin names and reduce
# for n in name_split:
#     ''.join(name_split)
#     print(name_split)
'''

'''
### Works
# Splits name by spaces and dynamically creates a variable for each name
name_split = name_raw.split(' ')
x = 0
for i in name_split:
    globals()[f'name{x}'] = f'{i}'
    print(f'name{x}')
    x = x + 1

print('name0:', name0)
print('name1:', name1)
print('name2:', name2)

print(x)
'''

'''
def split_name(name):
    name_split = name.split(' ')
    x = 0
    for i in name_split:
        globals()[f'name{x}'] = f'{i}'
        print(f'name{x}')
        x = x + 1

split_name(name_raw)

print('name0:', name0)
print('name1:', name1)
print('name2:', name2)
'''

'''
# Dynamically create variables based on length of name
name_split = name_raw.split(' ')
print(name_split)
# name_range = len(name_split)
# print(name_range)

# for i in len(name_split):
#     globals()[f"name{i}"] = f"Hello from name {i}!"
#     print(f'name{i}')
'''


'''
# Splits name into pieces [first, middle, last]
name_split = name_raw.split(' ')
first = name_split[0]
middle = name_split[1]
last = name_split[2]



# Dynamically create variables based on length of name
def split_name(name):
    name_split = name.split(' ')
    x = 0
    for i in name_split:
        globals()[f'name{x}'] = f'{i}'
        print(f'name{x}')
        x = x + 1

split_name(name_raw)

'''

'''
# From other code
print('name_num:')

# full_name = first + middle + last
full_name = name_num(full_name)
print('Before:',full_name)

# full_name = name_num(first) + name_num(middle) + name_num(last)
full_name = name_num(full_name)
print('After:',full_name)

print('master_check:')

total = full_name
souls_urge = master_check(total)
'''

'''
# def master_check():
#     r = 0
#     if master_numbers in total:
#         master = total
#         return master
'''

'''
# Removes non-numerical characters and spaces
non_numbers = "!@#$%^&*()-_=+._/\|?' '`~,<.>;:'0"
for chars in non_numbers:
    birth_raw = birth_raw.replace(chars, "")
'''

'''
# Reduces / sums amount down to one digit or notifies of master number
def reduce(birth_raw):
    x = sum(int(digit) for digit in str(birth_raw))
    if birth_raw == 11 or birth_raw == 22 or birth_raw == 33:
        master = birth_raw
        print('Congratulations, you have a Master Number of',master,'!')
        return master
    if x < 10:
        return x
    else:
        return reduce(x)

birth_path = reduce(birth_raw)
print(f"Your Birth Path of {birth_path} means ...")
'''
# Numerology
# Core Personality

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

# Changes characters in name to digits and reduces
def name_num(name):
    x = 0       # character
    total = 0   # total
    r = 0       # reduced
    for chars in name:
        x = ord(chars) - 96
        if x >= 10:
            r = sum(int(digit) for digit in str(x))
            total = total + r
        else:
            total = total + x
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
        return total
    else: 
        return total

def pull_vowels(name):
    vowels = list()
    for letter in name:
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            vowels.append(letter)
    return vowels

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

name = name_raw.lower()
name_split = name.split(' ')

# Figure out how many subnames are in the name
if len(name_split) < 2:
    print('Error:  More information needed.  Please use at least your First and Last name.')
    name_raw = input("Please enter the person's Full Name [First, Middle, Last]: \n")

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

pieces = birth_raw.split('/')

month = reduce(int(pieces[0]))
day = reduce(int(pieces[1]))
year = reduce(int(pieces[2]))
birth_date = month + day + year

# Life Path
life_path = reduce(birth_date)

# Birthday
birthday = reduce(day)

#----------#
#+# Name #+#
#----------#

# Expression (Name)
subname_value = list()

# If name is longer than four subnames, only use first and last name
if len(name_split) > 4:
    subname_value.append(reduce(master_check(name_num(name_split[0]))))
    subname_value.append(reduce(master_check(name_num(name_split[-1]))))
else:
    subname_value.append(reduce(master_check(name_num(name_split[0]))))
    
    try:
        subname_value.append(reduce(master_check(name_num(name_split[1]))))
        subname_value.append(reduce(master_check(name_num(name_split[2]))))
        subname_value.append(reduce(master_check(name_num(name_split[3]))))
    except:
        pass

expression = master_check(reduce(sum(subname_value)))

# Soul Urge (Vowels)
subname_vowels = list()
subname_vowels.append(master_check(name_num(pull_vowels(name_split[0]))))

try:
    subname_vowels.append(master_check(name_num(pull_vowels(name_split[1]))))
    subname_vowels.append(master_check(name_num(pull_vowels(name_split[2]))))
    subname_vowels.append(master_check(name_num(pull_vowels(name_split[3]))))
except:
    pass

soul_urge = master_check(reduce(sum(subname_vowels)))

#################
## Core Output ##
#################

print('\n[~-`*.] Core for', name_raw,'[.*`-~]\n')
# Core 1: Life Path (Birth Date)
print('1: Life Path:', life_path)
# Core 2: Expression (Name)
print('2: Expression:', expression)
# Core 3: Soul Urge (Vowels)
print("3: Soul Urge:", soul_urge)
# Core 4: Birthday
print('4: Birthday:', birthday)

##################
## Explanations ##
##################

#----------------------#
#+# General Meanings #+#
#----------------------#

general = ('General Meanings:', '1: INDIVIDUATION, INDEPENDENCE, ATTAINMENT')
# if (life_path or expression or soul_urge or birthday) == 1:
print(general[0], general[1])

#-------------#
#+# Details #+#
#-------------#


#------------------------------------------------------------------#


######################
## No Longer Needed ##
######################


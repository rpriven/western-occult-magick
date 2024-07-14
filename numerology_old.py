# Numerology
# Core Personality

#############
# Functions #
#############


# Reduces down to one digit or notifies of master number
def reduce(n):
    master_nums = [11, 22, 33, 44, 55]
    if n in master_nums:
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
    master_nums = [11, 22, 33, 44, 55]
    r = 0
    if total in master_nums:
        master = total
        print('Master found! Congtratulations, your name has a Master Number of', master)
        return master
    if total >= 10:
        r = sum(int(digit) for digit in str(total))
        total = r
        if total in master_nums:
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

print('\nHere are the meanings for your numbers: \n')
general_title = ('General Meanings of', '1 - INDIVIDUATION, INDEPENDENCE, ATTAINMENT', '2 - RELATION, COOPERATION', '3 - EXPRESSION, JOY OF LIVING', '4 - LIMITATION, ORDER, SERVICE', '5 - CONSTRUCTIVE FREEDOM', '6 - BALANCE, RESPONSIBILITY, LOVE', '7 - ANALYSIS, UNDERSTANDING', '8 - MATERIAL SATISFACTION', '9 - SELFLESSNESS, HUMANITARIANISM', 'MASTER NUMBER 11 - ILLUMINATION', 'MASTER NUMBER 22 - MASTER BUILDER')
general = ('\n    ',
    'Number 1: A person must distinguish himself from other people and acknowledge his own INDIVIDUATION.  The individual has to develop the capability of standing on his own and going from dependence to INDEPENDENCE.  Once independent, the person becomes aware of his potential for ATTAINMENT as an individual – for creating and pioneering when working alone – to leading and managing as an individual working with others.', 
    'Number 2: Independence is important but has its limitations.  There are other people all about, and another lesson involves being a meaningful part of a group – a small group like family or friends, a larger group like a business or community.  The person must learn adaptability, service, consideration for others, i.e, the meaning of a RELATION with others, the idea of COOPERATION.', 
    'Number 3: A person must discover, both as an individual and as a group member, his capability of EXPRESSION: (1) artistic expression – writing, painting, sculpting, singing or any of the many other means of expressing inner thoughts and emotions, and (2) expression of feelings toward others – friendship, affection, love.  The JOY OF LIVING can be expressed with optimism and enthusiasm.  There can be a purity, even a naivete here.  (This is, perhaps, the most enjoyable lesson of all the numbers.)',
    'Number 4: Life doesn’t always present opportunities for singing and laughing.  Life doesn’t always appear expansive or yours for the taking.  Often, it feels just the opposite.  The individual must learn the difficult law of LIMITATION.  Everyone has limitations – limitations presented by the environment, by the physical body, by the restrictions of the individual’s viewpoints.  Rather than struggle against these limits, it is necessary to learn to live with them, to accept them and to make a meaningful existence, not in spite of the limitations, but because of the limitations.  It is a difficult lesson.  The individual embarking on this course must learn system and organization, ORDER on a practical level.  He must be prepared to be of SERVICE to others.',
    'Number 5: There is a time for expansion, for dealing with change, unexpected happenings, adventure.  This lesson usually gives a person an abundance of talents in every direction, the capability of accomplishing almost anything for which an opportunity is presented – and many opportunities are presented.  With the freedom that this abundance of talent and opportunity brings, life can be exciting.  But the lesson is more difficult: the individual must not waste his many talents or misuse his ongoing opportunities; he must not get lost in solely physical desires – food, sex, alcohol, drugs.  He must not scatter his potential and end up with frustration.  He must make a meaningful existence by using freedom productively.',
    'Number 6: A person must learn to give the beauty of love and harmony, sympathy and understanding, protection and BALANCE.  Along with the balancing, the lesson of RESPONSIBILITY can be a meaningful one.  The individual may find himself responsible for more than what rightly seems his share.  Others will recognize his strength, and he may be expected to help them if they are in need and cannot help themselves.  He will probably be the one who holds the family together, who harmonizes and adjusts difficult situations.  He may choose to limit himself to his family, his friends, possibly the close community.  The friendship and LOVE the individual expresses to others will come back to him from those he helps.  He can bask in the glory of a job well done and the quiet reward of friendship and love returned. \nThe individual’s capability at harmony and balance may also be expressed creatively – there is the possibility of artistic achievement.',
    'Number 7: ',
    'Number 8: ',
    'Number 9: ',
    'Number 11: The master numbers exist on a higher spiritual plan than the single digits.  The first master number, the 11, must work to develop intuition, to tune into psychic forces not available to those with lower numbers.  He must stand ready to be a channel with a message from above.  In his life, he must inspire by his own example, living in the way revealed to him, spreading his ILLUMINATION for others to absorb and benefit.  This number is as difficult as it is rewarding. \nOften, particularly at an early age, the individual is aware of his special powers, yet unable to synthesize them for his own use or for the good of his fellow man.  He is often a relatively impractical idealist, far more a dreamer than a doer.  There is an undercurrent of nervous tension always present from the high power sources to which the individual is attuned.  He has to learn to live with his special powers, to set himself aside from the world of material accumulation in order to better understand the powerful forces which can reveal a higher guidance.',
    'Number 22: The second master number, the 22, is potentially capable of combining the idealism of the first master number, the 11, with the ability to put these ideals into a concrete form.  Enormous power is available to him to produce on a significant scale, for the benefit of humanity.  When this potential can be realized, the individual becomes a MASTER BUILDER, capable of feats well beyond all others. \nFew with this number can marshal their forces to reach anywhere near the ultimate potential.  The individual is aware of the forces within him, aware also of the nervous tension that accompanies these forces.  He spends his time grappling with powers that are difficult to comprehend and use.  Often, he is seen by his fellow men as a person with enormous potential who has not, for some unexplained reason, been able to fully use his capabilities.  The highest potential is also the most difficult to reach.')

if 11 in [life_path, expression, soul_urge, birthday]:
    print(general_title[0], general_title[10], general[0], general[10])
if 22 in [life_path, expression, soul_urge, birthday]:
    print(general_title[0], general_title[11], general[0], general[11])
if 1 in [life_path, expression, soul_urge, birthday]:
    print(general_title[0], general_title[1], general[0], general[1])
if 2 in [life_path, expression, soul_urge, birthday]:
    print(general_title[0], general_title[2], general[0], general[2])
if 3 in [life_path, expression, soul_urge, birthday]:
    print(general_title[0], general_title[3], general[0], general[3])
if 4 in [life_path, expression, soul_urge, birthday]:
    print(general_title[0], general_title[4], general[0], general[4])
if 5 in [life_path, expression, soul_urge, birthday]:
    print(general_title[0], general_title[5], general[0], general[5])
if 6 in [life_path, expression, soul_urge, birthday]:
    print(general_title[0], general_title[6], general[0], general[6])
if 7 in [life_path, expression, soul_urge, birthday]:
    print(general_title[0], general_title[7], general[0], general[7])
if 8 in [life_path, expression, soul_urge, birthday]:
    print(general_title[0], general_title[8], general[0], general[8])
if 9 in [life_path, expression, soul_urge, birthday]:
    print(general_title[0], general_title[9], general[0], general[9])

#-------------#
#+# Details #+#
#-------------#


#------------------------------------------------------------------#


######################
## No Longer Needed ##
######################


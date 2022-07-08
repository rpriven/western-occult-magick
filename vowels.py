
name_raw = 'Robert Eugene Pratt'
# name_raw = 'Rob Pratt'
# name_raw = 'Rob'

name = name_raw.lower()
name_split = name.split(' ')

### Functions
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

### End Functions

'''
vowels = list()
# For each letter in name (first, last, etc.) determine if there is a vowel
for letter in name:
    # if there is a vowel, add to list
    # if 'a' or 'e' or 'i' or 'o' or 'u' in letter:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        vowels.append(letter)
        print(vowels)
    # join list together
    # ''.join(vowels)
    # print(str(vowels))
    # reduce vowels to numbers
    # dir(vowels)
'''

# Cleaner
vowels = list()

def pull_vowels(name):
    for letter in name:
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            vowels.append(letter)
            print('In pull vowels:',vowels)

# pull_vowels(name)

print('name_split[0]', name_split[0])

first = name_split[0]
# v_first = pull_vowels(name_split[0])
v_first = pull_vowels(first)

# v_middle = pull_vowels(name_split[1])
# v_last = pull_vowels(name_split[2])

# print('Pull Vowels:', pull_vowels(name))

# pull_vowels(name_split[0])
print('first:', v_first)
# print('middle:', v_middle)
# print('last:', v_last)
# vowels = name_num(vowels)
# print('Vowels:',vowels)

vowels_as_num = name_num(v_first)

    # vowels_sum = sum(vowels)
    # print(vowels_sum)
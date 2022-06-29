# Numerology
# Life Path Script

###########
# Program #
###########
# from curses.ascii import isdigit
# from curses.ascii import isalpha


# Asks for the person's full name
name_raw = input("Please enter the person's Full Name: \n")

# Makes sure something was entered
while not name_raw:
    name_raw = input("Error:  Name cannot be blank.  Please enter the Full Name: ")

# Makes sure letters were entered and not numbers
while name_raw.isnumeric():
    print("Error:  Please enter your name, not numbers.")
    name_raw = input("Please enter the person's Full Name: \n")

name = name_raw

# Removes any spaces and makes the name lowercase
spaces = " "
for chars in spaces:
    name = name.replace(chars, "")
    name = name.lower()

# Changes the person's Name to a number
def name_num(name):
    x = 0
    total = 0   # total
    r = 0       # reduced
    
    # for each character in the name
    for chars in name:
        # convert to number
        x = ord(chars) - 96
        # print('char', chars, '=', x)

        # if number is greater than 1 digit
        if x >= 10:
            # reduce
            r = sum(int(digit) for digit in str(x))
            # and add to total
            total = total + r
            # print('reduced =', r)   # previously r

        # else add number to total
        else:
            # print('no need to reduce', chars)
            total = total + x
        # print('total =', total, '\n')
    return total

# Checks for master number, then reduces further as necessary
def master_check(total):
    r = 0

    # if total is a master number, do not reduce, return master
    if total == 11 or total == 22 or total == 33 or total == 44 or total == 55:
        master = total
        print('Master found! Congtratulations, your name has a Master Number of', master)
        return master

    # if total is more than one digit, reduce
    if total >= 10:
        r = sum(int(digit) for digit in str(total))
        # print('reduced =', r)
        total = r

        # repeat if necessary
        if total == 11 or total == 22 or total == 33 or total == 44 or total == 55:
            master = total
            print('Master found! Congtratulations, your name has a Master Number of', master)
            return master
        elif total >= 10:
            r = sum(int(digit) for digit in str(total))
            # print('reduced2 =', r)
            return r
        return total    # previously r

    # else return total
    else: 
        return total

##########
# Output #
##########

# print('Total =', master_check(total))
total = name_num(name)
life_path = master_check(total)
print("Life Path for", name_raw, "=", life_path)

# Life Path Information
# Summary
lp1 = "1 means Individual"
lp2 = "2 means Relation"
lp3 = "3 means Trinity"
lp4 = "4 means Stability"
lp5 = "5 means Home"
lp6 = "6 means Six"
lp7 = "7 means Seven"
lp8 = "8 means Physical"
lp9 = "9 means Completion"
lp11 = "11 is The Master Illuminator"
lp22 = "22 is The Master 4"
lp33 = "33 is The Master Builder"

# Detailed
lpath1 = "You are ...1"
lpath2 = "You are ...2"
lpath3 = "You are ...3"
lpath4 = "You are ...4"
lpath5 = "You are ...5"
lpath6 = "You are ...6"
lpath7 = "You are ...7"
lpath8 = "You are ...8"
lpath9 = "You are ...9"
lpath11 = "You are ...11"
lpath22 = "You are ...22"
lpath33 = "You are ...33"

# if statements
if life_path == 1: print(lp1, '\n', lpath1)
if life_path == 2: print(lp2, '\n', lpath2)
if life_path == 3: print(lp3, '\n', lpath3)
if life_path == 4: print(lp4, '\n', lpath4)
if life_path == 5: print(lp5, '\n', lpath5)
if life_path == 6: print(lp6, '\n', lpath6)
if life_path == 7: print(lp7, '\n', lpath7)
if life_path == 8: print(lp8, '\n', lpath8)
if life_path == 9: print(lp9, '\n', lpath9)
if life_path == 11: print(lp11, '\n', lpath11)
if life_path == 22: print(lp22, '\n', lpath22)
if life_path == 33: print(lp33, '\n', lpath33)


#########################
# Methodology / Outline #
#########################

# name_num
    # for each character in the name
        # convert to number
        # if number is greater than 1 digit
            # reduce
            # and add to total
        # or add number to total

# master_check
    # if total is a master number
        # do not reduce
        # return master
    # if total is more than one digit
        # reduce
        # repeat if necessary
            # if total is a master number
                # do not reduce
                # return master
            # if total is more than one digit
                # reduce
    # else return total
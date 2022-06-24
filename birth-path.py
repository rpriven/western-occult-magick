# Numerology

# Birth Path Raw Section

# Asks user for their birthdate
birth_raw = input("What is your full Date of Birth? (mm/dd/yyyy) [eg. 5/13/1982]  \n")
n = birth_raw

# Removes non-numerical characters and spaces
non_numbers = "._/-' '"
for chars in non_numbers:
    n = n.replace(chars, "")

birth_path = n

# Reduces / sums amount down to one digit or notifies of master number
def reduce(n):
    x = sum(int(digit) for digit in str(n))
    if n == 11 or n == 22 or n == 33 or n == 44 or n == 55:
        master = n
        print(f"Congratulations, you have a Master Number of {master}!")
        return master
    if x < 10:
        return x
    else:
        return reduce(x)

# print(reduce(n))
birth_path = reduce(n)
print(f"Your Birth Path of {birth_path} means ...")

birthNum = 0

#! Output
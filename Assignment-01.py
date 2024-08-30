# Python Program to count occurrence of a given characters in string.
name = input("Enter a name:")
count = 0
for i in name:
    count = count+1
print(count)

print("-----")

# Python Program to check if two Strings are Anagram.
element1 = input("Enter string one: ")
element2 = input("Enter string two: ")
if sorted(element1) == sorted(element2):
    print("The strings are in Anagrams.")
else:
    print("The strings are not in Anagrams.")

print("-----")

# Python program to check a String is palindrome or not.
name = input("Enter your name: ")
given_name = name[::-1]
if name == given_name:
    print("The given word is Palindrome")
else:
    print("The given word is not a Palindrome")

print("-----")

# Python program to replace the string space with a given character.
name = input("Enter your name: ")
result = ''

for char in name:
    if char == ' ':
        result += '-'
    else:
        result += char

print(result)

print("-----")

# Python program to replace the string space with a given character using replace() method.
name = input("Enter a name:")
given_name = name.replace(" ", "-")
print(given_name)

print("-----")

# Python program to convert lowercase char to uppercase of string.
name = input("Enter your name:")
print(name.upper())

print("-----")

# Python program to convert lowercase vowel to uppercase in string.
name = input("Enter your name: ")
vowels = "aeiou"
new_str = ""
for given_name in name:
    if given_name in vowels:
        new_str += given_name.upper()
    else:
        new_str += given_name
print(new_str)

print("-----")

# Python program to separate characters in a given string.
name = input("Enter your name:")
given_name = ""
for char in name:
    given_name = given_name + char + " "
print(given_name)

print("-----")

# Python program to remove blank space from string.
name = input("Enter your name:")
given_name = name.replace(" ", "")
print(given_name)

print("-----")

# Python program to concatenate two strings using join() method.
name1 = input("Enter your name:")
name2 = input("Enter your surname:")
given_name = "".join(name1 +" "+ name2)
print(given_name)

print("-----")

# Python program to concatenate two strings without using join() method.
name1 = input("Enter your name:")
name2 = input("Enter your surname:")
given_name = name1 +" "+ name2
print(given_name)

print("-----")

# Python program to remove repeated character from string.
name = input("Enter your name: ")
output = ""
for char in name:
    if char not in output:
        output += char
print(output)

print("-----")

# Python program to check given character is vowel or consonant.
char = input("Enter any char: ")
if char in 'AEIOUaeiou':
    print("Given char is a vowel.")
elif char.isalpha():
    print("Given char is a consonant.")
else:
    print("Invalid input, Please enter a valid one.")

print("-----")

# Python program to check given character is digit or not.
element = input("Enter your number: ")
if element.isdigit():
    print("It's a valid input")
else:
    print("Not a vaild input")

print("-----")

# Python program to delete vowels in a given string.
string = input("Enter your string: ")
vowels = "aeiouAEIOU"
result = ""
for char in string:
    if char not in vowels:
        result += char
print(result)

print("-----")

# Python program to count the Occurrence Of Vowels & Consonants in a String.
string = input("Enter your own string: ")
vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

vowel_count = 0
consonant_count = 0

for char in string:
    if char in vowels:
        vowel_count += 1
    elif char in consonants:
        consonant_count += 1

print("The number of vowels =", vowel_count)
print("The number of consonants =", consonant_count)

print("-----")

# Python program to print the highest frequency character in a String.
string = input("Enter a string: ")
max_count = 0
max_char = ''
for i in string:
    count = string.count(i)
    if count > max_count:
        max_count = count
        max_char = i
    elif count == max_count:
        continue
print("The highest frequency character is:", max_char)

print("-----")

# Python program to Replace First Occurrence Of Vowel With ‘-‘ in String.
string = input("Enter a string: ")
vowels = 'aeiouAEIOU'
for char in string:
    if char in vowels:
        string = string.replace(char, '-')
        break
print("Modified string: ", string)

print("-----")

# Python program to count alphabets, digits and special characters.
string = input("Enter your string : ")
alphabets = digits = special = 0

for i in range(len(string)):
    if(string[i].isalpha()):
        alphabets = alphabets + 1
    elif(string[i].isdigit()):
        digits = digits + 1
    else:
        special = special + 1
        
print("Total Number of Alphabets in this String :  ", alphabets)
print("Total Number of Digits in this String :  ", digits)
print("Total Number of Special Characters in this String :  ", special)

print("-----")

# Python program to check given character is digit or not using isdigit() method.
element = input("Enter your number: ")
if element.isdigit():
    print("It's a valid input")
else:
    print("Not a vaild input")

print("-----")

# Python program to calculate sum of integers in string.
int_string = input("Enter a string: ")
sum_of_integers = 0
for char in int_string:
    if char.isdigit():
        sum_of_integers += int(char)
print(sum_of_integers)

print("-----")

# Python program to print all non repeating character in string.
string = input('input is: ')
output= ""
for char in string:
    if char not in output:
        output += char
print(output)

print("-----")

# Python program to copy one string to another string.
original = input("Enter your name: ")
copied = original[:]
print(copied)

print("-----")

# Python program to check given character is vowel or consonant.
string = input("Enter your own string: ")

vowels_list = "aeiouAEIOU"
consonants_list = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

vowels = ""
consonants = ""

for char in string:
    if char in vowels_list:
        vowels += char
    elif char in consonants_list:
        consonants += char
        
print("The vowels in the given string are:", vowels)
print("The consonants in the given string are:", consonants)

print("-----")

# Python program to check given character is digit or not.
element = input("Enter your number: ")
if element.isdigit():
    print("It's a valid input")
else:
    print("Not a vaild input")

print("-----")

# Python program to check given character is digit or not.
element = input("Enter your number: ")
if element.isdigit():
    print("It's a valid input")
else:
    print("Not a vaild input")

print("Assignment 1 was done")
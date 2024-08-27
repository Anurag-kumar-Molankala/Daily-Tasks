""" String: A sequence of characters between single ' ' or double " " quotes. """
# Accessing Elements from a String -A string is a sequence of characters, and each character has a specific index starting from 0. You can access individual characters by specifying the index inside square brackets [].
user_input = input("Enter a string: ")
first_char = user_input[0]  # Accessing the first character
last_char = user_input[-1]  # Accessing the last character

print(f"First character: {first_char}")
print(f"Last character: {last_char}")

print("-----")

# Manipulating Strings:

#1. Concatenation - Concatenation combaines two or more into one.
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

concatenated_string = string1 + " " + string2
print(f"Concatenated string: {concatenated_string}")

print("-----")

#2. Repetition - Repetiton repeats a string multiple times.
string = input("Enter a string: ")
repeated_string = string * 3  # Repeating the string 3 times
print(f"Repeated string: {repeated_string}")

print("-----")

# String Methods:

#1. find() - The 'find()' method returns the lowest index of the substring if it is found otherwise it returns '-1'.
string = input("Enter a string: ")
substring = input("Enter a substring to find: ")

index = string.find(substring)
print(f"Index of first occurrence: {index}")

print("-----")

#2. rfind() - The rfind() method returns the highest index of the substring if it is found, otherwise it returns '-1'.
string = input("Enter a string: ")
substring = input("Enter a substring to find: ")

index = string.rfind(substring)
print(f"Index of last occurrence: {index}")

print("-----")

#3. index() - The index() method is similar to find(), but it raises a ValueError if the substring is not found.
string = input("Enter a string: ")
substring = input("Enter a substring to find: ")

try:
    index = string.index(substring)
    print(f"Index of first occurrence: {index}")
except ValueError:
    print("Substring not found!")

print("-----")

#4. Count() - The count() method returns the number of non-overlapping occurrences of a substring in the string.
string = input("Enter a string: ")
substring = input("Enter a substring to count: ")

count = string.count(substring)
print(f"Number of occurrences: {count}")

print("-----")

#5. Strip() - The strip() method removes any leading and trailing whitespaces from the string.
string = input("Enter a string with leading/trailing spaces: ")

stripped_string = string.strip()
print(f"Stripped string: '{stripped_string}'")

print("-----")

#6. rstrip() - The rstrip() method removes trailing whitespace or specified characters from the end of a string.
string = input("Enter a string with trailing spaces: ")

rstripped_string = string.rstrip()
print(f"Right stripped string: '{rstripped_string}'")

print("-----")

#7. lstrip() - The lstrip() method removes leading whitespace or specified characters from the start of a string.
string = input("Enter a string with leading spaces: ")

lstripped_string = string.lstrip()
print(f"Left stripped string: '{lstripped_string}'")

print("-----")

#8. Split() - The split() method splits the string into a list of substrings based on a specified delimiter (default is whitespace).
string = input("Enter a string: ")

split_string = string.split()
print(f"List of words: {split_string}")

print("-----")

print("End of the Day 5 Session")
# Membership Checking:

#1. in & not in - These operators check whether a substring exists within a string.
text = "Hello, world!"
print("world" in text)  # True
print("Python" in text)  # False
print("Python" not in text)  # True

print("-----")

# String Replacement:

#2. replace -  The "replace" method is used to replace a specified substring with another substring.
text = "Hello, world!"
new_text = text.replace("world", "Python")
print(new_text)  # "Hello, Python!"

print("-----")

# Joining Strings:

#3. join - The join method is used to concatenate the elements of a sequence (e.g., a list) into a single string, separated by a specified delimiter.
words = ["Hello", "world", "Python"]
sentence = " ".join(words)
print(sentence)  # "Hello world Python"

print("-----")

# Checking Start & End of a String:

#4. startswith & endswith - These methods check whether a string starts or ends with a specified substring.
text = "Hello, world!"
print(text.startswith("Hello"))  # True
print(text.endswith("world!"))  # True

print("-----")

# Chaning case of a string:
#5. upper() - Converts all characters to uppercase.
#6. lower(): Converts all characters to lowercase.
#7. swapcase(): Swaps the case of all characters (uppercase to lowercase and vice versa).
#8. title(): Converts the first character of each word to uppercase.
#9. capitalize(): Converts the first character of the string to uppercase and the rest to lowercase.
text = "hello, WORLD!"
print(text.upper())       # "HELLO, WORLD!"
print(text.lower())       # "hello, world!"
print(text.swapcase())    # "HELLO, world!"
print(text.title())       # "Hello, World!"
print(text.capitalize())  # "Hello, world!"

print("-----")

# Checking type of characters in a string:

#10. isalnum(): Checks if all characters are alphanumeric (letters or digits).
#11. isalpha(): Checks if all characters are alphabetic.
#12. isdigit(): Checks if all characters are digits.
#13. isupper(): Checks if all characters are uppercase.
#14. islower(): Checks if all characters are lowercase.
#15. istitle(): Checks if the string follows title case (first letter of each word is uppercase).
#16. isspace(): Checks if all characters are whitespace.
text = "Hello123"
print(text.isalnum())   # True
print(text.isalpha())   # False
print(text.isdigit())   # False
print(text.isupper())   # False
print(text.islower())   # False
print("Hello World".istitle())  # True
print("   ".isspace())  # True

print("-----")

# Handling Vowels in strings:
name = "Alice"
vowels = "aeiouAEIOU"
for char in name:
    if char in vowels:
        print(f"{char} is a vowel.")

print("-----")

name = "Learning Python"
count = 0
for i in name:
    if i in vowels:
        count =  count + 1
print(count)

print("-----")

print("End of the Day 6 Session")
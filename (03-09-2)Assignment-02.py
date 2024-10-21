# 1. Numbers divisible by 7 but not by 5

numbers = [str(i) for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0]
print(','.join(numbers))

print("-----")

# 2. Dictionary with squares

n = 8
dictionary = {i: i*i for i in range(1, n+1)}
print(dictionary)

print("-----")

# 3. List and tuple from comma-separated numbers

input_numbers = input("Enter numbers: ")
numbers_list = input_numbers.split(',')
numbers_tuple = tuple(numbers_list)
print(numbers_list, numbers_tuple)

print("-----")

# 4. Alphabetical sorting of words

input_words = input("Enter words: ")
words_list = input_words.split(',')
words_list.sort()
print(','.join(words_list))

print("-----")

# 5. Counting letters and digits

input_sentence = input("Enter a sentence: ")
letters = sum(c.isalpha() for c in input_sentence)
digits = sum(c.isdigit() for c in input_sentence)
print(f"LETTERS {letters} DIGITS {digits}")

print("-----")

# 6. Counting upper and lower case letters

input_sentence = input("Enter a sentence: ")
upper_case = sum(c.isupper() for c in input_sentence)
lower_case = sum(c.islower() for c in input_sentence)
print(f"UPPER CASE {upper_case} LOWER CASE {lower_case}")

print("-----")

# 7. Net amount of a bank account

input_transactions = input("Enter transactions: ")
transactions = input_transactions.split()
balance = 0
for i in range(0, len(transactions), 2):
    if transactions[i] == 'D':
        balance += int(transactions[i+1])
    elif transactions[i] == 'W':
        balance -= int(transactions[i+1])
print(balance)
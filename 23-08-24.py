# Control Statements - Control statements are used to manage the flow of execution in a program.

#1. Conditional Statement: Conditional statements allow you to execute certain bloks of code based on specific conditions.

# 'if' Statement - Condition is True the block of code executes.
age = int(input("Enter your age:"))
if age >= 18:
    print("You are eligible to Vote")
if age <= 18:
    print("You are not eligible to Vote")

print("-----")

# 'elif' Statement - If the previous statement is False this block of code will executes.
phn_no = input("Enter your phone number:")
if len(phn_no) == 10 and phn_no.isdigit():
    print("It's a Valid phone number")
elif len(phn_no) != 10 and phn_no.isdigit():
    print("It's not a vaild phone number")

print("-----")

# 'else' Statement - Executes a block of code if all previous conditions were False.
password = str(input("Enter your password:"))
if len(password) > 6:
    print("Password accepted")
elif len(password) == 6:
    print("Password not accepted")
else:
    print("Ivalid password")

print("-----")

#2. Iterative Statement - This (Loops) allows you to execute a block of code repeatedly.

# 'for' loop - It iterates over a sequence and executes the block of the code for each item (like tuple, list, and string).
num = {1, 2, 3, 4}
for int in num:
    print(int)

print("-----")

# 'range' - It generates a sequence of elements.
for num in range (0, 10+1):
    print(num)

print("-----")

# 'while' - It executes a block of code until the condition is True.
num = 20
while num < 30:
    num = num + 1
    print(num)

print("-----")

#3. Transfer Statement - This statements are used to alter the normal flow of a program.

# 'break' - It stops the execution of a block of code if the condition is True.
for i in range (0, 10):
  if i == 6:
    break
print(i)

print("-----")

# 'continue' - Skips current iterative and moves to the next iterative.
for i in range (0, 20 + 1):
    if i <= 10:
        continue
    print(i)

print("-----")

# 'pass' - Does nothing and is used as a placeholder.
for i in range (0, 20 + 1):
    if i %2 == 0:
        pass
    print(i)

print("-----")

# ATM Simulation Project:

# Initial balance
balance = 100000

def atm_operations():
    global balance  # Declare balance as global to modify it inside the function
    
    print("Welcome to the ATM")
    
    # User input for ATM ID
    atm_id = input("Enter your ATM ID: ")
    
    # Simple ID verification
    if atm_id == "1234":
        print("ID verified successfully!")
        
        while True:
            # Displaying the ATM menu
            print("\nATM Menu:")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            
            # User input for operation choice
            choice = int(input("Enter your choice (1-4): "))
            
            # Check balance
            if choice == 1:
                print(f"Your current balance is: ${balance}")
            
            # Deposit money
            elif choice == 2:
                deposit_amount = float(input("Enter the amount to deposit: "))
                
                if deposit_amount > 0:
                    balance += deposit_amount
                    print(f"${deposit_amount} deposited successfully!")
                    print(f"Updated balance: ${balance}")
                else:
                    print("Invalid deposit amount. Please enter a positive value.")
            
            # Withdraw money
            elif choice == 3:
                withdraw_amount = float(input("Enter the amount to withdraw: "))
                
                # Relational and logical operators to check if withdrawal is possible
                if withdraw_amount > 0 and withdraw_amount <= balance:
                    balance -= withdraw_amount
                    print(f"${withdraw_amount} withdrawn successfully!")
                    print(f"Updated balance: ${balance}")
                else:
                    print("Insufficient balance or invalid amount. Please try again.")
            
            # Exit
            elif choice == 4:
                print("Thank you for using the ATM. Goodbye!")
                break
            
            # Invalid choice
            else:
                print("Invalid choice. Please select a valid option.")
    
    else:
        print("Invalid ATM ID. Please try again.")

# Running the ATM operations function
atm_operations()

print("-----")

print("End of the Day 3 Session")
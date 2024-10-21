""" 
A package is a collection of related modules organized in a directory (folder). 
It allows you to structure your Python project into multiple, logically grouped files, making the code more modular and easier to manage.

To create a package, you organize your modules into a directory and include a special __init__.py file.
This file can be empty, but it signals to Python that the directory should be treated as a package.

Example: E-commerce System Package
Let’s create a simple e-commerce system with packages for:

ecommerce/
│
├── products/
│   ├── __init__.py
│   └── product_info.py
│
├── auth/
│   ├── __init__.py
│   └── authentication.py
│
├── order/
│   ├── __init__.py
│   └── order_management.py
│
├── payment/
│   ├── __init__.py
│   └── payment_processing.py
│
└── main.py
"""
# Products: Managing product information. products/product_info.py
def get_product_details(product_id):
    products = {
        1: "Laptop",
        2: "Smartphone",
        3: "Headphones"
    }
    return products.get(product_id, "Product not found")


# Authentication: User login and signup. auth/authentication.py
def login(username, password):
    if username == "user" and password == "pass":
        return "Login successful"
    else:
        return "Login failed"

def signup(username, password):
    return f"User {username} signed up successfully!"

# Order: Placing and viewing orders. order/order_management.py
def place_order(product_name):
    return f"Order placed for {product_name}"

def view_orders():
    return ["Laptop", "Smartphone"]

# Payment: Processing payments. payment/payment_processing.py
def process_payment(amount):
    return f"Payment of ${amount} processed successfully!"

# Product details
product = get_product_details(1)
print(product)  # Output: Laptop

# User authentication
login_status = login("user", "pass")
print(login_status)  # Output: Login successful

# Sign up a user
signup_status = signup("new_user", "new_pass")
print(signup_status)  # Output: User new_user signed up successfully!

# Place an order
order_status = place_order(product)
print(order_status)  # Output: Order placed for Laptop

# View orders
orders = view_orders()
print(orders)  # Output: ['Laptop', 'Smartphone']

# Process payment
payment_status = process_payment(500)
print(payment_status)  # Output: Payment of $500 processed successfully!

print("-----")

print("End of Day 16 Session")
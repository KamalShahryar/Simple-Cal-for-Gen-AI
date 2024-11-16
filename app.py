import streamlit as st

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero!"

# Streamlit User Interface
st.title("Simple Calculator")

# Get user inputs for the operation and numbers
operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# Perform the calculation based on the user's choice
if operation == "Add":
    result = add(num1, num2)
elif operation == "Subtract":
    result = subtract(num1, num2)
elif operation == "Multiply":
    result = multiply(num1, num2)
elif operation == "Divide":
    result = divide(num1, num2)

# Display the result
st.write(f"Result: {result}")

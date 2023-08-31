import streamlit as st

def find_max_number(num1, num2, num3):
    return max(num1, num2, num3)


st.title("Largest Number Finder Application")
st.write("Enter three numbers and find the largest one.")

num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")
num3 = st.number_input("Enter the third number:")

if st.button("Find Largest Number"):
  largest_number = find_max_number(num1, num2, num3)
  st.success(f"The largest number is: {largest_number}")


# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)
st.markdown("""
            ### Plan Code Generator👋
            """)

def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋")

st.number_input('Pick a number', 1,3)
st.radio('Choose your Company',['BLC','WNIC','Other'])

import random

# Generate a random four-digit number between 1 and 100 (inclusive)
random_number = random.randint(1, 10000)

# Ensure that the generated number has exactly four digits
while random_number < 1000:
    random_number *= 10

# Display the random four-digit number
st.write(f"Random four-digit number: {random_number}")

def case_one():
    return "This is case one."

def case_two():
    return "This is case two."

def case_three():
    return "This is case three."

# Define a dictionary to map cases to functions
case_dict = {
    'case1': case_one,
    'case2': case_two,
    'case3': case_three
}

# Input the case you want to execute
selected_case = 'case4'

# input("Enter a case (case1, case2, case3): ").strip().lower()

# Check if the selected case exists in the dictionary
if selected_case in case_dict:
    # Execute the selected case
    result = case_dict[selected_case]()
    st.write(result)
else:
   st.write("Invalid case. Please enter a valid case.")

import random
import string

# Define the characters to choose from (uppercase letters and digits)
characters = string.ascii_uppercase + string.digits

# Define the number of digits for each alphanumeric number
num_digits = 4

# Generate a random starting alphanumeric number
first_number = ''.join(random.choice(characters) for _ in range(num_digits))

# Create a list to store the sequential numbers
sequential_numbers = [first_number]

# Generate the next three sequential alphanumeric numbers
for i in range(1, 4):
    next_number = ''.join(random.choice(characters) for _ in range(num_digits))
    sequential_numbers.append(next_number)

# Print the generated numbers in uppercase
for i, number in enumerate(sequential_numbers, 1):
    st.write(f"Alphanumeric Number {i}: {number}")


import random

# Existing list of excluded numbers
excluded_numbers = [3, 7, 5]

# Initialize an empty list to store the random numbers
random_numbers = []

# Generate 4 random numbers that are 1 digit in length and not in the excluded list
while len(random_numbers) < 4:
    num = random.randint(0, 9)  # Generate a random number between 0 and 9
    if num not in excluded_numbers:
        random_numbers.append(num)

st.write(random_numbers)

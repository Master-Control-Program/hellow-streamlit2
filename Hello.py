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
            ### Data Warehouse Table Maintenance👋
            """)



# Title for the app
st.title("Search Criteria")

# Create a form with a text input and a submit button
search_criteria = st.text_input("Enter Search Criteria:")
if st.button("Search"):
    # You can perform some action here when the user clicks the "Search" button
    st.write(f"Searching for: {search_criteria}")

# Optionally, you can add more form elements like checkboxes, radio buttons, etc.
# Example:
# use_case = st.radio("Select Use Case:", ["Option 1", "Option 2", "Option 3"])
# if st.button("Submit"):
#     st.write(f"Selected Use Case: {use_case}")




 
       




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




import hmac
import streamlit as st
import sqlite3


'''def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    # Return True if the password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False


if not check_password():
    st.stop()  # Do not continue if check_password is not True.
'''





















import streamlit as st

# Title for the app
st.title("Search and Add Coverage")

# Create a section for "Search Criteria"
st.header("Search Criteria")

# Create search boxes for various criteria
search_coverage_plan = st.text_input("Coverage Plan (Search):")
search_company_code = st.text_input("Company Code (Search):")

# Create a dropdown menu for System Code with the specified choices (default to None)
system_code_options = [None, "SHARP", "CIC", "LIFEPRO"]
search_system_code = st.selectbox("System Code (Search):", system_code_options)

# Create a dropdown menu for LOB Name with the specified choices (default to None)
lob_name_options = [None, "ANNUITY", "GROUP", "HEALTH", "LIFE"]
search_lob_name = st.selectbox("LOB Name (Search):", lob_name_options)

# Create a dropdown menu for Major Product Group Name with specified choices (default to None)
major_product_group_options = [None, "EI ANN", "EIUL", "FIXED ANN", "GRP ANN", "GRP HEALTH", "GRP LIFE"]
search_major_product_group_name = st.selectbox("Major Product Group Name (Search):", major_product_group_options)

search_minor_product_group_name = st.text_input("Minor Product Group Name (Search):")
search_marketing_product_group_name = st.text_input("Marketing Product Group Name (Search):")
search_product_code = st.text_input("Product Code (Search):")

# Create a submit button for searching
search_button = st.button("Search")

# Create a clear button to reset the search form fields
clear_button = st.button("Clear")

# Create a new section for "Add New Coverage"
st.header("Add New Coverage")

# Add form fields for adding new coverage
new_coverage_plan = st.text_input("Coverage Plan (New):")
new_company_code = st.text_input("Company Code (New):")
new_system_code = st.text_input("System Code (New):")
new_lob_name = st.text_input("LOB Name (New):")
new_major_product_group_name = st.text_input("Major Product Group Name (New):")
new_minor_product_group_name = st.text_input("Minor Product Group Name (New):")
new_marketing_product_group_name = st.text_input("Marketing Product Group Name (New):")
new_product_code = st.text_input("Product Code (New):")

# Additional text entry boxes
new_coverage_plan_code = st.text_input("Coverage Plan Code (New):")
new_policy_company_code = st.text_input("Policy Company Code (New):")
new_effective_date = st.text_input("Effective Date (New):")
new_policy_form_code = st.text_input("Policy Form Code (New):")
new_termination_reason_code = st.text_input("Termination Reason Code (New):")

# Create a button to submit the new coverage information
add_new_coverage_button = st.button("Add New Coverage")

# Handle button clicks
if search_button:
    # Perform search
    pass

if clear_button:
    # Clear search form fields
    pass

if add_new_coverage_button:
    # Add new coverage
    pass

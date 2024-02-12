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


def check_password():
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






















import streamlit as st

# Title for the app
st.title("Search and Add Coverage")

# Create a section for "Search Criteria"
st.header("Search Criteria")

# Create search boxes for various criteria
coverage_plan = st.text_input("Coverage Plan:")
company_code = st.text_input("Company Code:")

# Create a dropdown menu for System Code with the specified choices (default to None)
system_code_options = [None, "SHARP", "CIC", "LIFEPRO"]
system_code = st.selectbox("System Code:", system_code_options)

# Create a dropdown menu for LOB Name with the specified choices (default to None)
lob_name_options = [None, "ANNUITY", "GROUP", "HEALTH", "LIFE"]
lob_name = st.selectbox("LOB Name:", lob_name_options)

# Create a dropdown menu for Major Product Group Name with specified choices (default to None)
major_product_group_options = [None, "EI ANN", "EIUL", "FIXED ANN", "GRP ANN", "GRP HEALTH", "GRP LIFE"]
major_product_group_name = st.selectbox("Major Product Group Name:", major_product_group_options)

minor_product_group_name = st.text_input("Minor Product Group Name:")
marketing_product_group_name = st.text_input("Marketing Product Group Name:")
product_code = st.text_input("Product Code:")

# Create a submit button for searching
if st.button("Search"):
    # You can perform some action here when the user clicks the "Search" button
    st.write("Search Results:")
    st.write(f"Coverage Plan: {coverage_plan}")
    st.write(f"Company Code: {company_code}")
    st.write(f"System Code: {system_code}")
    st.write(f"LOB Name: {lob_name}")
    st.write(f"Major Product Group Name: {major_product_group_name}")
    st.write(f"Minor Product Group Name: {minor_product_group_name}")
    st.write(f"Marketing Product Group Name: {marketing_product_group_name}")
    st.write(f"Product Code: {product_code}")

# Create a clear button to reset the search form fields
if st.button("Clear"):
    coverage_plan = company_code = system_code = lob_name = ""
    major_product_group_name = minor_product_group_name = ""
    marketing_product_group_name = product_code = ""

# Create a new section for "Add New Coverage"
st.header("Add Coverage")

# Add form fields for adding new coverage
new_coverage_plan = st.text_input("Coverage Plan:")
new_company_code = st.text_input("Company Code:")
new_system_code = st.text_input("System Code:")
new_lob_name = st.text_input("LOB Name:")
new_major_product_group_name = st.text_input("Major Product Group Name:")
new_minor_product_group_name = st.text_input("Minor Product Group Name:")
new_marketing_product_group_name = st.text_input("Marketing Product Group Name:")
new_product_code = st.text_input("Product Code:")

# Additional text entry boxes
coverage_plan_code = st.text_input("Coverage Plan Code:")
policy_company_code = st.text_input("Policy Company Code:")
effective_date = st.text_input("Effective Date:")
policy_form_code = st.text_input("Policy Form Code:")
termination_reason_code = st.text_input("Termination Reason Code:")

# Create a button to submit the new coverage information
if st.button("Add Coverage"):
    # You can perform some action here when the user clicks the "Add Coverage" button
    st.write("Coverage Added:")
    st.write(f"Coverage Plan: {new_coverage_plan}")
    st.write(f"Company Code: {new_company_code}")
    st.write(f"System Code: {new_system_code}")
    st.write(f"LOB Name: {new_lob_name}")
    st.write(f"Major Product Group Name: {new_major_product_group_name}")
    st.write(f"Minor Product Group Name: {new_minor_product_group_name}")
    st.write(f"Marketing Product Group Name: {new_marketing_product_group_name}")
    st.write(f"Product Code: {new_product_code}")

    # Additional fields
    st.write(f"Coverage Plan Code: {coverage_plan_code}")
    st.write(f"Policy Company Code: {policy_company_code}")
    st.write(f"Effective Date: {effective_date}")
    st.write(f"Policy Form Code: {policy_form_code}")
    st.write(f"Termination Reason Code: {termination_reason_code}")

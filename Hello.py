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




import streamlit as st

# Title for the app
st.title("Search Criteria")

# Create search boxes for various criteria
coverage_plan = st.text_input("Coverage Plan:")
company_code = st.text_input("Company Code:")

# Create a dropdown menu for System Code with the specified choices
system_code_options = ["SHARP", "CIC", "LIFEPRO"]
system_code = st.selectbox("System Code:", system_code_options)

# Create a dropdown menu for LOB Name with the specified choices
lob_name_options = ["ANNUITY", "GROUP", "HEALTH", "LIFE"]
lob_name = st.selectbox("LOB Name:", lob_name_options)

# Create a dropdown menu for Major Product Group Name with specified choices
major_product_group_options = ["EI ANN", "EIUL", "FIXED ANN", "GRP ANN", "GRP HEALTH", "GRP LIFE"]
major_product_group_name = st.selectbox("Major Product Group Name:", major_product_group_options)

minor_product_group_name = st.text_input("Minor Product Group Name:")
marketing_product_group_name = st.text_input("Marketing Product Group Name:")
product_code = st.text_input("Product Code:")

# Create a submit button
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

# Clear button to reset the form fields
if st.button("Clear"):
    coverage_plan = company_code = system_code = lob_name = ""
    major_product_group_name = minor_product_group_name = ""
    marketing_product_group_name = product_code = ""




 
       




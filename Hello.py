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
import sqlite3
import st-pages

# Custom CSS to style the title
st.markdown("<h1 style='text-align: left; color: yellow; font-size: 75px; font-weight: bold;'>Data Warehouse Table Maintenance</h1>", unsafe_allow_html=True)

# Custom CSS to style the title
st.markdown("<h1 style='text-align: center; color: white; font-size: 52px; font-weight: bold;'>Coverage</h1>", unsafe_allow_html=True)

# Custom CSS to style the title
st.markdown("<h1 style='text-align: left; color: red; font-size: 36px; font-weight: bold;'>Page listing defaults to system code 1/APS ***Please enter your Search Criteria.***</h1>", unsafe_allow_html=True)

# Create a section for "Search Criteria"
st.header("Search Criteria")

# Split the search criteria section into two columns
col1, col2 = st.columns(2)

# Create search boxes for various criteria in the first column
with col1:
    search_coverage_plan = st.text_input("Coverage Plan (Search):")
    search_company_code = st.text_input("Company Code (Search):")
    search_system_code = st.selectbox("System Code (Search):", [None, "SHARP", "CIC", "LIFEPRO"])
    search_lob_name = st.selectbox("LOB Name (Search):", [None, "ANNUITY", "GROUP", "HEALTH", "LIFE"])

# Create search boxes for various criteria in the second column
with col2:
    search_major_product_group_name = st.selectbox("Major Product Group Name (Search):", [None, "EI ANN", "EIUL", "FIXED ANN", "GRP ANN", "GRP HEALTH", "GRP LIFE"])
    search_minor_product_group_name = st.text_input("Minor Product Group Name (Search):")
    search_marketing_product_group_name = st.text_input("Marketing Product Group Name (Search):")
    search_product_code = st.text_input("Product Code (Search):")

# Create a submit button for searching
search_button = st.button("Search")

# Create a clear button to reset the search form fields
clear_button = st.button("Clear")

# Create a new section for "Add New Coverage"
st.header("Add New Coverage")

# Split the "Add New Coverage" section into two columns
col3, col4 = st.columns(2)

# Add form fields for adding new coverage in the first column
with col3:
    new_coverage_plan = st.text_input("Coverage Plan (New):")
    new_company_code = st.text_input("Company Code (New):")
    new_system_code = st.text_input("System Code (New):")
    new_lob_name = st.text_input("LOB Name (New):")

# Add form fields for adding new coverage in the second column
with col4:
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


from st_pages import Page, Section, show_pages, add_page_title

# Either this or add_indentation() MUST be called on each page in your
# app to add indendation in the sidebar
add_page_title()

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("streamlit_app.py", "Home", "🏠"),
        Page("other_pages/page2.py", "Page 2", ":books:"),
        Section("My section", icon="🎈️"),
        # Pages after a section will be indented
        Page("Another page", icon="💪"),
        # Unless you explicitly say in_section=False
        Page("Not in a section", in_section=False)
    ]
)
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

# streamlit_app.py

# streamlit_app.py

import streamlit as st
import pandas as pd

# Set page title
st.set_page_config(page_title="Region")

# Text input boxes
description = st.text_input("Description", "")
manager_name = st.text_input("Manager Name", "")

# Search and Clear Buttons
col1, col2 = st.columns([1, 1])
if col1.button("Search"):
    # Perform search action
    pass  # Placeholder for search action
if col2.button("Clear"):
    description = ""
    manager_name = ""

# Sample table data
data = {
    "Region": ["Region A", "Region B", "Region C"],
    "Description": ["Description A", "Description B", "Description C"],
    "Manager Name": ["Manager A", "Manager B", "Manager C"]
}
df = pd.DataFrame(data)

# Filter data based on input
filtered_df = df[(df["Description"].str.contains(description, case=False)) & 
                 (df["Manager Name"].str.contains(manager_name, case=False))]

# Display table
st.table(filtered_df)


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
import pandas as pd

# Path to your SQLite database
DB_PATH = "C:\\sqlite\\brad1.db"

def connect_to_db(path):
    """Connect to the SQLite database."""
    conn = sqlite3.connect(path)
    return conn

def load_data(conn, table_name):
    """Load data from a specified table."""
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, conn)
    return df

def main():
    """Main function to run the Streamlit app."""
    st.title("SQLite Database Viewer")

    # Connect to the database
    conn = connect_to_db(DB_PATH)

    # You can change this to a selectbox with table names if you have multiple tables
    table_name = 'IDW1'  # Replace with your table name
    
    if st.button("Load Data"):
        # Load and display the data
        df = load_data(conn, table_name)
        st.write(df)

    # Don't forget to close the connection
    conn.close()

if __name__ == "__main__":
    main()

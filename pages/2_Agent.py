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
import sqlite3
import pandas as pd

# Path to your SQLite database
DB_PATH = r"C:\sqllite\brad1.db"

def connect_to_db(path):
    """Connect to the SQLite database."""
    conn = sqlite3.connect(path)
    return conn

def get_table_names(conn):
    """Get a list of all table names in the database."""
    query = "SELECT name FROM sqlite_master WHERE type='table';"
    df = pd.read_sql(query, conn)
    return df['name'].tolist()

def main():
    """Main function to run the Streamlit app."""
    st.title("SQLite Database Table Viewer")

    # Connect to the database
    conn = connect_to_db(DB_PATH)

    try:
        # Get table names to display
        table_names = get_table_names(conn)
        
        # Display table names
        st.write("List of tables in the database:")
        for table_name in table_names:
            st.text(table_name)
    except Exception as e:
        st.error(f"An error occurred: {e}")
    finally:
        # Don't forget to close the connection
        conn.close()

if __name__ == "__main__":
    main()

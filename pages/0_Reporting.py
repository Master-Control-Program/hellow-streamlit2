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

# Specify the path to your SQLite database
DB_PATH = r"C:\sqllite\brad1.db"


# Attempt to connect to the database
conn = sqlite3.connect(DB_PATH)
print("Connected to the database successfully.")
    
    # You can add your database operations here
    
    # Create a cursor object using the cursor() method
cursor = conn.cursor()
    
    # Retrieve all the table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    
    # Fetch all results
tables = cursor.fetchall()
    
    # Print the list of tables
print("List of tables in the database:")
for table in tables:
    print(table[0])


def main():
    """Main function to run the Streamlit app."""
    st.title("SQLite Database Viewer")

    # Create a selectbox for table names
    table_name = st.selectbox("Choose a table", options=tables)

    # Don't forget to close the connection
    conn.close()

if __name__ == "__main__":
    main()
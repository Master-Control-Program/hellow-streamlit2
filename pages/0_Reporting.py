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

import sqlite3

# Specify the path to your SQLite database
database_path = r"C:\sqlite\brad1.db"

try:
    # Attempt to connect to the database
    conn = sqlite3.connect(database_path)
    print("Connected to the database successfully.")
    
    # You can add your database operations here
    
    # Close the database connection
    conn.close()
except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)

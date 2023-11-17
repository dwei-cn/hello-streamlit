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
import pandas as pd
import numpy as np
import time as ts
from datetime import time
from matplotlib import pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu



LOGGER = get_logger(__name__)

json_file = {"a": 1, "b": 2, "c": 3, "d": 4}
code = """print('hello world')"""

np.random.seed(42)
num_rows = 10
table_data = pd.DataFrame(data = {
    'ID': np.arange(1, num_rows + 1),
    'Name': np.random.choice(['Alice', 'Bob', 'Charlie', 'David'], num_rows),
    'Age': np.random.randint(20, 60, num_rows),
    'City': np.random.choice(['New York', 'San Francisco', 'Los Angeles', 'Chicago'], num_rows),
    'Salary': np.random.uniform(50000, 100000, num_rows)
})
youtube_url = "https://www.youtube.com/watch?v=J8TgKxomS2g"

x = np.linspace(0, 10, 100)

def run():
    st.set_page_config(
        page_title="Hello Streamlit!",
        page_icon=":tada:",
        initial_sidebar_state="collapsed"  # hide side bar in the beginning
    )

    st.write("# Welcome to Streamlit! 🚀")
    st.write("## Welcome to Streamlit! 🚀")
    st.write("### Welcome to Streamlit! 🚀")
    st.write("This is my first Streamlit page, rock'n'roll! 🚀")

             



    

if __name__ == "__main__":
    run()

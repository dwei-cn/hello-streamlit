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
        #initial_sidebar_state="collapsed"  # hide side bar in the beginning
    )

    st.write("# 食物禁忌")
    #st.write("## Welcome to Streamlit! 🚀")
    #st.write("### Welcome to Streamlit! 🚀")
    #st.write("This is my first Streamlit page, rock'n'roll! 🚀")

    ## editable dfs
    #st.subheader("Streamlit Editable Dataframes")
    st.write("大家可以在这个表格中填写自己的食物禁忌或者过敏等。")

    #st.session_state = load_session_state()

    df = pd.read_csv('./cache/food_restriction.csv')

    # df2 = pd.DataFrame(
    #     [
    #         {"command": "st.selectbox", "rating": 4, "is_widget": True},
    #         {"command": "st.balloons", "rating": 5, "is_widget": False},
    #         {"command": "st.time_input", "rating": 3, "is_widget": True},
    #     ]
    # )
    # df2['comments'] = None

    edited_df = st.data_editor(
        df, 
        key='my_key',
        num_rows="dynamic",
        use_container_width=True
        ) # 👈 An editable dataframe
    #st.dataframe(df2, use_container_width=True)

    # st.session_state["my_key"] = load_session_state()
    #favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
    #st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

    #st.write("Here's the value in Session State:")
    #st.write(st.session_state) # 👈 Show the value in Session State
    #st.write(st.session_state["my_key"]) # 👈 Show the value in Session State

    update_btn = st.button("Update Table")
    if update_btn:
        #save_session_state(st.session_state)
        pd.DataFrame(edited_df).to_csv('./cache/food_restriction.csv', index=False)
    

             



    

if __name__ == "__main__":
    run()

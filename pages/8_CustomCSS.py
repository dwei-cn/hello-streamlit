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

from urllib.error import URLError

import altair as alt
import pandas as pd

import streamlit as st
from streamlit.hello.utils import show_code
import streamlit.components.v1 as com

lottie_url = "https://lottie.host/?file=3a1f85e4-6c70-4278-91b2-297f9b470927/SebIrYSxUy.json"


with open("./assets/designing.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)


st.title("Its the summer time! 🌴")
st.markdown("---")




left_column, right_column = st.columns(2)
with left_column:
    # create a form
    with st.form('User Registration'):
        col1, col2 = st.columns(2)
        first_name = col1.text_input('First Name')
        last_name = col2.text_input('Last Name')

        email = st.text_input('Email')
        password = st.text_input('Password', type='password')
        confirm_password = st.text_input('Confirm Password', type='password')
        comments = st.text_area('Comment')

        day, month, year = st.columns(3)
        day.text_input('Day')
        month.text_input('Month')
        year.text_input('Year')

        form_button = st.form_submit_button('Submit')

        if form_button:
            if not first_name and not last_name:
                st.warning("Please fill in both first and last name")
            else:
                st.success("Registration successful!")

        print(first_name, last_name, email, password, confirm_password, comments)


with right_column:
    com.iframe(lottie_url)

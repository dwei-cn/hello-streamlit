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
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="My Webpage", page_icon=":china:", layout="wide")


lottie_url = "https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json"


with open("./assets/designing.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use Local CSS
def local_css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("./assets/style.css")

lottie_coding = load_lottieurl(lottie_url)

with st.container():
    st.subheader("Hi, I'm Dave :wave:")
    st.title("A Data Scientist From SF Bay Area")
    st.write("I am passionate about Data!")
    st.markdown("---")


with st.container():
    text_col, image_col = st.columns((2, 1))   # left col twice as wide as right col
    with text_col:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On my YouTube channel I am creating tutorials for people who:
            - are looking for a way to leverage the power of Python in their day-to-day work.
            - are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBA.
            - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
            - are working with Excel and found themselves thinking - "there has to be a better way."

            If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
            """
        )
        st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")

    with image_col:
        #com.iframe(lottie_url)
        st_lottie(lottie_coding)

    st.write("---")
    

with st.container():
    image_colm, text_col = st.columns((1, 2))
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/1280px-Image_created_with_a_mobile_phone.png")
    with text_column:
        st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
        st.write(
            """
            Learn how to use Lottie Files in Streamlit!
            Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
            In this tutorial, I'll show you exactly how to do it
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/1280px-Image_created_with_a_mobile_phone.png")
    with text_column:
        st.subheader("How To Add A Contact Form To Your Streamlit App")
        st.write(
            """
            Want to add a contact form to your Streamlit website?
            In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

    st.write("---")


with st.container():
    st.header("Get In Touch With Me!")
    left_column, mid_col, right_column = st.columns((1, 1, 1))
    
    with left_column:
        with st.form('User Registration'):
            col1, col2 = st.columns(2)
            first_name = col1.text_input('First Name')
            last_name = col2.text_input('Last Name')

            email = st.text_input('Email')
            # password = st.text_input('Password', type='password')
            # confirm_password = st.text_input('Confirm Password', type='password')
            comments = st.text_area('Comment')

            day, month, year = st.columns(3)
            day.text_input('Day')
            month.text_input('Month')
            year.text_input('Year')

            form_button = st.form_submit_button('Submit')

    with mid_col:
        st.empty()
    with right_column:
        st.empty()









# st.title("Its the summer time! 🌴")
# st.markdown("---")


# with st.container():
#     st.subheader("")






# left_column, right_column = st.columns(2)
# with left_column:
#     # create a form
#     with st.form('User Registration'):
#         col1, col2 = st.columns(2)
#         first_name = col1.text_input('First Name')
#         last_name = col2.text_input('Last Name')

#         email = st.text_input('Email')
#         password = st.text_input('Password', type='password')
#         confirm_password = st.text_input('Confirm Password', type='password')
#         comments = st.text_area('Comment')

#         day, month, year = st.columns(3)
#         day.text_input('Day')
#         month.text_input('Month')
#         year.text_input('Year')

#         form_button = st.form_submit_button('Submit')

#         if form_button:
#             if not first_name and not last_name:
#                 st.warning("Please fill in both first and last name")
#             else:
#                 st.success("Registration successful!")

#         print(first_name, last_name, email, password, confirm_password, comments)


# with right_column:
#     com.iframe(lottie_url)

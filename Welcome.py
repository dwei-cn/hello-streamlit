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
import base64


LOGGER = get_logger(__name__)



def run():
    st.set_page_config(
        page_title="我们结婚了!",
        page_icon=":tada:",
        #initial_sidebar_state="collapsed"  # hide side bar in the beginning
    )

        # load background img
    background_image_link = "./assets/wedding.jpeg"

    @st.cache_data
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()

    img = get_img_as_base64(background_image_link)

    ## manage all css elements
    with open('./assets/style.css') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
    st.markdown(
    f"""
    <style>
        [data-testid="stAppViewContainer"] > .main{{
        background-image: url("data:image/png;base64,{img}");
        background-size: cover;
        #background-attachment: local;
        }}
        
        [data-testid="stHeader"]{{
            background-color: white;
        }}

        [data-testid="stSidebar"] > div:first-child {{
            background-image: url("https://images.pexels.com/photos/255379/pexels-photo-255379.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2");
            opacity:100;
            background-position: center

        }}

    </style>
    """,
    unsafe_allow_html=True,
    )

    st.write("# Welcome to Our Wedding! 👩🏻‍❤️‍👨🏻")
    #st.write("### $$号外：Mia和Dave终于修成正果了!$$")
    #st.write("## Welcome to Streamlit! 🚀")
    #st.write("### Welcome to Streamlit! 🚀")
    st.write(" 首先非常感谢大家从世界各地前来（云）参加我们的婚礼！由于缺乏经验以及准备匆忙！导致整个过程略显匆忙和局促，希望大家能够多多包涵!")
    st.write(" 最后还是希望大家和我们一同享受这个美好的时刻！")


    
    

    ts.sleep(5)
    st.balloons()

             



    

if __name__ == "__main__":
    run()

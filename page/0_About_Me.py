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
from datetime import time
from streamlit_lottie import st_lottie
import requests

LOGGER = get_logger(__name__)


lottie_url = "https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json"

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    
lottie_coding = load_lottieurl(lottie_url)


def run():
    st.set_page_config(
        page_title="Hello Streamlit!",
        page_icon=":tada:",
        layout="wide"
        
    )

    # adjust the width of the page
    # Inject custom CSS to set the width of the sidebar
    st.markdown(
        """
        <style>
            section[data-testid="stSidebar"] {
                width: 5px !important; # Set the width to your desired value
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    
    with st.container():

        left_col, mid_col, right_col = st.columns((1.2, 0.5, 1))

        with left_col:
            st.write("# Hello. ")
            st.write("#### My name is Dave Wei.")          
            st.write("<br>", unsafe_allow_html=True)
            
            st.markdown("""
            
            I am an data scientist currently based in San Francisco Bay Area. I am the creator of the JavaScript framework [Vue.js](https://vuejs.org/) and the frontend build tool Vite. Most of my work is open source and publicly available on GitHub. If you happen to benefit from my OSS work, you can support me financially via GitHub Sponsors.

            You can follow me on Twitter where I mostly tweet about Vue and frontend technologies. If you happen to speak Chinese, my Chinese name is 尤雨溪 (yóu yǔ xī) and I have a Chinese-only Twitter alt for non-tech-focused musings. You can also find me on 微博 and 知乎.

            Outside of programming and helping my wife take care of our two kids, I enjoy video games, karaoke, sushi, watching UFC/F1, and collecting mechanical watches.
                
        
            """)
        
        # with right_col:
        #     st_lottie(lottie_coding)



    

if __name__ == "__main__":
    run()

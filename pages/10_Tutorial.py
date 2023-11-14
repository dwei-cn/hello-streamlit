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
        page_icon="👋",
    )

    st.write("# Welcome to Streamlit! 🚀")
    st.write("## Welcome to Streamlit! 🚀")
    st.write("### Welcome to Streamlit! 🚀")

    st.title("Welcome to Streamlit! ")
    st.header('Welcome to Streamlit!')
    st.subheader('Welcome to Streamlit!')

    st.text('Just some simple text.')

    st.sidebar.success("Select a demo above.")
    
    st.markdown("<h1 style='color: black; font-family: Arial, sans-serif;'>Custom Font</h1>", unsafe_allow_html=True)   # unsafe_allow_html 允许使用html hack

    # 利用markdown对界面的style进行调整
    # .st-emotion-cache-iiif1v.ef3psqc4  去除humberg
    # .st-emotion-cache-h5rgaw.ea3mdgi1 去除页面底部的made with streamlit
    st.markdown("""
    <style>  
    .st-emotion-cache-h5rgaw.ea3mdgi1
                {
                visibility: hidden;
                }
    </style>
  
    """, unsafe_allow_html=True)
    
    # <style>  
    # .st-emotion-cache-iiif1v.ef3psqc4
    #             {
    #             visibility: hidden;
    #             }
    # </style>

    st.markdown(    
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        **👈 Select a demo from the sidebar** to see some examples
        of what Streamlit can do!
        ### Want to learn more?
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
        - Let me know if you have any questions! ❤️
        - Yay! This is my first Streamlit app! 😈
    """
    )

    st.caption('This is a caption')
    st.json(json_file)
    st.code(code, language='python')
    st.metric(label='wind speed', value="120ms/sec", delta="1.4ms/sec")
    st.metric(label='wind speed', value="120ms/sec", delta="-1.4ms/sec")
    st.table(table_data)
    st.dataframe(table_data)

    #st.image('assets/kid.jpeg', caption='This is an image of kid', width=100)
    
    video_embed_code = f'<iframe width="560" height="315" src="{youtube_url}" frameborder="0" allowfullscreen></iframe>'
    #st.video(youtube_url)

    def checkbox_status_changed():
        """
        callback function to update the checkbox status
        每次checkbox_status变化的时候就会call checkbox_status_changed这个function
        """
        print(st.session_state.checker)
    
    checkbox_status = st.checkbox(label='checkbox or not to checkbox', 
                                  value=True,
                                  on_change=checkbox_status_changed,  # 每次change的时候会有动作
                                  key = "checker"    # 可以通过session_state查询状态
                                  )
    
    if checkbox_status:
        st.write("You selected checkbox")
    else:
        st.write("You didn't select checkbox")

    
    ans = st.radio("where do you want to go?", 
             options=("UK", "US", "JP"),
             key = "location" 
             )
    
    if ans:
        st.write("I want to go to", ans, "too!")
    else:
        pass

    def btn_click():    # callback function就是之后的function发生了，callback也会发生
        print("button clicked!")
    btn = st.button("Click me!", on_click=btn_click)  # click button就会执行function

    select = st.selectbox(label='whats your favorite car?', options=("Toyota", "Ford", "Honda"))

    # 注意multi-select我们最好加上一个button作为终点讯号
    multiselect = st.multiselect(label='whats your favorite brand?', options=("Google", "Highnote", "Amazon"))
    # 创建一个按钮
    multi_select_run_button = st.button("Run Multi-Select",)

    # 在按钮被点击时运行代码
    if multi_select_run_button:
        # 打印选中的汽车
        print(multiselect)
        st.write("Selected Cars:", multiselect)
        #print(multiselect)

    st.write("# Upload your file here")
    st.markdown("---")
    imgs = st.file_uploader(label='Upload your file here', 
                           type=['png', 'jpg', 'jpeg', 'gif'],
                           accept_multiple_files=True)
    if imgs:
        for img in imgs:
            st.image(img)

    slider_val = st.slider("this is a slider", min_value=0, max_value=100, value=20)
    print(slider_val)

    text_val = st.text_input("this is a text input", value="See something say somehting!", max_chars=250)

    text_val = st.text_area("this is a text area", value="See something say", max_chars=250)
    print(text_val)

    date_val = st.date_input("this is a date input", value="today")
    print(date_val)

    time_val = st.time_input("this is a time input", value = time(0, 0, 0))
    print(time_val)

    bar_val = st.progress(0)
    progress_status = st.empty()
    # for i in range(100):
    #     bar_val.progress(i+1)
    #     progress_status.write(f"progress: {i+1}%")
    #     ts.sleep(1)

    st.markdown('# User Registration', unsafe_allow_html=True)
    
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
    
    
    st.sidebar.write('this is my sidebar')
    opt = st.sidebar.radio('select any graph', options = ('line', 'bar'))

    fig = plt.figure()
    if opt == 'line': 
        plt.style.use("Solarize_Light2")
        plt.plot(x, np.sin(x))
        plt.plot(x, np.cos(x), '--')
    elif opt == 'bar': 
        plt.style.use("Solarize_Light2")
        plt.bar(x, x*10)

    st.write(fig)








             



    

if __name__ == "__main__":
    run()

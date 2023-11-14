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
import pandas as pd
import plotly.express as px

st.write("# Data Visualization")
st.write('---')

def print_name(x):
    st.write(x)
    #print(x)

def plot_line_chart():
    files = st.file_uploader(label='Upload your file here', type=['csv', 'xlsx'], accept_multiple_files=True)

    file_names = []
    if files:
        for file in files:
            file_names.append(file.name)
        selected_files = st.multiselect(label='Select files', options=file_names)

        df = pd.read_csv(file)
        selected_columns = st.multiselect(label='Select columns', options=df.columns.values.tolist())
        
        print(selected_columns)
        #st.write(df[selected_columns])
        #st.table(df[selected_columns])
        st.dataframe(df[selected_columns])

        x_axis_columns = st.selectbox(label='Select x-axis columns', options=selected_columns)
        y_axis_columns = st.selectbox(label='Select y-axis columns', options=selected_columns)
        
        plot_btn = st.button(label='Plot')
        if plot_btn:
            fig = px.bar(df[selected_columns], x = x_axis_columns, y = y_axis_columns)
            st.plotly_chart(fig)

        input = st.text_input('Enter a value')
        s_btn = st.button(label='Submit')
        if s_btn:
            s_checkbox = st.checkbox(label='Do you want to display your input?', on_change=print_name, args=(input,))
       
        
plot_line_chart()
        
        

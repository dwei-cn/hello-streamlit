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

st.write("# Callback")
st.markdown("> A `callback` is a python function which gets called when an input widget changes.")
st.markdown("在 Streamlit 中，`callback` 通常是与 `st.button`、`st.checkbox` 等交互性组件结合使用时，用于在用户与应用程序进行交互时触发特定的操作或功能，经常可能需要用到用户的input作为args。")
st.markdown("Check out this [link]([https://towardsdatascience.com/advanced-streamlit-session-state-and-callbacks-for-data-labelling-tool-1e4d9ad32a3f]) for more information.")
st.write('---')

# 检查语句的初始化很重要，由于每次click会rerun，直接设置st.session_state.projects的话每次都会reset
if 'projects' not in st.session_state:
    st.session_state.projects = [
        'Boring Project', 'Interesting Project'
]
st.session_state.current_project = st.radio(
    label='Select a project to work with:',
    options=st.session_state.projects,
)

# add projects
def check_added_project(project_name: str):
    """Callback function during clicking add project button (adding a new project)."""
    if project_name in st.session_state.projects:
        st.warning(f'Project {project_name} already exists.')
    else:
        st.session_state.projects.append(project_name)
        #st.session_state.current_project = project_name
        st.success(f'Added {project_name} to the list of projects.')

new_project = st.text_input(label='Enter a new project name:')   # 传入input作为argument
st.button('Add Project', on_click=check_added_project, args=(new_project,))


if st.button('Show Projects'):
    st.json(st.session_state.projects)


# del projects
def del_project(project_name: str):
    if project_name in st.session_state.projects:
        st.session_state.projects.remove(project_name)
        st.success(f'Removed {project_name} from the list of projects.')
    else:
        st.warning(f'Project {project_name} does not exist.')
to_del = st.selectbox(label='Select a project to delete:', options=st.session_state.projects)
st.button('Delete Project', on_click=del_project, args=(to_del,))

if st.button('Show Projects '): # 起一个和前面button不重复的名字
    st.json(st.session_state.projects)
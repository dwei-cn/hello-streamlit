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

st.write("# Session State")
st.markdown("> Session State is a way to share variables between reruns, for each user session.")
st.markdown("`Session State`主要就是在不同的rerun和refresh的操作之间储存variable，如果你不经常刷新page或者不怎么click某个button也不怎么需要用到，但是需要频繁click的话，就会很需要。")
st.write('---')
      
st.write("## An Example:")
# 初始化某个variable
if "Counter" not in st.session_state:
    st.session_state["Counter"] = 0

up = st.button("Click me up!")
if up:
    st.session_state["Counter"] += 1

down = st.button("Click me down!")
if down:
    st.session_state["Counter"] -= 1

reset = st.button("Reset")
if reset:
    st.session_state["Counter"] = 0

st.write(f"Counter: {st.session_state['Counter']}")

st.write('---')
st.markdown("""在 Streamlit 中，每次用户与应用进行交互（例如点击按钮）时，整个脚本会重新运行。因此，对于上述代码，每次用户点击按钮（"Click me up!"、"Click me down!"、"Reset"），整个脚本都会重新运行。这也包括 `st.session_state` 中的变量的重新初始化。

以下是每次用户点击按钮时的运行顺序：

1. **初始加载（首次访问应用）：**
   - `Counter` 变量不存在于 `st.session_state` 中，所以它会被初始化为 0。
   - 页面显示初始状态。

2. **点击 "Click me up!" 按钮：**
   - `up` 变量被设置为 True。
   - `st.session_state["Counter"]` 的值增加 1。
   - 页面重新运行，显示更新后的计数器值。

3. **点击 "Click me down!" 按钮：**
   - `down` 变量被设置为 True。
   - `st.session_state["Counter"]` 的值减少 1。
   - 页面重新运行，显示更新后的计数器值。

4. **点击 "Reset" 按钮：**
   - `reset` 变量被设置为 True。
   - `st.session_state["Counter"]` 的值被重置为 0。
   - 页面重新运行，显示更新后的计数器值。

每次用户与应用程序进行交互，整个脚本都会重新运行，因此 `st.session_state` 中的变量会在不同的按钮点击之间保持状态。
""")
        

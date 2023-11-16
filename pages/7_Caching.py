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
import numpy as np
import time
from transformers import pipeline

st.write("# Cache")
st.markdown("> `Caching` stores the results of slow function calls, so they only need to run once. This makes your app much faster and helps with persisting objects across reruns.")
st.markdown("`Caching`就是能记住之前的一些slow function calls，让我们每次rerun的时候减少运算和调用。")
st.markdown("- `st.cache_data`是缓存返回数据的计算的推荐方法：从CSV加载数据帧、转换NumPy数组、查询API或任何其他返回可序列化数据对象（str、int、float、DataFrame、array、list等）的函数。")
st.markdown("- `st.cache_resource`是缓存全局资源（如ML模型或数据库连接）的推荐方法–当你不想多次加载的不可序列化对象时可以使用它，st.cache_resource可以在应用的所有重新运行和会话之间共享这些资源。需要注意的是，对缓存返回值的任何更改都会直接改变缓存中的对象。")
st.write("实在不知道选啥就无脑`st.cache_data`就好")

st.write('---')

st.write("### Cache Data")
@st.cache_data  # 👈 Add the caching decorator
def load_data(url):
    st.write(time.time())
    df = pd.read_csv(url)
    return df

df = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
st.dataframe(df)

@st.cache_data(ttl=3600)
def transform(df):
    df = df.filter(items=['one', 'three'])
    df = df.apply(np.sum, axis=0)
    return df


st.code("""
connection = database.connect()
@st.cache_data
def query():
    return pd.read_sql_query("SELECT * from table", connection)

Initialize connection.
conn = st.connection("snowflake")

# Load the table as a dataframe using the Snowpark Session.
@st.cache_data
def load_table():
    session = conn.session()
    return session.table("mytable").to_pandas()

df = load_table()

# Print results.
for row in df.itertuples():
    st.write(f"{row.NAME} has a :{row.PET}:")
            """)


st.button("Rerun")


st.write("### Cache Resources")
st.write("#### ML Model")
st.code("""
@st.cache_resource  # 👈 Add the caching decorator
def load_model():
    return pipeline("sentiment-analysis")

model = load_model()

query = st.text_input("Your query", value="I love Streamlit! 🎈")
if query:
    result = model(query)[0]  # 👈 Classify the query text
    st.write(result)
""")

st.write("#### Database connections")
st.code("""
@st.cache_resource
def init_connection():
    host = "hh-pgsql-public.ebi.ac.uk"
    database = "pfmegrnargs"
    user = "reader"
    password = "NWDMCE5xdipIjRrp"
    return psycopg2.connect(host=host, database=database, user=user, password=password)

conn = init_connection()
            """)
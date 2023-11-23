import streamlit as st
import base64

# load background img
background_image_link = "./assets/cool-background.png"

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64(background_image_link)

## manage all css elements
with open('./assets/style_CSS2.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown(
    f"""
    <style>
        [data-testid="stAppViewContainer"] > .main{{
        background-image: url("data:image/png;base64,{img}");
        background-size: cover;
        background-attachment: local;
        }}
        
        [data-testid="stHeader"]{{
            background-color: white;
        }}

        [data-testid="stSidebar"] > div:first-child {{
            background-image: url("https://images.pexels.com/photos/255379/pexels-photo-255379.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2");
            opacity:100;
            background-position: center

        }}
            sada
    </style>
    """,
    unsafe_allow_html=True,
)


with st.container():
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "70 °F", "1.2 °F")
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "86%", "4%")


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



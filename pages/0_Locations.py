import streamlit as st
from streamlit_folium import st_folium
import folium
import pandas as pd
import base64

## manage all css elements
with open('./assets/style.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# load background img
background_image_link = "./assets/wedding.jpeg"

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64(background_image_link)

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

    </style>
    """,
    unsafe_allow_html=True,
    )

st.write("## Locations")
st.write("- $Sunset\ Garden\ Chapel\ 小教堂$")
st.write("[📍 3931 Sunset Rd, Las Vegas, NV 89120](https://www.google.com/maps/place/Sunset+Gardens/@36.070684,-115.0914899,17z/data=!3m1!4b1!4m6!3m5!1s0x80c8d0034d1f197d:0xf658fbefa1758df!8m2!3d36.070684!4d-115.088915!16s%2Fg%2F1tpc87fc?entry=ttu)")
st.write("- $Mott\ 32\ Las\ Vegas\ 餐厅$ ")
st.write("[📍 3325 S Las Vegas Blvd #206, Las Vegas, NV 89109](https://www.google.com/maps/place/Mott+32+Las+Vegas/@36.1248147,-115.1705473,17z/data=!3m2!4b1!5s0x80c8c43e5fe7780d:0xf87b9091b549198b!4m6!3m5!1s0x80c8c555a069355d:0x24660116790bf24d!8m2!3d36.1248147!4d-115.1679724!16s%2Fg%2F11fl7kthnx?entry=ttu)")
st.write("- $Las\ Vegas\ Harry\ Reid\ 国际机场$")
st.write("[📍 5757 Wayne Newton Blvd, Las Vegas, NV 89119](https://www.google.com/maps/place/Harry+Reid+International+Airport/@36.0831046,-115.1507772,17z/data=!3m1!4b1!4m6!3m5!1s0x80c8c59f1f049c5d:0x471359241ec41e1e!8m2!3d36.0831046!4d-115.1482023!16zL20vMDFtejJn?entry=ttu)")

st.markdown("")
st.write("### Map")
loc_data = pd.DataFrame({
    'latitude': [36.07082254199126, 36.07987114917208, 36.124979293296875],
    'longitude': [-115.08858239365492, -115.14882089925992,  -115.1676719855879],
    'location': ["chapel", "airport", "restaurant"],
    'address': ["Chapel: 3931 Sunset Rd, Las Vegas, NV 89120", 
                "Airport: 5757 Wayne Newton Blvd, Las Vegas, NV 89119", 
                "Restaurant: 3325 S Las Vegas Blvd #206, Las Vegas, NV 89109"],
    'icon': ['heart', 'plane', 'cutlery']
})

m_center = folium.Map(location=[36.11417527017081, -115.12921011803496], zoom_start=12.4)


for indice, row in loc_data.iterrows():
    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        tooltip=row['address'],
        icon=folium.Icon(icon=row['icon'], icon_color='red')
    ).add_to(m_center)



# folium.Marker(
#     location=[36.07082254199126, -115.08858239365492], 
#     #popup="Sunset Gardens Chapel, Las Vegas, NV",
#     tooltip="",
#     icon=folium.Icon(icon='heart', icon_color='red')

#     #icon=folium.DivIcon(html=f"""<div style="font-family: courier new; color: blue">{"Sunset Gardens Chapel"}</div>""")
# ).add_to(m_center)

st_data = st_folium(m_center, width=725)



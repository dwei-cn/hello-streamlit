import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder
from mitosheet.streamlit.v1 import spreadsheet
import json
#from utils.datatables import generate_html
#from utils.agstyler import PINLEFT, PRECISION_TWO, draw_grid


def generate_html(dataframe: pd.DataFrame, styles: dict = {}, entries: int = 10):
    # get the table HTML from the dataframe without index column
    table_html = dataframe.to_html(table_id="table", index=False)
    # construct the complete HTML with jQuery Data tables
    html = """
    <html>
    <head>
        <link href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.min.css" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css?family=Roboto:400,700&display=swap" rel="stylesheet"> <!-- Add this line to load Roboto font -->
        <style>
            /* Add CSS rules here */
            body {
                """ + styles.get("body", "font-family: 'Roboto', Arial, sans-serif;") + """ /* Apply Roboto font */
            }
            #table {
                """ + styles.get("table", "border-collapse: collapse;") + """ /* Remove table borders */
            }
            th, td {
                """ + styles.get("cell", "") + """ /* No additional font-family needed here */
                border: none; /* Remove cell borders */
                padding: 10px; /* Add padding to cells */
            }
            th:first-child, td:first-child {
                font: normal normal bold 16px/40px Roboto; /* Apply bold font style to first column */
                text-align: left; /* Left-align text in first column */
                letter-spacing: 0px; /* Set letter spacing */
                color: #333333; /* Set text color to grey */
                text-transform: capitalize; /* Capitalize text */
                opacity: 1; /* Set opacity */
            }
            th:not(:first-child), td:not(:first-child) {
                font: normal normal normal 16px/40px Roboto; /* Apply normal font style to other columns */
                text-align: left; /* Left-align text in other columns */
                letter-spacing: 0px; /* Set letter spacing */
                color: #333333; /* Set text color to grey */
                text-transform: capitalize; /* Capitalize text */
                opacity: 1; /* Set opacity */
            }
            tr:nth-child(odd) td {
                background-color: #FFFFFF; /* Set odd rows background color */
            }
            tr:nth-child(even) td {
                background-color: #F1F1F1; /* Set even rows background color */
            }
        </style>
    </head>
    <body>
    """ + table_html + """
    <script src="https://code.jquery.com/jquery-3.6.0.slim.min.js" integrity="sha256-u7e5khyithlIdTpu22PHhENmPcRdFiHRjhAuHcs05RI=" crossorigin="anonymous"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
    <script>
        function changeEntries() {
            var select = document.getElementById("entries");
            var selectedValue = select.value;
            $('#table').DataTable().page.len(selectedValue).draw();
        }

        $(document).ready( function () {
            $('#table').DataTable({
                "pageLength": """ + str(entries) + """,
                "paging": true,  // Enable pagination
            });
        });
    </script>
    </body>
    </html>
    """
    # return the html
    return html


st.set_page_config(layout='wide')
csv_path = "./assets/covid-variants.csv"


# 从文件中加载 session_state
def load_session_state():
    try:
        with open("./cache/session_state.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# 保存 session_state 到文件
def save_session_state(session_state):
    with open("./cache/session_state.json", "w") as f:
        json.dump(dict(session_state), f)


## body
st.title("Streamlit Tables")
st.markdown("---")

@st.cache_data
def data_upload():
    df = pd.read_csv(csv_path)
    return df

df = data_upload()

## Streamlit Default DataFrame Widget 
st.subheader('Streamlit Default DataFrame Widget')
st.dataframe(df.head())
st.info(df.shape)


## datatables
st.subheader('Streamlit DataTables')
st.markdown('https://datatables.net/')
html_table = generate_html(df)

# method 1: load html file to page
# Display the HTML content in Streamlit
st.components.v1.html(html_table)

# method 2: show the link of html file

# Create a hyperlink to the HTML file
#open("./assets/table.html", "w").write(html_table)

# Read the contents of the HTML file
#html_content = open("./assets/table.html", "r", encoding="utf-8").read()
# html_file_path = "./assets/table.html"
# abs_html_file_path = os.path.abspath(html_file_path)


# link_text = "View HTML File"
# link_url = f"file://{abs_html_file_path}"
# link_markdown = f"[{link_text}]({link_url})"

# Display the link using st.markdown
#st.markdown(link_markdown, unsafe_allow_html=True)
#st.markdown(f"<iframe src='data:text/html;base64,{html_table}' width='700' height='500'></iframe>", unsafe_allow_html=True)

#st.components.v1.html(html_table)
#st.markdown(html_table)
#st.info(df.shape)



## editable dfs
st.subheader("Streamlit Editable Dataframes")

#st.session_state = load_session_state()

df2 = pd.read_csv('./cache/table.csv')

# df2 = pd.DataFrame(
#     [
#         {"command": "st.selectbox", "rating": 4, "is_widget": True},
#         {"command": "st.balloons", "rating": 5, "is_widget": False},
#         {"command": "st.time_input", "rating": 3, "is_widget": True},
#     ]
# )
# df2['comments'] = None

edited_df = st.data_editor(
    df2, 
    key='my_key',
    num_rows="dynamic",
    use_container_width=True
    ) # 👈 An editable dataframe
#st.dataframe(df2, use_container_width=True)

# st.session_state["my_key"] = load_session_state()
favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

st.write("Here's the value in Session State:")
st.write(st.session_state) # 👈 Show the value in Session State
#st.write(st.session_state["my_key"]) # 👈 Show the value in Session State

update_btn = st.button("Update Table")
if update_btn:
    #save_session_state(st.session_state)
   pd.DataFrame(edited_df).to_csv('./cache/table.csv', index=False)
   

st.subheader('Streamlit with [Mito Spreadsheet](https://www.youtube.com/watch?v=Lxj4GfJCvxA)')
st.write("▶️ [Mito Spreadsheet Docs](https://blog.streamlit.io/data-analysis-with-mito-a-powerful-spreadsheet-in-streamlit/)")
# Display the dataframe in a Mito spreadsheet
final_dfs, code = spreadsheet(df)

# Display the final dataframes created by editing the Mito component
# This is a dictionary from dataframe name -> dataframe
#st.write(final_dfs)

# Display the code that corresponds to the script
#st.code(code)

st.subheader('Streamlit with AgGid Table 1 (Original, Not good with big data)')
AgGrid(df.head())

st.subheader('Streamlit with AgGid Table 2 (GridOptionsBuilder)')
#AgGrid(df.head())
gd = GridOptionsBuilder.from_dataframe(df)
gd.configure_pagination(enabled=True)
gd.configure_default_column(editable=True, groupable=True)
#gd.configure_auto_height(autoHeight = True)
#sel_mode = st.radio("Selection Type", options= ['single', 'multiple'])
#gd.configure_selection(selection_mode = sel_mode, use_checkbox=True)

gridoptions = gd.build()
grid_table = AgGrid(
    df,
    gridOptions=gridoptions,
    update_mode=GridUpdateMode.SELECTION_CHANGED | GridUpdateMode.VALUE_CHANGED,
    #fit_columns_on_grid_load = True,
    height=min(500, (1 + len(df.index)) * 29),
    #height=20,
    reload_data = True,
    enable_quicksearch = True,
    custom_css={
        "#gridToolBar": {
            "padding-bottom": "0px !important",
        }
    }

    )
sel_row = grid_table["selected_rows"]
st.write(sel_row)



st.subheader('Streamlit with [Google Sheet](https://www.youtube.com/watch?v=RKj7kzQY7OQ)')
st.markdown(
    """
    <iframe 
    src="https://docs.google.com/spreadsheets/d/e/2PACX-1vQSYaoiFmcem4jgp2nfXVML6Yd15UkmUg2I7ppYR82SGld0YUGV5Jj3vdwxLrsqNgPFml-wzP5OZseZ/pubhtml?widget=true&amp;headers=false"
    width=1050
    height=600>
    </iframe>
    
    """,
    unsafe_allow_html=True
)





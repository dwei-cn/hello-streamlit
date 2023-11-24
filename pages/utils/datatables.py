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

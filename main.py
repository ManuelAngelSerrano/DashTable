import dash
import dash_table
import pandas as pd

## df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
df = pd.read_csv('./solar.csv')

app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    id='table-interactivity',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
    filter_action="native",
    sort_action="native",
    sort_mode="multi",
    column_selectable="single",
    row_selectable="multi",
    row_deletable=True,
    selected_columns=[],
    selected_rows=[],
    page_action="native",
    page_current=0,
    page_size=10,
)

if __name__ == '__main__':
    app.run_server(debug=True)

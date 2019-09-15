import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#b1f2c2',
    'text': '#4c524d'
}

app.layout = html.Div([

    html.H2('Hello Dash',
            style={
                'color': colors['text'],
                'textAlign': 'center'
            }),

    html.Div('Dash: A web application framework for Python',
             style={
                 'color': colors['text'],
                 'textAlign': 'center'
             }),

    dcc.Graph(
        figure=go.Figure([
            go.Bar(
                x=['2017', '2018', '2019'],
                y=[150, 180, 220],
                marker_color='#9ed6f0',
                marker_line_color='#4c524d',
                marker_line_width=5,
                name='lokalnie'
            ),
            go.Bar(
                x=['2017', '2018', '2019'],
                y=[160, 100, 280],
                marker_color='#077eb5',
                marker_line_color='#4c524d',
                marker_line_width=5,
                name='online'
            )],
            layout=go.Layout(
                title='Wizualizacja danych',
                plot_bgcolor=colors['background'],
                paper_bgcolor='#08825f'
            )
        )
    )

], style={'backgroundColor': colors['background']})

if __name__ == '__main__':
    app.run_server(debug=True)
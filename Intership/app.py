import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import pandas as pd
import numpy as np
import joblib
import base64
import io

# Constants
MODEL_PATH = 'models/Random_Forest.pkl'
USD_TO_INR = 83.5
FONT_LINK = "https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap"

# Load the model once at startup
model = joblib.load(MODEL_PATH)

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Real Estate Price Predictor"
server = app.server  # For deployment

# Define reusable styles
STYLES = {
    'container': {
        'backgroundColor': '#1c2230',
        'fontFamily': 'Roboto, sans-serif',
        'minHeight': '100vh',
        'padding': '50px 20px',
        'color': '#ecf0f1',
    },
    'header': {
        'textAlign': 'center',
        'fontSize': '38px',
        'fontWeight': '700',
        'marginBottom': '40px',
        'color': '#ffffff'
    },
    'upload_box': {
        'width': '100%',
        'maxWidth': '450px',
        'margin': '0 auto 20px',
        'padding': '15px',
        'borderWidth': '2px',
        'borderStyle': 'dashed',
        'borderRadius': '8px',
        'textAlign': 'center',
        'cursor': 'pointer',
        'backgroundColor': '#fff',
        'color': '#34495e',
        'fontWeight': '600',
        'lineHeight': 'normal',
        'transition': 'border-color 0.3s ease'
    },
    'input_form': {
        'backgroundColor': '#ffffff',
        'padding': '30px',
        'borderRadius': '12px',
        'boxShadow': '0 4px 16px rgba(0,0,0,0.1)',
        'maxWidth': '450px',
        'margin': '20px auto',
        'display': 'none',
        'color': '#34495e'
    },
    'label': {
        'display': 'block',
        'fontWeight': '600',
        'marginBottom': '6px',
        'fontSize': '16px',
    },
    'input': {
        'width': '100%',
        'padding': '10px',
        'marginBottom': '20px',
        'fontSize': '16px',
        'borderRadius': '6px',
        'border': '1px solid #ccc',
        'boxSizing': 'border-box'
    },
    'dropdown': {
        'marginBottom': '20px'
    },
    'button': {
        'width': '100%',
        'padding': '14px',
        'fontSize': '18px',
        'color': '#fff',
        'backgroundColor': '#007BFF',
        'border': 'none',
        'borderRadius': '6px',
        'cursor': 'pointer',
        'fontWeight': '700',
        'transition': 'background-color 0.3s ease',
        'outline': 'none',
    },
    'button_disabled': {
        'backgroundColor': '#a3c0f9',
        'cursor': 'not-allowed',
    },
    'feedback': {
        'textAlign': 'center',
        'fontWeight': '600',
        'marginTop': '12px'
    },
    'error_text': {
        'color': '#e74c3c',
        'fontSize': '18px',
        'backgroundColor': '#fff',
        'padding': '15px',
        'borderRadius': '10px',
        'boxShadow': '0 2px 10px rgba(0,0,0,0.1)'
    },
    'success_text': {
        'color': '#2ecc71',
        'fontSize': '20px',
        'fontWeight': '700',
        'marginBottom': '15px',
    },
    'prediction_box': {
        'backgroundColor': '#ffffff',
        'padding': '30px',
        'borderRadius': '12px',
        'boxShadow': '0 4px 16px rgba(0,0,0,0.1)',
        'maxWidth': '500px',
        'margin': '40px auto',
        'color': '#34495e',
        'textAlign': 'center',
    },
    'footer': {
        'textAlign': 'center',
        'color': '#bdc3c7',
        'marginTop': '60px',
        'fontSize': '16px',
        'fontWeight': '700',
        'letterSpacing': '1px'
    }
}

# Layout
app.layout = html.Div([
    # External font
    html.Link(rel='stylesheet', href=FONT_LINK),

    # Header
    html.H1("Real Estate Price Predictor", style=STYLES['header']),

    # Upload
    dcc.Upload(
        id='upload-data',
        children=html.Div(['📂 Drag and Drop or ', html.A('Select an Excel File (.xlsx)')]),
        style=STYLES['upload_box'],
        multiple=False
    ),

    html.Div(id='upload-feedback', style=STYLES['feedback']),

    # Input form - initially hidden
    html.Div([
        html.Label("Location", style=STYLES['label']),
        dcc.Dropdown(
            id='location-dropdown',
            options=[
                {'label': 'Downtown', 'value': 'Downtown'},
                {'label': 'Suburb', 'value': 'Suburb'},
                {'label': 'Uptown', 'value': 'Uptown'}
            ],
            placeholder="Select a location",
            style=STYLES['dropdown']
        ),

        html.Label("Size (sqft)", style=STYLES['label']),
        dcc.Input(
            id='input-size',
            type='number',
            placeholder="Enter size",
            style=STYLES['input']
        ),

        html.Label("Rooms", style=STYLES['label']),
        dcc.Input(
            id='input-rooms',
            type='number',
            placeholder="Enter number of rooms",
            style=STYLES['input']
        ),

        html.Button(
            "Predict Price",
            id='predict-button',
            n_clicks=0,
            style=STYLES['button'],
            disabled=True
        )
    ], id='input-form', style=STYLES['input_form']),

    # Prediction output
    html.Div(id='output-prediction'),

    # Footer
    html.Div("Developed by Darshan M N", style=STYLES['footer'])
], style=STYLES['container'])


def parse_excel(contents):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        df = pd.read_excel(io.BytesIO(decoded))
        return df, None
    except Exception as e:
        return None, str(e)


@app.callback(
    Output('upload-feedback', 'children'),
    Output('input-form', 'style'),
    Input('upload-data', 'contents')
)
def handle_file_upload(contents):
    if contents is None:
        return "", STYLES['input_form'].copy() | {'display': 'none'}

    df, error = parse_excel(contents)
    if error:
        return f"❌ Error reading Excel file: {error}", STYLES['input_form'].copy() | {'display': 'none'}

    return "✅ Excel file uploaded successfully! You can now enter details and predict.", STYLES['input_form'].copy() | {'display': 'block'}


@app.callback(
    Output('predict-button', 'disabled'),
    Input('location-dropdown', 'value'),
    Input('input-size', 'value'),
    Input('input-rooms', 'value')
)
def toggle_predict_button(location, size, rooms):
    if location and size and rooms:
        return False
    return True


@app.callback(
    Output('output-prediction', 'children'),
    Input('predict-button', 'n_clicks'),
    State('location-dropdown', 'value'),
    State('input-size', 'value'),
    State('input-rooms', 'value')
)
def predict_price(n_clicks, location, size, rooms):
    if n_clicks == 0:
        return ""

    if not location or size is None or rooms is None:
        return html.Div(
            "❌ Please fill all fields to get prediction.",
            style=STYLES['error_text']
        )

    # One-hot encoding for location
    location_suburb = 1 if location == 'Suburb' else 0
    location_uptown = 1 if location == 'Uptown' else 0

    features = np.array([[size, rooms, location_suburb, location_uptown]])
    try:
        predicted_usd = model.predict(features)[0]
        predicted_inr = predicted_usd * USD_TO_INR
    except Exception as e:
        return html.Div(
            f"❌ Prediction failed: {e}",
            style=STYLES['error_text']
        )

    return html.Div([
        html.Div("✅ Prediction Complete", style=STYLES['success_text']),
        html.Div(f"Predicted Price (USD): ${predicted_usd:,.2f}", style={'fontSize': '22px', 'color': '#2980b9', 'marginBottom': '10px'}),
        html.Div(f"Predicted Price (INR): ₹{predicted_inr:,.2f}", style={'fontSize': '24px', 'color': '#f39c12', 'fontWeight': '700'})
    ], style=STYLES['prediction_box'])


if __name__ == '__main__':
    app.run(debug=True)

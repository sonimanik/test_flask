from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return '<a href="/redirect"><button>Click me to redirect</button></a>'

@app.route('/redirect')
def redirect_to_url():
    return redirect("https://exusia-streamlit.azurewebsites.net")

if __name__ == '__main__':
    app.run(debug=True)

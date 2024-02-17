from flask import Flask, render_template, request

app = Flask(__name__)

@app.route ('')

def convert():
    order1 = request.form['order1']
from flask import Flask, render_template, request
import main
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.route('/', methods=['POST'])


def convert():
    enterlocation1 = request.form['enterlocation1']
    enterlocation2 = request.form['enterlocation2']
    if enterlocation1:
        str1 = main.set(enterlocation1,1)
        return render_template('index.html', str1 = str1)
    else:
        str2 = main.set(enterlocation2,0)
        return render_template('index.html', str2 = str2)

if __name__ == '__main__':
    app.run(debug=True)

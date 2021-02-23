from flask import Flask, render_template, \
     request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def up():
    palavra = None
    palavra = request.form['palavra']
    if request.method == 'POST':
        if request.form['palavra'] != '':
            palavra = palavra.upper()
    return render_template('index.html', palavra=palavra)

if __name__ == "__main__":
    app.run(debug=True ,host="0.0.0.0")

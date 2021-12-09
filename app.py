from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/aboutme')
def about():
    return render_template('aboutme.html')

@app.route('/contactinfo')
def contact():
    return render_template('')

@app.route('/portfolio')
def portfolio():
    return render_template('')

if __name__ == "__main__":
    app.run(debug=True)

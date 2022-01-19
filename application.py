from flask import Flask, render_template, request


application = Flask(__name__)


@application.route('/')
@application.route('/home')
def index():
    return render_template('index.html')


@application.route('/aboutme')
def about():
    return render_template('aboutme.html')


@application.route('/contactinfo')
def contact():
    return render_template('contactinfo.html')


@application.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


@application.route('/form', methods=['POST'])
def form():
    name = request.form.get("name")
    email = request.form.get("email")
    msg = request.form.get("message")
    # store into mongoDB
    return render_template('form.html', name=name)


if __name__ == "__main__":
    application.run(debug=True)

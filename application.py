from flask import Flask, render_template, request
import smtplib
import os

application = Flask(__name__)

gmail_user = os.environ.get('EMAIL_USER')
gmail_pass = os.environ.get('mongo_pass')


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
    email_msg = f"Subject: Connection\n\n{name} @ {email} has sent a message: {msg}"
    print(email_msg)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(gmail_user, gmail_pass)
    server.sendmail(gmail_user, gmail_user, email_msg)

    return render_template('form.html', name=name)


if __name__ == "__main__":

    application.run(debug=True)

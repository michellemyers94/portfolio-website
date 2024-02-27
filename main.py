import os
from flask import Flask, url_for, render_template, request, redirect, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
# app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.j2')


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.j2')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message_body = request.form['message_body']

        msg = Message("Contact Form Submission for DevMichelle", sender=email,
                      recipients=['michelleliumyers@gmail.com'])
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message_body}"
        mail.send(msg)

        flash('Message sent successfully!', 'success')
        return redirect(url_for('index'))
    else:
        return render_template('contact.j2')


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, url_for, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.j2')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.j2')

@app.route('/contact')
def contact():
    return render_template('contact.j2')

if __name__ == '__main__':
    app.run(debug=True)

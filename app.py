from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def register():
    return render_template('register.html')


def submit():
    fname = request.register.get('register')
    return redirect(url_for('welcome'))


def welcome():
    return render_template('welcome.html', fname=register)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/register')
def register():
    return render_template('register')

@app.route('/submit', methods=['POST'])
def submit():
    fname = request.form.get('fname')
    return redirect(url_for('welcome', fname=fname))

@app.route('/welcome')
def welcome():
    fname = request.args.get('fname')
    return render_template('welcome.html', fname=fname)

if __name__ == '__main__':
    app.run(debug=True)

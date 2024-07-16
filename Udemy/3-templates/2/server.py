from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/thank_you', methods=['POST'])
def thank_you():
    print(request.args)
    email = request.form['email']
    password = request.form['password']
    return render_template('thank_you.html', email=email, password=password)


app.run(debug=True)

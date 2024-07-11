from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World<h1/>'


@app.route('/about')
def about():
    return '<h1>This is About</h1>'


@app.route('/forget/<name>')
def forget(name):
    return f'<h1>Forget {name}</h1>'


@app.route('/puppy_latin/<name>')
def pappy_latin(name):
    if name[-1] == 'y':
        return '<h1>Puppy Name is {}</h1>'.format(name[:-1]+'iful')
    else:
        return '<h1>Puppy Name is {}</h1>'.format(name[:-1]+'y')


if __name__ == '__main__':
    app.run(debug=True)

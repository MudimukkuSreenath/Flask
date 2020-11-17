from flask import Flask

ob = Flask(__name__)
@ob.route('/')
def index():
    return "<html><body><h1>Welcome to index page</h1></body></html>"


@ob.route('/sreenath')
def sreenath():
    return "<html><body><h1>Welcome to sreenath page</h1></body></html>"


if __name__ == '__main__':
    ob.run(debug=True)

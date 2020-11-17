from flask import Flask
ob = Flask(__name__)
@ob.route('/')
def index():
    return "<html><body><h1>Welcome to index page</h1></body></html>"
ob.add_url_rule('/index','index',index)
if __name__ == '__main__':
    ob.run(debug=True)

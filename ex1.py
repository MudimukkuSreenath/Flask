from  flask import Flask
ob=Flask(__name__)
@ob.route('/')
def index():
    return "<html><body><h1>Welcome to flask</h1>?</body></html>"
if __name__=='__main__':
    ob.run(debug=True)
    
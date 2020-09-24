from flask import Flask

application = Flask(__name__)

application.debug = True

@application.route('/', methods=['GET'])
def hello():
 return '<p>Hello world</p>'

@application.route('/aboutUs', methods=['GET'])
def welcome():
 return '<p>Welcome to our application!</p>'
if __name__ == "__main__":
 application.run()
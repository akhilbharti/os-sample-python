from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h2>Hello Worldccxvxcvd!</h2>"

if __name__ == "__main__":
    application.run()

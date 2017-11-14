from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/351449/charts/1?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&title=Temperature&type=spline&xaxis=Time&yaxis=Temperature&yaxismax=50&yaxismin=0"></iframe>"

if __name__ == "__main__":
    application.run()

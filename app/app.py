from flask import Flask
from datetime import datetime

app = Flask("app")

def gethtml():
    return '<html><body><h1>I am a python flask web application!</h1><div>' + str(datetime.now()) + '</div></body></html>'

@app.route("/")
def index():
    return gethtml()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
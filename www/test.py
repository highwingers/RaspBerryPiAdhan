from flask import Flask
from views.address import address_blueprint


app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World! 2"

if __name__ == '__main__':
    app.run()


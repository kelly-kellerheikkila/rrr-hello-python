from flask import Flask
from flask.ext.restful import Api
from .hello import HelloAPI

app = Flask(__name__)
app.config.from_pyfile('../config.py')

api = Api(app)
api.add_resource(HelloAPI, '/hello', '/hello/<string:name>')

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
  response.headers.add('Access-Control-Allow-Methods', 'OPTIONS,GET')
  return response


if __name__ == '__main__':
    app.run(debug=True)


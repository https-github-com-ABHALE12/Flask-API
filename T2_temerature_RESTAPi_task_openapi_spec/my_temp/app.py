from flask import Flask
from flask_restx import Resource, Api, fields
from flask import Flask, request
from requests import put, get
import json
import datetime

app = Flask(__name__)
api = Api(app)


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


my_model = api.model('MyModel', {
    'Timestamp': fields.String(required=True),
    'Temperature': fields.Integer(min=0),
    'Description': fields.String
})


@api.route('/my_resource/<int:Temperature>,<Description>', endpoint='/my_resource')
@api.doc(params={'Temperature': 'specify Temperature', 'Description': 'Mention Description'})
class MyResource(Resource):
    @api.doc(model=my_model)
    def post(self, Temperature, Description):
        x = datetime.datetime.now()
        x = str(x)
        return {"Timestamp": x, 'Temperature': "{0}°C".format(Temperature), "Description": Description}


if __name__ == '__main__':
    app.run(debug=True)

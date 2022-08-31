from flask import Flask
from flask_restx import Resource, Api, fields
from flask import Flask, request
from requests import put, get
import json
import datetime
from marshmallow import Schema, fields as ma_fields, post_load

app = Flask(__name__)
api = Api(app)


# @api.route('/hello')
# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}

class data(object):
    def __init__(self, Temperature, Description):
        self.Temperature = Temperature
        self.Description = Description

    def __repr__(self) -> str:
        return '{} is the Temperature.{} is the Description.'.format(self.Temperature, self.Description)


class dataSchema(Schema):
    'Timestamp': fields.String(required=True)
    'Temperature': fields.Integer(min=0)
    'Description': fields.String

    @post_load
    def create_data(self, data):
        return data(**data)


# my_model = api.model('MyModel', {
#     'Timestamp': fields.String(required=True),
#     'Temperature': fields.Integer(min=0),
#     'Description': fields.String
# })
data = []


@api.route('/temp')
class data(Resource):

    # @api.marshal_with(my_model)
    # def get(self):
    #     return data

    @api.expect(my_model)
    def post(self):
        for ele in my_model:
            data.append(my_model['Timestamp'])
            data.append(my_model['Temperature'])
            data.append(my_model['Description'])
        return {'result': data}, 201


if __name__ == '__main__':
    app.run(debug=True)

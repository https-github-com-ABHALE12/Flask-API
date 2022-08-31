
# from api import app # Flask instance of the API
from app import app
import json
# from flask_pytest_example.handlers.routes import configure_routes
# from flask import Flask


def get_info():
    response = app.test_client().get('/Get_info')
    res = json.loads(response.data.decode('utf-8')).get("Info")
    assert type(res[0]) is list
    assert res[0][0] == 'Sonali'
    assert response.status_code == 200
    assert type(res) is list

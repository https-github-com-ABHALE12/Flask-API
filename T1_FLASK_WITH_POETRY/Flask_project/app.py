from distutils.log import info
import json
import sqlite3
from pydantic import BaseModel

from flask_pydantic import validate
from flask import Flask, jsonify, render_template, request
from typing import Optional
# from flask_pytest_example.handlers.routes import configure_routes


app = Flask(__name__)


# @app.route("/")
# def main():
#     return "Connection is Succesfull!!!!!"


@app.route("/Register", methods=["POST"])
def Register():
    if request.method == "POST":
        data = request.get_json()
        PRN_NO = data['PRN_NO']
        F_NAME = data['F_NAME']
        EMAIL_ID = data['EMAIL_ID']
        MOBILE = data['MOBILE']

        con = sqlite3.connect(
            r"c:\Users\hp\Documents\Celebal_Technology\Data_Scientist\Tasks\flask_database2_SQLite\Registration.db")
        cur = con.cursor()
        # cur.execute("""CREATE TABLE student(fname varchar)""")
        cur.execute("""INSERT INTO Register(PRN_NO,F_NAME,EMAIL_ID,MOBILE)values(?,?,?,?)""",
                    (PRN_NO, F_NAME, EMAIL_ID, MOBILE))
        # cur.execute("""INSERT INTO Register(PRN_NO,F_NAME,EMAIL_ID,MOBILE)values("%S","%s","%s","%s")"""(PRN_NO,F_NAME,EMAIL_ID,MOBILE))
        con.commit()
        return {"Response": "Successful"}


@app.route("/Get_info", methods=["GET"])
def Get_info():
    if request.method == "GET":
        # data=request.get_json()
        con = sqlite3.connect(
            r"C:\Users\hp\Documents\Celebal_Technology\Data_Scientist\Tasks\flask_database2_SQLite\Registration.db")
        cur = con.cursor()
        cur.execute("""SELECT * FROM Register""")
        info = cur.fetchall()
        con.commit()
        return {"Info": info}


@app.route("/DELETE_info/<id>", methods=["POST"])
def Delete_info(id):
    if request.method == "POST":
        # data=request.get_json()
        con = sqlite3.connect(
            r"C:\Users\hp\Documents\Celebal_Technology\Data_Scientist\Tasks\flask_database2_SQLite\Registration.db")
        cur = con.cursor()
        cur.execute("""DELETE FROM Register WHERE PRN_NO =="%s" """ % id)
        cur.execute("""SELECT * FROM Register""")
        info = cur.fetchall()
        con.commit()
        return {"Info:": info}


class requestModel(BaseModel):
    # age: int
    PRN_NO: int
    F_NAME: str
    EMAIL_ID: str
    MOBILE: str


class responseModel(BaseModel):
    # age: int
    pRN_NO: int
    f_NAME: str
    eMAIL_ID: str
    mOBILE: str


@app.route("/valid", methods=["POST"])
@validate()
def valid(form: requestModel):
    PRN_NO = form.PRN_NO
    F_NAME = form.F_NAME
    EMAIL_ID = form.EMAIL_ID
    MOBILE = form.MOBILE
    return responseModel(PRN_NO=PRN_NO, F_NAME=F_NAME, EMAIL_ID=EMAIL_ID, MOBILE=MOBILE)


if __name__ == '__main__':
    app.run(debug=True)


# when we are renedering the html template in that case method select as GET

# ****************
# 1.Post Method Register student method
# Note : 1. we can write filed name as well or we cannot inside insert command
    # 2.inside the body of postman
    # a.If we select form-data filled in that case inside app.py filed we request for the request.get(name) filled and type key and value filed inside the body section
    # b.If we select raw data filled in that case select json filled and type the data inside the body in json format

 # data = request.form.get('name')


#  *******************************
# 1.Get method for getting data from table
#     a.go body <ra<json
#     whatever info is avalable inside inside table is return

# *****************************************

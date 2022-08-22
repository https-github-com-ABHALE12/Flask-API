# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
import sqlite3

from flask import Flask, request

app = Flask(__name__)
# @app.route("/")
# def index():
# return "string is working"


@app.route("/submit", methods=["POST"])
def save_details():
    """used to store details in database"""
    if request.method == "POST":
        data = request.get_json()
        fname = data['fname']
        lname = data['lname']
        roll_no = data['roll_no']
        phone = data['phone']
        con = sqlite3.connect("student.db")
        cur = con.cursor()
        # cur.execute("""CREATE TABLE student(fname varchar)""")
        cur.execute("""INSERT INTO student1(fname,lname,roll_no,phone)
        values(?,?,?,?)""", (fname, lname, roll_no, phone))
        con.commit()
        return {"Response":"Successful"}


@app.route("/getdata", methods=["GET"])
def get_details():
    """used to get details from database"""
    if request.method == "GET":
        # data=request.get_json()
        con = sqlite3.connect("student.db")
        cur = con.cursor()
        # cur.execute("""CREATE TABLE student(fname varchar)""")
        cur.execute("""SELECT * FROM student1""")
        a_data = cur.fetchall()
        con.commit()
        return {"DATA:": a_data}


if __name__ == "__main__":
    app.run(debug=True)

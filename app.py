from distutils.log import info
import json
import sqlite3
from flask import Flask ,jsonify,render_template,request


app = Flask(__name__) 
@app.route("/")  
def main():  
    return "Connection is Succesfull!!!!!"
 
@app.route("/Register",methods = ["POST"])  
def Register():   
    if request.method == "POST":  
        data=request.get_json()
        PRN_NO=data['PRN_NO']
        F_NAME=data['F_NAME']
        EMAIL_ID=data['EMAIL_ID']
        MOBILE=data['MOBILE']
        
        con=sqlite3.connect(r"c:\Users\hp\Documents\Celebal_Technology\Data_Scientist\Tasks\flask_database2_SQLite\Registration.db")
        cur=con.cursor()
        # cur.execute("""CREATE TABLE student(fname varchar)""")
        cur.execute("""INSERT INTO Register(PRN_NO,F_NAME,EMAIL_ID,MOBILE)values(?,?,?,?)""",(PRN_NO,F_NAME,EMAIL_ID,MOBILE))
        # cur.execute("""INSERT INTO Register(PRN_NO,F_NAME,EMAIL_ID,MOBILE)values("%S","%s","%s","%s")"""(PRN_NO,F_NAME,EMAIL_ID,MOBILE))
        con.commit()
        return {"Response":"Successful"}

@app.route("/Get_info",methods = ["GET"])  
def Get_info():  
    if request.method == "GET":  
        # data=request.get_json()
        con=sqlite3.connect(r"C:\Users\hp\Documents\Celebal_Technology\Data_Scientist\Tasks\flask_database2_SQLite\Registration.db")
        cur=con.cursor()
        cur.execute("""SELECT * FROM Register""")
        info=cur.fetchall()
        con.commit()
        return {"Info:":info}
    
@app.route("/DELETE_info/<id>",methods = ["POST"])
def Delete_info(id):
      if request.method == "POST":  
        # data=request.get_json()
        con=sqlite3.connect(r"C:\Users\hp\Documents\Celebal_Technology\Data_Scientist\Tasks\flask_database2_SQLite\Registration.db")
        cur=con.cursor()
        cur.execute("""DELETE FROM Register WHERE PRN_NO =="%s" """ %id)
        cur.execute("""SELECT * FROM Register""")
        info=cur.fetchall()
        con.commit()
        return {"Info:":info}




    
    
    
    
    
    
        """name = request.form["Fname"]  
        # lname = request.form["Lname"]  
        # phone = request.form["Phone"]  
        with sqlite3.connect("student1.db") as con:  
            cur = con.cursor()  
            # cur.execute("CREATE TABLE student (fname varchar(20))")
            # cur.execute('''create table student(Fname, Lname, Phone)''')
            cur.execute('''INSERT into student(fname) values (?)''',(name))  
            # cur.execute("select * from student")
            # a=cur.fetchall()
            # print(a)
            con.commit()  
            msg = "student successfully Added"  """

if __name__ == '__main__': 
    app.run(debug = True)
    
# when we are renedering the html template in that case method select as GET     

# ****************
# 1.Post Method Register student method
#Note : 1. we can write filed name as well or we cannot inside insert command
                # 2.inside the body of postman 
                    # a.If we select form-data filled in that case inside app.py filed we request for the request.get(name) filled and type key and value filed inside the body section
                    # b.If we select raw data filled in that case select json filled and type the data inside the body in json format
                    
 # data = request.form.get('name')  
 
 
 
#  *******************************
# 1.Get method for getting data from table
#     a.go body <ra<json
#     whatever info is avalable inside inside table is return  

# *****************************************
 
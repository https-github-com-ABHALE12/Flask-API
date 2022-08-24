from flask import Flask,render_template,request
import pickle
from datetime import datetime
import sqlite3

sentiments=["Negative","Some what negative","Neutral","Some what positive","Positive"]
with open(r'model_pkl' , 'rb') as f:
    model = pickle.load(f)


app=Flask(__name__)

#####################################Aniruddha################################
@app.route('/new',methods=["POST"])
def new():
    if request.method=='POST':
        data=request.get_json()
        Name=data['Name']
        Address=data['Address']

        con = sqlite3.connect('example.db')
        cur = con.cursor()

        def Insert(a,b):
            cur.execute('''INSERT INTO Information(Name, Address) VALUES("%s","%s")''' % (a,b))

        Insert(Name,Address)
        con.commit()
    return "Successful"

@app.route("/info",methods = ["GET"])  
def info():  
    if request.method == "GET":  
        con=sqlite3.connect(r"example.db")
        cur=con.cursor()
        cur.execute("""SELECT * FROM Information""")
        data=cur.fetchall()
        con.commit()
        return {"Records":data}

###########################################Sonali##################################################

'''
Student can register with PRN_NO,F_NAME,EMAIL_ID,MOBILE in registration.db database
'''
@app.route("/Register",methods = ["POST"])  
def Register():   
    if request.method == "POST":  
        data=request.get_json()
        PRN_NO=data['PRN_NO']
        F_NAME=data['F_NAME']
        EMAIL_ID=data['EMAIL_ID']
        MOBILE=data['MOBILE']
        con=sqlite3.connect(r"Registration.db")
        cur=con.cursor()
        # cur.execute("""CREATE TABLE student(fname varchar)""")
        cur.execute("""INSERT INTO Register(PRN_NO,F_NAME,EMAIL_ID,MOBILE)values(?,?,?,?)""",(PRN_NO,F_NAME,EMAIL_ID,MOBILE))
        con.commit()
        return {"Response":"Successful"}

 #Return the data in the form of JSON using GET method
@app.route("/Get_info",methods = ["GET"])  
def Get_info():  
    if request.method == "GET":  
        con=sqlite3.connect(r"Registration.db")
        cur=con.cursor()
        cur.execute("""SELECT * FROM Register""")
        info=cur.fetchall()
        con.commit()
        return {"Info:":info}

##########################################Aniket#################################################
@app.route('/submit',methods=["POST"])
def submit():
    '''
    This method will be called when we want to post the data.
    So This method will post the review and return the appropriate sentiment of the review
    '''
    if request.method=='POST':
        # Getting the details in json format using postman
        date1=datetime.now()
        data=request.get_json()
        review=data['review']
        res=(model.predict([review])) #Model doing prediction
        res=sentiments[res[0]]        # converting the output of int to string in list sentiments
        res=str(res) #typecasting
        print(res) #printing result to terminal
        connection=sqlite3.connect("details2.db") #Connecting to the database
        cursor=connection.cursor() #Creating cursor
        #Executing the query
        cursor.execute("""INSERT INTO details(review,result,timedetails) VALUES(?,?,?)"""  ,(review,res,date1,)) 
        #Closing the connection
        connection.commit()
        #Returning result in Json format
        return {"response": res}

@app.route('/getting',methods=["GET"])
def getting():
    '''
    This method will be using GET method.
    This method return the data in the database in the form of JSON
    '''
    #Creating connection and cursor
    connection=sqlite3.connect("details2.db")
    cursor=connection.cursor()
    # Executing query
    cursor.execute("""SELECT * FROM details""")
    A=cursor.fetchall()
    connection.commit()
    # returning the result
    return{"response":A}


###########################################Dipti#################################################
#push method for student info
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
#get method for student info
@app.route("/getdata", methods=["GET"])
def get_details():
    """used to get details from database"""
    if request.method == "GET":
        con = sqlite3.connect("student.db")
        cur = con.cursor()
        cur.execute("""SELECT * FROM student1""")
        a_data = cur.fetchall()
        con.commit()
        return {"DATA:": a_data}

#################################################################
if __name__=='__main__':
    app.run(debug=True)

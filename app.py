"""
Aniket Jawale
Jr. Data Science Associate
Celebal Technologies
aniket.jawale@celebaltech.com
"""
"""
List of Tasks:

1.Virtual Envirnment Created
2.Used poetry
3.Used pytest
4.Downloaded Requirenment.txt using freeze
5.Connected Flask
6.Connection with sqlite3 (File used:details.db)
7.Used Postman
8.Used sentiment analysis project to deploy using flask
"""

#importing necesary libraries
from flask import Flask,render_template,request
import pickle
import sqlite3
from datetime import datetime
#creating list 
sentiments=["Negative","Some what negative","Neutral","Some what positive","Positive"]

# load saved model
with open(r'model_pkl' , 'rb') as f:
    model = pickle.load(f)

#Creating Flask API
app=Flask(__name__)
#Post Method
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
@app.route("/delete",methods=["DELETE"])
def delete():
    '''
    Method to delete elements from the database
    '''
    a=datetime.now()
    connection=sqlite3.connect("details2.db")
    cursor=connection.cursor()
    cursor.execute(""" DELETE FROM details where timedetails<=(?) """ ,(a,))
    A=cursor.fetchall()
    connection.commit()
    return {"Data":A}
#Main Method (Driver Code)
if __name__=='__main__':
    app.run(debug=True) #Running with debug

"""
Output using Get method:

{
"response": [
        [
            "Good",
            "Somewhat Positive"
        ],
        [
            "bad",
            "[2]"
        ],
        [
            "bad",
            "[2]"
        ],
        [
            "bad",
            "[2]"
        ],
        [
            "bad",
            "Neutral"
        ],
        [
            "bad",
            "Neutral"
        ],
        [
            "bad",
            "Neutral"
        ]
    ]
}


"""
"""
Output Using Post method:
Input:
Body->Json->
{
    "review": "Very good"
}
Output:
{
    "response": "Some what positive"
}
"""


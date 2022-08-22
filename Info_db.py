# from crypt import methods
from flask import Flask,render_template,request
import sqlite3


app=Flask(__name__)


@app.route('/')
def html():
    return render_template('index.html')
    pass

@app.route('/submit',methods=["POST"])
def submit():
    if request.method=='POST':
        data=request.form['inp']
        d=data.split(",")
        Name=d[0]
        Address=d[1]

        con = sqlite3.connect('example.db')
        cur = con.cursor()

        
        def Insert(a,b):
            cur.execute('''INSERT INTO Information(Name, Address) VALUES("%s","%s")''' % (a,b))

        def Delete(n):
            cur.execute('''Delete from Information where Name="%s" ''' % n)

        def Show():
            cur.execute('''Select Name,Address from Information''')
            info=cur.fetchall()
            #print(info)
            return info


        Insert(Name,Address)
        con.commit()
        res=Show()
        # string=""
        # for i in res:
        #     string=string+str(i)
        html=f"<h1> {res}</h1>"
    return html


if __name__=='__main__':
    app.run(debug=True)

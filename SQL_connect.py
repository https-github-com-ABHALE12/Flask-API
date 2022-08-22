import sqlite3
con = sqlite3.connect('example.db')

cur = con.cursor()

# Create table
#cur.execute('''CREATE TABLE Information(Name, Address)''')

a=input()
b=input()


# Insert a row of data
def Insert(a,b):
    cur.execute('''INSERT INTO Information(Name, Address) VALUES("%s","%s")''' % (a,b))

def Delete(n):
    cur.execute('''Delete from Information where Name="%s" ''' % n)

def Show():
    cur.execute('''Select Name,Address from Information''')
    info=cur.fetchall()
    print(info)

Insert(a,b)
a=input()
b=input()
Insert(a,b)
Show()
name=input()
Delete(name)
Show()

# Save (commit) the changes
con.commit()

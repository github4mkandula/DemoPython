import mysql.connector

def getConnection(un,pw,dbname):

    try:
        conn = mysql.connector.connect(host="127.0.0.1", user=un ,passwd=pw, database=dbname)
        return conn
    except Exception as e:
        print('unable to connect')
        return e

def createStatement(conn):
    try:

        statement = conn.cursor()
        print(statement)
        return statement
    except Exception as e:
        print('error in creating statement')
        return e

def execute(statement,querystring):

    try:
       returnValue= statement.execute(querystring)
       return returnValue
    except Exception as e:
        print('error in creating statement')
        return e


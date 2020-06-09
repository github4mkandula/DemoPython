import mysql.connector
import DBConnection
import numpy


try:

    conn= DBConnection.getConnection("MARK","2WSXZAQ1","test")
    statement=conn.cursor()
    #queryString =" create table emp(ename varchar(20),emp_id INT)"
    dbscriptFile=open('dbscriptFile','rb')
    for i in dbscriptFile:
        queryString=i
        value=DBConnection.execute(statement,queryString)
        print('executing the query ' + i)
        if value ==None:
            print(i +' Query execution is success ')
        elif value.isinstance( Exception):
            print(i + ' Query execution on exception')
        else:
            print(i + ' Query execution is faile ')



except Exception as e:
    print('error ' , e)
    conn.close()

print('hello')
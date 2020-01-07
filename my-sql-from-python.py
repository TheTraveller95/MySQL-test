import os
import pymysql

username = os.getenv("C9_USER") 
''' I used the C9_USER because I used the Code Institute template to create the workspace. If I do not use it, ask to tutors how to replace it '''

# connect to the database

connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

finally:
    # close the connection regardeless of whether the above was successful
    connection.close()

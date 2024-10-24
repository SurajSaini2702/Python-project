import mysql.connector
from mysql.connector import MySQLConnection, Error

conn=mysql.connector.connect(host='localhost',database='student',user='root',password='1234')

try:
    cursor=conn.cursor(buffered=True)
    cursor.execute("Select * from records")

    row=cursor.fetchall()
    print(row)

except Error as e:
    print(e)

finally:
    cursor.close()
    conn.close()
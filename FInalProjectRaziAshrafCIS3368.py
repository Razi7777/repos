#importing needed things, used the same method as homework 2
import flask
from flask import Flask
from flask import jsonify
from flask import request




#stuff to connect to mysql database, same as homework 2
import mysql.connector
from mysql.connector import Error


conn = None
try:
    conn = mysql.connector.connect(host='cis3368fall.cjgzy39nyp3b.us-east-1.rds.amazonaws.com',
                                       database='cis3368fall',
                                       user='RaziAshraf',
                                       password='Razizain77')
    if conn.is_connected():
            print('Connected to MySQL database')

except Error as e:
    print(e)

#passing in dictionary as true so we can get our get Apis in a nice dictionary form, same as homework 2
cursor = conn.cursor(dictionary=True)


app = flask.Flask(__name__)#Setting up application name
app.config['DEBUG'] = True #allow to show errors in browser


mylist = [] #creating an empty list for the post api 

@app.route('/api/watches/get' , methods=['GET'])#api to get all watches, got help from https://webdamn.com/create-restful-api-using-python-mysql/, edited to fit criteria for exam 1, using https://www.w3schools.com/mysql/mysql_orderby.asp, same base method as homework 2 with minor alterations
def get_watches():
    try:
        cursor.execute("SELECT id, make, model, type, purchaseprice, saleprice FROM watches ORDER BY (saleprice - purchaseprice) DESC")   #filters by profit (salesprice - purchaseprice), leaves salesprice null values last  
        watchRows = cursor.fetchall()
        response = jsonify(watchRows)
        return response
    except Exception as e:
        print(e)












































app.run()
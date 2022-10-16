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



@app.route('/api/airports/get' , methods=['GET'])#api to get all airports, got help from https://webdamn.com/create-restful-api-using-python-mysql/
def get_airports():
    try:
        cursor.execute("SELECT id, airportcode, airportname, country FROM airports")   
        airportRows = cursor.fetchall()
        response = jsonify(airportRows)
        return response
    except Exception as e:
        print(e)


@app.route('/api/planes/get' , methods=['GET'])#api to get all planes
def get_planes():
    try:
        cursor.execute("SELECT id, make, model, year, capacity FROM planes")   
        planeRows = cursor.fetchall()
        response = jsonify(planeRows)
        return response
    except Exception as e:
        print(e)


@app.route('/api/flights/get' , methods=['GET'])#api to get all flights
def get_flights():
    try:
        cursor.execute("SELECT id, planeid, airportfromid, airporttoid, date FROM flights")   
        flightRows = cursor.fetchall()
        response = jsonify(flightRows)
        return response
    except Exception as e:
        print(e)





@app.route('/api/planes/post', methods=['POST'])  #creating a post api from the information shared in class, similar to homework 2 and exam 1
def create_plane():
    mylist = []
    request_data = request.get_json()
    newmake = request_data['make']
    newmodel = request_data['model']
    newyear = request_data['year']
    newcapacity= request_data['capacity']
    planes = [newmake, newmodel, newyear, newcapacity]
    mylist.append(planes)
    for plane in mylist:
        sql = "INSERT INTO planes (make, model, year, capacity) VALUES (%s, %s, %s, %s)" 
        val = (planes[0], planes[1], planes[2], planes[3])
        cursor.execute(sql,val)
        conn.commit()
    mylist.clear()
    return ("Add request successful")




@app.route('/api/airports/post', methods=['POST'])  #creating a post api from the information shared in class, similar to homework 2 and exam 1
def create_airport():
    mylist = []
    request_data = request.get_json()
    newcode = request_data['airportcode']
    newname = request_data['airportname']
    newcountry = request_data['country']
    airports = [newcode, newname, newcountry]
    mylist.append(airports)
    for airport in mylist:
        sql = "INSERT INTO airports (airportcode, airportname, country) VALUES (%s, %s, %s)" 
        val = (airports[0], airports[1], airports[2])
        cursor.execute(sql,val)
        conn.commit()
    mylist.clear()
    return ("Add request successful")






































app.run()
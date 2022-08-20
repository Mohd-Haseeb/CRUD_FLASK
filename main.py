from operator import imod, methodcaller
from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
import pymongo

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to HOME page !!!"

@app.route('/insert', methods=['GET','POST'])
def insert_query():
    # Login Credentials for MYSql server
    host_name = 'localhost'
    user_name = 'root'
    password = '<password>'

    # CONNECTING TO MONGODB ATLAS
    try:
        client = pymongo.MongoClient("mongodb+srv://<password>:ineuron@cluster0.ex1ru.mongodb.net/?retryWrites=true&w=majority")
    except Exception as e:
        print("Error => {e}")
    db = client.test

    if request.method == "POST":
        region = request.json['region']
        manager = request.json['manager']


        # CREATING A DATABASE 'dress' and a new collections 'sales' ans 'attribute' in 'dress' db
        try:
            database = client['superstore']
            collection = database['users']
            collection_attribute = database['users']
        except Exception as e:
            print("Error in creating database and collection [dress,sales]")
            print(f"Error => {e}")
        

        insert_document = {
            "Region" : region,
            "Manager" : manager
        }
        
        try:
            collection.insert_one(insert_document)
        except print(0):
            print("Mongo Db Insert Failed......")
        


        
        # FOR MYSQL
        try:
            connection = mysql.connector.connect(host=host_name, user = user_name, password=password, use_pure=True, auth_plugin='mysql_native_password')
        except Exception as e:
            print(f"Exception => {e}")
        
        cursor = connection.cursor()

        query_databses = """
            SHOW DATABASES
        """

        query_users = """
            SELECT * FROM `ineuron_data`.users
        """

        insert_user = f"""
            INSERT INTO `ineuron_data`.users(region, manager)
            VALUES ('{region}','{manager}')
        """

        cursor.execute(insert_user)
        # print(cursor.fetchall())
        # ans = cursor.fetchall()

        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({"Success":"True", "Message":"Insert Successful!!"})

@app.route('/update', methods=['GET','POST'])
def update_query():
    host_name = 'localhost'
    user_name = 'root'
    password = '<password>'


    # CONNECTING TO MONGODB ATLAS
    try:
        client = pymongo.MongoClient("mongodb+srv://<password>:ineuron@cluster0.ex1ru.mongodb.net/?retryWrites=true&w=majority")
    except Exception as e:
        print("Error => {e}")
    db = client.test


    if request.method == "POST":
        region = request.json['region']
        manager = request.json['manager']


        # CREATING A DATABASE 'dress' and a new collections 'sales' ans 'attribute' in 'dress' db
        try:
            database = client['superstore']
            collection = database['users']
            collection_attribute = database['users']
        except Exception as e:
            print("Error in creating database and collection [dress,sales]")
            print(f"Error => {e}")

        # Condition on which document is UPDATED
        filter = { 'Manager': manager }
 
        # Values to be updated.
        newvalues = { "$set": { 'Region': region } }
        
        # Using update_one() method for single updation.
        try:
            collection.update_one(filter, newvalues)
        except Exception as e:
            print("Exception => ", e)
        

        try:
            connection = mysql.connector.connect(host=host_name, user = user_name, password=password, use_pure=True, auth_plugin='mysql_native_password')
        except Exception as e:
            print(f"Exception => {e}")
        
        cursor = connection.cursor()

        query_users = """
            SELECT * FROM `ineuron_data`.users
        """

        update_user = f"""
            UPDATE `ineuron_data`.users
            SET region = '{region}' WHERE manager = '{manager}'
        """

        cursor.execute(update_user)

        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({"Success":"True", "Message":"Update Successful!!"})


@app.route('/delete', methods=['GET','POST'])
def delete_query():
    host_name = 'localhost'
    user_name = 'root'
    password = '<password>'


    # CONNECTING TO MONGODB ATLAS
    try:
        client = pymongo.MongoClient("mongodb+srv://<password>:ineuron@cluster0.ex1ru.mongodb.net/?retryWrites=true&w=majority")
    except Exception as e:
        print("Error => {e}")
    db = client.test

    if request.method == "POST":
        region = request.json['region']
        manager = request.json['manager']


        # CREATING A DATABASE 'dress' and a new collections 'sales' ans 'attribute' in 'dress' db
        try:
            database = client['superstore']
            collection = database['users']
            collection_attribute = database['users']
        except Exception as e:
            print("Error in creating database and collection [dress,sales]")
            print(f"Error => {e}")

        # Condition on which document is DELETED
        filter = { 'Region': region }

        
        # Using update_one() method for single updation.
        try:
            collection.delete_one(filter)
        except Exception as e:
            print("Exception => ", e)


        try:
            connection = mysql.connector.connect(host=host_name, user = user_name, password=password, use_pure=True, auth_plugin='mysql_native_password')
        except Exception as e:
            print(f"Exception => {e}")
        
        cursor = connection.cursor()

        query_users = """
            SELECT * FROM `ineuron_data`.users
        """

        delete_user = f"""
            DELETE FROM `ineuron_data`.users
            WHERE region = '{region}'
        """

        cursor.execute(delete_user)

        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({"Success":"True", "Message":"Row is deleted Successfully!!"})


if __name__ == "__main__":
    app.run(debug=True)
from operator import imod, methodcaller
from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to HOME page !!!"

@app.route('/insert', methods=['GET','POST'])
def insert_query():
    # Login Credentials for MYSql server
    host_name = 'localhost'
    user_name = 'root'
    password = 'haseeb123'

    if request.method == "POST":
        region = request.json['region']
        manager = request.json['manager']

        print(region)
        print(manager)

        

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
    password = 'haseeb123'

    if request.method == "POST":
        region = request.json['region']
        manager = request.json['manager']

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
    password = 'haseeb123'

    if request.method == "POST":
        region = request.json['region']
        manager = request.json['manager']

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
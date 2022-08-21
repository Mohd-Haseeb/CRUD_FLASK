## **Built APIs to perform basic CRUD operartions**:


## MYSQL:
- Database used for mysql -> ineuron_data
- Table used -> users
- This table contains only two columns => Region, Manager


## MONGODB
- Database used for mysql -> superstore
- Collecttion used -> users
- This collection contains only two attributes => Region, Manager

> 4 APIs are created in this application

1. '/' (GET)
    - Home Route.
    - This api returns a simple string 
2. '/update' (POST)
    - update Route.
    - This api recieves data required to updaet form the body.
    - Flask application is connected to MYSQL and MONGODB using **MYSQL.CONNECTOR** and **PYMONGO**
    - Values are updated in both the databases (SQL and NOSQL) conditioned on value of "Manager"
3. '/insert' (POST)
    - Insert Route.
    - This api recieves data required to updaet form the body.
    - Flask application is connected to MYSQL and MONGODB using **MYSQL.CONNECTOR** and **PYMONGO**
    - Values are inseretd in both the databases (SQL and NOSQL)
4. '/update' (POST)
    - update Route.
    - This api recieves data required to updaet form the body.
    - Flask application is connected to MYSQL and MONGODB using **MYSQL.CONNECTOR** and **PYMONGO**
    - Values are updated in both the databases (SQL and NOSQL)conditioned on value of "REGION"
5. '/details' (GET)
    - read db data Route.
    - This api recieves data required to updaet form the query parameters (db and table).
    - Flask application is connected to MYSQL and the params sent by the end point is held by the code using `request.args.get('<param name>')`
    - By using these values we fetch the table data and return in JSON format back to the server.


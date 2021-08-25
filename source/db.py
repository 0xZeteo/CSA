import mysql.connector
from mysql.connector import Error


def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password
        )
        print("MySQL Database Connection Successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query Successful")
    except Error as err:
        print(f"Error: '{err}'")


def execute_query_data(connection, query, data):
    cursor = connection.cursor()
    try:
        cursor.execute(query, data)
        connection.commit()
        print("Query Successful")
    except Error as err:
        print(f"Error: '{err}'")


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


def read_query_data(connection, query, data):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query, data)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


server_connection = create_server_connection("localhost", "root", "TempNewPass#158")
create_database_query = "CREATE DATABASE IF NOT EXISTS CSA"
create_database(server_connection, create_database_query)
server_connection.close()

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    uid INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(40) NOT NULL,
    last_name VARCHAR(40) NOT NULL,
    date_of_birth DATE NOT NULL,
    email VARCHAR(40) NOT NULL,
    company VARCHAR(40) NOT NULL,
    username VARCHAR(40) UNIQUE NOT NULL,
    password VARCHAR(150) NOT NULL,
    salt VARCHAR(100) NOT NULL
);
"""

create_irp_table = """
CREATE TABLE IF NOT EXISTS irp (
    iid INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(40) UNIQUE NOT NULL,
    date DATETIME NOT NULL,
    user INT NOT NULL,
    company VARCHAR(40) NOT NULL,
    least INT NOT NULL,
    minimal INT NOT NULL,
    moderate INT NOT NULL,
    significant INT NOT NULL,
    most INT NOT NULL,
    risk_level VARCHAR(20) NOT NULL,
    FOREIGN KEY (user) REFERENCES users(uid)
)
"""

db_connection = create_db_connection("localhost", "root", "TempNewPass#158", "CSA")
execute_query(db_connection, create_users_table)
execute_query(db_connection, create_irp_table)
db_connection.close()

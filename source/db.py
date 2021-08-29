""" Here are the functions that handle the creation and connection to the database and the query functions (read, write)"""

import mysql.connector
from mysql.connector import Error
from tkinter import messagebox


# Establish a server connection with @args: host, username, password
# returns a connection object
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password
        )
    except Error as err:
        messagebox.showwarning("Error", f"Error: {err}")

    return connection


# Creates a database with @args: connection, query
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
    except Error as err:
        messagebox.showwarning("Error", f"Error: {err}")


# Establish a database connection with @args: host, username, password, db name
# returns a connection object
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
        )
    except Error as err:
        messagebox.showwarning("Error", f"Error: {err}")

    return connection


# Executes a query with @args: db connection, query
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as err:
        messagebox.showwarning("Error", f"Error: {err}")


# Executes a query with data, @args: db connection, query, data as a list
def execute_query_data(connection, query, data):
    cursor = connection.cursor()
    try:
        cursor.execute(query, data)
        connection.commit()
    except Error as err:
        messagebox.showwarning("Error", f"Error: {err}")


# Reads from a database with @args: db connection, query
# returns the result of the query
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        messagebox.showwarning("Error", f"Error: {err}")


# Reads from a database with @args: db connection, query, data as a list
# returns the result of the query
def read_query_data(connection, query, data):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query, data)
        result = cursor.fetchall()
        return result
    except Error as err:
        messagebox.showwarning("Error", f"Error: {err}")


# Create database query
create_database_query = "CREATE DATABASE IF NOT EXISTS CSA"

# Create users table query that stores information about the users with their passwords and their information
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

# Create irp table query that stores all the information of the Inherent Risk Profile
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

# Create csm table query that stores all the information of the Cybersecurity Maturity
create_csm_table = """
CREATE TABLE IF NOT EXISTS csm (
    cid INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(40) UNIQUE NOT NULL,
    date DATETIME NOT NULL,
    user INT NOT NULL,
    company VARCHAR(40) NOT NULL,
    baseline_yes INT NOT NULL,
    baseline_compensating INT NOT NULL,
    baseline_no INT NOT NULL,
    evolving_yes INT NOT NULL,
    evolving_compensating INT NOT NULL,
    evolving_no INT NOT NULL,
    intermediate_yes INT NOT NULL,
    intermediate_compensating INT NOT NULL,
    intermediate_no INT NOT NULL,
    advanced_yes INT NOT NULL,
    advanced_compensating INT NOT NULL,
    advanced_no INT NOT NULL,
    innovative_yes INT NOT NULL,
    innovative_compensating INT NOT NULL,
    innovative_no INT NOT NULL,
    maturity_level VARCHAR(20) NOT NULL,
    FOREIGN KEY (user) REFERENCES users(uid)
)
"""

server_connection = create_server_connection("localhost", "root", "TempNewPass#158")    # server connection
create_database(server_connection, create_database_query)                               # create database
server_connection.close()                                                               # close connection

db_connection = create_db_connection("localhost", "root", "TempNewPass#158", "CSA")     # db connection
execute_query(db_connection, create_users_table)                                        # create users table
execute_query(db_connection, create_irp_table)                                          # create irp table
execute_query(db_connection, create_csm_table)                                          # create csm table
db_connection.close()                                                                   # close connection

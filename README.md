Student Management System using Python and MySQL
This is a simple student management system built using Python and MySQL. It allows basic operations such as adding, viewing, updating, and deleting student records stored in a MySQL database.

Requirements
To run this project, make sure the following are installed:

Python

MySQL Server

pymysql Python library

Setup Instructions
Step 1: Install MySQL Server
Download and install MySQL Server from the official website: https://dev.mysql.com/downloads/
During installation, you will be prompted to set a root password. This password will be required later in the Python code to connect to the database.

Step 2: Create Database and Table
After installing MySQL, open the MySQL command line or any GUI tool and execute the following SQL commands:

CREATE DATABASE studentdb;
USE studentdb;
CREATE TABLE students (
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(100),
roll_no VARCHAR(20),
course VARCHAR(100),
marks INT
);

Step 3: Install Required Python Library
Open terminal or command prompt and run:
pip install pymysql

Step 4: Python Script Configuration
In your Python code, use the following format to connect to the MySQL database:

connection = pymysql.connect(
host="localhost",
user="root",
password="your_mysql_password",
database="studentdb"
)

Replace "your_mysql_password" with your actual MySQL password. This is necessary for the program to connect to the database.

Step 5: Run the Python Program
Run the Python file. The program will allow you to insert, read, update, and delete student data from the MySQL database.

Important Note
The MySQL password must be included in the Python script to allow the database connection. While this is fine for local or learning purposes, do not expose passwords in real-world applications. Use environment variables or secure configurations for production.

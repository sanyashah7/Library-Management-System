Library Management System
This is a terminal-based application developed in Python that uses a MySQL database to manage library records. It provides a simple way for administrators to manage a book collection and for customers to search for and borrow books.

Description
A Python and MySQL system that handles book inventory, user registration, and borrowing. It tracks book quantities, manages secure logins, and logs return dates automatically.

Features
Admin Features
Secure Access: Admins must enter a specific Access ID (Admin123) to view administrative options.

User Management: Ability to register new admin accounts with a username and password.

Inventory Control: Admins can add new books, update existing book details, or delete books from the system.

Book Transactions: Admins have the authority to issue books to students and process returns manually.

Customer Features
Registration: New members can register by providing their name, mobile number, email, and address.

Book Search: Users can search for specific books using keywords to see if they are in stock.

Borrowing: Customers can view available books and check them out using a unique Issue ID.

Return System: Users can return books, which automatically updates the library inventory.

Technical Setup
1. Prerequisites
Python 3.x: The primary programming language.

MySQL Server: Used for permanent data storage.

PyMySQL Library: The connector used to link Python to MySQL.

2. Database Installation
The script is designed to be "plug-and-play". It automatically creates the following structures upon execution:

Database: lms.

Tables: user, member, books, and issu_book.

3. How to Run
Install the required library: pip install pymysql.

Open the script and update the m.connect credentials (host, user, and password) to match your local MySQL settings.

Run the script: python library.py.

Use the Access ID Admin123 to access the administrator menu.

Database Schema
The system manages four connected tables:

user: Stores login credentials.

member: Stores personal details of library members.

books: Contains the book titles, authors, and quantities.

issu_book: Tracks which books are currently borrowed and their return status.

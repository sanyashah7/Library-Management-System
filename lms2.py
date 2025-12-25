import pymysql as m
from datetime import date

db=m.connect(host="localhost",user="root",password="Root@1234")
cur=db.cursor()
cur.execute("create database if not exists lms")
cur.execute("use lms")

cur.execute("create table if not exists user(username varchar(50) primary key, password varchar(15))")
cur.execute("create table if not exists member(id int primary key auto_increment,first_name varchar(20),last_name varchar(20),mobline_no varchar(10),email_id varchar(50),address varchar(100))")
cur.execute("create table if not exists books(id int primary key auto_increment,title varchar(200),author varchar(100),qty int)")
cur.execute("create table if not exists issu_book(iid int primary key auto_increment,bid int references books(id),sname varchar(200),idate date,rdate date)")

def login(unm,pwd):
    cur.execute("select password from user where username='"+unm+"'")
    ans=cur.fetchone()
    if ans is None:
        return 0
    return ans[0]==pwd

def register(unm,pwd):
    try:
        cur.execute("insert into user(username,password) values('"+unm+"','"+pwd+"')")
        db.commit()
        print("Account Created!!!")
    except:
        print("error")

def member_info():
    fname=input("Enter your First Name: ")
    lname=input("Enter your Last Name: ")
    mobile=input("Enter your Mobile Number: ")
    email=input("Enter your Email ID: ")
    home_add=input("Enter your Home Address: ")

    cur.execute("insert into member(first_name,last_name,mobline_no,email_id,address) values('"+fname+"','"+lname+"','"+mobile+"','"+email+"','"+home_add+"')")
    db.commit()

def add_book():
    title=input("Enter Book Title: ")
    author=input("Enter Author Name: ")
    qty=int(input("Enter Quantity: "))
    cur.execute("insert into books(title,author,qty) values('"+title+"','"+author+"','"+str(qty)+"')")
    db.commit()
    print("New Book Added Succesfully!!!")

def display_book_cust():
    print("********** The Available Books are **********")
    cur.execute("select * from books where qty>1")
    for i in cur:
        print(i)
        
def display_book_admin():
    print("********** The Available Books are **********")
    cur.execute("select * from books")
    for i in cur:
        print(i)

def update_book():
    id1=input("Enter the Book id for the updating the book: ")
    t2=input("Enter the new book name: ")
    a2=input("Enter the author name: ")
    q2=input("Enter quantity: ")
    cur.execute("update books set title='"+t2+"',author='"+a2+"',qty='"+q2+"' where id='"+id1+"'")
    db.commit()
    print("Book Updated Successfully!")

def delete_book():
    id2=input("Enter the ID which has to be deleted: ")

    cur.execute("select * from issu_book where bid='"+id2+"' and rdate is null")
    x=cur.fetchone()

    if x:
        print("Book is currently issued. Cannot delete.")
    else:
        cur.execute("delete from books where id='"+id2+"'")
        db.commit()
        print("The Book is Deleted.....")

def search_book():
    name=input("Enter book name: ")
    cur.execute("select * from books where title like '%"+name+"%'")
    x=cur.fetchall()

    if len(x)==0:
        print("No books found with the name",name )
    else:
        for i in x:
            print(i)

def issue_book():
    id3=input("Enter Book ID: ")
    name=input("Enter your name: ")

    cur.execute("insert into issu_book(bid,sname) values('"+id3+"','"+name+"')")
    iid=cur.lastrowid

    cur.execute("update books set qty=qty-1 where id='"+id3+"'")
    db.commit()

    print("Book Issued Successfully!")
    print("Book ID:",id3)
    print("Issue ID:",iid)
    print("Please keep the details for returning the book.")


def return_book():
    id4=input("Enter Book ID: ")
    iid1=input("Enter Issue ID: ")
    rd=date.today()
    cur.execute("update books set qty=qty+1 where id='"+id4+"'")
    cur.execute("update issu_book set rdate='"+str(rd)+"' where iid='"+iid1+"'")
    db.commit()
    print("Book returned Successfully!")

while True:
    print("---------Library Management System--------")
    print("1.Admin")
    print("2.Customer")
    print("0.Exit")
    ch=int(input("Enter Your Choice: "))

    if ch==1: 
        id=input("Enter Access ID: ")
        if id=="Admin123":
            
            print("1.Login")
            print("2.Register")
            s=int(input("Enter Choice: "))

            if s==1:
                unm=input("Enter User Name: ")
                pwd=input("Enter Password: ")
                if login(unm,pwd):
                    while True:
                        print("----ADMIN MENU----")
                        print("1.Add Book")
                        print("2.Display Books")
                        print("3.Update Book")
                        print("4.Delete Book")
                        print("5.Issue Book")
                        print("6.Return Book")
                        print("0.Exit")

                        c=int(input("Enter Choice: "))
                        if c==1: add_book()
                        elif c==2: 
                            display_book_admin()
                        elif c==3: 
                            update_book()
                        elif c==4: 
                            delete_book()
                        elif c==5: 
                            issue_book()
                        elif c==6: 
                            return_book()
                        elif c==0: 
                            break
                else:
                    print("Wrong Username or Password!")

            elif s==2:
                unm=input("Enter User Name: ")
                pwd=input("Enter Password: ")
                register(unm,pwd)
            else:
                print("Invalid choice")
        else:
            print("You need correct Admin Access ID!")

    elif ch==2: 
        print("1.Login")
        print("2.Register")
        s=int(input("Enter Choice: "))

        if s==1:
            unm=input("Enter User Name: ")
            pwd=input("Enter Password: ")
            if login(unm,pwd):
                print("Login Successful!!")
                while True:
                    print("----CUSTOMER MENU----")
                    print("1.Display Books")
                    print("2.Issue Book")
                    print("3.Return Book")
                    print("4.Search Book")
                    print("0.Exit")

                    c=int(input("Enter Choice: "))
                    if c==1: 
                        display_book_cust()
                    elif c==2: 
                        issue_book()
                    elif c==3: 
                        return_book()
                    elif c==4:
                        search_book()
                    elif c==0:
                        break
            else:
                print("Wrong Username or Passwrd")

        elif s==2:
            print("Please Fill the following Details to Register....")
            member_info()
            
            unm=input("Enter User Name: ")
            pwd=input("Enter Password: ")
            register(unm,pwd)

    elif ch==0:
        break

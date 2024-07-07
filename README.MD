Run this Query in You're MySQL Workbench First


# creating Database
 cursor.execute("create database crm")

# creating table into database
 cursor.execute("Create table crm.customer (userid int(4) auto_increment Primary key,
                 firstname varchar(255),
                 lastname varchar(255),
                 Address varchar(255),
                 city varchar(255),
                 state varchar(255),
                 zipcode int(10),
                 country varchar(255),
                 phone varchar(255),
                 email varchar(255))")

# after This Open Your Terminal to this repository and run this command to your teminal
pip install -r requirements.txt

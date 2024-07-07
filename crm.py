from tkinter import *
import random
from tkinter import font
import mysql.connector
from tkinter import messagebox
from mysql.connector import Error
from tkinter import PhotoImage,Image

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Salvador@123",
    auth_plugin='mysql_native_password'
        )

root = Tk()
root.geometry("400x500")
root.iconbitmap('icons\dbico.ico')
root.title("Customer Realtional Database")



cursor = mydb.cursor()




# creating Database
# cursor.execute("create database crm")

# Viewing database
# cursor.execute("Show databases")
# for db in cursor:
#     print(db)

# creating table into database
# cursor.execute("Create table crm.customer (firstname varchar(255),\
#                 lastname varchar(255),\
#                 zipcode int(10),\
#                 userid int(4) auto_increment Primary key,\
#                 email varchar(255),\
#                 Address varchar(255),\
#                 city varchar(255),\
#                 state varchar(255),\
#                 country varchar(255),\
#                 phone varchar(255))")


    
    
def update():
    cursor = mydb.cursor(dictionary =True)
    upnew = Toplevel()
    upnew.geometry("400x150")
    upnew.iconbitmap('icons\dbico.ico')
    upnew.title("Customer Realtional Database")
    bold_font = font.Font(weight='bold',size='10')
    userid = Label(upnew,text="Enter User Id You Wanted to Update",font=bold_font,fg="green").grid(row=1,column=1,pady=10)
    userid_box = Entry(upnew)
    userid_box.grid(row=1,column=2)
    def ups():
        entered = userid_box.get()
        cursor.execute("SELECT firstname,lastname,address,city,state,zipcode,country,phone,email FROM crm.customer WHERE userid = %s", (entered,))
        exist = cursor.fetchone()
        upnew.destroy()
        if exist:
            upnew2 = Toplevel()
            upnew2.geometry("400x400")
            upnew2.iconbitmap('icons\dbico.ico')
            upnew2.title("Customer Realtional Database")
            firstname_label = Label(upnew2,text="First Name").grid(row=1,column=0,sticky=W,padx=10,pady=5)
            lastname_label = Label(upnew2,text="Last Name").grid(row=2,column=0,sticky=W,padx=10,pady=5)
            address_label = Label(upnew2,text="Local Address").grid(row=3,column=0,sticky=W,padx=10,pady=5)
            city_label = Label(upnew2,text="City").grid(row=4,column=0,sticky=W,padx=10,pady=5)
            state_label = Label(upnew2,text="State").grid(row=5,column=0,sticky=W,padx=10,pady=5)
            zipcode_label = Label(upnew2,text="Zip Code").grid(row=6,column=0,sticky=W,padx=10,pady=5)
            country_label = Label(upnew2,text="Country").grid(row=7,column=0,sticky=W,padx=10,pady=5)
            phone_label = Label(upnew2,text="Phone Number").grid(row=8,column=0,sticky=W,padx=10,pady=5)
            email_label = Label(upnew2,text="Email").grid(row=9,column=0,sticky=W,padx=10,pady=5)


            firstname_box = Entry(upnew2)
            firstname_box.grid(row=1,column=1)

            lastname_box = Entry(upnew2)
            lastname_box.grid(row=2,column=1)

            address_box = Entry(upnew2)
            address_box.grid(row=3,column=1)

            city_box = Entry(upnew2)
            city_box.grid(row=4,column=1)

            state_box = Entry(upnew2)
            state_box.grid(row=5,column=1)

            zipcode_box = Entry(upnew2)
            zipcode_box.grid(row=6,column=1)

            country_box = Entry(upnew2)
            country_box.grid(row=7,column=1)

            phone_box = Entry(upnew2)
            phone_box.grid(row=8,column=1)

            email_box = Entry(upnew2)
            email_box.grid(row=9,column=1)
            

            firstname_box.insert(0,exist['firstname'])
            lastname_box.insert(0,exist['lastname'])
            address_box.insert(0,exist['address'])
            city_box.insert(0,exist['city'])
            state_box.insert(0,exist['state'])
            zipcode_box.insert(0,exist['zipcode'])
            country_box.insert(0,exist['country'])
            phone_box.insert(0,exist['phone'])
            email_box.insert(0,exist['email'])
            
            
            def update2():
                key_command = """update crm.customer
                set firstname = %s,
                    lastname = %s,
                    address = %s,
                    city = %s,
                    state = %s,
                    zipcode = %s,
                    country = %s,
                    phone = %s,
                    email = %s
                where userid  = %s 
                """
                value = (firstname_box.get(),
                         lastname_box.get(),
                         address_box.get(),
                         city_box.get(),
                         state_box.get(),
                         zipcode_box.get(),
                         country_box.get(),
                         phone_box.get(),
                         email_box.get(),
                         entered)
                cursor.execute(key_command,value)
                mydb.commit()
                upnew2.destroy()
                messagebox.showinfo("Success","Successfully Updated Data")
                
                
            updatebtn = Button(upnew2,text="Confirm Update",command=update2,bg="green",fg="black")
            updatebtn.grid(row=12,column=0,pady=5,ipadx=38,padx=5)
                
    
    
        else:
            upnew.destroy()    
            messagebox.showerror("Error","WRONG USER ID")
            
    def show():
         cursor = mydb.cursor(dictionary =False)
         newwin2 = Toplevel()
         newwin2.iconbitmap('icons\dbico.ico')
         cursor.execute("SELECT * FROM crm.customer")
         data = cursor.fetchall()

         table_frame = Frame(newwin2)
         table_frame.pack()


         bold_font = font.Font(weight='bold', size=12)

         # Display the column headers
         headers = ["User ID", "First Name", "Last Name", "Zip Code", "Email", "Local Address", "City", "State", "Country", "Phone Number"]
         for j, header in enumerate(headers):
             header_label = Label(table_frame, text=header, font=bold_font, padx=10, pady=5, borderwidth=1, relief="solid")
             header_label.grid(row=0, column=j, sticky='nsew')

         # Display the data in the table
         for id, row in enumerate(data):
             for j, value in enumerate(row):
                 data_label = Label(table_frame, text=value, padx=10, pady=5, borderwidth=1, relief="solid")
                 data_label.grid(row=id+1, column=j, sticky='nsew')

         # Configure row and column weights to make the table expandable
         for i in range(len(headers)):
             table_frame.grid_columnconfigure(i, weight=1)
         for i in range(len(data) + 1):
             table_frame.grid_rowconfigure(i, weight=1)


    confirm = Button(upnew,text="Confirm?",bg="#33ff33",fg="black",command=ups).grid(row=3,column=1,pady=10,ipadx=39)
            
    showdb = Button(upnew,text="Show Database",command=show,bg="yellow",fg="Black")
    showdb.grid(row=4,column=1,ipadx=24)
    
    

    
def deli():
    secwin = Toplevel()
    secwin.geometry("400x150")
    secwin.iconbitmap('icons\dbico.ico')
    bold_font = font.Font(weight='bold',size='10')
    userid = Label(secwin,text="Enter User Id You Wanted to Delete",font=bold_font,fg="red").grid(row=1,column=1,pady=10)
    userid_box = Entry(secwin)
    userid_box.grid(row=1,column=2)
    def dele():
        entered = userid_box.get()
        exist = cursor.execute(f"delete from crm.customer where userid ={entered}")
        if exist == True:
            mydb.commit()
            secwin.destroy()    
        else:
            secwin.destroy()    
            messagebox.showerror("Error","WRONG USER ID")
    deletebtn = Button(secwin,text="Delete!",command=dele,fg="white",bg="black")
    deletebtn.grid(row=2,column=0,columnspan=2,ipadx=44)
            
        
    def show():
        newwin2 = Toplevel()
        newwin2.iconbitmap('icons\dbico.ico')
        cursor.execute("SELECT * FROM crm.customer")
        data = cursor.fetchall()

        table_frame = Frame(newwin2)
        table_frame.pack()


        bold_font = font.Font(weight='bold', size=12)

        # Display the column headers
        headers = ["User ID", "First Name", "Last Name", "Zip Code", "Email", "Local Address", "City", "State", "Country", "Phone Number"]
        for j, header in enumerate(headers):
            header_label = Label(table_frame, text=header, font=bold_font, padx=10, pady=5, borderwidth=1, relief="solid")
            header_label.grid(row=0, column=j, sticky='nsew')

        # Display the data in the table
        for id, row in enumerate(data):
            for j, value in enumerate(row):
                data_label = Label(table_frame, text=value, padx=10, pady=5, borderwidth=1, relief="solid")
                data_label.grid(row=id+1, column=j, sticky='nsew')

        # Configure row and column weights to make the table expandable
        for i in range(len(headers)):
            table_frame.grid_columnconfigure(i, weight=1)
        for i in range(len(data) + 1):
            table_frame.grid_rowconfigure(i, weight=1)

    showdb = Button(secwin,text="Show Database",command=show,bg="yellow",fg="Black")
    showdb.grid(row=3,column=0,columnspan=2,pady=5,ipadx=24)
        
        
    
    
    
def show():
    newwin = Toplevel()
    newwin.iconbitmap('icons\dbico.ico')        
    cursor.execute("SELECT * FROM crm.customer")
    data = cursor.fetchall()

    table_frame = Frame(newwin)
    table_frame.pack()


    bold_font = font.Font(weight='bold', size=12)

    # Display the column headers
    headers = ["User ID", "First Name", "Last Name", "Zip Code", "Email", "Local Address", "City", "State", "Country", "Phone Number"]
    for j, header in enumerate(headers):
        header_label = Label(table_frame, text=header, font=bold_font, padx=10, pady=5, borderwidth=1, relief="solid")
        header_label.grid(row=0, column=j, sticky='nsew')

    # Display the data in the table
    for id, row in enumerate(data):
        for j, value in enumerate(row):
            data_label = Label(table_frame, text=value, padx=10, pady=5, borderwidth=1, relief="solid")
            data_label.grid(row=id+1, column=j, sticky='nsew')

    # Configure row and column weights to make the table expandable
    for i in range(len(headers)):
        table_frame.grid_columnconfigure(i, weight=1)
    for i in range(len(data) + 1):
        table_frame.grid_rowconfigure(i, weight=1)



def clear():
    firstname_box.delete(0,END)
    lastname_box.delete(0,END)
    address_box.delete(0,END)
    city_box.delete(0,END)
    state_box.delete(0,END)
    zipcode_box.delete(0,END)
    country_box.delete(0,END)
    phone_box.delete(0,END)
    email_box.delete(0,END)

def add():
    random_id = random.randint(1000, 9999)
    key_command = "insert into crm.customer (userid,firstname,lastname,address,city,state,zipcode,country,phone,email) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    value = (random_id,firstname_box.get(),lastname_box.get(),address_box.get(),city_box.get(),state_box.get(),zipcode_box.get(),country_box.get(),phone_box.get(),email_box.get())
    cursor.execute(key_command,value)
    
    mydb.commit()
    clear()
    
    
    
Heading = Label(root,text="CRM Database",font=("Calibre",16),fg="green").grid(row=0,column=0,columnspan=2)
firstname_label = Label(root,text="First Name").grid(row=1,column=0,sticky=W,padx=10,pady=5)
lastname_label = Label(root,text="Last Name").grid(row=2,column=0,sticky=W,padx=10,pady=5)
address_label = Label(root,text="Local Address").grid(row=3,column=0,sticky=W,padx=10,pady=5)
city_label = Label(root,text="City").grid(row=4,column=0,sticky=W,padx=10,pady=5)
state_label = Label(root,text="State").grid(row=5,column=0,sticky=W,padx=10,pady=5)
zipcode_label = Label(root,text="Zip Code").grid(row=6,column=0,sticky=W,padx=10,pady=5)
country_label = Label(root,text="Country").grid(row=7,column=0,sticky=W,padx=10,pady=5)
phone_label = Label(root,text="Phone Number").grid(row=8,column=0,sticky=W,padx=10,pady=5)
email_label = Label(root,text="Email").grid(row=9,column=0,sticky=W,padx=10,pady=5)





#  = Label(root,text="").grid(row=1,column=0,sticky=W,padx=10,pady=20)

firstname_box = Entry(root)
firstname_box.grid(row=1,column=1)

lastname_box = Entry(root)
lastname_box.grid(row=2,column=1)

address_box = Entry(root)
address_box.grid(row=3,column=1)

city_box = Entry(root)
city_box.grid(row=4,column=1)

state_box = Entry(root)
state_box.grid(row=5,column=1)

zipcode_box = Entry(root)
zipcode_box.grid(row=6,column=1)

country_box = Entry(root)
country_box.grid(row=7,column=1)

phone_box = Entry(root)
phone_box.grid(row=8,column=1)

email_box = Entry(root)
email_box.grid(row=9,column=1)


# Buttons From Here
clearinputs = Button(root,text="Clear",command=clear,bg="black",fg="white")
clearinputs.grid(row=10,column=1,pady=5,ipadx=50)

addinputs = Button(root,text="Add User Info",command=add,bg="green",fg="white")
addinputs.grid(row=10,column=0,pady=5,ipadx=44)

showdb = Button(root,text="Show Database",command=show,bg="yellow",fg="Black")
showdb.grid(row=11,column=0,pady=5,ipadx=42)

delete = Button(root,text="Delete Entries?",command=deli,bg="#ff4d4d",fg="black")
delete.grid(row=11,column=1,pady=5,ipadx=20,padx=5)

updatebtn = Button(root,text="Want to Update?",command=update,bg="#1ad1ff",fg="black")
updatebtn.grid(row=12,column=0,pady=5,ipadx=38,padx=5)


root.mainloop()

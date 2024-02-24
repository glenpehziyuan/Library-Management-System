from datetime import datetime
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
from tkinter import *
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey,update,select,DateTime, null,delete
from datetime import datetime
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
from create_db import *

import tkinter.font as font
engine = create_engine('mysql+mysqlconnector://root:22Bullet7011@localhost/db')                
connection = engine.connect()
def create_member(root):

    #so that other functions can access
    global membership_ID_e,name_e,faculty_e,phone_e,email_e
    root.title("Create Member")
    root.minsize(width=400,height=400)
    root.geometry("700x600")
    frame = Frame(root,bg="#abdbe3",bd=5,relief=GROOVE)
    frame.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    #setting labels and buttons
    main_headingLabel = Label(frame, text="Create Member",bg="#abdbe3",  fg='black', font=('Arial',25), relief=RAISED)
    main_headingLabel.place(relx=0.32,rely=0.05, relwidth=0.35, relheight=0.1)
    
    membership_ID_label = Label(frame, text="Membership ID", bg="#abdbe3" , fg='Black', font=('Arial',10))
    membership_ID_label.place(relx=0.1,rely=0.18, relwidth=0.18, relheight=0.15)

    name_label = Label(frame, text="Name", bg="#abdbe3", fg='black', font=('Arial',10))
    name_label.place(relx=0.1,rely=0.3, relwidth=0.15, relheight=0.1)
    faculty_label = Label(frame, text="Faculty", bg="#abdbe3", fg='black', font=('Arial',10))
    faculty_label.place(relx=0.1,rely=0.4, relwidth=0.15, relheight=0.1)
    phone_label = Label(frame, text="Phone Number", bg="#abdbe3", fg='black', font=('Arial',10))
    phone_label.place(relx=0.1,rely=0.5, relwidth=0.15, relheight=0.1)
    email_label = Label(frame, text="Email Address", bg="#abdbe3", fg='black', font=('Arial',10))
    email_label.place(relx=0.1,rely=0.6, relwidth=0.15, relheight=0.1)

    membership_ID_e = Entry(frame)
    membership_ID_e.place(relx=0.32,rely=0.22, relwidth=0.4, relheight=0.05)
    
    name_e = Entry(frame)
    name_e.place(relx=0.32,rely=0.32, relwidth=0.4, relheight=0.05)
    
    faculty_e = Entry(frame)
    faculty_e.place(relx=0.32,rely=0.42, relwidth=0.4, relheight=0.05)
    
    phone_e = Entry(frame)
    phone_e.place(relx=0.32,rely=0.52, relwidth=0.4, relheight=0.05)
    
    email_e = Entry(frame)
    email_e.place(relx=0.32,rely=0.62, relwidth=0.4, relheight=0.05)
    

    #Submit Button
    submit_btn = Button(root,text="Create Member",bg='black', fg='white', command=create_user_fn)
    submit_btn.place(relx=0.28,rely=0.85, relwidth=0.18,relheight=0.08)

    quit_btn = Button(root,text="Back to Main Menu",bg='black', fg='white', command=root.destroy)
    quit_btn.place(relx=0.6,rely=0.85, relwidth=0.18,relheight=0.08)

def delete_member(root):

    #so that other functions can access
    global membership_ID_e
    root.title("Delete Member")
    root.minsize(width=400,height=400)
    root.geometry("700x600")
    frame = Frame(root,bg="#abdbe3",bd=5,relief=GROOVE)
    frame.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    #setting labels and buttons
    main_headingLabel = Label(frame, text="Delete Member",bg="#abdbe3",  fg='black', font=('Arial',25), relief=RAISED)
    main_headingLabel.place(relx=0.32,rely=0.05, relwidth=0.35, relheight=0.1)
    
    membership_ID_label = Label(frame, text="Membership ID", bg="#abdbe3" , fg='Black', font=('Arial',10))
    membership_ID_label.place(relx=0.1,rely=0.18, relwidth=0.18, relheight=0.15)
    
    membership_ID_e = Entry(frame)
    membership_ID_e.place(relx=0.32,rely=0.22, relwidth=0.4, relheight=0.05)

    #Submit Button
    submit_btn = Button(root,text="Delete Member",bg='black', fg='white', command = delete_member_fn1)
    submit_btn.place(relx=0.28,rely=0.85, relwidth=0.18,relheight=0.08)

    quit_btn = Button(root,text="Back to Membership Menu",bg='black', fg='white', command=root.destroy)
    quit_btn.place(relx=0.6,rely=0.85, relwidth=0.25,relheight=0.08)



def update_member(root):

    #so that other functions can access
    global membership_ID_e,name_e,faculty_e,phone_e,email_e
    root.title("Update Member")
    root.minsize(width=400,height=400)
    root.geometry("700x600")
    frame = Frame(root,bg="#abdbe3",bd=5,relief=GROOVE)
    frame.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    #setting labels and buttons
    main_headingLabel = Label(frame, text="To Update a Member, Please enter Membership ID:",bg="#abdbe3",  fg='black', font=('Arial',15), relief=RAISED)
    main_headingLabel.place(relx=0.05,rely=0.05, relwidth=0.9, relheight=0.1)
    
    membership_ID_label = Label(frame, text="Membership ID", bg="#abdbe3" , fg='Black', font=('Arial',10))
    membership_ID_label.place(relx=0.1,rely=0.18, relwidth=0.2, relheight=0.15)

    membership_ID_e = Entry(frame)
    membership_ID_e.place(relx=0.32,rely=0.22, relwidth=0.4, relheight=0.05)
      

    #Submit Button
    submit_btn = Button(root,text="Update Member",bg='black', fg='white',command = update_member_fn1)
    submit_btn.place(relx=0.28,rely=0.85, relwidth=0.18,relheight=0.08)

    quit_btn = Button(root,text="Back to Membership Menu",bg='black', fg='white', command=root.destroy)
    quit_btn.place(relx=0.6,rely=0.85, relwidth=0.25,relheight=0.08)

def empty(val):
    return val == ""

def create_user_fn():

    #getting value from the entries
    m_id = membership_ID_e.get()
    name = name_e.get()
    faculty = faculty_e.get()
    phone = phone_e.get()
    email = email_e.get()
    ins = members.insert()
    if empty(m_id) or empty(name) or empty(faculty) or empty(phone) or empty(email):
        messagebox.showerror(message="Error! \n Member already exists; Missing or Incomplete fields.")
        return
    with engine.connect() as con:
        try:
            if (m_id[0].isalpha() == True and m_id[1:-1].isnumeric() == True and phone.isnumeric() == True):                
                con.execute(ins, {"alphanumeric_id":m_id,"name":name,"faculty":faculty,"phone_num":phone,"email_address":email})
                messagebox.showinfo(message= "Success! \n ALS Membership created.")
            else:
                raise ValueError()
                
        except:
            messagebox.showerror(message="Error! \n Member already exists; Missing or Incomplete fields.")
            
        
def delete_member_fn1():
    global membership_ID
    membership_ID = membership_ID_e.get()
    connection = engine.connect()
    statement = select(
        members.c.name,
        members.c.faculty,
        members.c.phone_num,
        members.c.email_address,
        ).where(members.c.alphanumeric_id == membership_ID)
    result = connection.execute(statement)
    result = result.fetchall()
    if result == []:
         messagebox.showerror(message="Error! \n No such ID.")
    else:
        root = Tk()
        root.geometry("600x500")
        frame = Frame(root,bg="#abdbe3",bd=5,relief=GROOVE)
        frame.place(relx=0,rely=0,relwidth=1,relheight=1)
        member_name = result[0][0]
        member_faculty = result[0][1]
        member_phone_num = result[0][2]
        member_email_address = result[0][3]
        main_headingLabel = Label(frame, text="Please Confirm Details to Be Correct",bg="#abdbe3",  fg='black', font=('Arial',10), relief=RAISED)
        main_headingLabel.place(relx=0.32,rely=0.05, relwidth=0.38, relheight=0.1)      
        membership_ID_label = Label(frame, text="Membership ID", bg="#abdbe3" , fg='Black', font=('Arial',10))
        membership_ID_label.place(relx=0.1,rely=0.18, relwidth=0.2, relheight=0.15)
        name_label = Label(frame, text="Name", bg="#abdbe3", fg='black', font=('Arial',10))
        name_label.place(relx=0.1,rely=0.3, relwidth=0.2, relheight=0.1)
        faculty_label = Label(frame, text="Faculty", bg="#abdbe3", fg='black', font=('Arial',10))
        faculty_label.place(relx=0.1,rely=0.4, relwidth=0.2, relheight=0.1)
        phone_label = Label(frame, text="Phone Number", bg="#abdbe3", fg='black', font=('Arial',10))
        phone_label.place(relx=0.1,rely=0.5, relwidth=0.2, relheight=0.1)
        email_label = Label(frame, text="Email Address", bg="#abdbe3", fg='black', font=('Arial',10))
        email_label.place(relx=0.1,rely=0.6, relwidth=0.2, relheight=0.1)        
        membership_ID_label2 = Label(frame, text=membership_ID, bg="#abdbe3" , fg='Black', font=('Arial',10))
        membership_ID_label2.place(relx=0.5,rely=0.18, relwidth=0.2, relheight=0.15)
        name = Label(frame, text=member_name, bg="#abdbe3", fg='black', font=('Arial',10))
        name.place(relx=0.5,rely=0.3, relwidth=0.2, relheight=0.1)
        faculty = Label(frame, text=member_faculty, bg="#abdbe3", fg='black', font=('Arial',10))
        faculty.place(relx=0.5,rely=0.4, relwidth=0.2, relheight=0.1)
        phone = Label(frame, text=member_phone_num, bg="#abdbe3", fg='black', font=('Arial',10))
        phone.place(relx=0.5,rely=0.5, relwidth=0.2, relheight=0.1)
        email = Label(frame, text= member_email_address, bg="#abdbe3", fg='black', font=('Arial',10))
        email.place(relx=0.5,rely=0.6, relwidth=0.3, relheight=0.1)    


        submit_btn = Button(root,text="Delete Member",bg='black', fg='white',command = delete_member_sql)
        submit_btn.place(relx=0.2,rely=0.85, relwidth=0.18,relheight=0.08)
        myFont = font.Font(size=10)
        quit_btn = Button(root,text="Back to Membership Menu",bg='black', fg='white', font=('Arial',10), command=root.destroy)

        quit_btn.place(relx=0.6,rely=0.85, relwidth=0.3,relheight=0.08)

#problem
def delete_member_sql():
    connection = engine.connect()

    fine_statement = select(fine_payment_table.c.alphanumeric_id).where(fine_payment_table.c.alphanumeric_id == membership_ID).where(
    fine_payment_table.c.payment_date.is_(null()))

    loan_statement = select(loan.c.accession_number).where(loan.c.alphanumeric_id ==  membership_ID).where(loan.c.return_date.is_(null()))
##    reserve_statement = select(reserve.c.alphanumeric_id).where(reserve.c.alphanumeric_id  == membership_ID)
    fine_result = connection.execute(fine_statement)
    loan_result = connection.execute(loan_statement)
##    reserve_result = connection.execute(reserve_statement)
    fine_result = fine_result.fetchall()
    loan_result = loan_result.fetchall()
##    reserve_result = reserve_result.fetchall()
##    and reserve_result == []
    if fine_result == []  and loan_result == [] :
        try:
            delete_statement =  delete(members).where(members.c.alphanumeric_id == membership_ID)
            connection.execute(delete_statement)
            messagebox.showinfo(message = "Member deleted successfully")
        except Exception as e:
            print(e)
    else:
        messagebox.showerror(message = "Error! \n Member loans, reservations or outstanding fines.")

def update_member_fn1():
    global membership_ID_e,name_e,faculty_e,phone_e,email_e
    membership_ID = membership_ID_e.get()
    connection = engine.connect()
    statement = select(
        members.c.name,
        members.c.faculty,
        members.c.phone_num,
        members.c.email_address,
        ).where(members.c.alphanumeric_id == membership_ID)
    result = connection.execute(statement)
    result = result.fetchall()
    if result == []:
         messagebox.showerror(message="Error! \n No such ID.")
    else:
        root = Tk()
        root.geometry("600x500")
        frame = Frame(root,bg="#abdbe3",bd=5,relief=GROOVE)
        frame.place(relx=0,rely=0,relwidth=1,relheight=1)
        main_headingLabel = Label(frame, text="Please Enter Requested Information Below",bg="#abdbe3",  fg='black', font=('Arial',10), relief=RAISED)
        main_headingLabel.place(relx=0.2,rely=0.05, relwidth=0.5, relheight=0.1)      
        membership_ID_label = Label(frame, text="Membership ID", bg="#abdbe3" , fg='Black', font=('Arial',10))
        membership_ID_label.place(relx=0.1,rely=0.18, relwidth=0.2, relheight=0.15)
        
        name_label = Label(frame, text="Name", bg="#abdbe3", fg='white', font=('Arial',10))
        name_label.place(relx=0.1,rely=0.3, relwidth=0.2, relheight=0.1)
        
        faculty_label = Label(frame, text="Faculty", bg="#abdbe3", fg='white', font=('Arial',10))
        faculty_label.place(relx=0.1,rely=0.4, relwidth=0.2, relheight=0.1)
        
        phone_label = Label(frame, text="Phone Number", bg="#abdbe3", fg='white', font=('Arial',10))
        phone_label.place(relx=0.1,rely=0.5, relwidth=0.2, relheight=0.1)
        
        email_label = Label(frame, text="Email Address", bg="#abdbe3", fg='white', font=('Arial',10))
        email_label.place(relx=0.1,rely=0.6, relwidth=0.2, relheight=0.1)
        
        membership_ID = Label(frame, text=membership_ID, bg="#abdbe3" , fg='black', font=('Arial',10))
        membership_ID.place(relx=0.5,rely=0.18, relwidth=0.2, relheight=0.15)

        name_e = Entry(frame)
        name_e.place(relx=0.32,rely=0.32, relwidth=0.4, relheight=0.05)
        
        faculty_e = Entry(frame)
        faculty_e.place(relx=0.32,rely=0.42, relwidth=0.4, relheight=0.05)
        
        phone_e = Entry(frame)
        phone_e.place(relx=0.32,rely=0.52, relwidth=0.4, relheight=0.05)
        
        email_e = Entry(frame)
        email_e.place(relx=0.32,rely=0.62, relwidth=0.4, relheight=0.05)

      
        submit_btn = Button(root,text="Update Member",bg='black', fg='white', command=  update_member_fn2 )
        submit_btn.place(relx=0.2,rely=0.85, relwidth=0.18,relheight=0.08)
        myFont = font.Font(size=10)
        quit_btn = Button(root,text="Back to Membership Menu",bg='black', fg='white', font=('Arial',10), command=root.destroy)
        quit_btn.place(relx=0.6,rely=0.85, relwidth=0.3,relheight=0.08)
    


def update_member_fn2():
        global membership_ID,name,faculty,phone_num,email_address
        root = Tk()
        membership_ID = membership_ID_e.get()
        name = name_e.get()
        faculty = faculty_e.get()
        phone_num = phone_e.get()
        email_address = email_e.get()
        root.geometry("600x500")
        frame = Frame(root,bg="#abdbe3",bd=5,relief=GROOVE)
        frame.place(relx=0,rely=0,relwidth=1,relheight=1)
        main_headingLabel = Label(frame, text="Please Confirm Details to Be Correct",bg="#abdbe3",  fg='black', font=('Arial',10), relief=RAISED)
        main_headingLabel.place(relx=0.32,rely=0.05, relwidth=0.38, relheight=0.1)      
        membership_ID_label = Label(frame, text="Membership ID", bg="#abdbe3" , fg='Black', font=('Arial',10))
        membership_ID_label.place(relx=0.1,rely=0.18, relwidth=0.2, relheight=0.15)
        name_label = Label(frame, text="Name", bg="#abdbe3", fg='black', font=('Arial',10))
        name_label.place(relx=0.1,rely=0.3, relwidth=0.2, relheight=0.1)
        faculty_label = Label(frame, text="Faculty", bg="#abdbe3", fg='black', font=('Arial',10))
        faculty_label.place(relx=0.1,rely=0.4, relwidth=0.2, relheight=0.1)
        phone_label = Label(frame, text="Phone Number", bg="#abdbe3", fg='black', font=('Arial',10))
        phone_label.place(relx=0.1,rely=0.5, relwidth=0.2, relheight=0.1)
        email_label = Label(frame, text="Email Address", bg="#abdbe3", fg='black', font=('Arial',10))
        email_label.place(relx=0.1,rely=0.6, relwidth=0.2, relheight=0.1)        
        membership_ID_label2 = Label(frame, text=membership_ID, bg="#abdbe3" , fg='Black', font=('Arial',10))
        membership_ID_label2.place(relx=0.5,rely=0.18, relwidth=0.2, relheight=0.15)
        name_label2 = Label(frame, text=name, bg="#abdbe3", fg='black', font=('Arial',10))
        name_label2.place(relx=0.5,rely=0.3, relwidth=0.2, relheight=0.1)
        faculty_label2 = Label(frame, text=faculty, bg="#abdbe3", fg='black', font=('Arial',10))
        faculty_label2.place(relx=0.5,rely=0.4, relwidth=0.2, relheight=0.1)
        phone_label2 = Label(frame, text=phone_num, bg="#abdbe3", fg='black', font=('Arial',10))
        phone_label2.place(relx=0.5,rely=0.5, relwidth=0.2, relheight=0.1)
        email_label2 = Label(frame, text= email_address, bg="#abdbe3", fg='black', font=('Arial',10))
        email_label2.place(relx=0.5,rely=0.6, relwidth=0.3, relheight=0.1)    

        submit_btn = Button(root,text="Confirm Update",bg='black', fg='white',command = update_member_sql)
        submit_btn.place(relx=0.2,rely=0.85, relwidth=0.18,relheight=0.08)
        myFont = font.Font(size=10)
        quit_btn = Button(root,text="Back to Back to Update Function",bg='black', fg='white', font=('Arial',10), command=root.destroy)

        quit_btn.place(relx=0.4,rely=0.85, relwidth=0.4,relheight=0.08)

def update_member_sql():
    if empty(membership_ID) or empty(name) or empty(faculty) or empty(phone_num) or empty(email_address):
        messagebox.showerror(message="Error \n Missing or Incomplete fields")
        return
    try:
        statement = update(members).where(members.c.alphanumeric_id == membership_ID).values(name = name,faculty=faculty,
                                                                                             phone_num = phone_num,email_address = email_address)
        connection.execute(statement)
        messagebox.showinfo(message = "Success\n ALS Membership Updated")
    except Exception as e:
        print(e)
        messagebox.showerror(message="Error \n Missing or Incomplete fields")

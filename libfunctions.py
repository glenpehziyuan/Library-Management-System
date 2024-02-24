from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import Column,String,DateTime,Integer,select, insert,update, null,delete
import datetime as dt
from datetime import datetime
from datetime import timedelta
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
from tkinter import *
from create_db import *
engine = create_engine('mysql+mysqlconnector://root:22Bullet7011@localhost/db')                
connection = engine.connect()

def book_acquisition(root):

    #so that other functions can access
    global bookAccession_e,title_e,authors_e,publisher_e,publication_year_e,isbn_e
    root.title("Acquire books")
    root.minsize(width=400,height=400)
    root.geometry("700x600")
    frame = Frame(root,bg="#abdbe3",bd=5,relief=GROOVE)
    frame.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    #setting labels and buttons
    main_headingLabel = Label(frame, text="Acquire books",bg="#abdbe3",  fg='black', font=('Arial',25), relief=RAISED)
    main_headingLabel.place(relx=0.32,rely=0.05, relwidth=0.3, relheight=0.1)
    
    accession_number_label = Label(frame, text="Accession Number", bg="#abdbe3" , fg='Black', font=('Arial',10))
    accession_number_label.place(relx=0.1,rely=0.2, relwidth=0.18, relheight=0.1)
    title_label = Label(frame, text="Title", bg="#abdbe3", fg='black', font=('Arial',10))
    title_label.place(relx=0.1,rely=0.3, relwidth=0.15, relheight=0.1)
    authors_label = Label(frame, text="Authors", bg="#abdbe3", fg='black', font=('Arial',10))
    authors_label.place(relx=0.1,rely=0.4, relwidth=0.15, relheight=0.1)
    isbn_label = Label(frame, text="ISBN", bg="#abdbe3", fg='black', font=('Arial',10))
    isbn_label.place(relx=0.1,rely=0.5, relwidth=0.15, relheight=0.1)
    publisher_label = Label(frame, text="Publisher", bg="#abdbe3", fg='black', font=('Arial',10))
    publisher_label.place(relx=0.1,rely=0.6, relwidth=0.15, relheight=0.1)
    publication_yr_label = Label(frame, text="Publication Year", bg="#abdbe3", fg='black', font=('Arial',10))
    publication_yr_label.place(relx=0.1,rely=0.7, relwidth=0.15, relheight=0.1)

    bookAccession_e = Entry(frame)
    bookAccession_e.place(relx=0.32,rely=0.22, relwidth=0.4, relheight=0.05)
    
    title_e = Entry(frame)
    title_e.place(relx=0.32,rely=0.32, relwidth=0.4, relheight=0.05)
    
    authors_e = Entry(frame)
    authors_e.place(relx=0.32,rely=0.42, relwidth=0.4, relheight=0.05)
    
    isbn_e = Entry(frame)
    isbn_e.place(relx=0.32,rely=0.52, relwidth=0.4, relheight=0.05)
    
    publisher_e = Entry(frame)
    publisher_e.place(relx=0.32,rely=0.62, relwidth=0.4, relheight=0.05)
    
    publication_year_e = Entry(frame)
    publication_year_e.place(relx=0.32,rely=0.72, relwidth=0.4, relheight=0.05)

    #Submit Button
    submit_btn = Button(root,text="Add new book",bg='black', fg='white', command = book_acquisition_fn)
    submit_btn.place(relx=0.28,rely=0.85, relwidth=0.25,relheight=0.08)

    quit_btn = Button(root,text="Back to books menu",bg='black', fg='white', command=root.destroy)
    quit_btn.place(relx=0.6,rely=0.85, relwidth=0.3,relheight=0.08)




def book_withdraw(root):

    #so that other functions can access
    global bookAccession_e
    root.title("Withdraw books")
    root.minsize(width=400,height=400)
    root.geometry("700x600")
    frame = Frame(root,bg="#abdbe3",bd=5,relief=GROOVE)
    frame.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    #setting labels and buttons
    main_headingLabel = Label(frame, text="To Remove Outdated Books From System, Please Enter Required Information Below:",bg="#abdbe3",  fg='black', font=('Arial',10), relief=RAISED)
    main_headingLabel.place(relx=0.05,rely=0.05, relwidth=0.9, relheight=0.1)
    
    accession_number_label = Label(frame, text="Accession Number", bg="#abdbe3" , fg='Black', font=('Arial',10))
    accession_number_label.place(relx=0.1,rely=0.2, relwidth=0.18, relheight=0.1)

    bookAccession_e = Entry(frame)
    bookAccession_e.place(relx=0.32,rely=0.22, relwidth=0.4, relheight=0.05)
    

    #Submit Button
    submit_btn = Button(root,text="Withdraw Book",bg='black', fg='white', command = book_withdraw_fn1)
    submit_btn.place(relx=0.28,rely=0.85, relwidth=0.26,relheight=0.08)

    quit_btn = Button(root,text="Back to Books Menu",bg='black', fg='white', command=root.destroy)
    quit_btn.place(relx=0.6,rely=0.85, relwidth=0.25,relheight=0.08)


def book_borrow(root):

    #so that other functions can access
    global membership_ID_e,bookAccession_e
    root.title("Borrow book")
    root.minsize(width=400,height=400)
    root.geometry("700x600")
    frame = Frame(root,bg="#abdbe3",bd=5,relief=GROOVE)
    frame.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    #setting labels and buttons
    main_headingLabel = Label(frame, text="Borrow books",bg="#abdbe3",  fg='black', font=('Arial',25), relief=RAISED)
    main_headingLabel.place(relx=0.32,rely=0.05, relwidth=0.35, relheight=0.1)
    
    membership_ID_label = Label(frame, text="Membership ID", bg="#abdbe3" , fg='Black', font=('Arial',10))
    membership_ID_label.place(relx=0.1,rely=0.18, relwidth=0.18, relheight=0.15)

    accession_num_label = Label(frame, text="Accession Number", bg="#abdbe3", fg='black', font=('Arial',10))
    accession_num_label.place(relx=0.1,rely=0.38, relwidth=0.18, relheight=0.15)

    membership_ID_e = Entry(frame)
    membership_ID_e.place(relx=0.32,rely=0.22, relwidth=0.4, relheight=0.05)
    
    bookAccession_e = Entry(frame)
    bookAccession_e.place(relx=0.32,rely=0.42, relwidth=0.4, relheight=0.05)
 

    #Submit Button replace the command part
    submit_btn = Button(root,text="Borrow Book",bg='black', fg='white', command = book_borrow_fn1)
    submit_btn.place(relx=0.28,rely=0.85, relwidth=0.18,relheight=0.08)

    quit_btn = Button(root,text="Back to Loans Menu",bg='black', fg='white', command=root.destroy)
    quit_btn.place(relx=0.6,rely=0.85, relwidth=0.18,relheight=0.08)



def book_return(root):
    #so that other functions can access
    global bookAccession_e, return_date_e
    root.title("Return book")
    root.minsize(width=400,height=400)
    root.geometry("700x600")
    frame = Frame(root,bg="#abdbe3",bd=5,relief=GROOVE)
    frame.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    #setting labels and buttons
    main_headingLabel = Label(frame, text="To Return book, Please Enter Information Below",bg="#abdbe3",  fg='black', font=('Arial',15), relief=RAISED)
    main_headingLabel.place(relx=0.15,rely=0.05, relwidth=0.7, relheight=0.1)
    
    accession_number_label = Label(frame, text="Accession Number", bg="#abdbe3" , fg='Black', font=('Arial',10))
    accession_number_label.place(relx=0.1,rely=0.2, relwidth=0.18, relheight=0.1)

    bookAccession_e = Entry(frame)
    bookAccession_e.place(relx=0.32,rely=0.22, relwidth=0.4, relheight=0.05)
    
    return_date_label = Label(frame, text="Return date", bg="#abdbe3" , fg='Black', font=('Arial',10))
    return_date_label.place(relx=0.1,rely=0.4, relwidth=0.18, relheight=0.1)

    return_date_e = Entry(frame)
    return_date_e.place(relx=0.32,rely=0.42, relwidth=0.4, relheight=0.05)
     

    #Submit Button
    submit_btn = Button(root,text="Return Book",bg='black', fg='white', command = book_return_fn)
    submit_btn.place(relx=0.28,rely=0.85, relwidth=0.18,relheight=0.08)

    quit_btn = Button(root,text="Back To Loan Menus",bg='black', fg='white', command=root.destroy)
    quit_btn.place(relx=0.6,rely=0.85, relwidth=0.25,relheight=0.08)

def book_reserve(root):

    #so that other functions can access
    global bookAccession_e,membership_ID_e,reserve_date_e
    root.title("Reserve book")
    root.minsize(width=400,height=400)
    root.geometry("700x600")
    frame = Frame(root,bg="#abdbe3",bd=5,relief=GROOVE)
    frame.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    #setting labels and buttons
    main_headingLabel = Label(frame, text="To Reserve a Book, Please Enter Information Below",bg="#abdbe3",  fg='black', font=('Arial',15), relief=RAISED)
    main_headingLabel.place(relx=0.12,rely=0.05, relwidth=0.7, relheight=0.1)
    
    membership_ID_label = Label(frame, text="Membership ID", bg="#abdbe3" , fg='Black', font=('Arial',10))
    membership_ID_label.place(relx=0.1,rely=0.2, relwidth=0.18, relheight=0.1)
    accession_number_label = Label(frame, text="Accession Number", bg="#abdbe3", fg='black', font=('Arial',10))
    accession_number_label.place(relx=0.1,rely=0.3, relwidth=0.18, relheight=0.1)

    membership_ID_e = Entry(frame)
    membership_ID_e.place(relx=0.32,rely=0.22, relwidth=0.4, relheight=0.05)
    
    bookAccession_e = Entry(frame)
    bookAccession_e.place(relx=0.32,rely=0.32, relwidth=0.4, relheight=0.05)
    
    return_date_label = Label(frame, text="Reserve date", bg="#abdbe3" , fg='Black', font=('Arial',10))
    return_date_label.place(relx=0.1,rely=0.4, relwidth=0.18, relheight=0.1)

    reserve_date_e = Entry(frame)
    reserve_date_e.place(relx=0.32,rely=0.42, relwidth=0.4, relheight=0.05)
 
    #Submit Button
    submit_btn = Button(root,text="Reserve Book",bg='black', fg='white', command = book_reserve_fn)
    submit_btn.place(relx=0.28,rely=0.85, relwidth=0.18,relheight=0.08)

    quit_btn = Button(root,text="Back to Reservation Menu",bg='black', fg='white', command=root.destroy)
    quit_btn.place(relx=0.5,rely=0.85, relwidth=0.25,relheight=0.08)

def cancel_reservation(root):

    #so that other functions can access
    global bookAccession_e,membership_ID_e,cancel_reserve_e
    root.title("Cancel reservation")
    root.minsize(width=400,height=400)
    root.geometry("700x600")
    frame = Frame(root,bg="#abdbe3",bd=5,relief=GROOVE)
    frame.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    #setting labels and buttons
    main_headingLabel = Label(frame, text="Cancel Reservation",bg="#abdbe3",  fg='black', font=('Arial',15), relief=RAISED)
    main_headingLabel.place(relx=0.22,rely=0.05, relwidth=0.5, relheight=0.1)
    
    accession_number_label = Label(frame, text="Accession Number", bg="#abdbe3", fg='black', font=('Arial',10))
    accession_number_label.place(relx=0.1,rely=0.2, relwidth=0.18, relheight=0.1)    
    membership_ID_label = Label(frame, text="Membership ID", bg="#abdbe3" , fg='Black', font=('Arial',10))
    membership_ID_label.place(relx=0.1,rely=0.3, relwidth=0.18, relheight=0.1)

    cancel_reserve_label = Label(frame, text="Cancel Date", bg="#abdbe3", fg='black', font=('Arial',10))
    cancel_reserve_label.place(relx=0.1,rely=0.4, relwidth=0.18, relheight=0.1)

    bookAccession_e = Entry(frame)
    bookAccession_e.place(relx=0.32,rely=0.22, relwidth=0.4, relheight=0.05)
    membership_ID_e = Entry(frame)
    membership_ID_e.place(relx=0.32,rely=0.32, relwidth=0.4, relheight=0.05)   

    cancel_reserve_e = Entry(frame)
    cancel_reserve_e.place(relx=0.32,rely=0.42, relwidth=0.4, relheight=0.05)
    

    #Submit Button
    submit_btn = Button(root,text="Cancel Reservation",bg='black', fg='white', command = cancel_reservation_fn)
    submit_btn.place(relx=0.28,rely=0.85, relwidth=0.18,relheight=0.08)

    quit_btn = Button(root,text="Back to Reservation Menu",bg='black', fg='white', command=root.destroy)
    quit_btn.place(relx=0.6,rely=0.85, relwidth=0.3,relheight=0.08)

def empty(val):
    return val == ""


def book_acquisition_fn():
    #getting value from the entries
    bk_accession= bookAccession_e.get()
    title = title_e.get()
    authors = authors_e.get()
    publisher = publisher_e.get()
    publication_year = publication_year_e.get()
    isbn = isbn_e.get()
    if empty(bk_accession) or empty(title) or empty(authors) or empty(publisher) or empty(publication_year) or empty(isbn):
        messagebox.showerror(message="Book already added; Duplicate,Missing or Incomplete fields")
        return
    
    book_ins = books.insert()
##    author_book_ins = author_book.insert()
    author_ins = author_table.insert()
    authors_list = authors.split(',')
    
    with engine.connect() as con:
        try:
            con.execute(book_ins, {"accession_number":bk_accession,"title":title,"isbn_id":isbn,'publication_yr':publication_year, "publisher_name":publisher})
            
            for author in authors_list:
                check_authorid_statement = select(author_table.c.author_name).where(author_table.c.author_name == author)
                result = connection.execute(check_authorid_statement)
                result = result.fetchall()
                if result == []:
                    con.execute(author_ins, {"author_name": author})
                    
                    
                statement = select(author_table.c.author_id).where(author_table.c.author_name == author)
                result_id = con.execute(statement)
                result_id = result_id.fetchall()[0]
                statement = insert(author_book).values(author_id = result_id[0], accession_number = bk_accession)
                con.execute(statement)
                
            messagebox.showinfo(message= "Success! \n New book added in Library.")
                
        except Exception as e:
            messagebox.showerror(message="Book already added; Duplicate,Missing or Incomplete fields")
            



def book_borrow_fn1():
    global borrow_date_e,date_due,book_title,membership_ID,bookAccession
    connection = engine.connect()
    bookAccession = bookAccession_e.get()
    membership_ID = membership_ID_e.get()
    connection = engine.connect()
    statement = select(
        books.c.title,
        ).where(books.c.accession_number == bookAccession)
    result_books = connection.execute(statement)
    result_books = result_books.fetchall()   
    statement = select(
        members.c.name,
        ).where(members.c.alphanumeric_id == membership_ID)
    result_member = connection.execute(statement)
    result_member = result_member.fetchall()
    if result_member == [] or result_books == [] :
        messagebox.showerror(message="Error! \n No such ID or Book.")
    else:        
        borrow_date_e = dt.date.today()
        book_title = result_books[0][0]
        member_name = result_member[0][0]
        date_due = borrow_date_e + timedelta(days=14)
        root = Tk()
        root.geometry("600x500")
        frame = Frame(root,bg="#abdbe3",bd=5,relief=GROOVE)
        frame.place(relx=0,rely=0,relwidth=1,relheight=1)
        
        main_headingLabel = Label(frame, text="Please Confirm Details to Be Correct",bg="#abdbe3",  fg='black', font=('Arial',10), relief=RAISED)
        main_headingLabel.place(relx=0.32,rely=0.05, relwidth=0.38, relheight=0.1)
        
        accession_number_label = Label(frame, text="Accession Number", bg="#abdbe3" , fg='Black', font=('Arial',10))
        accession_number_label.place(relx=0.1,rely=0.18, relwidth=0.2, relheight=0.15)
        
        title_label = Label(frame, text="Title", bg="#abdbe3", fg='black', font=('Arial',10))
        title_label.place(relx=0.1,rely=0.3, relwidth=0.2, relheight=0.1)
        
        borrow_date_label = Label(frame, text="Borrow Date", bg="#abdbe3", fg='black', font=('Arial',10))
        borrow_date_label.place(relx=0.1,rely=0.4, relwidth=0.2, relheight=0.1)
        
        mem_ID_label = Label(frame, text="Membership ID", bg="#abdbe3", fg='black', font=('Arial',10))
        mem_ID_label.place(relx=0.1,rely=0.5, relwidth=0.2, relheight=0.1)
        
        mem_name_label = Label(frame, text="Membership Name", bg="#abdbe3", fg='black', font=('Arial',10))
        mem_name_label.place(relx=0.1,rely=0.6, relwidth=0.2, relheight=0.1)
        
        due_date_label = Label(frame, text="Due Date", bg="#abdbe3", fg='black', font=('Arial',10))
        due_date_label.place(relx=0.1,rely=0.7, relwidth=0.2, relheight=0.1)
                
        accession_number = Label(frame, text=bookAccession, bg="#abdbe3" , fg='Black', font=('Arial',10))
        accession_number.place(relx=0.5,rely=0.18, relwidth=0.2, relheight=0.15)
        
        title_input = Label(frame, text=book_title, bg="#abdbe3", fg='black', font=('Arial',10))
        title_input.place(relx=0.5,rely=0.3, relwidth=0.2, relheight=0.1)
        
        borrow_date_input = Label(frame, text=borrow_date_e, bg="#abdbe3", fg='black', font=('Arial',10))
        borrow_date_input.place(relx=0.5,rely=0.4, relwidth=0.3, relheight=0.1)
        
        mem_ID = Label(frame, text=membership_ID, bg="#abdbe3", fg='black', font=('Arial',10))
        mem_ID.place(relx=0.5,rely=0.5, relwidth=0.2, relheight=0.1)
        
        mem_name = Label(frame, text= member_name, bg="#abdbe3", fg='black', font=('Arial',10))
        mem_name.place(relx=0.5,rely=0.6, relwidth=0.2, relheight=0.1)
        
        due_date = Label(frame, text= date_due, bg="#abdbe3", fg='black', font=('Arial',10))
        due_date.place(relx=0.5,rely=0.7, relwidth=0.3, relheight=0.1)
        

        submit_btn = Button(root,text="Confirm Loan",bg='black', fg='white',command = book_borrow_sql)
        submit_btn.place(relx=0.2,rely=0.85, relwidth=0.18,relheight=0.08)
        quit_btn = Button(root,text="Back to Borrow Function",bg='black', fg='white', font=('Arial',10), command=root.destroy)

        quit_btn.place(relx=0.6,rely=0.85, relwidth=0.35,relheight=0.08)
            
        
def book_borrow_sql():
    connection = engine.connect()
    try:
        statement_limit = select(
            loan.c.alphanumeric_id
            ).where(loan.c.alphanumeric_id == membership_ID).where(loan.c.return_date.is_(null()))
        result = connection.execute(statement_limit)
        result = result.fetchall()

        if len(result) >= 2:
            messagebox.showerror(message = "Member loan quota exceeded")
            return
            
        statement_availability = select(
            loan.c.alphanumeric_id,
            loan.c.borrow_date
            ).where(loan.c.return_date.is_(null())).where(loan.c.accession_number == bookAccession)
        result = connection.execute(statement_availability)
        result = result.fetchall()

        if len(result) == 1:
            borrow_date = result[0][1]
            due_date = borrow_date + timedelta(days = 14)
            messagebox.showerror(message = f"Book currently on loan until {due_date}")
            return
        statement_fine = select(
            fine_payment_table.c.amount
            ).where(fine_payment_table.c.alphanumeric_id == membership_ID).where(fine_payment_table.c.payment_date.is_(null()))
        
        result = connection.execute(statement_fine)
        result = result.fetchall()
        if result != []:
            messagebox.showerror(message = f"Member has outstanding fine")
            return
        statement_reserve = select(reserve.c.accession_number, reserve.c.alphanumeric_id).where(reserve.c.accession_number == bookAccession)
        result_reserve = connection.execute(statement_reserve)
        result_reserve = result_reserve.fetchall()
        if len(result_reserve) > 0:
            if result_reserve[0][1] != membership_ID:
                messagebox.showerror(message = f"Book is currently reserved")
                return
            else:
                statement_update = delete(reserve).where(reserve.c.accession_number == bookAccession)
                connection.execute(statement_update)
                             
        statement = insert(loan).values(accession_number = bookAccession,alphanumeric_id = membership_ID,borrow_date = borrow_date_e)
        connection.execute(statement)
        messagebox.showinfo(message = "Book borrowed")

    except Exception as e:
        print(e)
        messagebox.showerror(message = f"Error borrowing book")
    
    
    
def book_withdraw_fn1() :
    global bookAccession
    bookAccession = bookAccession_e.get()
    connection = engine.connect()
    statement = select(
        books.c.title,
        books.c.isbn_id,
        books.c.publisher_name,
        books.c.publication_yr
        ).where(books.c.accession_number == bookAccession)
    result_books = connection.execute(statement)
    result_books = result_books.fetchall()
    
    if result_books == []:
        messagebox.showerror(message="Error! \n No such ID.")
    else:
        title = result_books[0][0]   
        publication_year = result_books[0][3]       
        publisher_name = result_books[0][2]
        isbn_id = result_books[0][1]
        statement3 = select(
            author_book.c.author_id
            ).where(author_book.c.accession_number == bookAccession)
        result_authors_id = connection.execute(statement3)
        result_authors_id = result_authors_id.fetchall()
        author_list = []
        for auth_id in result_authors_id:
            statement = select(author_table.c.author_name).where(author_table.c.author_id == auth_id[0])
            result = connection.execute(statement)
            result = result.fetchall()[0]
            author_list.append(result[0])
                                                    
        author_list = [x + ", " for x in author_list]
        authors = "".join(author_list)
        authors = authors[:-2]
        root = Tk()
        root.geometry("600x500")
        frame = Frame(root,bg="#abdbe3",bd=5,relief=GROOVE)
        frame.place(relx=0,rely=0,relwidth=1,relheight=1)
        main_headingLabel = Label(frame, text="Please Confirm Details to Be Correct",bg="#abdbe3",  fg='black', font=('Arial',10), relief=RAISED)
        main_headingLabel.place(relx=0.32,rely=0.05, relwidth=0.38, relheight=0.1)      
        accession_number_label = Label(frame, text="Accession Number", bg="#abdbe3" , fg='Black', font=('Arial',10))
        accession_number_label.place(relx=0.1,rely=0.18, relwidth=0.2, relheight=0.15)
        title_label = Label(frame, text="Title", bg="#abdbe3", fg='black', font=('Arial',10))
        title_label.place(relx=0.1,rely=0.3, relwidth=0.2, relheight=0.1)
        authors_label = Label(frame, text="Authors", bg="#abdbe3", fg='black', font=('Arial',10))
        authors_label.place(relx=0.1,rely=0.4, relwidth=0.2, relheight=0.1)
        isbn_label = Label(frame, text="ISBN", bg="#abdbe3", fg='black', font=('Arial',10))
        isbn_label.place(relx=0.1,rely=0.5, relwidth=0.2, relheight=0.1)
        
        publisher_label = Label(frame, text="Publisher", bg="#abdbe3", fg='black', font=('Arial',10))
        publisher_label.place(relx=0.1,rely=0.6, relwidth=0.2, relheight=0.1)
        publication_yr_label = Label(frame, text="Year", bg="#abdbe3", fg='black', font=('Arial',10))
        publication_yr_label.place(relx=0.1,rely=0.7, relwidth=0.2, relheight=0.1)
        
        accession_number = Label(frame, text=bookAccession, bg="#abdbe3" , fg='Black', font=('Arial',10))
        accession_number.place(relx=0.5,rely=0.18, relwidth=0.2, relheight=0.15)
        
        title_input = Label(frame, text=title, bg="#abdbe3", fg='black', font=('Arial',10))
        title_input.place(relx=0.5,rely=0.3, relwidth=0.2, relheight=0.1)
        
        authors = Label(frame, text=authors, bg="#abdbe3", fg='black', font=('Arial',10))
        authors.place(relx=0.5,rely=0.4, relwidth=0.2, relheight=0.1)
        
        isbn = Label(frame, text=isbn_id, bg="#abdbe3", fg='black', font=('Arial',10))
        isbn.place(relx=0.5,rely=0.5, relwidth=0.2, relheight=0.1)
        
        publisher = Label(frame, text=publisher_name, bg="#abdbe3", fg='black', font=('Arial',10))
        publisher.place(relx=0.5,rely=0.6, relwidth=0.2, relheight=0.1)
        
        pub_year = Label(frame, text= publication_year, bg="#abdbe3", fg='black', font=('Arial',10))
        pub_year.place(relx=0.5,rely=0.7, relwidth=0.2, relheight=0.1)    


        submit_btn = Button(root,text="Confirm Withdrawal",bg='black', fg='white',command = book_withdrawal_sql)
        submit_btn.place(relx=0.2,rely=0.85, relwidth=0.25,relheight=0.08)
        quit_btn = Button(root,text="Back to Withdrawal Function",bg='black', fg='white', font=('Arial',10), command=root.destroy)

        quit_btn.place(relx=0.6,rely=0.85, relwidth=0.35,relheight=0.08)
    
def book_withdrawal_sql():
    connection = engine.connect()
    statement = select(loan.c.accession_number).where(loan.c.accession_number == bookAccession).where(loan.c.return_date.is_(null()))
    result = connection.execute(statement)
    result = result.fetchall()

    statement_reserve = select(reserve.c.accession_number).where(reserve.c.accession_number == bookAccession)
    result_reserve = connection.execute(statement_reserve)
    result_reserve = result_reserve.fetchall()

    if result != []:
        messagebox.showerror(message = "Error \n Book is currently on loan")
    elif result_reserve != []:
        messagebox.showerror(message = "Error \n Book is currently reserved")
    else:
        delete_statement = delete(books).where(books.c.accession_number == bookAccession)
        connection.execute(delete_statement)
        messagebox.showinfo(message="Book withdrawn")
    
    
        



#did not use due date
def book_return_fn():
    global fine,return_date_input,bookAccession,membership_ID
    connection = engine.connect()
    bookAccession = bookAccession_e.get()
    return_date_input = datetime.strptime(return_date_e.get(),'%d/%m/%Y')
    connection = engine.connect()
    statement = select(
        books.c.title,
        ).where(books.c.accession_number == bookAccession)
    result_books = connection.execute(statement)
    result_books = result_books.fetchall()
    statement = select(
        loan.c.alphanumeric_id,
        #due_date
        loan.c.borrow_date
        ).where(loan.c.return_date == None)
    result_loan = connection.execute(statement)
    result_loan = result_loan.fetchall()


    if result_loan == [] or result_books == [] :
        messagebox.showerror(message="Error! \n No such ID or Book.")
    else:
        membership_ID = result_loan[0][0]
        #
        borrow_date = result_loan[0][1]

        statement = select(
            members.c.name,
            ).where(members.c.alphanumeric_id == membership_ID)
        result_member = connection.execute(statement)
        result_member = result_member.fetchall()

        book_title = result_books[0][0]
        member_name = result_member[0][0]
        root = Tk()
        root.geometry("600x500")
        frame = Frame(root,bg="#abdbe3",bd=5,relief=GROOVE)
        frame.place(relx=0,rely=0,relwidth=1,relheight=1)

        fine = (return_date_input - (borrow_date + timedelta(days =14))).days * 1
        if fine <= 0:
            fine = 0    
        main_headingLabel = Label(frame, text="Please Confirm Details to Be Correct",bg="#abdbe3",  fg='black', font=('Arial',10), relief=RAISED)
        main_headingLabel.place(relx=0.32,rely=0.05, relwidth=0.38, relheight=0.1)
        
        accession_number_label = Label(frame, text="Accession Number", bg="#abdbe3" , fg='Black', font=('Arial',10))
        accession_number_label.place(relx=0.1,rely=0.18, relwidth=0.2, relheight=0.15)
        
        title_label = Label(frame, text="Book Title", bg="#abdbe3", fg='black', font=('Arial',10))
        title_label.place(relx=0.1,rely=0.3, relwidth=0.2, relheight=0.1)
             
        mem_ID_label = Label(frame, text="Membership ID", bg="#abdbe3", fg='black', font=('Arial',10))
        mem_ID_label.place(relx=0.1,rely=0.4, relwidth=0.2, relheight=0.1)
        
        mem_name_label = Label(frame, text="Membership Name", bg="#abdbe3", fg='black', font=('Arial',10))
        mem_name_label.place(relx=0.1,rely=0.5, relwidth=0.2, relheight=0.1)
        
        return_date_label = Label(frame, text="Return Date", bg="#abdbe3", fg='black', font=('Arial',10))
        return_date_label.place(relx=0.1,rely=0.6, relwidth=0.2, relheight=0.1)

        fine_label = Label(frame, text="Fine", bg="#abdbe3", fg='black', font=('Arial',10))
        fine_label.place(relx=0.1,rely=0.7, relwidth=0.2, relheight=0.1)          
                
        accession_number = Label(frame, text=bookAccession, bg="#abdbe3" , fg='Black', font=('Arial',10))
        accession_number.place(relx=0.5,rely=0.18, relwidth=0.2, relheight=0.15)
        
        title_input = Label(frame, text=book_title, bg="#abdbe3", fg='black', font=('Arial',10))
        title_input.place(relx=0.5,rely=0.3, relwidth=0.2, relheight=0.1)
        
        mem_ID = Label(frame, text=membership_ID, bg="#abdbe3", fg='black', font=('Arial',10))
        mem_ID.place(relx=0.5,rely=0.4, relwidth=0.2, relheight=0.1)
        
        mem_name = Label(frame, text= member_name, bg="#abdbe3", fg='black', font=('Arial',10))
        mem_name.place(relx=0.5,rely=0.5, relwidth=0.2, relheight=0.1)
        
        return_date = Label(frame, text= return_date_input , bg="#abdbe3", fg='black', font=('Arial',10))
        return_date.place(relx=0.5,rely=0.6, relwidth=0.3, relheight=0.1)

        fine_e = Label(frame, text="$" + str(fine), bg="#abdbe3", fg='black', font=('Arial',10))
        fine_e.place(relx=0.5,rely=0.7, relwidth=0.2, relheight=0.1)          
                
        
        submit_btn = Button(root,text="Confirm Return",bg='black', fg='white',command = book_return_sql)
        submit_btn.place(relx=0.2,rely=0.85, relwidth=0.18,relheight=0.08)
        quit_btn = Button(root,text="Back to Return Function",bg='black', fg='white', font=('Arial',10), command=root.destroy)

        quit_btn.place(relx=0.6,rely=0.85, relwidth=0.35,relheight=0.08)
            

def book_return_sql():
    connection = engine.connect()
    try:
        statement_return = update(loan).where(loan.c.accession_number == bookAccession, loan.c.return_date == None).values(return_date = return_date_input)
        connection.execute(statement_return)
        if fine > 0:            
            statement_fine = insert(fine_payment_table).values(alphanumeric_id = membership_ID, amount = fine)
            connection.execute(statement_fine)
            messagebox.showerror(message = "Book returned successfully but has fines")
        else:
            messagebox.showinfo(message = "Book returned successfully")
    except Exception as e:
        print(e)
        messagebox.showerror(message = "Error returning book")


def book_reserve_fn():
    global reserve_date,book_title,membership_ID,bookAccession
    connection = engine.connect()
    bookAccession = bookAccession_e.get()
    membership_ID = membership_ID_e.get()
    connection = engine.connect()
    statement = select(
        books.c.title,
        ).where(books.c.accession_number == bookAccession)
    result_books = connection.execute(statement)
    result_books = result_books.fetchall()   
    statement = select(
        members.c.name,
        ).where(members.c.alphanumeric_id == membership_ID)
    result_member = connection.execute(statement)
    result_member = result_member.fetchall()
    if result_member == [] or result_books == [] :
        messagebox.showerror(message="Error! \n No such ID or Book.")
    else:
        reserve_date = datetime.strptime(reserve_date_e.get(),'%d/%m/%Y')
        book_title = result_books[0][0]
        member_name = result_member[0][0]
        root = Tk()
        root.geometry("600x500")
        frame = Frame(root,bg="#abdbe3",bd=5,relief=GROOVE)
        frame.place(relx=0,rely=0,relwidth=1,relheight=1)
        
        main_headingLabel = Label(frame, text="Confirm Reservation Details To Be Correct",bg="#abdbe3",  fg='black', font=('Arial',10), relief=RAISED)
        main_headingLabel.place(relx=0.12,rely=0.05, relwidth=0.7, relheight=0.1)
        
        accession_number_label = Label(frame, text="Accession Number", bg="#abdbe3" , fg='Black', font=('Arial',10))
        accession_number_label.place(relx=0.1,rely=0.18, relwidth=0.2, relheight=0.15)
        
        title_label = Label(frame, text="Title", bg="#abdbe3", fg='black', font=('Arial',10))
        title_label.place(relx=0.1,rely=0.3, relwidth=0.2, relheight=0.1)
        
        mem_ID_label = Label(frame, text="Membership ID", bg="#abdbe3", fg='black', font=('Arial',10))
        mem_ID_label.place(relx=0.1,rely=0.4, relwidth=0.2, relheight=0.1)
        
        mem_name_label = Label(frame, text="Membership Name", bg="#abdbe3", fg='black', font=('Arial',10))
        mem_name_label.place(relx=0.1,rely=0.5, relwidth=0.2, relheight=0.1)
        
        due_date_label = Label(frame, text="Reserve Date", bg="#abdbe3", fg='black', font=('Arial',10))
        due_date_label.place(relx=0.1,rely=0.6, relwidth=0.2, relheight=0.1)
                
        accession_number = Label(frame, text=bookAccession, bg="#abdbe3" , fg='Black', font=('Arial',10))
        accession_number.place(relx=0.5,rely=0.18, relwidth=0.2, relheight=0.15)
        
        title_input = Label(frame, text=book_title, bg="#abdbe3", fg='black', font=('Arial',10))
        title_input.place(relx=0.5,rely=0.3, relwidth=0.2, relheight=0.1)
        
        mem_ID = Label(frame, text=membership_ID, bg="#abdbe3", fg='black', font=('Arial',10))
        mem_ID.place(relx=0.5,rely=0.4, relwidth=0.2, relheight=0.1)
        
        mem_name = Label(frame, text= member_name, bg="#abdbe3", fg='black', font=('Arial',10))
        mem_name.place(relx=0.5,rely=0.5, relwidth=0.2, relheight=0.1)
        
        reserve_date_label = Label(frame, text= reserve_date, bg="#abdbe3", fg='black', font=('Arial',10))
        reserve_date_label.place(relx=0.5,rely=0.6, relwidth=0.3, relheight=0.1)
        

        submit_btn = Button(root,text="Confirm Reservation",bg='black', fg='white',command = book_reserve_sql)
        submit_btn.place(relx=0.2,rely=0.85, relwidth=0.25,relheight=0.08)
        quit_btn = Button(root,text="Back to Reserve Function",bg='black', fg='white', font=('Arial',10), command=root.destroy)
        quit_btn.place(relx=0.6,rely=0.85, relwidth=0.35,relheight=0.08)
     
    

#yet to finish
def book_reserve_sql():
    connection = engine.connect()
    reserve_statement = select(reserve.c.alphanumeric_id).where(reserve.c.alphanumeric_id == membership_ID)
    fine_statement = select(fine_payment_table.c.amount).where(fine_payment_table.c.alphanumeric_id == membership_ID).where(fine_payment_table.c.payment_date.is_(null()))
    reserve_result = connection.execute(reserve_statement)
    fine_result = connection.execute(fine_statement)
    reserve_result = reserve_result.fetchall()
    fine_result = fine_result.fetchall()

    if fine_result != []:
        fine = fine_result[0][0]
        messagebox.showerror(message = f"Member has outstanding fine of ${fine}")
        return
    if len(reserve_result) >= 2:
        messagebox.showerror(message = f"Member currently has 2 books on reservation")
        return
    
    try:
        statement = insert(reserve).values(accession_number = bookAccession, reserve_date = reserve_date, alphanumeric_id = membership_ID )
        connection.execute(statement)
        messagebox.showinfo(message = "Book reserved")
    except Exception as e:
        messagebox.showerror(message = "Book has already been reserved")
    
                            
    
    
    
    
    
def cancel_reservation_fn() :
    global cancel_reserve_date,book_title,membership_ID,bookAccession
    connection = engine.connect()
    bookAccession = bookAccession_e.get()
    membership_ID = membership_ID_e.get()
    cancel_reserve_date = datetime.strptime(cancel_reserve_e.get(),'%d/%m/%Y')
    connection = engine.connect()
    statement = select(
        books.c.title,
        ).where(books.c.accession_number == bookAccession)
    result_books = connection.execute(statement)
    result_books = result_books.fetchall()   
    statement = select(
        members.c.name,
        ).where(members.c.alphanumeric_id == membership_ID)
    result_member = connection.execute(statement)
    result_member = result_member.fetchall()
    if result_member == [] or result_books == [] :
        messagebox.showerror(message="Error! \n No such ID or Book.")
    else:
        book_title = result_books[0][0]
        member_name = result_member[0][0]
        root = Tk()
        root.geometry("600x500")
        frame = Frame(root,bg="#abdbe3",bd=5,relief=GROOVE)
        frame.place(relx=0,rely=0,relwidth=1,relheight=1)
        
        main_headingLabel = Label(frame, text="Confirm Cancellation Details To Be Correct",bg="#abdbe3",  fg='black', font=('Arial',10), relief=RAISED)
        main_headingLabel.place(relx=0.12,rely=0.05, relwidth=0.7, relheight=0.1)
        
        accession_number_label = Label(frame, text="Accession Number", bg="#abdbe3" , fg='Black', font=('Arial',10))
        accession_number_label.place(relx=0.1,rely=0.18, relwidth=0.2, relheight=0.15)
        
        title_label = Label(frame, text="Title", bg="#abdbe3", fg='black', font=('Arial',10))
        title_label.place(relx=0.1,rely=0.3, relwidth=0.2, relheight=0.1)
        
        mem_ID_label = Label(frame, text="Membership ID", bg="#abdbe3", fg='black', font=('Arial',10))
        mem_ID_label.place(relx=0.1,rely=0.4, relwidth=0.2, relheight=0.1)
        
        mem_name_label = Label(frame, text="Membership Name", bg="#abdbe3", fg='black', font=('Arial',10))
        mem_name_label.place(relx=0.1,rely=0.5, relwidth=0.2, relheight=0.1)
        
        cancel_date_label = Label(frame, text="Cancellation Date", bg="#abdbe3", fg='black', font=('Arial',10))
        cancel_date_label.place(relx=0.1,rely=0.6, relwidth=0.2, relheight=0.1)
                
        accession_number = Label(frame, text=bookAccession, bg="#abdbe3" , fg='Black', font=('Arial',10))
        accession_number.place(relx=0.5,rely=0.18, relwidth=0.2, relheight=0.15)
        
        title_input = Label(frame, text=book_title, bg="#abdbe3", fg='black', font=('Arial',10))
        title_input.place(relx=0.5,rely=0.3, relwidth=0.2, relheight=0.1)
        
        mem_ID = Label(frame, text=membership_ID, bg="#abdbe3", fg='black', font=('Arial',10))
        mem_ID.place(relx=0.5,rely=0.4, relwidth=0.2, relheight=0.1)
        
        mem_name = Label(frame, text= member_name, bg="#abdbe3", fg='black', font=('Arial',10))
        mem_name.place(relx=0.5,rely=0.5, relwidth=0.2, relheight=0.1)
        
        cancel_date_input_label = Label(frame, text= cancel_reserve_date, bg="#abdbe3", fg='black', font=('Arial',10))
        cancel_date_input_label.place(relx=0.5,rely=0.6, relwidth=0.3, relheight=0.1)
        

        submit_btn = Button(root,text="Confirm Cancellation",bg='black', fg='white',command = cancel_reserve_sql)
        submit_btn.place(relx=0.2,rely=0.85, relwidth=0.25,relheight=0.08)
        quit_btn = Button(root,text="Back to Reserve Function",bg='black', fg='white', font=('Arial',10), command=root.destroy)
        quit_btn.place(relx=0.6,rely=0.85, relwidth=0.35,relheight=0.08)

def cancel_reserve_sql():
    connection = engine.connect()
    find_reserve = select(reserve.c.accession_number).where(reserve.c.alphanumeric_id == membership_ID).where(reserve.c.accession_number == bookAccession)
    try:
        result = connection.execute(find_reserve)
        result = result.fetchall()
        if result == []:
            messagebox.showerror(message = "Error!\n Member has no such reservation")
        else:
            delete_reserve = delete(reserve).where(reserve.c.accession_number == bookAccession)
            try:
                connection.execute(delete_reserve)
                messagebox.showinfo(message = "Reservation deleted")
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
   

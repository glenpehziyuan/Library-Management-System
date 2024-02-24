from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import Column,String,DateTime,Integer
from datetime import datetime
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
from tkinter import *
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey,select,null, or_
from sqlalchemy import inspect
from datetime import datetime
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
from sqlalchemy import MetaData
from create_db import *
from tkinter import ttk
import tkinter as tk
engine = create_engine('mysql+mysqlconnector://root:22Bullet7011@localhost/db')

def display_members_with_fine(root):
    root.title("Show members with fine")
    connection = engine.connect()
    # add condition for fine
    members_fine_statement = select(fine_payment_table.c.alphanumeric_id).where(fine_payment_table.c.amount > 0)
    
    result = connection.execute(members_fine_statement)
    
    tree = ttk.Treeview(root, column=("id", "name", "faculty","phone","email"), show='headings')
    tree.heading("id", text="Membership ID")
    tree.heading("name", text="Name")
    tree.heading("faculty", text="Faculty")
    tree.heading("phone", text="Phone Number")
    tree.heading("email", text="Email Address")

    rows = result.fetchall()    

    
    for row in rows:
        members_statement = select(members.c.alphanumeric_id, members.c.name, members.c.faculty, members.c.phone_num, members.c.email_address).where(members.c.alphanumeric_id == row[0])
        members_result = connection.execute(members_statement)
        members_result = members_result.fetchone()
        
        tree.insert("", tk.END, values=(members_result[0],members_result[1],members_result[2],members_result[3], members_result[4]))
       
           
    result.close()
    tree.grid(row=0, column=0, sticky='nsew')
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')


 
def display_books_on_loan(root):
    connection = engine.connect()
    root.title("Books on Loan Report")
    # add condition for fine
    statement = select(loan.c.accession_number).where(loan.c.return_date.is_(null()))
    result = connection.execute(statement)
    
    tree = ttk.Treeview(root, column=("accession_number", "title", "authors","isbn","publisher","pub_year"), show='headings')
    tree.heading("accession_number", text="Accession Number")
    tree.heading("title", text="Title")
    tree.heading("authors", text= "Authors")
    tree.heading("isbn", text="ISBN")
    tree.heading("publisher", text="Publisher")
    tree.heading("pub_year", text="Year")
    
    rows = result.fetchall()
    
    
    for row in rows:
        book_statement = select(books.c.title,books.c.isbn_id, books.c.publisher_name, books.c.publication_yr).where(books.c.accession_number == row[0])
        authorid_statement = select(author_book.c.author_id).where(author_book.c.accession_number == row[0])
        result_book = connection.execute(book_statement)
        result_authors = connection.execute(authorid_statement)
        result_book = result_book.fetchone()
        
        result_authors_id = result_authors.fetchall()
        author_list = []
        for auth_id in result_authors_id:
            statement = select(author_table.c.author_name).where(author_table.c.author_id == auth_id[0])
            result = connection.execute(statement)
            result = result.fetchall()[0]
            author_list.append(result[0])
                                                    
        author_list = [x + ", " for x in author_list]
        authors = "".join(author_list)
        authors_names = authors[:-2]



        tree.insert("", tk.END, values=(row[0],result_book[0],authors_names,result_book[1], result_book[2],result_book[3]))
       
       
           
    tree.grid(row=0, column=0, sticky='nsew')
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

    
def display_books_on_reservation(root):
    connection = engine.connect()
    root.title("Books on Reservation Report")
    statement = select(reserve.c.accession_number,reserve.c.alphanumeric_id)
    result = connection.execute(statement)
    
    tree = ttk.Treeview(root, column=("accession_number", "title", "membership_id","name"), show='headings')
    tree.heading("accession_number", text="Accession Number")
    tree.heading("title", text="Name")
    tree.heading("membership_id", text="Membership ID")
    tree.heading("name", text="Name")

    rows = result.fetchall()
    
    
    for row in rows:
        title_statement = select(books.c.title).where(books.c.accession_number == row[0])
        name_statement = select(members.c.name).where(members.c.alphanumeric_id == row[1])
        result_title = connection.execute(title_statement)
        result_name = connection.execute(name_statement)
        title = result_title.fetchone()[0]
        name = result_name.fetchone()[0]
        tree.insert("", tk.END, values=(row[0],title,row[1],name))
       
           
    result.close()
    tree.grid(row=0, column=0, sticky='nsew')
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')




def display_books_on_loan_member(root):
    global membership_ID_e

    root.title("Books On Loan to Member")
    root.minsize(width=400,height=400)
    root.geometry("700x600")
    frame = Frame(root,bg="#abdbe3",bd=5,relief=GROOVE)
    frame.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    main_headingLabel = Label(frame, text="Books On Loan to Member",bg="#abdbe3",  fg='black', font=('Arial',15), relief=RAISED)
    main_headingLabel.place(relx=0.22,rely=0.05, relwidth=0.5, relheight=0.1)
    membership_ID_label = Label(frame, text="Membership ID", bg="#abdbe3" , fg='Black', font=('Arial',10))
    membership_ID_label.place(relx=0.1,rely=0.18, relwidth=0.18, relheight=0.15)
    membership_ID_e = Entry(frame)
    membership_ID_e.place(relx=0.32,rely=0.22, relwidth=0.4, relheight=0.05)

    submit_btn = Button(root,text="Select Member",bg='black', fg='white', command= display_books_on_loan_member_sql)
    submit_btn.place(relx=0.28,rely=0.85, relwidth=0.18,relheight=0.08)

    quit_btn = Button(root,text="Back to Reports Menu",bg='black', fg='white', command=root.destroy)
    quit_btn.place(relx=0.6,rely=0.85, relwidth=0.18,relheight=0.08)

def display_books_on_loan_member_sql():
    root = Tk()
    root.title("Books on loan to member")
    membership_ID = membership_ID_e.get()
    connection = engine.connect()
    statement = select(loan.c.accession_number).where(loan.c.alphanumeric_id == membership_ID)
    result = connection.execute(statement)

    tree = ttk.Treeview(root, column=("accession_number", "title", "authors","isbn","publisher","pub_year"), show='headings')
    tree.heading("accession_number", text="Accession Number")
    tree.heading("title", text="Title")
    tree.heading("authors", text= "Authors")
    tree.heading("isbn", text="ISBN")
    tree.heading("publisher", text="Publisher")
    tree.heading("pub_year", text="Year")
    
    rows = result.fetchall()
    
    
    
    for row in rows:
        book_statement = select(books.c.title,books.c.isbn_id, books.c.publisher_name, books.c.publication_yr).where(books.c.accession_number == row[0])
        authorid_statement = select(author_book.c.author_id).where(author_book.c.accession_number == row[0])
        result_book = connection.execute(book_statement)
        result_authors = connection.execute(authorid_statement)
        result_book = result_book.fetchone()
        
        result_authors_id = result_authors.fetchall()
        author_list = []
        for auth_id in result_authors_id:
            statement = select(author_table.c.author_name).where(author_table.c.author_id == auth_id[0])
            result = connection.execute(statement)
            result = result.fetchall()[0]
            author_list.append(result[0])
                                                    
        author_list = [x + ", " for x in author_list]
        authors = "".join(author_list)
        authors_names = authors[:-2]



        tree.insert("", tk.END, values=(row[0],result_book[0],authors_names,result_book[1], result_book[2],result_book[3]))
       
           
    
    tree.grid(row=0, column=0, sticky='nsew')
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')


def book_search(root):

    #so that other functions can access
    global title_e,authors_e,publisher_e,publication_year_e,isbn_e
    root.title("Search book")
    root.minsize(width=400,height=400)
    root.geometry("700x600")
    frame = Frame(root,bg="#abdbe3",bd=5,relief=GROOVE)
    frame.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    #setting labels and buttons
    main_headingLabel = Label(frame, text="Search books",bg="#abdbe3",  fg='black', font=('Arial',25), relief=RAISED)
    main_headingLabel.place(relx=0.32,rely=0.05, relwidth=0.3, relheight=0.1)
    

    title_label = Label(frame, text="Title", bg="#abdbe3", fg='black', font=('Arial',10))
    title_label.place(relx=0.1,rely=0.2, relwidth=0.15, relheight=0.1)
    authors_label = Label(frame, text="Authors", bg="#abdbe3", fg='black', font=('Arial',10))
    authors_label.place(relx=0.1,rely=0.3, relwidth=0.15, relheight=0.1)
    isbn_label = Label(frame, text="ISBN", bg="#abdbe3", fg='black', font=('Arial',10))
    isbn_label.place(relx=0.1,rely=0.4, relwidth=0.15, relheight=0.1)
    publisher_label = Label(frame, text="Publisher", bg="#abdbe3", fg='black', font=('Arial',10))
    publisher_label.place(relx=0.1,rely=0.5, relwidth=0.15, relheight=0.1)
    publication_yr_label = Label(frame, text="Publication Year", bg="#abdbe3", fg='black', font=('Arial',10))
    publication_yr_label.place(relx=0.1,rely=0.6, relwidth=0.15, relheight=0.1)

    
    title_e = Entry(frame)
    title_e.place(relx=0.32,rely=0.22, relwidth=0.4, relheight=0.05)
    
    authors_e = Entry(frame)
    authors_e.place(relx=0.32,rely=0.32, relwidth=0.4, relheight=0.05)
    
    isbn_e = Entry(frame)
    isbn_e.place(relx=0.32,rely=0.42, relwidth=0.4, relheight=0.05)
    
    publisher_e = Entry(frame)
    publisher_e.place(relx=0.32,rely=0.52, relwidth=0.4, relheight=0.05)
    
    publication_year_e = Entry(frame)
    publication_year_e.place(relx=0.32,rely=0.62, relwidth=0.4, relheight=0.05)

    #Submit Button
    submit_btn = Button(root,text="Search book",bg='black', fg='white', command = book_search_fn)
    submit_btn.place(relx=0.28,rely=0.85, relwidth=0.18,relheight=0.08)

    quit_btn = Button(root,text="Back to reports menu",bg='black', fg='white', command=root.destroy)
    quit_btn.place(relx=0.6,rely=0.85, relwidth=0.18,relheight=0.08)

def book_search_fn():
    title = title_e.get()
    author = authors_e.get()
    isbn = isbn_e.get()
    publisher = publisher_e.get()
    pub_yr = publication_year_e.get()
    f = [title_search,author_search,isbn_search,publisher_search,pub_yr_search]
    search = {title_search:title,author_search:author,isbn_search:isbn,publisher_search:publisher,pub_yr_search:pub_yr}
    for k,v in search.items():
        if v != "":
            return k(v)

def title_search(title):
    root = Tk() 
    connection = engine.connect()
    root.title("Book Search Results")
    # add condition for fine
    statement = select(books.c.accession_number,books.c.title,books.c.isbn_id,books.c.publisher_name,books.c.publication_yr).where(or_(books.c.title == title,
                                                                                                                                       books.c.title.like(f"% {title}"),
                                                                                                                                       books.c.title.like(f"{title} %"),
                                                                                                                                       books.c.title.like(f"% {title} %")))
    result = connection.execute(statement)
    
    tree = ttk.Treeview(root, column=("accession_number", "title", "authors","isbn","publisher","pub_year"), show='headings')
    tree.heading("accession_number", text="Accession Number")
    tree.heading("title", text="Title")
    tree.heading("authors", text= "Authors")
    tree.heading("isbn", text="ISBN")
    tree.heading("publisher", text="Publisher")
    tree.heading("pub_year", text="Year")
    
    rows = result.fetchall()
    
    
    for row in rows:
        authorid_statement = select(author_book.c.author_id).where(author_book.c.accession_number == row[0])
        result_authors = connection.execute(authorid_statement)        
        result_authors_id = result_authors.fetchall()
        author_list = []
        for auth_id in result_authors_id:
            statement = select(author_table.c.author_name).where(author_table.c.author_id == auth_id[0])
            result = connection.execute(statement)
            result = result.fetchall()[0]
            author_list.append(result[0])
                                                    
        author_list = [x + ", " for x in author_list]
        authors = "".join(author_list)
        authors_names = authors[:-2]



        tree.insert("", tk.END, values=(row[0],row[1],authors_names,row[2], row[3], row[4]))
       
           
    tree.grid(row=0, column=0, sticky='nsew')
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')
    

def isbn_search(isbn) :
    root = Tk() 
    connection = engine.connect()
    root.title("Book Search Results")
    # add condition for fine
    statement = select(books.c.accession_number,books.c.title,books.c.isbn_id,books.c.publisher_name,books.c.publication_yr).where(books.c.isbn_id == isbn)
    result = connection.execute(statement)
    
    tree = ttk.Treeview(root, column=("accession_number", "title", "authors","isbn","publisher","pub_year"), show='headings')
    tree.heading("accession_number", text="Accession Number")
    tree.heading("title", text="Title")
    tree.heading("authors", text= "Authors")
    tree.heading("isbn", text="ISBN")
    tree.heading("publisher", text="Publisher")
    tree.heading("pub_year", text="Year")
    
    rows = result.fetchall()
    
    
    for row in rows:
        authorid_statement = select(author_book.c.author_id).where(author_book.c.accession_number == row[0])
        result_authors = connection.execute(authorid_statement)        
        result_authors_id = result_authors.fetchall()
        author_list = []
        for auth_id in result_authors_id:
            statement = select(author_table.c.author_name).where(author_table.c.author_id == auth_id[0])
            result = connection.execute(statement)
            result = result.fetchall()[0]
            author_list.append(result[0])
                                                    
        author_list = [x + ", " for x in author_list]
        authors = "".join(author_list)
        authors_names = authors[:-2]



        tree.insert("", tk.END, values=(row[0],row[1],authors_names,row[2], row[3], row[4]))
       
           
    tree.grid(row=0, column=0, sticky='nsew')
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

def publisher_search(pub):
    root = Tk() 
    connection = engine.connect()
    root.title("Book Search Results")
    # add condition for fine
    statement = select(books.c.accession_number,books.c.title,books.c.isbn_id,books.c.publisher_name,books.c.publication_yr).where(or_(books.c.publisher_name == pub,
                                                                                                                                       books.c.publisher_name.like(f"% {pub}%"),
                                                                                                                                       books.c.publisher_name.like(f"{pub} %"),
                                                                                                                                        books.c.publisher_name.like(f"% {pub} %")))
    result = connection.execute(statement)
    
    tree = ttk.Treeview(root, column=("accession_number", "title", "authors","isbn","publisher","pub_year"), show='headings')
    tree.heading("accession_number", text="Accession Number")
    tree.heading("title", text="Title")
    tree.heading("authors", text= "Authors")
    tree.heading("isbn", text="ISBN")
    tree.heading("publisher", text="Publisher")
    tree.heading("pub_year", text="Year")
    
    rows = result.fetchall()
    
    
    for row in rows:
        authorid_statement = select(author_book.c.author_id).where(author_book.c.accession_number == row[0])
        result_authors = connection.execute(authorid_statement)        
        result_authors_id = result_authors.fetchall()
        author_list = []
        for auth_id in result_authors_id:
            statement = select(author_table.c.author_name).where(author_table.c.author_id == auth_id[0])
            result = connection.execute(statement)
            result = result.fetchall()[0]
            author_list.append(result[0])
                                                    
        author_list = [x + ", " for x in author_list]
        authors = "".join(author_list)
        authors_names = authors[:-2]



        tree.insert("", tk.END, values=(row[0],row[1],authors_names,row[2], row[3], row[4]))
       
           
    tree.grid(row=0, column=0, sticky='nsew')
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')
    

def pub_yr_search(pub_yr):
    root = Tk() 
    connection = engine.connect()
    root.title("Book Search Results")
    # add condition for fine
    statement = select(books.c.accession_number,books.c.title,books.c.isbn_id,books.c.publisher_name,books.c.publication_yr).where(or_(books.c.publication_yr == pub_yr,
                                                                                                                                       books.c.publication_yr.like(f"% {pub_yr}%"),
                                                                                                                                       books.c.publication_yr.like(f"{pub_yr} %")))
    result = connection.execute(statement)
    
    tree = ttk.Treeview(root, column=("accession_number", "title", "authors","isbn","publisher","pub_year"), show='headings')
    tree.heading("accession_number", text="Accession Number")
    tree.heading("title", text="Title")
    tree.heading("authors", text= "Authors")
    tree.heading("isbn", text="ISBN")
    tree.heading("publisher", text="Publisher")
    tree.heading("pub_year", text="Year")
    
    rows = result.fetchall()
    
    
    for row in rows:
        authorid_statement = select(author_book.c.author_id).where(author_book.c.accession_number == row[0])
        result_authors = connection.execute(authorid_statement)        
        result_authors_id = result_authors.fetchall()
        author_list = []
        for auth_id in result_authors_id:
            statement = select(author_table.c.author_name).where(author_table.c.author_id == auth_id[0])
            result = connection.execute(statement)
            result = result.fetchall()[0]
            author_list.append(result[0])
                                                    
        author_list = [x + ", " for x in author_list]
        authors = "".join(author_list)
        authors_names = authors[:-2]



        tree.insert("", tk.END, values=(row[0],row[1],authors_names,row[2], row[3], row[4]))
       
           
    tree.grid(row=0, column=0, sticky='nsew')
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

def author_search(author):
    root = Tk() 
    connection = engine.connect()
    root.title("Book Search Results")
    # add condition for fine
    statement = select(author_table.c.author_id).where(or_(author_table.c.author_name == author,
                                                           author_table.c.author_name.like(f"% {author}"),
                                                        author_table.c.author_name.like(f"{author} %"),
                                                           author_table.c.author_name.like(f"% {author} %")))
    result_author_id = connection.execute(statement)
    result_author_id = result_author_id.fetchall();
    book_ids = []
    for auth_id in result_author_id:

        statement = select(author_book.c.accession_number).where(author_book.c.author_id == auth_id[0])
        result = connection.execute(statement)
        result = result.fetchall();
        for r in result:
            if r[0] not in book_ids:
                book_ids.append(r[0])


            
    final = []
    for b in book_ids:
        statement = select(books.c.accession_number,books.c.title,books.c.isbn_id,books.c.publisher_name,books.c.publication_yr).where(books.c.accession_number == b)
        result = connection.execute(statement)
        result = result.fetchone()

        authorid_statement = select(author_book.c.author_id).where(author_book.c.accession_number == b)
        result_authors = connection.execute(authorid_statement)        
        result_authors_id = result_authors.fetchall()
        author_list = []
        for auth_id in result_authors_id:
            statement = select(author_table.c.author_name).where(author_table.c.author_id == auth_id[0])
            result1 = connection.execute(statement)
            result1 = result1.fetchall()[0]
            author_list.append(result1[0])
                                                    
        author_list = [x + ", " for x in author_list]
        authors = "".join(author_list)
        authors_names = authors[:-2]

        final.append((result[0],result[1],authors_names,result[2],result[3],result[4]))

    
    
    tree = ttk.Treeview(root, column=("accession_number", "title", "authors","isbn","publisher","pub_year"), show='headings')
    tree.heading("accession_number", text="Accession Number")
    tree.heading("title", text="Title")
    tree.heading("authors", text= "Authors")
    tree.heading("isbn", text="ISBN")
    tree.heading("publisher", text="Publisher")
    tree.heading("pub_year", text="Year")
    
    for row in final:

        tree.insert("", tk.END, values=row)
       
           
    tree.grid(row=0, column=0, sticky='nsew')
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

def display_reserve(root):
    root.title("Display reservation")
    connection = engine.connect()
    statement = select(reserve.c.accession_number)
    result = connection.execute(statement)

    tree = ttk.Treeview(root, column=("accession_number", "title", "authors","isbn","publisher","pub_year"), show='headings')
    tree.heading("accession_number", text="Accession Number")
    tree.heading("title", text="Title")
    tree.heading("authors", text= "Authors")
    tree.heading("isbn", text="ISBN")
    tree.heading("publisher", text="Publisher")
    tree.heading("pub_year", text="Year")
    
    rows = result.fetchall()
    
    
    for row in rows:
        book_statement = select(books.c.title,books.c.isbn_id,books.c.publisher_name,books.c.publication_yr).where(books.c.accession_number == row[0])
        authorid_statement = select(author_book.c.author_id).where(author_book.c.accession_number == row[0])
        result_book = connection.execute(book_statement)
        result_authorid = connection.execute(authorid_statement)
        book = result_book.fetchone()
        authorsid = result_authorid.fetchall()
        author_list = []
        for auth_id in authorsid:
            statement = select(author_table.c.author_name).where(author_table.c.author_id == auth_id[0])
            result = connection.execute(statement)
            result = result.fetchall()[0]
            author_list.append(result[0])                                            
        author_list = [x + ", " for x in author_list]
        authors = "".join(author_list)
        authors_names = authors[:-2]

        tree.insert("", tk.END, values=(row[0],book[0],authors_names,book[1], book[2],book[3]))
       
           
    
    tree.grid(row=0, column=0, sticky='nsew')
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')
  

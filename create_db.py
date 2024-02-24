
from sqlalchemy import Column,String,DateTime,Integer,Table,ForeignKey,BigInteger,Date
from datetime import datetime
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
from sqlalchemy import MetaData


engine = create_engine('mysql+mysqlconnector://root:GlenPeh8310@localhost/db')                


meta = MetaData()    
members = Table(
    'members',meta,
    Column('alphanumeric_id', String(20), primary_key=True),
    Column('name', String(500),nullable = False),
    Column('faculty',String(50),nullable = False),
    Column('phone_num',String(50),nullable = False),
    Column('email_address',String(50),nullable = False),
    )
    

books = Table(
    'books', meta,
    Column('accession_number', Integer, primary_key = True),
    Column('title', String(100), nullable = False),
    Column("isbn_id", BigInteger , primary_key = True),
    Column('publication_yr',Integer(),nullable = False),
    Column("publisher_name", String(50),nullable = False),
    )
    
author_table = Table(
    'author_table', meta,
    Column('author_id', Integer, primary_key = True),
    Column('author_name',String(50), nullable = False, unique= True)
    )
    
author_book = Table(
    #note
    'author_book', meta,
    Column('author_id', Integer,ForeignKey("author_table.author_id", ondelete = "CASCADE"),primary_key=True),
    Column('accession_number', Integer, ForeignKey("books.accession_number", ondelete = "CASCADE"), primary_key=True)
    )

loan = Table (
    'loan', meta,
    Column("loan_id", Integer, primary_key = True),
    Column("accession_number", Integer, ForeignKey("books.accession_number", ondelete = "CASCADE"), nullable=False),
    Column('alphanumeric_id', String(50), ForeignKey('members.alphanumeric_id', ondelete = "CASCADE"), nullable = False),
    Column("borrow_date", DateTime,nullable=False),
    Column("return_date", DateTime, nullable=True)
    )

reserve = Table (
    'reserve', meta,
    Column("accession_number", Integer,ForeignKey("books.accession_number", ondelete = "CASCADE"), nullable=False, primary_key = True),
    Column("reserve_date", DateTime, nullable=False),
    Column("alphanumeric_id", String(50), ForeignKey("members.alphanumeric_id", ondelete = "CASCADE"), nullable=False))


fine_payment_table = Table (
    'fine_payment_table', meta,
    Column('fine_id', Integer, primary_key = True),
    Column('alphanumeric_id', String(20) , ForeignKey("members.alphanumeric_id", ondelete = "CASCADE"), nullable=False),
    Column('payment_date', DateTime, nullable = True),
    Column("amount", Integer, nullable = False))






    


    
    
    



meta.create_all(engine)


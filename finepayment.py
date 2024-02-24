from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import Column,String,DateTime,Integer,select,update,null
from datetime import datetime
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
from tkinter import *
from create_db import *
engine = create_engine('mysql+mysqlconnector://root:22Bullet7011@localhost/db')                
Session = sessionmaker(bind=engine)
session = Session()

def pay_fine(root):

    #so that other functions can access
    global membership_ID_e, payment_e, payment_date_e
    root.title("Pay fine")
    root.minsize(width=400,height=400)
    root.geometry("700x600")
    frame = Frame(root,bg="#abdbe3",bd=5,relief=GROOVE)
    frame.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    #setting labels and buttons
    main_headingLabel = Label(frame, text="Pay fine",bg="#abdbe3",  fg='black', font=('Arial',25), relief=RAISED)
    main_headingLabel.place(relx=0.32,rely=0.05, relwidth=0.3, relheight=0.1)
    
    membership_ID_label = Label(frame, text="Membership ID", bg="#abdbe3" , fg='Black', font=('Arial',10))
    membership_ID_label.place(relx=0.1,rely=0.2, relwidth=0.18, relheight=0.1)
    payment_date_label = Label(frame, text="Payment Date", bg="#abdbe3", fg='black', font=('Arial',10))
    payment_date_label.place(relx=0.1,rely=0.3, relwidth=0.15, relheight=0.1)
    payment_amount_label = Label(frame, text="Payment Amount", bg="#abdbe3", fg='black', font=('Arial',10))
    payment_amount_label.place(relx=0.1,rely=0.4, relwidth=0.17, relheight=0.1)
                                 


    membership_ID_e = Entry(frame)
    membership_ID_e.place(relx=0.32,rely=0.22, relwidth=0.4, relheight=0.05)
    
    payment_date_e = Entry(frame)
    payment_date_e.place(relx=0.32,rely=0.32, relwidth=0.4, relheight=0.05)
                                 
    payment_e = Entry(frame)
    payment_e.place(relx=0.32,rely=0.42, relwidth=0.4, relheight=0.05)
    

    #Submit Button
    submit_btn = Button(root,text="Pay Fine",bg='blue', fg='white', command = pay_fine_fn)
    submit_btn.place(relx=0.28,rely=0.85, relwidth=0.18,relheight=0.08)

    quit_btn = Button(root,text="Back to Fines Menue",bg='blue', fg='white', command=root.destroy)
    quit_btn.place(relx=0.6,rely=0.85, relwidth=0.18,relheight=0.08)

def pay_fine_fn():
    global membership_ID,fee_e, payment_date_input_g
    root = Tk()
    root.title("Pay fine")
    root.minsize(width=400,height=400)
    root.geometry("700x600")
    frame = Frame(root,bg="#abdbe3",bd=5,relief=GROOVE)
    frame.place(relx=0,rely=0,relwidth=1,relheight=1)
      
    payment_date_input_g = datetime.strptime(payment_date_e.get(),'%d/%m/%Y')
    membership_ID = membership_ID_e.get()
    fee_e = payment_e.get()
    
    main_headingLabel = Label(frame, text="Please confirm details to be correct",bg="#abdbe3",  fg='black', font=('Arial',15), relief=RAISED)
    main_headingLabel.place(relx=0.22,rely=0.05, relwidth=0.5, relheight=0.1)
    
    membership_ID_label = Label(frame, text="Membership ID", bg="#abdbe3" , fg='Black', font=('Arial',10))
    membership_ID_label.place(relx=0.1,rely=0.2, relwidth=0.18, relheight=0.1)
    payment_date_label = Label(frame, text="Payment Date", bg="#abdbe3", fg='black', font=('Arial',10))
    payment_date_label.place(relx=0.1,rely=0.3, relwidth=0.15, relheight=0.1)
    payment_amount_label = Label(frame, text="Payment Amount(Exact fee only)", bg="#abdbe3", fg='black', font=('Arial',10))
    payment_amount_label.place(relx=0.1,rely=0.4, relwidth=0.3, relheight=0.1)
    
    mem_ID = Label(frame, text= membership_ID, bg="#abdbe3" , fg='Black', font=('Arial',10))
    mem_ID.place(relx=0.5,rely=0.18, relwidth=0.2, relheight=0.15)
    
    p_date = Label(frame, text=payment_date_input_g, bg="#abdbe3", fg='black', font=('Arial',10))
    p_date.place(relx=0.5,rely=0.3, relwidth=0.2, relheight=0.1)
    
    fee_label = Label(frame, text= "$" + str(fee_e), bg="#abdbe3", fg='black', font=('Arial',10))
    fee_label.place(relx=0.5,rely=0.4, relwidth=0.2, relheight=0.1)

    submit_btn = Button(root,text="Pay Fine",bg='blue', fg='white', command = pay_fine_sql)
    submit_btn.place(relx=0.28,rely=0.85, relwidth=0.18,relheight=0.08)

    quit_btn = Button(root,text="Back to Fines Menue",bg='blue', fg='white', command=root.destroy)
    quit_btn.place(relx=0.6,rely=0.85, relwidth=0.18,relheight=0.08)     


def pay_fine_sql():
    connection = engine.connect()
    get_fine_statement = select(fine_payment_table.c.amount).where(fine_payment_table.c.alphanumeric_id == membership_ID).where(
        fine_payment_table.c.payment_date.is_(null()))
    get_fine_result = connection.execute(get_fine_statement)
    get_fine_result = get_fine_result.fetchall()
    if get_fine_result == []:
        messagebox.showerror(message = "Error! \n Member has no fine")
    else:
        fine = get_fine_result[0][0]
        fine = int(fine)
        fee = int(fee_e)
        if fee != fine:
            messagebox.showerror(message = "Error! \n Incorrect fine payment amount")
        else:
            try:
                update_fine_statement = update(fine_payment_table).values(amount = 0, payment_date = payment_date_input_g)
                connection.execute(update_fine_statement)
                messagebox.showinfo(message = "Fine paid")
            except Exception as e:
                print(e)


                                 
   
    
    
 




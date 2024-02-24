from tkinter import *

import sqlalchemy
from tkinter import messagebox
from libfunctions import *
from membershipfunctions import *
from finepayment import *
from displayfunctions import *
class App:

    def __init__(self, master):
        self.new_window = None
        self.master = master
        self.master.title("Library")
        self.master.minsize(width=400,height=400)
        self.master.geometry("600x500")
        self.frame = Frame(self.master,bg="#abdbe3",bd=5,relief=GROOVE)
        self.showMain()
    
        
    def showMain(self):

        self.frame.place(relx=0,rely=0,relwidth=1,relheight=1)


        headingLabel = Label(self.frame, text="Library", bg='blue', fg='white', font=('Arial',30), relief=RAISED)

        headingLabel.place(relx=0.3,rely=0.1, relwidth=0.4, relheight=0.1)

        btn_membership = Button(self.frame,text="Membership", bg= "black", fg = "white", command= lambda : self.change_frame(self.showMembershipSection))
        btn_membership.place(relx=0.35,rely=0.35,relwidth=0.3, relheight= 0.05)
            
        btn_book = Button(self.frame,text="Book", bg= "black", fg = "white", command= lambda : self.change_frame(self.showBookSection))
        btn_book.place(relx=0.35,rely=0.42,relwidth=0.3, relheight= 0.05)
        
        btn_loans = Button(self.frame,text="Loans", bg= "black", fg = "white", command= lambda : self.change_frame(self.showLoans))
        btn_loans.place(relx=0.35,rely=0.49,relwidth=0.3, relheight= 0.05)
           

        btn_reservations = Button(self.frame,text="Reservations", bg= "black", fg = "white", command= lambda : self.change_frame(self.showReservations))
        btn_reservations.place(relx=0.35,rely=0.56,relwidth=0.3, relheight= 0.05)

        btn_fine = Button(self.frame,text="Fines", bg= "black", fg = "white", command= lambda : self.change_frame(self.showFines))
        btn_fine.place(relx=0.35,rely=0.63,relwidth=0.3, relheight= 0.05)
        
        btn_reports = Button(self.frame,text="Reports", bg= "black", fg = "white", command= lambda : self.change_frame(self.showReport))
        btn_reports.place(relx=0.35,rely=0.70,relwidth=0.3, relheight= 0.05)

    def showReport(self):
        headingLabel1 = Label(self.frame, text="Select one of the Options below", bg='blue', fg='white', font=('Arial',10))
        headingLabel1.place(relx=0.3,rely=0.1,relwidth=0.4,relheight=0.1)
        btn_search = Button(self.frame,text="Book Search", bg= "black", fg = "white", command= lambda : self.pop_new_window(book_search))
        btn_search.place(relx=0.3,rely=0.25,relwidth=0.4, relheight= 0.05)
        btn_display_all_loan_books = Button(self.frame,text="Books on Loan", bg= "black", fg = "white", command= lambda :self.pop_new_window(display_books_on_loan))
        btn_display_all_loan_books.place(relx=0.30,rely=0.35,relwidth=0.4, relheight= 0.05)
        btn_display_reservations = Button(self.frame,text="Books on Reservation", bg= "black", fg = "white", command=  lambda : self.pop_new_window(display_reserve))
        btn_display_reservations.place(relx=0.30,rely=0.45,relwidth=0.4, relheight= 0.05)
        btn_fines = Button(self.frame,text="Outstanding Fines", bg= "black", fg = "white", command= lambda : self.pop_new_window(display_members_with_fine))
        btn_fines.place(relx=0.30,rely=0.55,relwidth=0.4, relheight= 0.05)
        btn_lib_member_loans = Button(self.frame,text="Books on Loan to Member", bg= "black", fg = "white", command= lambda : self.pop_new_window(display_books_on_loan_member))
        btn_lib_member_loans.place(relx=0.30,rely=0.65,relwidth=0.4, relheight= 0.05)  
        btn_back = Button(self.frame,text="Back To Main Menu", bg= "blue", fg = "white", command= self.go_back)
        btn_back.place(relx=0.3,rely=0.75,relwidth=0.4, relheight= 0.05)
        
                

#create membership section       
    def showMembershipSection(self):
        headingLabel1 = Label(self.frame, text="Select one of the Options below", bg='blue', fg='white', font=('Arial',10))
        headingLabel1.place(relx=0.3,rely=0.1,relwidth=0.4,relheight=0.1)
    #Create buttons 
        btn_creation = Button(self.frame,text="Creation", bg= "black", fg = "white", command= lambda : self.pop_new_window(create_member))
        btn_creation.place(relx=0.35,rely=0.35,relwidth=0.3, relheight= 0.05)
        btn_update = Button(self.frame,text="Update", bg= "black", fg = "white", command= lambda : self.pop_new_window(update_member))
        btn_update.place(relx=0.35,rely=0.45,relwidth=0.3, relheight= 0.05)
        btn_delete = Button(self.frame,text="Deletion", bg= "black", fg = "white", command= lambda : self.pop_new_window(delete_member))
        btn_delete.place(relx=0.35,rely=0.55,relwidth=0.3, relheight= 0.05)
        btn_back = Button(self.frame,text="Back To Main Menu", bg= "blue", fg = "white", command= self.go_back)
        btn_back.place(relx=0.3,rely=0.7,relwidth=0.4, relheight= 0.05)
#create book section
    def showFines(self):
        headingLabel1 = Label(self.frame, text="Select one of the Options below", bg='blue', fg='white', font=('Arial',10))
        headingLabel1.place(relx=0.3,rely=0.1,relwidth=0.4,relheight=0.1)
        btn_fine = Button(self.frame,text="Payment", bg= "black", fg = "white", command= lambda : self.pop_new_window(pay_fine))
        btn_fine.place(relx=0.35,rely=0.35,relwidth=0.3, relheight= 0.1)
        btn_back = Button(self.frame,text="Back To Main Menu", bg= "blue", fg = "white", command= self.go_back)
        btn_back.place(relx=0.3,rely=0.7,relwidth=0.4, relheight= 0.05)
    def showBookSection(self):
        headingLabel1 = Label(self.frame, text="Select one of the Options below", bg='blue', fg='white', font=('Arial',10))
        headingLabel1.place(relx=0.3,rely=0.02,relwidth=0.4,relheight=0.1)
            #Create buttons
        btn_acquisition = Button(self.frame,text="Acquisition", bg= "black", fg = "white", command= lambda : self.pop_new_window(book_acquisition))
        btn_acquisition.place(relx=0.35,rely=0.3,relwidth=0.3, relheight= 0.17)
        
        btn_withdrawal = Button(self.frame,text="Withdrawal", bg= "black", fg = "white", command= lambda : self.pop_new_window(book_withdraw))
        btn_withdrawal.place(relx=0.35,rely=0.5,relwidth=0.3, relheight= 0.17)
        

      

        btn_back = Button(self.frame,text="Back to Main menu", bg= "blue", fg = "white", command= self.go_back)
        btn_back.place(relx=0.3,rely=0.7,relwidth=0.4, relheight= 0.05)
        
    def showLoans(self):
        headingLabel1 = Label(self.frame, text="Select one of the Options below", bg='blue', fg='white', font=('Arial',10))
        headingLabel1.place(relx=0.3,rely=0.02,relwidth=0.4,relheight=0.1)
        btn_borrow = Button(self.frame,text="Book Borrowing", bg= "black", fg = "white", command= lambda : self.pop_new_window(book_borrow))
        btn_borrow.place(relx=0.35,rely=0.3,relwidth=0.3, relheight= 0.17)
        
        btn_return = Button(self.frame,text="Book Returning", bg= "black", fg = "white", command= lambda : self.pop_new_window(book_return))
        btn_return.place(relx=0.35,rely=0.5,relwidth=0.3, relheight= 0.17)

        btn_back = Button(self.frame,text="Back to Main menu", bg= "blue", fg = "white", command= self.go_back)
        btn_back.place(relx=0.3,rely=0.7,relwidth=0.4, relheight= 0.05)

    def showReservations(self):
        headingLabel1 = Label(self.frame, text="Select one of the Options below", bg='blue', fg='white', font=('Arial',10))
        headingLabel1.place(relx=0.3,rely=0.02,relwidth=0.4,relheight=0.1)
        
        btn_reservation = Button(self.frame,text="Make a Reservation", bg= "black", fg = "white", command= lambda : self.pop_new_window(book_reserve))
        btn_reservation.place(relx=0.35,rely=0.3,relwidth=0.3, relheight= 0.17)
        
        btn_cancellation = Button(self.frame,text="Cancel Reservation", bg= "black", fg = "white", command= lambda : self.pop_new_window(cancel_reservation))
        btn_cancellation.place(relx=0.35,rely=0.5,relwidth=0.3, relheight= 0.17)
        
        btn_back = Button(self.frame,text="Back To Main Menu", bg= "blue", fg = "white", command= self.go_back)
        btn_back.place(relx=0.3,rely=0.7,relwidth=0.4, relheight= 0.05)  
        
#create display section
    def showDisplay(self) :
        headingLabel1 = Label(self.frame, text="Library", bg='blue', fg='white', font=('Arial',30))
        headingLabel1.place(relx=0.3,rely=0.1,relwidth=0.4,relheight=0.1)

    def go_back(self):
        self.change_frame(self.showMain)
           
    def change_frame(self,section):
        for widget in self.frame.winfo_children():
            widget.destroy()
        section()
   
     
        
    def pop_new_window(self,section):
        root = Tk()
        self.new_window = root
        section(self.new_window)


   

if __name__ == "__main__" :
    root = Tk()
    app = App(root)
    app.showMain()
    app.master.mainloop()


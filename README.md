The Final Logical Schema: \n
  members (alphanumeric_id, phone_num, name, faculty, email_address) 
  books (accession_number, publication_yr, publisher_name, isbn_id, title)
  loan (loan_id, accession_number, borrow_date, return_date, alphanumeric_id) 
  reserve (accession_number, alphanumeric_id, reserve_date) 
  fine_payment_table  (fine_id, alphanumeric_id, payment_date, amount) 
  author_table (author_id, author_name)
  author_book (author_id, accession_number) 

The Final Logical Data Model:
  members (alphanumeric_id, phone_num, name, faculty, email_address) 
    Primary key alphanumeric_id
  loan (loan_id, accession_number, borrow_date, return_date, alphanumeric_id) 
    Primary key loan_id
    Foreign key accession_number references books(accession_number) 
    Foreign key alphanumeric_id references members(alphanumeric_id) 
  fine_payment_table  (fine_id, alphanumeric_id, payment_date, amount) 
    Primary key fine_id
    Foreign key alphanumeric_id references members(alphanumeric_id) 
  author_book (author_id, accession_number) 
    Primary key author_id, accession_number
    Foreign key accession_number references books(accession_number) 
    Foreign key author_id  references author_table(author_id) 
  books (accession_number, publication_yr, publisher_name, isbn_id, title)
    Primary key accession_number
  reserve (accession_number, alphanumeric_id, reserve_date) 
    Primary key accession_number 
    Foreign key accession_number references books(accession_number) 
    Foreign key alphanumeric_id references members(alphanumeric_id) 
  author_table (author_id, author_name)
    Primary key author_id
  

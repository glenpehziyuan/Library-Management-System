DROP DATABASE IF EXISTS db;
CREATE DATABASE db;
USE db;
CREATE TABLE members(
	alphanumeric_id VARCHAR(50) NOT NULL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    faculty VARCHAR(50) NOT NULL,
    phone_num VARCHAR(20) NOT NULL,
    email_address VARCHAR(50) NOT NULL
    );
CREATE TABLE books(
	accession_number VARCHAR(10) NOT NULL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
	isbn_id BIGINT NOT NULL,	
    publication_yr INT NOT NULL,
    publisher_name VARCHAR(50) NOT NULL 
    ); 

CREATE TABLE author_table(
	author_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(50) NOT NULL,
    CONSTRAINT NAME_PERSON UNIQUE (author_name)
    );

CREATE TABLE author_book(
	author_id INT NOT NULL AUTO_INCREMENT,
    accession_number VARCHAR(10) NOT NULL,
    PRIMARY KEY(author_id,accession_number),
    FOREIGN KEY(author_id) REFERENCES author_table(author_id) ON DELETE CASCADE,
    FOREIGN KEY(accession_number) REFERENCES books(accession_number) ON DELETE CASCADE
    );

# REMOVE DUE DATE?   

CREATE TABLE loan(
	loan_id INT NOT NULL PRIMARY KEY auto_increment,
    accession_number VARCHAR(10) NOT NULL,
    alphanumeric_id VARCHAR(50) NOT NULL,
    borrow_date DATETIME,
    return_date DATETIME,
    FOREIGN KEY (accession_number) REFERENCES books(accession_number) ON DELETE CASCADE,
    FOREIGN KEY (alphanumeric_id) REFERENCES members(alphanumeric_id) ON DELETE CASCADE
    );

CREATE TABLE reserve(
	accession_number VARCHAR(10) NOT NULL PRIMARY KEY,
    reserve_date DATETIME NOT NULL,
    alphanumeric_id VARCHAR(50) NOT NULL,
    FOREIGN KEY(accession_number) REFERENCES books(accession_number) ON DELETE CASCADE,
    FOREIGN KEY(alphanumeric_id) REFERENCES members(alphanumeric_id) ON DELETE CASCADE
    );
    
CREATE TABLE fine_payment_table (
	fine_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    alphanumeric_id VARCHAR(50) NOT NULL,
    payment_date DATETIME,
    amount INT NOT NULL,
    FOREIGN KEY(alphanumeric_id) REFERENCES members(alphanumeric_id) ON DELETE CASCADE
    );
 
INSERT INTO members (alphanumeric_id, name, faculty, phone_num, email_address)
VALUES ('A101A', 'Hermione Granger', 'Science', '33336663', 'flying@als.edu');
INSERT INTO members (alphanumeric_id, name, faculty, phone_num, email_address)
VALUES ('A201B', 'Sherlock Holmes', 'Law', '44327676', 'elementarydrw@als.edu');
INSERT INTO members (alphanumeric_id, name, faculty, phone_num, email_address)
VALUES ('A301C', 'Tintin', 'Engineering', '14358788', 'luvmilu@als.edu');
INSERT INTO members (alphanumeric_id, name, faculty, phone_num, email_address)
VALUES ('A401D', 'Prinche Hamlet', 'FASS', '16091609', 'tobeornot@als.edu');
INSERT INTO members (alphanumeric_id, name, faculty, phone_num, email_address)
VALUES ('A5101E', 'Willy Wonka', 'FASS', '9701970', 'choco1@als.edu');
INSERT INTO members (alphanumeric_id, name, faculty, phone_num, email_address)
VALUES ('A601F', 'Holly Golightly', 'Business', '55548008', 'diamond@als.edu');
INSERT INTO members (alphanumeric_id, name, faculty, phone_num, email_address)
VALUES ('A701G', 'Raskolnikov', 'Law', '18661866', 'oneaxe@als.edu');
INSERT INTO members (alphanumeric_id, name, faculty, phone_num, email_address)
VALUES ('A801H', 'Patrick Bateman', 'Business', '38548544', 'mice@als.edu');
INSERT INTO members (alphanumeric_id, name, faculty, phone_num, email_address)
VALUES ('A901I', 'Captain Ahab', 'Science', '18511851', 'wwhale@als.edu');

INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES ('A01', 'A 1984 Story', 9790000000001, 'Intra S.r.l.s.', 2021);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A02", '100 anos de soledad', 9790000000002, "Vintage Espanol", 2017);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A03",'Brave New World',9790000000003,'Harper Perennial', 2006);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A04",'Crime and Punishment',9790000000004,'Penguin', 2002);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES('A05', "The Lion, The Witch and The Wardrobe", 9790000000005,"Harper Collins", 2002); 
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A06", "Frankenstein", 9790000000006, "Reader's Library Classics", 2021);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES('A07', 'The Grapes of Wrath', 9790000000007, "Penguin Classics", 2006);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A08", 'The Adventures of Huckleberry Finn', 9790000000008, 'SeaWolf Press', 2021);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A09", "Great Expectations", 9790000000009, "Penguin Classics", 2002);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A10", "Catch-22", 9790000000010, "Simon & Schuster",2011);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A11", "The Iliad", 9790000000011, "Penguin Classics", 1998);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A12", "Les Miserables", 9790000000012, "Signet", 2013);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A13", "Ulysses", 9790000000013, "Vintage", 1990);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A14", "Lolita", 9790000000014, "Vintage", 1989);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A15", "Atlas Shrugged", 9790000000015, "Dutton", 2005);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A16", "Perfume", 9790000000016, "Vintage", 2001);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A17", "The Metamorphosis", 9790000000017, "12th Media Services", 2017);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A18", "American Psycho", 9790000000018, "ROBERT LAFFONT", 2019);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A19", "Asterix the Gaul", 9790000000019, "Papercutz", 2020);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A20", "Fahrenheit 451", 9790000000020, "Simon & Schuster", 2012);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A21", "Foundation", 9790000000021, "Bantam Spectra Books", 1991);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A22", "The Communist Manifesto", 9790000000022, "Penguin Classics", 2002);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A23", "”Rights of Man, Common Sense, and Other Political Writings”", 9790000000023, "Oxford University Press", 2009);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A24", "The Prince", 9790000000024, "Independently published", 2019);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A25", "The Wealth of Nations", 9790000000025, "Royal Classics", 2021);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A26", "Don Quijote", 9790000000026, "Ecco", 2005);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A27", "The Second Sex", 9790000000027, "Vintage", 2011);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A28", "Critique of Pure Reason", 9790000000028, "Cambridge University Press", 1999);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A29", "On The Origin of Species", 9790000000029, "Signet", 2003);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A30", "Philosophae Naturalis Principia Mathematica", 9790000000030, "University of California Press", 2016);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A31", "The Unbearable Lightness of Being", 9790000000031, "Harper Perennial Modern Classics", 2009);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A32", "The Art of War", 9790000000032, "LSC Communications", 2007);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A33", "Ficciones", 9790000000033, "Penguin Books", 1999);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A34", "El Amor en Los Tiempos del Colera", 9790000000034, "Vintage", 2007);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A35", "Pedro Paramo", 9790000000035, "Grove Press", 1994);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A36", "The Labyrinth of Solitude", 9790000000036, "Penguin Books", 2008);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A37", "Twenty Love Poems and a Song of Despair", 9790000000037, "Penguin Classics", 2006);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A38", "QED: The Strange Theory of Light and Matter", 9790000000038, "Princeton University Press", 2014);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A39", "A Brief History of Time", 9790000000039, "Bantam", 1996);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A40", "Cosmos", 9790000000040, "Ballantine Books", 2013);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A41", "Calculus Made Easy", 9790000000041, "St Martins Pr", 1970);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A42", "Notes on Thermodynamics and Statistics", 9790000000042, "University of Chicago Press", 1988);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A43", "The Federalist", 9790000000043, "Coventry House Publishing", 2015);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A44", "Second Treatise of Government", 9790000000044, "Hackett Publishing Company, Inc.", 1980);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A45", "The Open Society and Its Enemies", 9790000000045, "Princeton University Press", 2020);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A46", "A People's History of the United States", 9790000000046, "Harper Perennial Modern Classics", 2015);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES('A47', "Lord of the Flies", 9790000000047, 'Penguin Books', 2003);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A48", "Animal farm", 9790000000048, "Wisehouse Classics", 2021);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A49", "The Old Man and the Sea", 9790000000049, "Scribner", 1995);
INSERT INTO books (accession_number, title, isbn_id, publisher_name, publication_yr)
VALUES("A50", "Romance of the Three Kingdoms", 9790000000050, "Penguin Books", 2018);

INSERT INTO author_table (author_name)
VALUES ('George Orwell');
INSERT INTO author_table (author_name)
VALUES ('Gabriel Garcia Marquez');
INSERT INTO author_table (author_name)
VALUES ('Aldous Huxley');
INSERT INTO author_table (author_name)
VALUES ('Fyodor Dostoevsky');
INSERT INTO author_table (author_name)
VALUES ('C.S. Lewis');
INSERT INTO author_table (author_name)
VALUES ('Mary Shelley,');
INSERT INTO author_table (author_name)
VALUES ('John Steinbeck');
INSERT INTO author_table (author_name)
VALUES ('Mark Twain');
INSERT INTO author_table (author_name)
VALUES ('Charles Dickens');
INSERT INTO author_table (author_name)
VALUES ('Joseph Heller');
INSERT INTO author_table (author_name)
VALUES ('Homer');
INSERT INTO author_table (author_name)
VALUES ('Victor Hugo');
INSERT INTO author_table (author_name)
VALUES ('James Joyce');
INSERT INTO author_table (author_name)
VALUES ('Vladimir Nabokov');
INSERT INTO author_table (author_name)
VALUES ('Ayn Rand');
INSERT INTO author_table (author_name)
VALUES ('Patrick Suskind');
INSERT INTO author_table (author_name)
VALUES ('Franz Kafka');
INSERT INTO author_table (author_name)
VALUES ('Bret Easton Ellis');
INSERT INTO author_table (author_name)
VALUES ('Rene Goscinny');
INSERT INTO author_table (author_name)
VALUES ('Albert Uderzo');
INSERT INTO author_table (author_name)
VALUES ('Ray Bradbury');
INSERT INTO author_table (author_name)
VALUES ('Isaac Asimov');
INSERT INTO author_table (author_name)
VALUES ('Karl Marx');
INSERT INTO author_table (author_name)
VALUES ('Friedrich Engels');
INSERT INTO author_table (author_name)
VALUES ('Thomas Paine');
INSERT INTO author_table (author_name)
VALUES ('Niccolo Machiavelli');
INSERT INTO author_table (author_name)
VALUES ('Adam Smith');
INSERT INTO author_table (author_name)
VALUES ('Miguel de Cervantes Saavedra');
INSERT INTO author_table (author_name)
VALUES ('Simone de Beauvoir');
INSERT INTO author_table (author_name)
VALUES ('Immanuel Kant');
INSERT INTO author_table (author_name)
VALUES ('Charles Darwin');
INSERT INTO author_table (author_name)
VALUES ('Isaac Newton');
INSERT INTO author_table (author_name)
VALUES ('Milan Kundera');
INSERT INTO author_table (author_name)
VALUES ('Sun Tzu');
INSERT INTO author_table (author_name)
VALUES ('Jorge Luis Borges');
INSERT INTO author_table (author_name)
VALUES ('Juan Rulfo');
INSERT INTO author_table (author_name)
VALUES ('Octavio Paz');
INSERT INTO author_table (author_name)
VALUES ('Pablo Neruda');
INSERT INTO author_table (author_name)
VALUES ('Richard Feynman');
INSERT INTO author_table (author_name)
VALUES ('Stephen Hawking');
INSERT INTO author_table (author_name)
VALUES ('Carl Sagan');
INSERT INTO author_table (author_name)
VALUES ('Silvanus P. Thompson');
INSERT INTO author_table (author_name)
VALUES ('Martin Gardner');
INSERT INTO author_table (author_name)
VALUES ('Enrico Fermi');
INSERT INTO author_table (author_name)
VALUES ('Alexander Hamilton');
INSERT INTO author_table (author_name)
VALUES ('James Madison');
INSERT INTO author_table (author_name)
VALUES ('John Jay');
INSERT INTO author_table (author_name)
VALUES ('John Lcke');
INSERT INTO author_table (author_name)
VALUES ('C. B. Macpherson');
INSERT INTO author_table (author_name)
VALUES ('Karl Popper');
INSERT INTO author_table (author_name)
VALUES ('Howard Zinn');
INSERT INTO author_table (author_name)
VALUES ('William Golding');

INSERT INTO author_table (author_name)
VALUES ('Ernest Hemingway');
INSERT INTO author_table (author_name)
VALUES ('Luo Guanzhong');

INSERT INTO author_book (author_id, accession_number)
VALUES ('1','A01');
INSERT INTO author_book (author_id, accession_number)
VALUES ('1','A48');
INSERT INTO author_book (author_id, accession_number)
VALUES ('2','A02');
INSERT INTO author_book (author_id, accession_number)
VALUES ('2','A34');
INSERT INTO author_book (author_id, accession_number)
VALUES ('3','A03');
INSERT INTO author_book (author_id, accession_number)
VALUES ('4','A04');
INSERT INTO author_book (author_id, accession_number)
VALUES ('5','A05');
INSERT INTO author_book (author_id, accession_number)
VALUES ('6','A06');
INSERT INTO author_book (author_id, accession_number)
VALUES ('7','A07');
INSERT INTO author_book (author_id, accession_number)
VALUES ('8','A08');
INSERT INTO author_book (author_id, accession_number)
VALUES ('9','A09');
INSERT INTO author_book (author_id, accession_number)
VALUES ('10','A10');
INSERT INTO author_book (author_id, accession_number)
VALUES ('11','A11');
INSERT INTO author_book (author_id, accession_number)
VALUES ('12','A12');
INSERT INTO author_book (author_id, accession_number)
VALUES ('13','A13');
INSERT INTO author_book (author_id, accession_number)
VALUES ('14','A14');
INSERT INTO author_book (author_id, accession_number)
VALUES ('15','A15');
INSERT INTO author_book (author_id, accession_number)
VALUES ('16','A16');
INSERT INTO author_book (author_id, accession_number)
VALUES ('17','A17');
INSERT INTO author_book (author_id, accession_number)
VALUES ('18','A18');
INSERT INTO author_book (author_id, accession_number)
VALUES ('19','A19');
INSERT INTO author_book (author_id, accession_number)
VALUES ('20','A19');
INSERT INTO author_book (author_id, accession_number)
VALUES ('21','A20');
INSERT INTO author_book (author_id, accession_number)
VALUES ('22','A21');
INSERT INTO author_book (author_id, accession_number)
VALUES ('23','A22');
INSERT INTO author_book (author_id, accession_number)
VALUES ('24','A22');
INSERT INTO author_book (author_id, accession_number)
VALUES ('25','A23');
INSERT INTO author_book (author_id, accession_number)
VALUES ('26','A24');
INSERT INTO author_book (author_id, accession_number)
VALUES ('27','A25');
INSERT INTO author_book (author_id, accession_number)
VALUES ('28','A26');
INSERT INTO author_book (author_id, accession_number)
VALUES ('29','A27');
INSERT INTO author_book (author_id, accession_number)
VALUES ('30','A28');
INSERT INTO author_book (author_id, accession_number)
VALUES ('31','A29');
INSERT INTO author_book (author_id, accession_number)
VALUES ('32','A30');
INSERT INTO author_book (author_id, accession_number)
VALUES ('33','A31');
INSERT INTO author_book (author_id, accession_number)
VALUES ('34','A32');
INSERT INTO author_book (author_id, accession_number)
VALUES ('35','A33');
INSERT INTO author_book (author_id, accession_number)
VALUES ('36','A35');
INSERT INTO author_book (author_id, accession_number)
VALUES ('37','A36');
INSERT INTO author_book (author_id, accession_number)
VALUES ('38','A37');
INSERT INTO author_book (author_id, accession_number)
VALUES ('39','A38');
INSERT INTO author_book (author_id, accession_number)
VALUES ('40','A39');
INSERT INTO author_book (author_id, accession_number)
VALUES ('41','A40');
INSERT INTO author_book (author_id, accession_number)
VALUES ('42','A41');
INSERT INTO author_book (author_id, accession_number)
VALUES ('43','A41');
INSERT INTO author_book (author_id, accession_number)
VALUES ('44','A42');
INSERT INTO author_book (author_id, accession_number)
VALUES ('45','A43');
INSERT INTO author_book (author_id, accession_number)
VALUES ('46','A43');
INSERT INTO author_book (author_id, accession_number)
VALUES ('47','A43');
INSERT INTO author_book (author_id, accession_number)
VALUES ('48','A44');
INSERT INTO author_book (author_id, accession_number)
VALUES ('49','A44');
INSERT INTO author_book (author_id, accession_number)
VALUES ('50','A45');
INSERT INTO author_book (author_id, accession_number)
VALUES ('51','A46');
INSERT INTO author_book (author_id, accession_number)
VALUES ('52','A47');
INSERT INTO author_book (author_id, accession_number)
VALUES ('53','A49');
INSERT INTO author_book (author_id, accession_number)
VALUES ('54','A50');







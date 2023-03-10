import sqlite3

DATABASE="book_database.db"
def create_book_database():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS book_database(management_code,isbn_code,status,last_rental_date,book_title,author,headline,sample_url,number_of_pages,release_date,register)")
    con.close()
    
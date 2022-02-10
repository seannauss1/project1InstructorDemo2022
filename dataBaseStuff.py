import sqlite3


def open_db(filename: str) -> tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)  # connect to existing DB or create new one
    cursor = db_connection.cursor()  # get ready to read/write data
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()  # make sure any changes get saved
    connection.close()

def create_top250_table(cursor:sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS top_show_data(
    ttid TEXT PRIMARY KEY,
    ''')
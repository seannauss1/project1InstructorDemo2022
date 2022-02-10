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
    rank INT DEFAULT 0,
    title TEXT,
    fulltitle TEXT,
    year INT,
    image_url TEXT,
    crew TEXT,
    imdb_rating REAL,
    imdb_rating_count INT);''')

def create_ratings_table(cursor:sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS show_ratings(
    ratings_key INT PRIMARY_KEY,
    imdb_ttcode TEXT NOT NULL,
    title TEXT,
    fulltitle TEXT,
    year INT,
    total_rating INT DEFAULT 0,
    rating10_percent REAL,
    rating10_votes INT,
    rating9_percent REAL,
    rating9_votes INT,
    rating8_percent REAL,
    rating8_votes INT,
    rating7_percent REAL,
    rating7_votes INT,
    rating6_percent REAL,
    rating6_votes INT,
    rating5_percent REAL,
    rating5_votes INT,
    rating4_percent REAL,
    rating4_votes INT,
    rating3_percent REAL,
    rating3_votes INT,
    rating2_percent REAL,
    rating2_votes INT,
    rating1_percent REAL,
    rating1_votes INT,
    FOREIGN KEY (imdb_ttcode) REFERENCES top_show_data (ttid)
    ON DELETE CASCADE ON UPDATE NO ACTION
    );''')
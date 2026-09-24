import sqlite3


DATABASE_NAME = "smartmail.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def create_tables():
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS email_analysis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email_id INTEGER,
            intent TEXT,
            priority TEXT,
            confidence REAL,
            response TEXT
        )
    """)

    connection.commit()
    connection.close()


def save_analysis(
    email_id,
    intent,
    priority,
    confidence,
    response
):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO email_analysis
        (email_id, intent, priority, confidence, response)
        VALUES (?, ?, ?, ?, ?)
    """, (
        email_id,
        intent,
        priority,
        confidence,
        response
    ))

    connection.commit()
    connection.close()

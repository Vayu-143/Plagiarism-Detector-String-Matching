import sqlite3

DB_NAME = "database.db"


# ==================================================
# CREATE DATABASE
# ==================================================

def create_database():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # USERS TABLE

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT UNIQUE,

        email TEXT UNIQUE,

        password TEXT

    )
    """)

    # SCANS TABLE

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scans (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER,

        scan_date TEXT,

        submitted_file TEXT,

        matched_file TEXT,

        score REAL

    )
    """)

    conn.commit()
    conn.close()


# ==================================================
# REGISTER USER
# ==================================================

def register_user(username, email, password):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            INSERT INTO users
            (
                username,
                email,
                password
            )
            VALUES (?, ?, ?)
            """,
            (
                username,
                email,
                password
            )
        )

        conn.commit()

        return True

    except sqlite3.IntegrityError:

        return False

    finally:

        conn.close()


# ==================================================
# LOGIN USER
# ==================================================

def login_user(username_or_email, password):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE (username=? OR email=?)
        AND password=?
        """,
        (
            username_or_email,
            username_or_email,
            password
        )
    )

    user = cursor.fetchone()

    conn.close()

    return user


# ==================================================
# SAVE SCAN
# ==================================================

def save_scan(
        user_id,
        scan_date,
        submitted_file,
        matched_file,
        score
):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO scans
        (
            user_id,
            scan_date,
            submitted_file,
            matched_file,
            score
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            user_id,
            scan_date,
            submitted_file,
            matched_file,
            score
        )
    )

    conn.commit()
    conn.close()


# ==================================================
# GET USER HISTORY
# ==================================================

def get_user_scans(user_id):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT

            scan_date,

            submitted_file,

            matched_file,

            score

        FROM scans

        WHERE user_id=?

        ORDER BY id DESC
        """,
        (user_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


# ==================================================
# GET USER DETAILS
# ==================================================

def get_user(user_id):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            username,
            email
        FROM users
        WHERE id=?
        """,
        (user_id,)
    )

    user = cursor.fetchone()

    conn.close()

    return user
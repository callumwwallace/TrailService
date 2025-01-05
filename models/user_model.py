from database import get_db_connection

def fetch_users():
    """Fetch all users from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT UserID, Username, Email FROM CW2.[User]")
    users = [{"UserID": row[0], "Username": row[1], "Email": row[2]} for row in cursor.fetchall()]
    conn.close()
    return users

def insert_user(username, email, password_hash):
    """Insert a new user into the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO CW2.[User] (Username, Email, PasswordHash) VALUES (?, ?, ?)",
        (username, email, password_hash)
    )
    conn.commit()
    conn.close()
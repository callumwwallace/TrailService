from database import get_db_connection

def fetch_trails():
    """Fetch all trails from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM CW2.Trail")
    trails = [{"TrailID": row[0], "Name": row[1], "Description": row[2], "Difficulty": row[3],
               "Duration": row[4], "Elevation": row[5], "TrailLength": row[6], "UserID": row[7]}
              for row in cursor.fetchall()]
    conn.close()
    return trails

def get_trail_by_id(trail_id):
    """Get a single trail by its ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM CW2.Trail WHERE TrailID = ?", (trail_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"TrailID": row[0], "Name": row[1], "Description": row[2], "Difficulty": row[3],
                "Duration": row[4], "Elevation": row[5], "TrailLength": row[6], "UserID": row[7]}
    return None

def insert_trail(name, description, difficulty, duration, elevation, trail_length, user_id):
    """Insert a new trail into the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO CW2.Trail (Name, Description, Difficulty, Duration, Elevation, TrailLength, UserID)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (name, description, difficulty, duration, elevation, trail_length, user_id)
    )
    conn.commit()
    conn.close()

def update_trail(trail_id, name, description, difficulty, duration, elevation, trail_length, user_id):
    """Update an existing trail in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE CW2.Trail
        SET Name = ?, Description = ?, Difficulty = ?, Duration = ?, Elevation = ?, TrailLength = ?, UserID = ?
        WHERE TrailID = ?
        """,
        (name, description, difficulty, duration, elevation, trail_length, user_id, trail_id)
    )
    conn.commit()
    rowcount = cursor.rowcount
    conn.close()
    return rowcount > 0

def delete_trail(trail_id):
    """Delete a trail from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM CW2.Trail WHERE TrailID = ?", (trail_id,))
    conn.commit()
    rowcount = cursor.rowcount
    conn.close()
    return rowcount > 0
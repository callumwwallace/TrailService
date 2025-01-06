import pyodbc

def get_db_connection():
    """Establish and return a database connection."""
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=dist-6-505.uopnet.plymouth.ac.uk.;"
        "DATABASE=COMP2001_CWallace;"
        "UID=CWallace;"
        "PWD=OelP598*;"
    )
    return conn
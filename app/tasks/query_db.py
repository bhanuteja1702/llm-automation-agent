import sqlite3
import os
from ..file_utils import write_text

def query_db(db_path: str,  output_file: str, sql_query):
    path = os.path.abspath(db_path)
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    cursor.execute("""
        {sql_query}
    """)
    total_sales = cursor.fetchone()[0] or 0
    write_text(output_file, str(total_sales))
# check_tables.py
from app import db

# Print table names in your SQLite database
print("Available tables:", db.engine.table_names())

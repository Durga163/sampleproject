from app import db


print("Tables in the database:")
print(db.engine.table_names())

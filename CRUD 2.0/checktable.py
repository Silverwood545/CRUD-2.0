from sqlalchemy import create_engine, MetaData

# Create an SQLAlchemy engine to connect to the database
# Replace 'database_url' with the actual connection string for your database
engine = create_engine('sqlite:///C:/Users/mathe/Desktop/CRUD 2.0/instance/CRUD.db')

# Create a MetaData object
metadata = MetaData()

# Reflect the existing database schema to the MetaData object
metadata.reflect(bind=engine)

# Access the table metadata
table_metadata = metadata.tables.get('project')  # Replace 'table_name' with your table's name

if table_metadata is not None:
    print("Table exists. Here is its structure:")
    print(table_metadata)
else:
    print("Table does not exist.")

if table_metadata is not None:
    print("Table exists. Here are its columns:")
    for column in table_metadata.columns:
        print(column.name)
else:
    print("Table does not exist.")

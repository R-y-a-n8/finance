import psycopg2

def connect_db():
    conn = psycopg2.connect(
        dbname='your_db_name',  # Change to your database name
        user='your_actual_username',  # Your PostgreSQL username
        password='your_actual_password',  # Your PostgreSQL password
        host='localhost'
    )
    return conn


def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100)
        );
        
        CREATE TABLE IF NOT EXISTS categories (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100)
        );

        CREATE TABLE IF NOT EXISTS transactions (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            amount DECIMAL,
            date DATE,
            type VARCHAR(10),
            category_id INTEGER REFERENCES categories(id)
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_tables()

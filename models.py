import psycopg2

def connect_db():
    conn = psycopg2.connect(
        dbname='business_finance',  # Use your actual database name
        user='your_username',        # Use your actual PostgreSQL username
        password='your_password',     # Use your actual password
        host='localhost'
    )
    return conn

def add_user(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (%s) RETURNING id;", (name,))
    user_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return user_id

def user_exists(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT EXISTS(SELECT 1 FROM users WHERE id = %s);", (user_id,))
    exists = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return exists

def add_transaction(user_id, amount, date, transaction_type, category_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO transactions (user_id, amount, date, type, category_id)
        VALUES (%s, %s, %s, %s, %s);
    """, (user_id, amount, date, transaction_type, category_id))
    conn.commit()
    cursor.close()
    conn.close()

def view_transactions():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions;")
    transactions = cursor.fetchall()
    cursor.close()
    conn.close()
    return transactions

def category_exists(category_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT EXISTS(SELECT 1 FROM categories WHERE id = %s);", (category_id,))
    exists = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return exists

def delete_transaction(transaction_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transactions WHERE id = %s;", (transaction_id,))
    conn.commit()
    cursor.close()
    conn.close()

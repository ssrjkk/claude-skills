import psycopg2

def seed_users(conn):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name) VALUES ('Test User 1'), ('Test User 2)'")
    conn.commit()

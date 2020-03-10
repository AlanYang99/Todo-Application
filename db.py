import psycopg2

def connect():
    conn = None
    try:
        conn = psycopg2.connect(
                host = "127.0.0.1",
                database = "todolist",
                user = "", #hidden for obvious reasons
                password = "" #hidden for obvious reasons
        )        
        conn.set_client_encoding('UTF8')
    except Exception as e:
        print("Unable to connect to the database")
    return conn

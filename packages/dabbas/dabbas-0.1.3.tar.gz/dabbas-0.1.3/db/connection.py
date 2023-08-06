import os


def hello():
    print("Hello, World!")


def connection_url():
    pg_user = os.environ['PG_USER']
    pg_password = os.environ['PG_PASSWORD']
    pg_host = os.environ['PG_HOST']
    pg_dbname = os.environ['PG_DBNAME']
    return f'postgresql://{pg_user}:{pg_password}@{pg_host}:5432/{pg_dbname}'

def connect():
    pg_user = os.environ['PG_USER']
    pg_password = os.environ['PG_PASSWORD']
    pg_host = os.environ['PG_HOST']
    pg_dbname = os.environ['PG_DBNAME']

    import psycopg2
    conn = psycopg2.connect(dbname=pg_dbname, user=pg_user,
                            password=pg_password, host=pg_host, port='5432')

    return conn


def query(sql):
    conn = connect()
    cur = conn.cursor()

    # Execute query and fetch results
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    conn.close()
    return cur.description, results


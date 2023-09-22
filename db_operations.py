import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read("dwh.cfg")
    DWH_DB = config.get("DWH", "DWH_DB")
    DWH_DB_USER = config.get("DWH", "DWH_DB_USER")
    DWH_DB_PASSWORD = config.get("DWH", "DWH_DB_PASSWORD")
    DWH_PORT = config.get("DWH", "DWH_PORT")
    DWH_ENDPOINT = "my-redshift-cluster.cwxqkuxop6uo.us-west-2.redshift.amazonaws.com"

    try:
        conn = psycopg2.connect(
            f"host={DWH_ENDPOINT} port={DWH_PORT} dbname=dev user={DWH_DB_USER} password={DWH_DB_PASSWORD}"
        )
        print(conn)
        print("Connected to Amazon Redshift Instance")
    except psycopg2.Error as e:
        print("Error: Could not make connection to Amazon Redshift")
        print(e)
    print("1. Connected")
    cur = conn.cursor()
    print("2. Created Cursor")

    drop_tables(cur, conn)
    print("3. Dropped tables if already exists")
    create_tables(cur, conn)
    print("4.Created tables")

    conn.close()
    print("5. Closed the connection")


if __name__ == "__main__":
    main()

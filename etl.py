import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    for query in insert_table_queries:
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

    load_staging_tables(cur, conn)
    print("2. Loaded to staging")
    insert_tables(cur, conn)
    print("3. Inserted into tables")

    conn.close()
    print("4. Closed the connection")


if __name__ == "__main__":
    main()

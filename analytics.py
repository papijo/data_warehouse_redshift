import configparser
import psycopg2
from sql_queries import select_number_rows_queries


def get_results(cur, conn):
    """
    Get the number of rows stored into each table
    """
    for query in select_number_rows_queries:
        # print('Running ' + query)
        cur.execute(query)
        results = cur.fetchone()

        for row in results:
            print("Number of rows", row)


def main():
    """
    Run queries on the staging and dimensional tables to validate that the project has been created successfully
    """
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
        cur = conn.cursor()
        print("Cursor created successfully")
    except psycopg2.Error as e:
        print("Error: Could not make connection to Amazon Redshift")
        print(e)

    get_results(cur, conn)

    conn.close()

    print("Closed the connection")


if __name__ == "__main__":
    main()

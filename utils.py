import MySQLdb
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def update_database_with_analysis(id, summary, sentiment, key_figures):
    """Update the database with the analysis results."""
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    update_query = """
    UPDATE earnings_calls
    SET summary = %s, sentiment = %s, key_figures = %s, analyzed = 1
    WHERE id = %s
    """
    cursor.execute(update_query, (summary, sentiment, key_figures, id))
    conn.commit()
    cursor.close()
    conn.close()


def main():
    # Connect to the database
    connection = MySQLdb.connect(
        host=os.getenv("DATABASE_HOST"),
        user=os.getenv("DATABASE_USERNAME"),
        passwd=os.getenv("DATABASE_PASSWORD"),
        db=os.getenv("DATABASE"),
        autocommit=True
    )

    try:
        # Create a cursor to interact with the database
        cursor = connection.cursor()

        # Execute "SHOW TABLES" query
        cursor.execute("SHOW TABLES")

        # Fetch all the rows
        tables = cursor.fetchall()

        # Print out the tables
        print("Tables in the database:")
        for table in tables:
            print(table[0])

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()


if __name__ == "__main__":
    main()

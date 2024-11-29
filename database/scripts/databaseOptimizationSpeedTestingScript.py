import psycopg2
import time
import sys

# Database connection configurations
DB_CONFIG_INDEXED = {
    'dbname': 'dbTestFast',
    'user': 'postgres',
    'password': 'arda',
    'host': 'localhost',
    'port': '5432',
}

DB_CONFIG_NON_INDEXED = {
    'dbname': 'dbSlowTest',
    'user': 'postgres',
    'password': 'arda',
    'host': 'localhost',
    'port': '5432',
}

def connect_db(db_config):
    try:
        conn = psycopg2.connect(**db_config)
        conn.autocommit = True
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        sys.exit(1)

def execute_query(cursor, query, params=None):
    #TODO IMPLEMENT THE execute_query() FUNCTION
    return

def main():
    # Connect to indexed and non-indexed databases
    conn_indexed = connect_db(DB_CONFIG_INDEXED)
    conn_non_indexed = connect_db(DB_CONFIG_NON_INDEXED)
    cursor_indexed = conn_indexed.cursor()
    cursor_non_indexed = conn_non_indexed.cursor()

    # List to store results
    results = []

    # 10 Common Queries Utilizing Indexes
    queries = [
        #TODO WRITE THE 10 MOST COMMON QUERIES
    ]

    # Execute and time the queries on both databases
    for q in queries:
        print(f"Executing {q['name']}")

        # Indexed Database
        time_indexed, _ = execute_query(cursor_indexed, q['query'], q['params'])

        # Non-Indexed Database
        time_non_indexed, _ = execute_query(cursor_non_indexed, q['query'], q['params'])

        # Calculate improvement
        improvement = ((time_non_indexed - time_indexed) / time_non_indexed) * 100 if time_non_indexed != 0 else 0

        results.append({
            'Query': q['name'],
            'Description': q['description'],
            'Time Indexed (s)': time_indexed,
            'Time Non-Indexed (s)': time_non_indexed,
            'Improvement (%)': improvement
        })

    # Queries Utilizing Materialized Views
    materialized_queries = [
        #TODO WRITE THE MATERIALIZED VIEW QUERIES AND THEIR SLOW COUNTERPARTS QUERIES
    ]

    #TODO IMPLEMENT THE LOGIC THAT RUNS THE MATERIAL VIEW QUERIS ON DATABASE AND THEN EVALUEATES THEM 

    # Close database connections
    cursor_indexed.close()
    conn_indexed.close()
    cursor_non_indexed.close()
    conn_non_indexed.close()

    # Print results
    print("\nPerformance Results:")
    for res in results:
        print(f"Query: {res['Query']}")
        print(f"Description: {res['Description']}")
        if 'Time Indexed (s)' in res:
            print(f"Time Indexed DB: {res['Time Indexed (s)']:.4f}s")
            print(f"Time Non-Indexed DB: {res['Time Non-Indexed (s)']:.4f}s")
        else:
            print(f"Time Using MV: {res['Time Using MV (s)']:.4f}s")
            print(f"Time Without MV: {res['Time Without MV (s)']:.4f}s")
        print(f"Improvement: {res['Improvement (%)']:.2f}%\n")

if __name__ == "__main__":
    main()


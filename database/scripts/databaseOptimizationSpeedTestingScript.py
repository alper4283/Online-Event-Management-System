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
    start_time = time.time()
    cursor.execute(query, params)
    rows = cursor.fetchall()
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time, rows

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
        {
            'name': 'Query 1: Upcoming Events in a Specific City',
            'query': """
                -- Retrieve upcoming events in New York
                SELECT
                    e.EventID,
                    e.Title,
                    e.Date,
                    e.StartTime,
                    e.EndTime,
                    a.City,
                    a.Country
                FROM
                    Events e
                JOIN
                    Address a ON e.AddressID = a.AddressID
                WHERE
                    a.City = %s AND
                    e.Date >= CURRENT_DATE
                ORDER BY
                    e.Date, e.StartTime;
            """,
            'params': ('Holmeston',),
            'description': 'Retrieve upcoming events in New York.'
        },
        {
            'name': 'Query 2: Events by a Specific Organizer',
            'query': """
                -- Find events organized by Tech Innovators Inc.
                SELECT
                    e.EventID,
                    e.Title,
                    e.Date,
                    o.Name AS OrganizerName
                FROM
                    Events e
                JOIN
                    EventOrganizators eo ON e.EventID = eo.EventID
                JOIN
                    Organizers o ON eo.OrganizerID = o.OrganizerID
                WHERE
                    o.Name = %s
                ORDER BY
                    e.Date DESC;
            """,
            'params': ('Hall Inc',),
            'description': 'Find events organized by Tech Innovators Inc.'
        },
        {
            'name': 'Query 3: Events in a Specific Category',
            'query': """
                -- Get events in the Technology category
                SELECT
                    e.EventID,
                    e.Title,
                    c.Name AS CategoryName,
                    e.Date
                FROM
                    Events e
                JOIN
                    EventCategories ec ON e.EventID = ec.EventID
                JOIN
                    Categories c ON ec.CategoryID = c.CategoryID
                WHERE
                    c.Name = %s
                ORDER BY
                    e.Date;
            """,
            'params': ('Technology',),
            'description': 'Get events in the Technology category.'
        },
        {
            'name': 'Query 4: Events Offering a Specific Service',
            'query': """
                -- Find upcoming events offering Live Streaming
                SELECT
                    e.EventID,
                    e.Title,
                    s.ServiceType,
                    e.Date
                FROM
                    Events e
                JOIN
                    EventServices es ON e.EventID = es.EventID
                JOIN
                    Services s ON es.ServiceID = s.ServiceID
                WHERE
                    s.ServiceType = %s AND
                    e.Date >= CURRENT_DATE
                ORDER BY
                    e.Date;
            """,
            'params': ('Catering',),
            'description': 'Find upcoming events offering Live Streaming.'
        },
        {
            'name': 'Query 5: Users Registered for a Specific Event',
            'query': """
                -- List users registered for a specific event
                SELECT
                    u.UserID,
                    u.First,
                    u.Last,
                    r.Status,
                    r.Date AS RegistrationDate
                FROM
                    Users u
                JOIN
                    Registrations r ON u.UserID = r.UserID
                WHERE
                    r.EventID = %s
                ORDER BY
                    r.Date;
            """,
            'params': (1,),  # Replace 123 with an actual EventID from your database
            'description': 'List users registered for a specific event.'
        },
        {
            'name': 'Query 6: Average Rating for a Specific Event',
            'query': """
                -- Get average rating for a specific event
                SELECT
                    e.EventID,
                    e.Title,
                    AVG(r.Rating) AS AverageRating
                FROM
                    Events e
                JOIN
                    Reviews r ON e.EventID = r.EventID
                WHERE
                    e.EventID = %s
                GROUP BY
                    e.EventID, e.Title;
            """,
            'params': (1,),  # Replace 123 with an actual EventID from your database
            'description': 'Get average rating for a specific event.'
        },
        {
            'name': 'Query 7: Search Events by Keyword',
            'query': """
                -- Search events by keyword in title or description
                SELECT
                    e.EventID,
                    e.Title,
                    e.Description,
                    e.Date
                FROM
                    Events e
                WHERE
                    to_tsvector('english', e.Title || ' ' || e.Description) @@ plainto_tsquery('english', %s)
                ORDER BY
                    e.Date;
            """,
            'params': ('2024',),
            'description': 'Search events by keyword in title or description.'
        },
        {
            'name': 'Query 8: Events a User Has Registered For',
            'query': """
                -- Find events a user has registered for
                SELECT
                    e.EventID,
                    e.Title,
                    e.Date,
                    r.Status
                FROM
                    Events e
                JOIN
                    Registrations r ON e.EventID = r.EventID
                WHERE
                    r.UserID = %s
                ORDER BY
                    e.Date;
            """,
            'params': (1,),  # Replace 456 with an actual UserID from your database
            'description': 'Find events a user has registered for.'
        },
        {
            'name': 'Query 9: Get Top-Rated Organizers',
            'query': """
                -- Get organizers with rating 8 or higher
                SELECT
                    o.OrganizerID,
                    o.Name,
                    o.Rating
                FROM
                    Organizers o
                WHERE
                    o.Rating >= %s
                ORDER BY
                    o.Rating DESC;
            """,
            'params': (7,),
            'description': 'Get organizers with rating 8 or higher.'
        }
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
        # Materialized View 1: mv_top_rated_events
        {
            'name': 'Top Rated Events Using Materialized View',
            'query': """
                -- Query using the materialized view
                SELECT
                    EventID,
                    Title,
                    AverageRating
                FROM
                    mv_top_rated_events
                ORDER BY
                    AverageRating DESC;
            """,
            'non_mv_query': """
                -- Equivalent query without using the materialized view
                SELECT
                    e.EventID,
                    e.Title,
                    AVG(r.Rating) AS AverageRating
                FROM
                    Events e
                JOIN
                    Reviews r ON e.EventID = r.EventID
                GROUP BY
                    e.EventID, e.Title
                HAVING
                    AVG(r.Rating) >= 7
                ORDER BY
                    AverageRating DESC;
            """,
            'params': None,
            'description': 'Retrieve top-rated events.'
        },
        # Materialized View 2: mv_high_registration_events
        {
            'name': 'High Registration Events Using Materialized View',
            'query': """
                -- Query using the materialized view
                SELECT
                    EventID,
                    Title,
                    RegistrationCount
                FROM
                    mv_high_registration_events
                ORDER BY
                    RegistrationCount DESC;
            """,
            'non_mv_query': """
                -- Equivalent query without using the materialized view
                SELECT
                    e.EventID,
                    e.Title,
                    COUNT(r.UserID) AS RegistrationCount
                FROM
                    Events e
                JOIN
                    Registrations r ON e.EventID = r.EventID
                GROUP BY
                    e.EventID, e.Title
                HAVING
                    COUNT(r.UserID) >= 50
                ORDER BY
                    RegistrationCount DESC;
            """,
            'params': None,
            'description': 'Retrieve events with high registration counts.'
        },
        # Materialized View 3: mv_events_with_location
        {
            'name': 'Closest Events Using Materialized View',
            'query': """
                -- Query using the materialized view
                SELECT
                    EventID,
                    Title,
                    Description,
                    EventType,
                    Capacity,
                    Date,
                    StartTime,
                    EndTime,
                    Price,
                    ZipCode,
                    City,
                    Country,
                    ST_Distance(Location, ST_SetSRID(ST_MakePoint(%s, %s), 4326)) AS distance_meters
                FROM
                    mv_events_with_location
                WHERE
                    Date >= CURRENT_DATE
                ORDER BY
                    distance_meters
                LIMIT 10;
            """,
            'non_mv_query': """
                -- Equivalent query without using the materialized view
                SELECT
                    e.EventID,
                    e.Title,
                    e.Description,
                    e.EventType,
                    e.Capacity,
                    e.Date,
                    e.StartTime,
                    e.EndTime,
                    e.Price,
                    a.ZipCode,
                    a.City,
                    a.Country,
                    ST_Distance(a.Location, ST_SetSRID(ST_MakePoint(%s, %s), 4326)) AS distance_meters
                FROM
                    Events e
                JOIN
                    Address a ON e.AddressID = a.AddressID
                WHERE
                    e.Date >= CURRENT_DATE
                ORDER BY
                    distance_meters
                LIMIT 10;
            """,
            'params': (26.433614, 24.5625355),  # User's longitude and latitude
            'description': 'Retrieve the 10 closest upcoming events to a given location.'
        },
    ]

    # Execute and time the materialized view queries
    for mq in materialized_queries:
        print(f"Executing {mq['name']}")

        # Using Materialized View
        if mq['params']:
            time_mv, _ = execute_query(cursor_indexed, mq['query'], mq['params'])
            time_non_mv, _ = execute_query(cursor_indexed, mq['non_mv_query'], mq['params'])
        else:
            time_mv, _ = execute_query(cursor_indexed, mq['query'])
            time_non_mv, _ = execute_query(cursor_indexed, mq['non_mv_query'])

        # Calculate improvement
        improvement = ((time_non_mv - time_mv) / time_non_mv) * 100 if time_non_mv != 0 else 0

        results.append({
            'Query': mq['name'],
            'Description': mq['description'],
            'Time Using MV (s)': time_mv,
            'Time Without MV (s)': time_non_mv,
            'Improvement (%)': improvement
        })

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


import sqlite3

def get_user_info(user_id):
    # Connect to the database
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Safe SQL query
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))

    # Fetch and print the results
    result = cursor.fetchall()
    for row in result:
        print(row)

    # Close the connection
    conn.close()

# Example usage
user_input = input("Enter user ID: ")
get_user_info(user_input)

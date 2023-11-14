def get_earnings_calls_to_analyze():
    """Retrieve earnings calls from the database that need analysis."""
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, text_content FROM earnings_calls WHERE analyzed = 0")
    calls_to_analyze = cursor.fetchall()
    cursor.close()
    conn.close()
    return calls_to_analyze

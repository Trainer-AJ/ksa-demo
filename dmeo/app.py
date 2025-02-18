from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)

# Azure SQL Database connection string
server = 'your-server.database.windows.net'  # Replace with your Azure SQL Server name
database = 'your-database'  # Replace with your database name
username = 'your-username'  # Replace with your Azure SQL username
password = 'your-password'  # Replace with your Azure SQL password
driver = '{ODBC Driver 17 for SQL Server}'  # Ensure that the ODBC driver is installed in your container

# Connect to Azure SQL Database
def get_db_connection():
    conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}')
    return conn

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/get_data')
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT TOP 5 * FROM your_table')  # Replace with your actual table
    rows = cursor.fetchall()
    data = []
    for row in rows:
        data.append({'column_name': row.column_name})  # Modify based on your table's schema
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

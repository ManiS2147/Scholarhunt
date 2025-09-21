import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, jsonify, request

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="xyzcompany.supabase.co",
        database="postgres",           # default DB name in supabase
        user="postgres",               # default user for supabase
        password="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBsd2FmaG94aGlleGtzb2dwYW1zIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1ODM3OTMzMSwiZXhwIjoyMDczOTU1MzMxfQ.cd_Q36Wl6HEKFODCd3MDEcb2B5_E-ihIYSskvfWeAlY",  # Your service role key here
        port=5432,
        cursor_factory=RealDictCursor
    )
    return conn

@app.route('/api/scholarships', methods=['GET'])
def get_scholarships():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM scholarships;")
    scholarships = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(scholarships)

if __name__ == '__main__':
    app.run(debug=True)

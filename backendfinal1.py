from supabase import create_client # type: ignore

SUPABASE_URL = "https://xyzcompany.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBsd2FmaG94aGlleGtzb2dwYW1zIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgzNzkzMzEsImV4cCI6MjA3Mzk1NTMzMX0.1BstkNuxMzLYSOsSzTJ0IMzT27toIstGHxlZ1KzPwm0"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/api/scholarships', methods=['GET'])
def get_scholarships():
    data = supabase.table("scholarships").select("*").execute()
    return jsonify(data.data)

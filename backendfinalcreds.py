import os
conn = psycopg2.connect(
    host=os.getenv("SUPABASE_HOST"),
    database=os.getenv("SUPABASE_DB"),
    user=os.getenv("SUPABASE_USER"),
    password=os.getenv("SUPABASE_PASS"),
    port=5432,
)

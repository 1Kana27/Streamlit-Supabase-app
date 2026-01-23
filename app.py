from supabase import create_client, Client

# Supabase の接続情報（Settings → API からコピー）
url = "https://jdmtdnqixszsitggbvql.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpkbXRkbnFpeHN6c2l0Z2didnFsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjkwNzgyNTksImV4cCI6MjA4NDY1NDI1OX0.GuT7YFU5guprN9bZZbqmyvzKA_KodSNTWmpZbFmj4XU"

supabase: Client = create_client(url, key)

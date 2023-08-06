# minio credentials
minio_endpoint = "http://localhost:9000"
minio_region = "us-east-1"
minio_bucket = "reddit-data-lake"

# postgres credentials
postgres_host = "127.0.0.1,::1"
postgres_port = "5432"
postgres_db = "reddit_dw"
postgres_user = "postgres"
postgres_pass = "admin"
postgres_url = f"jdbc:postgresql://{postgres_host}:{postgres_port}/{postgres_db}"
postgres_props = {"user": postgres_user, "password": postgres_pass}

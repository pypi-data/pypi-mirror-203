import json
import requests
from datetime import date
from includes.functions import *
from includes.vars import *

def data_ingest():
    headers = reddit_connection()

    # Send a GET request to get the hot posts in the "popular" subreddit
    res = requests.get("https://oauth.reddit.com/r/popular",
                    headers=headers)

    # Get the JSON data from the response
    data = res.json()

    # Convert the JSON data to a string
    json_data = json.dumps(data)

    minio_client = minio_connection()

    file_date = date.today().strftime('%Y%m%d')

    # Upload the JSON data to the MinIO bucket
    minio_client.put_object(Bucket=minio_bucket,
                        Key=f'raw/popular_{file_date}.json',
                        Body=json_data.encode('utf-8'))
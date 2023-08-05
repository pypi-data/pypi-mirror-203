from pyspark.sql import SparkSession
from includes.vars import *
from datetime import date
from includes.functions import loadConfigs

def load_author_flair():
    spark = SparkSession.builder \
        .config("spark.hadoop.fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider") \
        .config("spark.jars", "/jars/postgresql-42.2.5.jar") \
        .getOrCreate()
    loadConfigs(spark.sparkContext)

    today = date.today().strftime('%Y%m%d')
    today = 20230326

    input_folder = "author_flair"
    input_file = "author_flair"
    table_name = "staging.author_flair"
    mode = "append"

    df = spark.read.option("header", "true") \
        .parquet(f"s3a://{minio_bucket}/processed/{input_folder}/{input_file}_{today}")

    properties = {"user": postgres_user, "password": postgres_pass}
    df.write.jdbc(url=postgres_url, table=table_name, mode=mode, properties=properties)
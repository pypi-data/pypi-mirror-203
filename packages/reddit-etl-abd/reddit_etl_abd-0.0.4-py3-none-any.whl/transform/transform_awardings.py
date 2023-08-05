from pyspark.sql import SparkSession
from includes.vars import *
from datetime import date
from includes.functions import loadConfigs
from pyspark.sql.functions import lit
from pyspark.sql.functions import explode

def transform_awardings():
    spark = SparkSession.builder \
        .config("spark.hadoop.fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider") \
        .config("spark.jars", "/jars/postgresql-42.2.5.jar") \
        .getOrCreate()
    loadConfigs(spark.sparkContext)

    today = date.today().strftime('%Y%m%d')
    today = 20230326

    output_folder = "awardings"
    output_file = "awardings"

    df_raw = spark.read.option("header", "true") \
        .json(f"s3a://{minio_bucket}/raw/popular_{today}.json")

    df_raw = df_raw.select(explode(df_raw.data.children.data).alias("data"))
    df_raw = df_raw.select("data.*")

    df_awardings = df_raw.select("id", "author", "all_awardings") \
                        .withColumnRenamed("id", "post_id")

    df_awardings_exploded = df_awardings.select("post_id", "author", explode("all_awardings").alias("all_awardings"))

    df_awardings_cleaned = df_awardings_exploded.select("*", "all_awardings.*")
    df_awardings_cleaned = df_awardings_cleaned.drop("all_awardings")

    columns_to_drop = ["resized_icons","resized_static_icons","icon_format","icon_height","icon_url","icon_width","static_icon_height",
                    "static_icon_url","static_icon_width","sticky_duration_seconds"]

    df_final = df_awardings_cleaned.drop(*[col for col in df_awardings_cleaned.columns if any(s in col for s in columns_to_drop)])

    df_final = df_final.dropDuplicates()

    df_final = df_final.withColumn("dateid", lit(today))

    df_final.write.mode("overwrite").parquet(f"s3a://{minio_bucket}/processed/{output_folder}/{output_file}_{today}")
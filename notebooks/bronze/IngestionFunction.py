from pyspark.sql.functions import col, current_timestamp
from utils.Config import Config


class Ingestion:

    def __init__(self, spark, volume_csv, table_name):
        self.spark = spark
        self.volume_csv = volume_csv
        self.table_name = table_name

        self.path_to_read = f"{Config.RAW_PATH}/{volume_csv}"

        self.path_to_write = (
            f"{Config.BRONZE_DATABASE}.{table_name}"
        )

    def add_bronze_metadata(self):

        df = (
            self.spark.read
            .format("csv")
            .option("header", "true")
            .load(self.path_to_read)
        )

        updated_df = (
            df
            .withColumn("source", col("_metadata.file_name"))
            .withColumn("ingested_at", current_timestamp())
        )

        return updated_df

    def ingest(self):

        (
            self.add_bronze_metadata()
            .write
            .format("delta")
            .mode("overwrite")
            .option("overwriteSchema", "true")
            .saveAsTable(self.path_to_write)
        )
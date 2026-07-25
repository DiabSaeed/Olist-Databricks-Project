class Config:
    CATALOG = "olist_dataset"

    RAW_SCHEMA = "raw_dataset"
    BRONZE_SCHEMA = "bronze"
    SILVER_SCHEMA = "silver"
    GOLD_SCHEMA = "gold"

    RAW_VOLUME = "raw_csvs"

    RAW_PATH = f"/Volumes/{CATALOG}/{RAW_SCHEMA}/{RAW_VOLUME}"
    FILE_NAMES = dbutils.fs.ls(RAW_PATH)
    BRONZE_DATABASE = f"{CATALOG}.{BRONZE_SCHEMA}"
    SILVER_DATABASE = f"{CATALOG}.{SILVER_SCHEMA}"
    GOLD_DATABASE = f"{CATALOG}.{GOLD_SCHEMA}"
    DATASET = {
        path.name.split("_")[1]: path.name for path in FILE_NAMES
    }


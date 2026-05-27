from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType
from delta import configure_spark_with_delta_pip

spark = (
    SparkSession.builder
    .appName("create_gold_sample")
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
    .getOrCreate()
)


spark.sparkContext.setLogLevel("WARN")

# Sample gold data — monthly sales per product
data = [
    ("2024-01", "product_a", "electronics", 150, 45000.0),
    ("2024-01", "product_b", "clothing",    200, 12000.0),
    ("2024-02", "product_a", "electronics", 180, 54000.0),
    ("2024-02", "product_b", "clothing",    220, 13200.0),
    ("2024-03", "product_a", "electronics", 160, 48000.0),
    ("2024-03", "product_b", "clothing",    195, 11700.0),
]

schema = StructType([
    StructField("month",       StringType(),  False),
    StructField("product_id",  StringType(),  False),
    StructField("category",    StringType(),  False),
    StructField("units_sold",  IntegerType(), False),
    StructField("revenue",     DoubleType(),  False),
])

df = spark.createDataFrame(data, schema)

output_path = "data/gold/sales"

df.write.format("delta").mode("overwrite").save(output_path)

print(f"✅ Gold Delta table written to {output_path}")
spark.stop()
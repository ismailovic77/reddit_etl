from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType
from pyspark.sql.functions import col, round as sprak_round

spark = SparkSession.builder.appName("RedditETL").getOrCreate()

schema = StructType([
    StructField("Employee_id", IntegerType(), nullable=False),
    StructField("name", StringType(), nullable=False),
    StructField("department", StringType(), nullable=True),
    StructField("salary", DoubleType(), nullable=True),
    StructField("years_exp", IntegerType(), nullable=True)
])

data = [
    (1,"Alice","Engineering",95000.0,7),
    (2,"Bob","Marketing",72000.0,3),
    (3,"Carol","Engineering",105000.0,10),
    (4,"David","HR",61000.0,2),
    (5,"Eva","Engineering",88000.0,5),
    (6,"Frank","Finance",79000.0,6),
    (7,"Grace","Marketing",68000.0,4),
    (8,"Henry","Finance",83000.0,8),
    (9,"Isla","HR",59000.0,1),
    (10,"Jacques","Engineering",112000.0,12),
]

df = spark.createDataFrame(data, schema=schema)
print(df.show())
df.printSchema()


export PYSPARK_PYTHON=/Users/user/Desktop/learning/reddit_etl/.venv/bin/python
export PYSPARK_DRIVER_PYTHON=/Users/user/Desktop/learning/reddit_etl/.venv/bin/python
spark-submit --master spark://127.0.0.1:7077 /Users/user/Desktop/learning/reddit_etl/processing/bronze/get_data.py

#this is for dbt. run from dbt analysis : 

#export AWS_ACCESS_KEY_ID=minioadmin
#export AWS_SECRET_ACCESS_KEY=minioadmin
#export SPARK_SUBMIT_OPTS="-Dspark.hadoop.fs.s3a.endpoint=http://localhost:9000
 -Dspark.hadoop.fs.s3a.path.style.access=true -Dspark.hadoop.fs.s3a.impl=org.apache.hadoop.fs.s3a.S3AFileSystem -Dspark.sql.warehouse.dir=s3a://spark-data/warehouse"
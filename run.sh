export PYSPARK_PYTHON=$(pwd)/.venv/bin/python
export PYSPARK_DRIVER_PYTHON=$(pwd)/.venv/bin/python
spark-submit --master spark://Host-001.lan:7077 processing/bronze/get_data.py
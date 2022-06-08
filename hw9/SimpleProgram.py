from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SimpleSparkProject').getOrCreate()

def main():
    df = spark.read.format("csv").load("PS_20174392719_1491204439457_log.csv")
    df.printSchema()
    num_rows = df.count()
    # df.show(truncate=False)
    print(f'NUM ROWS: {num_rows}\n')

if __name__ == '__main__':
    main()
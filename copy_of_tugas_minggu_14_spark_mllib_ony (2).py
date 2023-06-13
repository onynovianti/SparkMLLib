# -*- coding: utf-8 -*-
"""Copy of Tugas Minggu 14 - Spark MLlib - Ony.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16oUHUNnsjXqc_poTosjnwXWA9qbdEj94

## Ony Novianti
#### 2041720029 (TI-3A)
"""

# Sumber : https://github.com/cloudxlab/bigdata/blob/master/spark/examples/mllib/ml-recommender.scala

# Connect Google Drive Untuk Ambil Data
from google.colab import drive
drive.mount('/content/drive')

# Install PySpark
!pip install pyspark

# Import Library
from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("Movie Lens").getOrCreate()
sc = spark.sparkContext

raw = sc.textFile("/content/drive/MyDrive/TI-3A/ml-1m/ratings.dat")
mydata = [(2, 1), (3, 3), (4, 2)]
mydatardd = sc.parallelize(mydata).map(lambda x: Rating(0, x[0], x[1]))

class Rating:
    def __init__(self, userId, movieId, rating):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating

# Parse String Menjadi Objek Rating
def parseRating(str):
    fields = str.split("::")
    assert len(fields) == 4
    return Rating(int(fields[0]), int(fields[1]), float(fields[2]))

ratings = raw.map(parseRating)
ratings_df = ratings.toDF(["userId", "movieId", "rating"])

# Convert the additional data to a DataFrame
mydata_df = mydatardd.toDF(["userId", "rating"])

# Combine the ratings and additional data
totalratings_df = ratings_df.union(mydata_df)

# Build the recommendation model using ALS
als = ALS(userCol="userId", itemCol="movieId", ratingCol="rating", coldStartStrategy="drop")
model = als.fit(totalratings_df)

# Generate product recommendations for user ID 1
products = model.recommendForUserSubset(spark.createDataFrame([(1,)]).toDF("userId"), 10)
# Load data from movies, join it, and display the names ordered by ratings

products.show()


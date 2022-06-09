import json

from pyspark.sql import SparkSession, functions
from pyspark.sql.functions import split, col, count, max as max_, to_date

spark = SparkSession.builder.appName('SimpleSparkProject').getOrCreate()
spark.sparkContext.setLogLevel("WARN")


def top10_videos(df_vids):
    """
    Find Top 10 videos that were amongst the trending videos for the highest
    number of days (it doesn't need to be a consecutive period of time).
    You should also include information about different metrics for each day
    the video was trending.
    :param df_vids: dataframe
    :return: json
    """
    df_top10 = df_vids.groupBy('video_id').count()
    df_top10 = df_top10.sort('count', ascending=False).limit(10)

    df_trending_days = df_top10.join(df_vids, 'video_id', 'left').select('video_id', 'trending_date', 'views', 'likes',
                                                                         'dislikes')

    dict_trending_days = {
        video_id['video_id']: df_trending_days.where(df_trending_days['video_id'] == video_id['video_id']).drop(
            'video_id').dropDuplicates(['trending_date']) for video_id in
        df_trending_days.select('video_id').collect()}

    df_videos = df_top10.join(df_vids, 'video_id', 'left').select('video_id', 'trending_date', 'title', 'description',
                                                                  'views', 'likes',
                                                                  'dislikes').dropDuplicates(
        ['video_id', 'trending_date'])

    df_videos = df_videos.withColumn('trending_date', to_date(col("trending_date"), 'yy.dd.MM'))

    df_max_dates = (df_videos.withColumn("datetime", to_date(col("trending_date"), 'yy.dd.MM'))
                    .groupBy("video_id")
                    .agg(max_("datetime").alias("last_date")))

    df_latest = df_max_dates.join(df_videos, (df_max_dates.video_id == df_videos.video_id) & (
                df_max_dates.last_date == df_videos.trending_date), 'left').dropDuplicates(['video_id']).drop(
        df_max_dates.video_id).drop(df_videos.trending_date)

    final_json = {'videos': []}
    for video in df_latest.collect():
        final_json['videos'].append({"id": video["video_id"],
                                     "title": video["title"],
                                     "description": video["description"],
                                     "latest_views": video["views"],
                                     "latest_likes": video["likes"],
                                     "latest_dislikes": video["dislikes"],
                                     "trending_days": dict_trending_days[video["video_id"]].collect()})

    return json.dumps(final_json)


def top10_tags(df_vids):
    df_videos_tags = df_vids.select()

def main():
    df_vids = spark.read.options(header=True, multiline=True).format("csv").load("KRvideos.csv")
    df_vids = df_vids.filter((col('video_id') != '#NAME?'))

    df_ctgs = spark.read.options(multiline=True).format("json").load("KR_category_id.json")
    df_ctgs = df_ctgs.withColumn("categories",
                                 functions.explode(functions.arrays_zip("items.id", "items.snippet.title")))
    df_ctgs = df_ctgs.select(col('categories.id').alias('id'), col('categories.title').alias('title'))

    with open("answer1.json", "w") as outfile:
        outfile.write(top10_videos(df_vids))


if __name__ == '__main__':
    main()

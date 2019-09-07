import sys

from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split

if len(sys.argv) != 3:
    print("Usage: structured_network_wordcount.py <hostname> <port>", file=sys.stderr)
    sys.exit(-1)

host = sys.argv[1]
port = int(sys.argv[2])

# SparkSession を作る
park = SparkSession\
            .builder\
            .appName("StructuredNetworkWordCount")\
            .getOrCreate()

# TCP からのデータストリームを表すものとして、DataFrame オブジェクトを作る
lines = spark\
        .readStream\
        .format('socket')\
        .option('host', host)\
        .option('port', port)\
        .load()

# 行を単語に分割
words = lines.select(
        # explode は配列の個々のデータを Colum データに変換する。
        explode(
            split(lines.value, ' ')
            ).alias('word')
        )

# 単語を計測する計算機を作る。
wordCounts = words.groupBy('word').count()


# クエリを起動する。結果をコンソールに出力する。
query = wordCounts\
        .writeStream\
        .outputMode('complete')\
        .format('console')\
        .start()

query.awaitTermination()

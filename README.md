# Hello Spark Structured Streaming
Apache Spark の Structured Streaming のサンプルです。

## バージョン
Apache Spark version 2.4.4 での動作を確認

## 使い方
以下のコマンドで、TCPポートへ接続します。
```
nc -lk 9999
```

別のターミナルから、以下のコマンドで Spark に job を submit します。
```
make
```

最初のターミナルから入力を行い、単語がカウントされるのを確認してください。

Spark のコンソールに大量の情報が出力され、単語の集計結果がすぐに流れてしまう場合は、
log4j.properties を以下のように変更してください。

```
-log4j.rootCategory=INFO, console
+log4j.rootCategory=WARN, console
```

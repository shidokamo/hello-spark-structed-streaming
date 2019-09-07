run:
	spark-submit word-count-tcp.py localhost 9999
nc:
	nc -lk 9999

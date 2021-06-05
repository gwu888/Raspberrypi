import datetime, threading
def foo():
	print datetime.datetime.now()
	threading.Timer(10, foo).start()

foo()

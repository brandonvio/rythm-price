import _thread
from src.OandaStream import oanda_stream
from src.TwitterFilteredStream import twitter_stream

if __name__ == "__main__":
    _thread.start_new_thread(twitter_stream, ())
    _thread.start_new_thread(oanda_stream, ())

    while 1:
        pass

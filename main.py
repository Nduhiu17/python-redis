# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import redis
redis_host = "localhost"
redis_port = 6379
redis_password = ""

def hello_redis():
    """Example Hello Redis Program"""
    try:
        r = redis.StrictRedis(host=redis_host,port=redis_port,password=redis_password)
        r.set("msg:hello","Hello Redis!!!!")
        msg = r.get("msg:hello")
        print(msg)
    except Exception as e:
        print(e)
    # Use a breakpoint in the code line below to debug your script.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hello_redis()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

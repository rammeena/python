import requests
def retry(func):

    def new_func():
        try:
            return func()
        except:
            return func()
    return new_func

@retry
def get_current_time():
    return requests.get('http://time.is')

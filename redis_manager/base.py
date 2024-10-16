import redis

class RedisManager():

    @staticmethod
    def get_client():
        pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
        r = redis.Redis(connection_pool=pool)
        #r = redis.Redis(host='localhost',  port=6379, db=0)
        return r
    @staticmethod
    def add_data(data):
        r = RedisManager.get_client()
        r.add(data)
        return "Data added"
        

    @staticmethod
    def get_data(key):
        r = RedisManager.get_client()
        return r.get(key)

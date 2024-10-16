from redis_manager.base import RedisManager

def add_data(key):
    data = {}
    for i in range(10):
        data.update({'i': i})
    print("adding data to redis")
    RedisManager.add_data(key, data)

def get_data(key):
    return RedisManager.get_data(key)


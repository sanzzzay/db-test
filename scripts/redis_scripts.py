from redis_manager.base import RedisManager

def add_data():
    data = {}
    for i in range(10):
        data.update({'i': i})
    print("adding data to redis")
    RedisManager.add_data(data)

def get_data(key):
    return RedisManager.get_data(key)


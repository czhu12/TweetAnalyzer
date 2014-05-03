import redis

class RedisWrapper:

  def __init__(self, host="localhost", port=6379, db=0):
    self.redis = redis.StrictRedis(host=host, port=port, db=db)

  def addToken(self, key, value=1):
    if(self.rContains(key)):
      self.rAdd(key, value)
    else:
      self.rIncrement(key)

  def rContains(key):
    return self.redis.get(key) is not None

  def rIncrement(key):
    self.redis.set(key, self.redis.get(key) + 1)

  def rAdd(key, value):
    self.redis.set(key, value)

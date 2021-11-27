from redis import Redis
from pottery import RedisDict

redisClient = Redis.from_url('redis://localhost:6379/')

tel = RedisDict({'jack': 4098, 'sape': 4139}, redis=redisClient, key='tel')
tel['guido'] = 4127
tel
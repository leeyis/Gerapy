from gerapy.libs.configparser import config


MYSQL_HOST = config('mysql', 'host')
MYSQL_PORT = config('mysql', 'port')
MYSQL_DATABASE = config('mysql', 'database')
MYSQL_USERNAME = config('mysql', 'username')
MYSQL_PASSWORD = config('mysql', 'password')
MYSQL_CHARSET = config('mysql', 'charset')

print(MYSQL_HOST, MYSQL_DATABASE)


BOT_NAME = 'Gerapy'


# Enables scheduling storing requests queue in redis.
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# Ensure all spiders share same duplicates filter through redis.
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# Store scraped item in redis for post-processing.
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 300
}

REDIS_HOST = config('redis', 'host')
REDIS_PORT = config('redis', 'port')
REDIS_PASSWORD = config('redis', 'password')
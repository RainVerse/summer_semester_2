import pymysql
from CONFIG import config

conn = pymysql.connect(host=config.DATABASE_HOST,
                       port=config.DATABASE_PORT,
                       user=config.DATABASE_USER,
                       passwd=config.DATABASE_PASSWORD,
                       db=config.DATABASE_NAME)
conn.close()


from os import getenv, urandom

DB_NAME = getenv("BESTIARY_DB_NAME", "bestiary")
DB_USER = getenv("BESTIARY_DB_USER", "bestiary")
DB_HOST = getenv("BESTIARY_DB_HOST", "localhost")
DB_PASSWORD = getenv("BESTIARY_DB_PASSWORD", "")
DB_PORT = getenv("BESTIARY_DB_PORT", "5432")

SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

REDIS_USER = getenv("BESTIARY_REDIS_USER", "bestiary")
REDIS_AUTH = getenv("BESTIARY_REDIS_AUTH", "bestiary")
REDIS_HOST = getenv("BESTIARY_REDIS_HOST", "localhost")
REDIS_PORT = getenv("BESTIARY_REDIS_PORT", "2344")

REDIS_URL = f"redis://{REDIS_USER}:{REDIS_AUTH}@{REDIS_HOST}:{REDIS_PORT}/"

SECRET_KEY = urandom(128)

WHOOSHEE_DIR = "bestiary/app/.whooshee/"
WHOOSHEE_MEMORY_STORAGE = True

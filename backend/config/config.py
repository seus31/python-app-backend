import datetime
import settings


class SystemConfig:
    # Flask
    DEBUG = True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db}?charset=utf8mb4'.format(**{
        'user': settings.MYSQL_USER,
        'password': settings.MYSQL_PASSWORD,
        'host': settings.MYSQL_HOST,
        'db': settings.MYSQL_DATABASE
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    JWT_SECRET_KEY = settings.JWT_SECRET_KEY
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=15)


Config = SystemConfig

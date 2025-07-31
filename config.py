import os

class Config:
    SECRET_KEY = os.environ["SECRET_KEY"]

    DB_USER = os.environ["DB_USER"]
    DB_PASSWORD = os.environ["DB_PASSWORD"]
    DB_HOST = os.environ["DB_HOST"]
    DB_NAME = os.environ["DB_NAME"]

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = "filesystem"






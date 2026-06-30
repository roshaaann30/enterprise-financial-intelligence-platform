from sqlalchemy import text

from app.database.session import engine


def database_health():

    with engine.connect() as connection:

        connection.execute(text("SELECT 1"))

    return True


if __name__ == "__main__":

    if database_health():

        print("Database Healthy")
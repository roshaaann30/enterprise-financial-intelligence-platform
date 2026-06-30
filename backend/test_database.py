from sqlalchemy import text

from app.core.logger import logger
from app.database.session import engine

try:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
        logger.info("Database connection successful!")
        print("✅ Connected to PostgreSQL")
except Exception as e:
    logger.error(e)
    print("❌ Connection failed")
    print(e)
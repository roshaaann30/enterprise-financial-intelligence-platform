from app.core.logger import logger
from app.core.settings import settings

logger.info("Application Started")

print("Application Name :", settings.APP_NAME)
print("Environment      :", settings.APP_ENV)
print("Database URL     :", settings.DATABASE_URL)
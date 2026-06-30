from apscheduler.schedulers.blocking import BlockingScheduler

from app.core.logger import logger
from app.ingestion.pipeline import run_pipeline

scheduler = BlockingScheduler()


@scheduler.scheduled_job(
    "cron",
    hour=18,
    minute=0,
)
def scheduled_pipeline():

    logger.info("=" * 80)
    logger.info("SCHEDULED PIPELINE STARTED")
    logger.info("=" * 80)

    run_pipeline()

    logger.info("=" * 80)
    logger.info("SCHEDULED PIPELINE FINISHED")
    logger.info("=" * 80)


if __name__ == "__main__":
    logger.info("Scheduler Started")
    scheduler.start()
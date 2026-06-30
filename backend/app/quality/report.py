from app.core.logger import logger


class QualityReportGenerator:

    @staticmethod
    def generate(reports):

        summary = {
            "total_checks": len(reports),
            "passed": 0,
            "failed": 0,
            "results": reports,
        }

        for report in reports:

            if report["status"] == "PASS":
                summary["passed"] += 1
            else:
                summary["failed"] += 1

        logger.info("Quality Report Generated")

        return summary
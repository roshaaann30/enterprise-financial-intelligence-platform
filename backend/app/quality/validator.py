import pandas as pd

from app.core.logger import logger
from app.quality.missing_value_detector import MissingValueDetector
from app.quality.duplicate_detector import DuplicateDetector
from app.quality.schema_validator import SchemaValidator
from app.quality.invalid_value_detector import InvalidValueDetector
from app.quality.outlier_detector import OutlierDetector
from app.quality.report import QualityReportGenerator
from app.services.data_quality_service import DataQualityService


class DataValidator:

    def __init__(self, db):

        self.quality_service = DataQualityService(db)

        logger.info("Data Validator Initialized")

    def validate_schema(
        self,
        dataset_name: str,
        dataframe: pd.DataFrame,
        expected_columns: list,
    ):

        report = SchemaValidator.validate(
            dataframe,
            expected_columns,
        )

        if report["schema_valid"]:

            self.quality_service.save_report(
                dataset=dataset_name,
                check_type="Schema Validation",
                status="PASS",
                message="Schema matches expected format.",
            )

        else:

            message = (
                f"Missing: {report['missing_columns']} | "
                f"New: {report['new_columns']}"
            )

            self.quality_service.save_report(
                dataset=dataset_name,
                check_type="Schema Validation",
                status="FAIL",
                message=message,
            )

        return report

    def validate_missing_values(
        self,
        dataset_name: str,
        dataframe: pd.DataFrame,
    ):

        report = MissingValueDetector.detect(dataframe)

        if report["total_missing"] == 0:

            self.quality_service.save_report(
                dataset=dataset_name,
                check_type="Missing Values",
                status="PASS",
                message="No missing values detected.",
            )

        else:

            self.quality_service.save_report(
                dataset=dataset_name,
                check_type="Missing Values",
                status="FAIL",
                message=str(report["missing_columns"]),
            )

        return report

    def validate_duplicates(
        self,
        dataset_name: str,
        dataframe: pd.DataFrame,
    ):

        report = DuplicateDetector.detect(dataframe)

        if report["total_duplicates"] == 0:

            self.quality_service.save_report(
                dataset=dataset_name,
                check_type="Duplicate Records",
                status="PASS",
                message="No duplicate records detected.",
            )

        else:

            self.quality_service.save_report(
                dataset=dataset_name,
                check_type="Duplicate Records",
                status="FAIL",
                message=f"{report['total_duplicates']} duplicate rows found.",
            )

        return report

    def validate_invalid_values(
        self,
        dataset_name: str,
        dataframe: pd.DataFrame,
    ):

        report = InvalidValueDetector.detect(
            dataframe
        )

        if report["total_invalid"] == 0:

            self.quality_service.save_report(
                dataset=dataset_name,
                check_type="Invalid Values",
                status="PASS",
                message="No invalid values detected.",
            )

        else:

            self.quality_service.save_report(
                dataset=dataset_name,
                check_type="Invalid Values",
                status="FAIL",
                message=str(report["invalid_columns"]),
            )

        return report

    def validate_outliers(
        self,
        dataset_name: str,
        dataframe: pd.DataFrame,
    ):

        report = OutlierDetector.detect(
            dataframe
        )

        if report["total_outliers"] == 0:

            self.quality_service.save_report(
                dataset=dataset_name,
                check_type="Outlier Detection",
                status="PASS",
                message="No outliers detected.",
            )

        else:

            self.quality_service.save_report(
                dataset=dataset_name,
                check_type="Outlier Detection",
                status="FAIL",
                message=str(report["outlier_columns"]),
            )

        return report

    def generate_quality_report(
        self,
        dataset_name: str,
        dataframe: pd.DataFrame,
        expected_columns: list,
    ):

        reports = []

        reports.append(
            {
                "check": "Missing Values",
                "status": (
                    "PASS"
                    if self.validate_missing_values(
                        dataset_name,
                        dataframe,
                    )["total_missing"] == 0
                    else "FAIL"
                ),
            }
        )

        reports.append(
            {
                "check": "Duplicate Records",
                "status": (
                    "PASS"
                    if self.validate_duplicates(
                        dataset_name,
                        dataframe,
                    )["total_duplicates"] == 0
                    else "FAIL"
                ),
            }
        )

        reports.append(
            {
                "check": "Schema Validation",
                "status": (
                    "PASS"
                    if self.validate_schema(
                        dataset_name,
                        dataframe,
                        expected_columns,
                    )["schema_valid"]
                    else "FAIL"
                ),
            }
        )

        reports.append(
            {
                "check": "Invalid Values",
                "status": (
                    "PASS"
                    if self.validate_invalid_values(
                        dataset_name,
                        dataframe,
                    )["total_invalid"] == 0
                    else "FAIL"
                ),
            }
        )

        reports.append(
            {
                "check": "Outlier Detection",
                "status": (
                    "PASS"
                    if self.validate_outliers(
                        dataset_name,
                        dataframe,
                    )["total_outliers"] == 0
                    else "FAIL"
                ),
            }
        )

        return QualityReportGenerator.generate(reports)
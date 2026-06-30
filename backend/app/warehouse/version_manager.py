from datetime import datetime


class VersionManager:

    @staticmethod
    def generate_version():

        return datetime.now().strftime("v%Y%m%d%H%M%S")
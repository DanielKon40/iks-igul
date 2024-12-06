
"""The game result logger"""

import csv
import datetime
from functools import lru_cache
import os


class file_export:
    def __init__(self, file_name="results.csv"):
        self.file_name = file_name
        self.fieldnames = ['date_and_time', 'winner']

        # Checks if the file already exists and creates a new one if not
        if not os.path.exists(self.file_name):
            with open(self.file_name, mode='w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
                writer.writeheader()

    @lru_cache()
    def log_result(self, winner):
        """Logs the result of a game"""
        current_time = datetime.datetime.now()
        with open(self.file_name, mode='a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writerow({"date_and_time": current_time, "winner": winner})


if __name__ == "__main__":
    logger = file_export()
    logger.log_result("Player")
    logger.log_result("CPU")


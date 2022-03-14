from datetime import datetime


class Logger:
    def __init__(self, file_name):
        self.file = open(file_name, "a")

    def log(self, log_level, message):
        self.file.write(f"[{datetime.now()}] {log_level}: {message}\n")
        print(f"\n [{datetime.now()}] {log_level}: {message}\n")

    def close_file(self):
        self.file.close()

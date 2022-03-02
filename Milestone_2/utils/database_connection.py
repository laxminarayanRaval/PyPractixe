import sqlite3


class DatabaseConnection:
    def __init__(self, host):
        self.cnn = None
        self.host = host

    def __enter__(self):
        self.cnn = sqlite3.connect(self.host)
        return self.cnn  # REASON FOR ERROR

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb or exc_val or exc_type:
            self.close()
        else:
            self.cnn.commit()
            self.cnn.close()

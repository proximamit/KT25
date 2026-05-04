# Forwarding Arguments (Framework Pattern)

class Database:
    def connect(self, *args, **kwargs):
        print("Connecting with:", args, kwargs)

class MySQLDatabase(Database):
    def connect(self, *args, **kwargs):
        kwargs["engine"] = "MySQL"
        super().connect(*args, **kwargs)

db = MySQLDatabase()
db.connect(host="localhost", port=3306)

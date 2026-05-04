# Config-Driven Systems

def connect_db(**config):
    default = {"host": "localhost", "port": 5432}
    default.update(config)
    return default

config = connect_db(user="admin", password="secret")
print(config)

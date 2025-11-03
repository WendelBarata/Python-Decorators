# ############# ALL YOU NEED IS THE FOLLOWING FUNCTION ########################

"""Useful information about the decorator:
- The singleton decorator ensures a class has only one instance
- Useful for configuration managers, database connections, loggers
- Automatically returns the same instance on subsequent instantiations
- Thread-safe implementation for multi-threaded applications
"""

from functools import wraps
import threading


def singleton(cls):
    """
    Decorator that converts a class into a singleton

    This decorator ensures that only one instance of the decorated class
    can exist. All attempts to create new instances will return the same
    object. Thread-safe implementation.

    Parameters:
        cls (class): class to be converted to singleton

    Returns:
        class: singleton wrapper for the class

    Example:
        @singleton
        class Database:
            def __init__(self):
                self.connection = "Connected"
    """
    instances = {}
    lock = threading.Lock()

    @wraps(cls)
    def get_instance(*args, **kwargs):
        # Double-checked locking for thread safety
        if cls not in instances:
            with lock:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


###############################################################################
# Here's a generic example of how to use the decorator ########################
###############################################################################


# First: define a class that you want to make a singleton
# Second: use @singleton before the class definition

# General structure of the class that you want to decorate with singleton
@singleton
class YourClass:  # This class will be a singleton
    def __init__(self):
        ...  # Your initialization code here
        self.attribute = "value"  # Your attributes here


###############################################################################
# Sample classes to test the singleton decorator ##############################
###############################################################################


@singleton
class DatabaseConnection:
    """Singleton database connection"""

    def __init__(self):
        print("Initializing database connection...")
        self.connection_string = "postgresql://localhost:5432/mydb"
        self.connected = True

    def query(self, sql: str):
        return f"Executing: {sql}"


@singleton
class ConfigManager:
    """Singleton configuration manager"""

    def __init__(self):
        print("Loading configuration...")
        self.settings = {
            "debug": True,
            "max_connections": 100,
            "timeout": 30
        }

    def get(self, key: str):
        return self.settings.get(key)

    def set(self, key: str, value):
        self.settings[key] = value


@singleton
class Logger:
    """Singleton logger"""

    def __init__(self):
        print("Initializing logger...")
        self.logs = []

    def log(self, message: str):
        self.logs.append(message)
        print(f"LOG: {message}")

    def get_logs(self):
        return self.logs


# Test the decorator
print("=== Testing DatabaseConnection ===")
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(f"db1 is db2: {db1 is db2}")  # Should be True
print(db1.query("SELECT * FROM users"))

print("\n=== Testing ConfigManager ===")
config1 = ConfigManager()
config2 = ConfigManager()
print(f"config1 is config2: {config1 is config2}")  # Should be True
config1.set("debug", False)
print(f"config2.get('debug'): {config2.get('debug')}")  # Should be False

print("\n=== Testing Logger ===")
logger1 = Logger()
logger2 = Logger()
print(f"logger1 is logger2: {logger1 is logger2}")  # Should be True
logger1.log("First message")
logger2.log("Second message")
print(f"Total logs: {len(logger1.get_logs())}")  # Should be 2

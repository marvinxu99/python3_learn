import logging
import logging.config
import json
import os

class LoggingManager:
    """
    A Singleton class to encapsulate logging configuration and provide methods to manage loggers.
    """
    _instance = None  # Class-level attribute to store the single instance

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(LoggingManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, config_file='logging_config.json', default_level=logging.INFO):
        # Prevent re-initialization if already initialized
        if not hasattr(self, '_initialized'):
            self.config_file = config_file
            self.default_level = default_level
            self._config_loaded = False
            self._load_logging_config()
            self._initialized = True  # Mark as initialized

    def _load_logging_config(self):
        """
        Load logging configuration from a JSON file. If the file is not found, use a basic configuration.
        """
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                config = json.load(f)
            logging.config.dictConfig(config)
            self._config_loaded = True
        else:
            print(f"Warning: Config file {self.config_file} not found. Using default configuration.")
            logging.basicConfig(level=self.default_level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            self._config_loaded = True

    def get_logger(self, logger_name):
        """
        Get a logger with the given name. Ensure that the logging configuration is loaded before calling this.
        """
        if not self._config_loaded:
            raise RuntimeError("Logging configuration not loaded. Please initialize 'LoggingManager' properly.")
        return logging.getLogger(logger_name)

    def set_logger_level(self, logger_name, level):
        """
        Dynamically update the log level of a specific logger.
        """
        logger = self.get_logger(logger_name)
        if hasattr(logging, level.upper()):
            logger.setLevel(getattr(logging, level.upper()))
            print(f"Logger '{logger_name}' level set to {level.upper()}")
        else:
            print(f"Invalid log level: {level}")


# Example of how to use the Singleton LoggingManager
# logging_manager = LoggingManager()
# logger = logging_manager.get_logger("app.moduleA")
# logger.info("This is an info message")

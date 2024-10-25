import logging
import logging.config
import json
import os
from logging.handlers import RotatingFileHandler

class LoggingManager:
    """
    A Singleton class to encapsulate logging configuration and provide methods to manage loggers.
    """
    _instance = None  # Class-level attribute to store the single instance

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, config_file='logging_config.json', default_level=logging.INFO, log_file='application.log', max_bytes=10485760, backup_count=5):
        # Prevent re-initialization if already initialized
        if not hasattr(self, '_initialized'):
            self.config_file = config_file
            self.default_level = default_level
            self.log_file = log_file
            self.max_bytes = max_bytes  # Maximum size in bytes before rotating the log file
            self.backup_count = backup_count  # Number of backup files to keep
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
            self._set_default_logging_config()
            self._config_loaded = True

    def _set_default_logging_config(self):
        """
        Set a default logging configuration if the config file is not found.
        """
        # Create a rotating file handler
        rotating_handler = RotatingFileHandler(
            self.log_file, maxBytes=self.max_bytes, backupCount=self.backup_count
        )

        # Create the basic logging configuration
        logging.basicConfig(
            level=self.default_level,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                rotating_handler,  # File handler with rotation
                logging.StreamHandler()  # Console handler
            ]
        )

    def get_logger(self, logger_name):
        """
        Get a logger with the given name. Ensure that the logging configuration is loaded before calling this.
        """
        if not self._config_loaded:
            raise RuntimeError("Logging configuration not loaded. Please initialize 'LoggingManager' properly.")
        
        # print(f"Logging to file: {self.log_file}")
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

# Example of how to use the Singleton LoggingManager with rotating log files
# logging_manager = LoggingManager(log_file='app.log', max_bytes=1048576, backup_count=5)  # 1 MB per file, 5 backups
# logger = logging_manager.get_logger("app.moduleA")
# logger.info("This is an info message")

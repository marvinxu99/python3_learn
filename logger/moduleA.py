from logging_manager import LoggingManager

# Create an instance of LoggingManager
logging_manager = LoggingManager()

# Get the logger for this module
logger = logging_manager.get_logger('app.moduleA')

def moduleA_function():
    logger.debug("Debug message from module A")
    logger.info("Info message from module A")
    try:
        result = 10 / 0
    except ZeroDivisionError:
        logger.error("Error occurred in module A", exc_info=True)

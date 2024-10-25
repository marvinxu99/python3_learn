from logging_manager import LoggingManager

# Get the Singleton instance of LoggingManager with a specified log file and rotating handler
logman = LoggingManager(
    # log_file=r'D:/dDev/Python/python3_learn/logger/app.log', 
    max_bytes=1024 * 1024, 
    backup_count=5)  # 1 MB per file, 5 backups

# Get the logger for this module
logger = logman.get_logger('app.moduleA')
logman.set_logger_level('app.moduleA', "DEBUG")


def moduleA_function():
    logger.debug("Debug message from module A")
    logger.info("Info message from module A")
    try:
        result = 10 / 0
    except ZeroDivisionError:
        logger.error("Error occurred in module A", exc_info=True)

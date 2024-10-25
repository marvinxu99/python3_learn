from logging_manager import LoggingManager
from moduleA import moduleA_function

if __name__ == "__main__":
    # Get the Singleton instance of LoggingManager with a specified log file and rotating handler
    logman = LoggingManager(
        # log_file=r'D:/dDev/Python/python3_learn/logger/app.log', 
        max_bytes=1024 * 1024, 
        backup_count=5)  # 1 MB per file, 5 backups

    # Simulate function calls
    moduleA_function()

    # Dynamically change the log level for moduleA
    logman.set_logger_level('app.moduleA', "ERROR")
    moduleA_function()  # Will only show error messages now

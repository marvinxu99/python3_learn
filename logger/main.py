from logging_manager import LoggingManager
from moduleA import moduleA_function

if __name__ == "__main__":
    # Create an instance of LoggingManager and load the configuration
    logging_manager = LoggingManager()

    # Simulate function calls
    moduleA_function()

    # Dynamically change the log level for moduleA
    logging_manager.set_logger_level('app.moduleA', "ERROR")
    moduleA_function()  # Will only show error messages now

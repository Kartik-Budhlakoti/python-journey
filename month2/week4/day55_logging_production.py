import logging 
from pathlib import Path

def setup_logger(name, log_file =None,level = logging.INFO):
    """
    Setting up a logger that writes to both terminal and optionally a file.
    This is the reusable pattern to be used in future.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Formatter -- what each log line looks like
    formatter = logging.Formatter(
        "{asctime} - {name} - {levelname} - {message}",
        style="{", datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Always add terminal handler
    terminal_handler = logging.StreamHandler()
    terminal_handler.setFormatter(formatter)
    logger.addHandler(terminal_handler)

    if log_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger
logger= setup_logger(
    name="health_reporter",
    log_file="logs/health_reporter.log",
    level=logging.DEBUG
)
logger.info("Script started..")
logger.debug("Debug mode active - showing details")
logger.warning("This is a warning message")
logger.error("This is a error message")
logger.info("Script finished..")

# Checking the logs folder was created and file exists
log_file = Path("logs/health_reporter.log")
if log_file.exists():
    print(f"\nLog file created: {log_file}")
    print("Log file contents : ")
    print(log_file.read_text())
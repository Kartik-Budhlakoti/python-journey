import logging
from pathlib import Path

# basicConfig file to configure root logger
logging.basicConfig(
    level=logging.DEBUG,
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
    handlers=[
        logging.FileHandler("basic_log.txt"),# write to file
        logging.StreamHandler() # also print to terminal
    ]
)
logging.debug("DEBUG: detailed diagnostic, helpful for debugging.")
logging.info("INFO: confirmation that the things are working as expeceted.")
logging.warning("WARNING: something unexpected happened but program still works.")
logging.error("ERROR: something failed, program may not work correctly.")
logging.critical("CRITICAL: serious error, program may not continue")

# getlogger - better for multi-functional scripts
# its best if each module gets its own logger
logger = logging.getLogger(__name__)

def process_file(filepath):
    logger.debug(f"Starting process file with : {filepath}")

    path = Path(filepath)

    if not path.exists():
        logger.error(f"File not found : {filepath}")
        return None
    logger.info(f"Processing file : {path.name}")

    try:
        content = path.read_text()
        word_count = len(content.split())
        logger.info(f"Successfully read {word_count} words from {path.name}")
        return word_count
    except PermissionError:
        logger.warning(f"Permission denied reading : {filepath}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error : {e}")
        return None

# testing with real file
result = process_file("/home/kartik007/Desktop/python-new/python-journey/month2/week4/practice-save")
if result :
    print(f"\nWord count : {result}")

# testing with non-existing file
result = process_file("/home/kartik007/python-new/non-existant.txt")
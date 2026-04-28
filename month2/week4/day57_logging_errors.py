import logging
from pathlib import Path

# setting up logger
logging.basicConfig(
    level= logging.DEBUG,
    format="{asctime} - {levelname} - {message}",
    style='{',
    handlers=[
        logging.FileHandler('error_handling.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class DataProcessingError(Exception):
    pass

def process_data_files(filepath, min_lines=1):
    """
    process a file with error handling and logging
    combining logging and custom exceptions
    """
    logger.info(f"Starting to process : {filepath}")
    path= Path(filepath)
    if not path.exists():
        logger.error(f"File not found : {filepath}")
        raise FileNotFoundError(f"File not found : {filepath}")
    if not path.is_file():
        logger.error(f"Path is not a file : {filepath}")
        raise ValueError(f"Not a file : {filepath}")
    logger.debug(f"File size : {path.stat().st_size} bytes")

    try:
        content = path.read_text()
        lines = [line.strip() for line in content.split('\n') if line.strip()]

        logger.debug(f"Read {len(lines)} non-empty lines")

        if len(lines) < min_lines:
            raise DataProcessingError(
                f"File has {len(lines)} lines, minimum required is {min_lines}"
            )
        
        # Processing each line
        results = []
        errors = []
        for i , line in enumerate(lines, 1):
            try:
                # try to convert to a number
                value = float(line)
                results.append(value)
                logger.debug(f"Line {i}: processed value {value}")
            except ValueError:
                errors.append(f"Line {i} : '{line}' is not a number ")
                logger.warning(f"Line {i} : could not convert '{line}' to number")
        logger.info(f"Processing Complete : {len(results)} values , {len(errors)} errors")

        if errors:
            for error in errors:
                logger.warning(error)
        return results , errors
    
    except DataProcessingError :
        raise  # re-raise the custom exception without wrapping
    except Exception as e:
        logger.error(f"Unexpected error processing {filepath} : {e}")
        raise DataProcessingError(f"Failed to process {filepath} :{e}")
    finally :
        logger.debug(f"Finished processing attempt for : {filepath}")

# testing
test_file = Path("text_data.txt")
test_file.write_text("42\n17.5\nnot_a_number\n99\nhello\n3.14")

try:
    values ,errors = process_data_files(str(test_file))
    print(f"Results: {values}")
    print(f"Errors : {errors}")
    print(f"Average : {sum(values)/len(values):.2f}")
except FileNotFoundError as e:
    print(f"File not found : {e}")
except DataProcessingError as e :
    print(f"Processing Error : {e}")
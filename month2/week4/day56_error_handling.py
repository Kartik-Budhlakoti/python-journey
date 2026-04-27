#  try/except/else/finally
print(f"===== TRY/EXCEPT/ELSE/FINALLY ===== ")

def read_file_safe(filepath):
    try:
        with open (filepath , 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error - file not found : {filepath}") 
        return None
    except PermissionError:
        print(f"Error - No permission to read : {filepath}")
        return None
    except Exception as e : 
        print(f"Unexpected error : {type(e).__name__} : {e}")
        return None
    else:
        print(f"Successfully read {len(content)} characters.")
        return content
    finally:
        print(f"Finished attempting to read : {filepath}")
result = read_file_safe("/home/kartik007/Desktop/python-new/python-journey/month2/week4/practice-save")
result = read_file_safe("/month2/week4/file.txt")

# ----------- CUSTOM EXCEPTIONS ----------
print("====   CUSTOM EXCEPTIONS   ====")
# Defining custom exception by inheriting from EXCEPTION
# or more specific built-in exception

class InvalidDirectoryError(Exception):
    pass # raised when path is not valid
class FileTooLargeError(Exception):
    pass # raised when file exceeds maximum allowed size
class NetworkError(Exception):
    pass # raised when network operation fails

# using custom exceptions
def scan_directory(path , max_size_mb =10):
    from pathlib import Path
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError (f" Path does not exist : {path}")
    if not p.is_dir():
        raise InvalidDirectoryError(f" Path is not directory : {path}")
    results = []
    for file in p.iterdir():
        if not file.is_file():
            continue

        size_mb = file.stat().st_size / (1024 * 1024)
        if size_mb > max_size_mb:
            raise FileTooLargeError(
                f"{file.name} is {size_mb:.2f}MB - exceeds {max_size_mb}MB limit"
            )
        results.append(file.name)
    return results

# Try custom exceptions
# if i want the file names in the dir then i have to change this entire try/except block
# Basically print the function call i.e. the files just below
try :
    files = scan_directory('/home/kartik007/Desktop/python-new/python-journey/month2')
    print(f"Found {len(files)} files")
except FileNotFoundError as e:
    print(f"Not found : {e}")
except InvalidDirectoryError as e :
    print(f"Invalid Directory : {e}")
except FileTooLargeError as e :
    print (f"File too large : {e}")

#  testing  with a file path instead of directory
try:
    files = scan_directory('/home/kartik007/Desktop/python-new/python-journey/README.md') 
except InvalidDirectoryError as e:
    print(f"Caught custom exception : {e}")

# -------------- Raising exceptions -------------
print(f"=====  Raising Exceptions  =====")
def validate_cgpa(cgpa):
    """ Validate that CGPA is within excepted range """
    if not isinstance(cgpa, (int, float)):
        raise TypeError(f"CGPA must be a number , got {type(cgpa).__name__}")
    if cgpa<0 or  cgpa>10:
        raise ValueError(f"CGPA must be between 0 and 10 , got {cgpa}")
    return True

#   test validation
test_values = [ 7.5, -1, 11,"six", 0, 10]
for value in test_values:
    try:
        validate_cgpa(value)
        print(f"Valid CGPA : {value}")
    except TypeError as e :
        print(f"Type error : {e}")
    except ValueError as e :
        print(f"Value error : {e}")
import subprocess

result = subprocess.run(
    ['ls' , '-la'],
    capture_output=True,
    text=True
)
print(result.stdout)
print('------------')
print(result.returncode)
print('------------')
print(result.stderr)

# old way
process = subprocess.Popen(
    ['ls', '-la'],
    stdout= subprocess.PIPE,
    stderr= subprocess.PIPE
)
stdout, stderr = process.communicate()
print(stdout.decode('utf-8'))

def run_command(command):
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout= 30
        )
        if result.returncode != 0:
            print(f'Command failed( exit {result.returncode}): {result.stderr.strip()}')
            return None

        return result.stdout
    except subprocess.TimeoutExpired:
        print(f'Command timed out after 30 seconds: {' '.join(command)}')
        return None
    except FileNotFoundError:
        print(f'Command not found: {command[0]}')
        return None

print(run_command(['df', '-h']))
print(run_command(['akerbg', '--test']))
print(run_command(['ping', '-c', '100', '8.8.8.8']))

def check_disk_usage():
    result = subprocess.run(
        ['df', '-h'],
        capture_output=True,
        text=True
    )
    return result.stdout
def check_memory():
    result = subprocess.run(
        ['free', '-h'],
        capture_output=True,
        text=True
    )
    return result.stdout
def check_top_processes():
    result = subprocess.run(
        ['ps', 'aux', '--sort=-%cpu'],
        capture_output=True,
        text=True
    )
    lines = result.stdout.split('\n')
    return '\n'.join(lines[:11])
def check_connectivity(host= '8.8.8.8'):
    result= subprocess.run(
        ['ping', '-c', '3', '-W', '2', host],
        capture_output=True,
        text=True
    )
    return result.returncode == 0
def check_logged_in_users():
    result = subprocess.run(['who'], capture_output=True, text=True)
    return result.stdout.strip() if result.stdout.strip() else 'NO user logged in'

print('====DISK====')
print(check_disk_usage())
print('====MEMORY====')
print(check_memory())
print('====TOP PROCESSES====')
print(check_top_processes())
print('====Connectivity====')
print(check_connectivity())
print('====USERS====')
print(check_logged_in_users())

result = subprocess.run(
    # also can be folder specific with this path 
    ['find', '/home/kartik007/Desktop/python-new/python-journey',
     '-name', '*.py',
     '-not', '-path', '*/venv/*',
     '-not', '-path', '*/__pycache__/*'],
     capture_output=True, text=True
)
lines = result.stdout.strip().split('\n')
python_files = [line for line in lines if line]
print(f'Found {len(python_files)} Python files...')
for f in python_files:
    print(f'  {f}')
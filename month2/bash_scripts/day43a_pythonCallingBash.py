import subprocess
from pathlib import Path

def run_bash_script(script_path, args=None):
    # running bash script from python and return the output
    # args is an optional list of arguments to pass to the script

    command = ['bash', script_path]
    if args: 
        command.extend(args)
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode != 0:
            print(f'Script failed: {result.stderr.strip()}')
            return None
        
        return result.stdout
    
    except subprocess.TimeoutExpired:
        print(f'Script timed out')
        return None
    except FileNotFoundError:
        print(f'File not found: {script_path}')

script = '/home/kartik007/Desktop/python-new/python-journey/month2/bash_scripts/day40_conditionals.sh'
output = run_bash_script(script, ['/home/kartik007/Desktop/python-new/python-journey/week1'])

if output:
    print(f'Output from the bash script: ')
    print(output)

    # processing the output in python
    lines = output.strip().split('\n')
    print(f'\nPython processed {len(lines)} lines of output.')
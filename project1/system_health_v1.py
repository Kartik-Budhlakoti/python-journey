from pathlib import Path
import datetime
import subprocess
import os
import argparse

def run_command(command):
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text= True,
            timeout = 30
        )
        if result.returncode != 0:
            return f'Error running {command[0]}: {result.stderr.strip()}'
        return result.stdout
    except subprocess.TimeoutExpired:
        return f"TImeout: {' '.join(command)}"
    except FileNotFoundError:
        return f'File not found: {command[0]}'

def check_disk_usage():
    return run_command(['df', '-h'])
def check_memory():
    return run_command(['free', '-h'])

def check_processes():
    output= run_command(['ps', 'aux', '--sort=-%cpu'])
    if output:
        lines = output.split('\n')
        return '\n'.join(lines[:11])
    return 'Could not get the processes list.'

def check_connectivity(host):
    try:
        result = subprocess.run(
            ['ping', '-c', '3', '-W', '2', host],
            capture_output=True,
            text=True,
            timeout=15
        )
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        return False
    
def check_logged_in_users():
    output = run_command(['who'])
    return output.strip() if output and output.strip() else 'No Users logged in.'

def count_project_files():
    project = Path('/home/kartik007/Desktop/python-new/python-journey')
    py_files = [
        f for f in project.rglob('*.py')
        if 'venv' not in f.parts and '__pycache__' not in f.parts
    ]
    return len(py_files)

def generate_report(ping_host):
    """Combine all checks into a fornmatted report."""
    timestamp= datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    seperator = '=' *50
    sections = [
        f'SYSTEM  HEALTH  REPORT',
        f'Generated: {timestamp}',
        seperator,
        '\n----Disk Usage----',
        check_disk_usage(),
        '\n----Memory----',
        check_memory(),
        '\n----Top processes by CPU----',
        check_processes(),
        '\n----Connectivity----',
        f"Internet ({ping_host}): {'REACHABLE' if check_connectivity(ping_host) else 'UNREACHABLE'}",
        '\n----LOGGED  IN  USERS----',
        check_logged_in_users(),
        '\n----Project Files Count----',
        f'Python files in project: {count_project_files()}',
        seperator,
        'Report Complete.'
    ]
    return '\n'.join(str(s) for s in sections)

def main():
    parser = argparse.ArgumentParser(
    description="I am adding argparse to this project on day-53",
    epilog="Example : python system_health_v1.py --ping 8.8.8.8 --output /home/kartik007/Desktop/python-new/python-journey/project1/health_report.txt"
    )
    parser.add_argument(
        '--ping',
        required=True,
        help= "Enter the server IP " 
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Enter the complete path for output file"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print detailed output..."
    )
    args = parser.parse_args()
    print(f"The server is : {args.ping}")
    print(f"The output directory is : {args.output}")
    print(f"Verbose : {args.verbose}")
    if args.verbose:
        print("Verbose mode on - printing some key details of argparse")
        print(f"full args object: {args}")

    # output_path = os.environ.get('OUTPUT_PATH', 'health_report.txt')
    #  I won't be needing this line cause i am using the 
    #  argparse to give the output location through terminal , So

    output_path = args.output
    output_file = Path(output_path)

    print('Running system health checks ...')
    report = generate_report(args.ping)

    output_file.write_text(report)
    print(f'\nReport written to: {output_file.resolve()}')
    print('\n' + report)

if __name__ == '__main__':
    main()
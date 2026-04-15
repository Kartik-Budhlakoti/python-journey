import subprocess
from pathlib import Path
import sys

def run_backup(source, destination):

    script = Path('/home/kartik007/Desktop/python-new/python-journey/month2/bash_scripts/day44a_backup.sh')

    if not script.exists():
        print(f"Error: Backup script not found at {script}")
        sys.exit(1)

    print(f'Running Backup...')
    print(f'Source: {source}')
    print(f"Destination: {destination}\n")

    result = subprocess.run(
        ['bash', str(script), source, destination],
        capture_output=True,
        text=True,
        timeout=30
    )

    if result.stdout:
        print(result.stdout)
    
    # Errors
    if result.returncode!=0:
        print(f" Backup failed : ")
        print(result.stderr)
        return False
    
    backup_path = None
    for line in result.stdout.split('\n'):
        if line.startswith("BACKUP_PATH="):
            backup_path = line.split("=")[1]
    
    if  backup_path:
        print(f"\n Backup location : {backup_path}")

    return True

def main():
    source = '/home/kartik007/Desktop/python-new/python-journey/week1'
    destination= '/home/kartik007/Desktop/python-new/python-backups'

    success = run_backup(source, destination)

    if success:
        print('\nBackup Completed Successfully.')

        dest_path = Path(destination)
        if dest_path.exists():
            files = list(dest_path.iterdir())
            print(f'Total items in location: {len(files)}')
    else:
        print(f"\nBACKUP  FAILED.")
        sys.exit(1)
if __name__== "__main__":
    main()
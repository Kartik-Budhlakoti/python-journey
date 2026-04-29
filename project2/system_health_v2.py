import argparse
from pathlib import Path
import logging
import sys
import datetime
import subprocess

# -------CUSTOM EXCEPTION--------
class CommandError(Exception):
    """Raised when the command fails."""
    pass
class CheckError(Exception):
    """Raised when health check cannot complete"""
    pass

# -------LOGGER SETUP---------
def setup_logger(verbose=False, log_file=None):
    """Configuring the logging for the application"""
    level = logging.DEBUG if verbose else logging.INFO
    handlers = [logging.StreamHandler()]

    if log_file:
        Path(log_file).parent.mkdir(exist_ok=True, parents=True)
        handlers.append(logging.FileHandler(log_file))
    logging.config(
        level = level,
        format= "{asctime} - {levelname} - {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers = handlers
    )
    return logging.getlogger(__name__)

# -------Argument Parser-------

def create_parser():
    parser= argparse.ArgumentParser(
        description="System Health Reporter - checks disk, memory, processes and network"
        epilog="Example: python system_health_v2.py --output report.txt --checks disk memory"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="health_report.txt",
        help="Output file path ( default health_report.txt )"
    )
    parser.add_argument(
        "--checks",
        nargs="+",
        choices=['disk', 'memory','processes','network','users','files'],
        default=['disk', 'memory','processes','network','users','files'],
        help="What are the checksto run (default : all)"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose/debug logging"
    )
    parser.add_argument(
        "--log-file",
        type=str,
        default = None,
        help="Save logs to this file (optional)"
    )
    parser.add_argument(
        "--project-dir",
        default="/home/kartik007/Desktop/python-new/python-journey",
        help="Project directory to count files in "
    )
    return parser

# ---------- HEALTH CHECK CLASS ------------
class HealthChecker:
    def __init__(self, logger):
        self.logger = logger

    def run_command(self, command, timeout=30):
        """
        Safely run a system command .
        Returns stdout string or raises CommandError .
        """
        self.logger.debug(f"Running Command : {' '.join(command)}")
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            if result.returncode !=0:
                raise CommandError(f"Command failed (exit{result.returncode} : {result.stderr.strip()})")
            return result.stdout
        except subprocess.TimeoutExpired():
            raise CommandError(f"Command timed out after : {timeout}s : {' '.join(command)}")
        except FileNotFoundError():
            raise CommandError(f"Command not found : {command[0]}")
    
    #-------- Check Diskl and Memory Usage ----------
    def check_disk(self):
        self.logger.info(f"Running disk check")
        try:
            output = self.run_command(['df', '-h'])
            self.logger.debug(f"Disk check complete.")
            return output
        except CommandError as e:
            raise CommandError(f"Disk check failed : {e}")
    def check_memory(self):
        self.logger.info(f"Running memory check")
        try:
            output = self.run_command(['free', '-h'])
            self.logger.debug(f"Memory check complete.")
            return output
        except CommandError as e:
            raise CommandError(f"Memory check failed : {e}")
    #--------- Check processes and network -----------

    def check_processes(self):
        self.logger.info(f"Running process check")
        try :
            output = self.run_command(['ps', 'aux' , '--sort=-%cpu'])
            lines = output.split('\n')
            result = '\n'.join(lines[:11])
            return result
        except CommandError as e:
            raise CommandError(f"Process check failed : {e}")
    def check_network(self):
        self.logger.info(f"Running Network check")
        try:
            self.run_command(['ping', '-c', '3', '-W', '2', '8.8.8.8'], timeout=15)
            self.logger.debug(f"Network check complete")
            return "Reachable"
        except CommandError:
            self.logger.debug(f"Network check failed - unreachable")
            return "Unnreachable"
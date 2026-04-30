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
    logging.basicConfig(
        level = level,
        format= "{asctime} - {levelname} - {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers = handlers
    )
    return logging.getLogger(__name__)

# -------Argument Parser-------

def create_parser():
    parser= argparse.ArgumentParser(
        description="System Health Reporter - checks disk, memory, processes and network",
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
    
#-------- Check Disk and Memory Usage ----------
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
        
# ---------- Check Users and Files -------------- 
    def check_users(self):
        self.logger.info(f"Running user check")
        try:
            output = self.run_command(['who'])
            result = output.strip() if output.strip() else "No users logged in"
            self.logger.debug(f"User check complete")
            return result
        except CommandError as e:
            raise CommandError(f"User check failed : {e}")
    def check_files(self, project_dir):
        self.logger.info(f"Running file check on : {project_dir}")
        path = Path(project_dir)

        if not path.exists():
            raise CommandError(f"Project directory not found : {project_dir}")
        
        py_files = [
            f for f in path.rglob("*.py")
            if "venv" not in f.parts and "__pycache__" not in f.parts
        ]
        self.logger.debug(f"File check complete - {len(py_files)} python files found")
        return len(py_files)

# ------------ Report writer class -----------
class ReportWriter:
    """ Builds and saves the health report """
    def __init__(self, output_path, logger):
        self.output_path = Path(output_path)
        self.logger = logger
        self.sections = []
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def add_header(self):
        self.sections.append("="*60)
        self.sections.append(f"SYSTEM  HEALTH  REPORT")
        self.sections.append(f"Generated {self.timestamp}")
        self.sections.append("="*60)
    
    def add_section(self, title , content):
        self.sections.append(f"\n------- {title.upper()} --------")
        self.sections.append(str(content))
    
    def add_error(self, title , error_message):
        self.sections.append(f"/n ----- {title.upper()} -----")
        self.sections.append(f"\nREPORT  FAILED : {error_message}")
    
    def add_footer(self):
        self.sections.append(f"\n" + "="*60)
        self.sections.append("END  OF  REPORT")
        self.sections.append(f"="*60)
    
    def save(self):
        content = "\n".join(self.sections)

        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_path.write_text(content)

        self.logger.info(f"Report was saved to : {self.output_path.resolve()}")
        return content

# ----- MAIN -----
def main():
    parser = create_parser()
    args = parser.parse_args()

    logger = setup_logger(
        verbose=args.verbose,
        log_file=args.log_file
    )
    logger.info(f"SYSTEM HEALTH REPORTER V2 starting")
    logger.debug(f"Arguments : {args}")

    checker = HealthChecker(logger)
    report = ReportWriter(args.output, logger)

    report.add_header()

# Running each requested check
    check_map = {
        'disk': ('Disk Usage',lambda: checker.check_disk()),
        'memory':('Memory', lambda: checker.check_memory()),
        'processes':('Top Processes',lambda: checker.check_processes()),
        'network':('Network Connectivity',lambda:checker.check_network()),
        'users':('Logged In Users', lambda:checker.check_users()),
        'files':('Project files', lambda: str(checker.check_files(args.project_dir)) + ' Python files found'),
    }

    for check_name in args.checks:
        if check_name in check_map:
            title , check_func = check_map[check_name]
            try:
                result = check_func()
                report.add_section(title, result)
            except CheckError as e:
                logger.error(f"Check failed - {check_name} : {e}")
                report.add_error(title , str(e))
    
    report.add_footer()

# Save and print
    content = report.save()
    print(f"\n" + content)

    logger.info(f"System Health Reporter v2 complete")

if __name__ == "__main__":
    main()

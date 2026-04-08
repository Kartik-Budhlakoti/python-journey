# System Health Reporter v1

A Python script that checks system health and generates a report.

## What it checks
- Disk usage
- Memory usage  
- Top 10 processes by CPU
- Internet connectivity
- Logged in users
- Python file count in project

## How to run
```bash
# Default output to health_report.txt
python system_health_v1.py

# Custom output path
OUTPUT_PATH=~/Desktop/python-new/python-journey/project1/health_report.txt python system_health_v1.py
```

## Requirements
- Python 3.8+
- Linux system with df, free, ps, ping, who commands available

## What I learned building this
- pathlib for file handling
- os module for environment variables
- subprocess for running Linux commands from Python
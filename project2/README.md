# System Health Reporter v2

Production-quality system health checking tool.

## Features
- Modular health checks — disk, memory, processes, network, users, files
- Full CLI interface via argparse
- Logging to terminal and optionally to file
- Custom exceptions for clean error handling
- OOP structure with HealthChecker and ReportWriter classes
- Graceful failure — one failed check doesn't stop others

## How to run

```bash
# Activate venv
source venv/bin/activate

# Run all checks (default)
python system_health_v2.py

# Run specific checks only
python system_health_v2.py --checks disk memory network

# Save output to custom file
python system_health_v2.py --output /tmp/report.txt

# Enable verbose logging
python system_health_v2.py --verbose

# Save logs to file
python system_health_v2.py --log-file logs/health.log

# Combine options
python system_health_v2.py --checks disk memory --output report.txt --verbose --log-file logs/health.log
```

## What I learned building this
- argparse for professional CLI interfaces
- logging module for production-quality output
- Custom exceptions for meaningful error messages
- OOP design — separating concerns into classes
- Combining all month 2 skills into one tool

## Running with Docker

Build the image:
```bash
docker build -t system-health-reporter:v2 .
```

Run with default checks:
```bash
docker run system-health-reporter:v2
```

Save report to your machine:
```bash
docker run -v $(pwd)/reports:/app/reports system-health-reporter:v2
```

Run specific checks:
```bash
docker run system-health-reporter:v2 \
  python system_health_v2.py \
  --output /app/reports/report.txt \
  --checks disk memory network
```
#!/bin/bash

echo "===  Bash script starting  ==="
echo "Running system health reporter..."

python3 /home/kartik007/Desktop/python-new/python-journey/project1/system_health_v1.py

exit_code=$?
if [ $exit_code -eq 0 ]; then
    echo "Pthon script completed successfully"
else
    echo "Python script failed wwith exit code: $exit_code"
    exit 1
fi

echo "=== Bash script complete ==="
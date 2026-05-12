FROM python:3.11-slim
RUN apt-get update && apt-get install -y \
	 procps \
	 iputils-ping \
	 && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY system_health_v2.py /app/
ENV OUTPUT_DIR=/app/reports
RUN mkdir -p /app/reports
CMD ["python", "system_health_v2.py",\
	 "--output", "/app/reports/health_report.txt",\
	 "--checks", "disk", "memory", "processes","network","users"]



import psutil
import os
import logging
import time
# Set up logging
logging.basicConfig(filename='system_health.log', level=logging.INFO)

# Define thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    return psutil.virtual_memory().percent

def get_disk_usage():
    return psutil.disk_usage('/').percent

def get_running_processes():
    return len(psutil.pids())

def check_system_health():
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()
    disk_usage = get_disk_usage()
    running_processes = get_running_processes()

    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"CPU usage is high: {cpu_usage}%")
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f"Memory usage is high: {memory_usage}%")
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f"Disk usage is high: {disk_usage}%")

    logging.info(f"System health: CPU={cpu_usage}%, Memory={memory_usage}%, Disk={disk_usage}%, Processes={running_processes}")

if __name__ == "__main__":
    while True:
        check_system_health()
        time.sleep(10)
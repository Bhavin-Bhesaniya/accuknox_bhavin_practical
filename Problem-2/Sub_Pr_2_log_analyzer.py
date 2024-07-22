import re
from collections import defaultdict

# Regular expression patterns for parsing Nginx log lines
PATTERN_IP = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
PATTERN_STATUS_CODE = r'\b\d{3}\b'
PATTERN_REQUEST_URI = r'\b(?:GET|POST|PUT|DELETE) (.*?) HTTP/1\.[01]"\b'


LOG_FILE = '/var/log/nginx/access.log'

ip_requests = defaultdict(int)
status_code_counts = defaultdict(int)
most_requested_pages = defaultdict(int)

# Open the log file and read it line by line
with open(LOG_FILE, 'r') as f:
    for line in f:
        ip_match = re.search(PATTERN_IP, line)
        if ip_match:
            ip = ip_match.group()
            ip_requests[ip] += 1

        status_code_match = re.search(PATTERN_STATUS_CODE, line)
        if status_code_match:
            status_code = status_code_match.group()
            status_code_counts[status_code] += 1

        request_uri_match = re.search(PATTERN_REQUEST_URI, line)
        if request_uri_match:
            request_uri = request_uri_match.group(1)
            most_requested_pages[request_uri] += 1

print("Log File Analyzer Report")
print("----------------------------")

print("Top 10 IP Addresses with Most Requests:")
for ip, count in sorted(ip_requests.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(f"{ip}: {count} requests")

print("\nStatus Code Counts:")
for status_code, count in status_code_counts.items():
    print(f"{status_code}: {count} occurrences")

print("\nTop 10 Most Requested Pages:")
for page, count in sorted(most_requested_pages.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(f"{page}: {count} requests")

print("\n404 Error Count:")
print(f"404 errors: {status_code_counts.get('404', 0)} occurrences")
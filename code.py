import time
import random
from datetime import datetime

# List of possible HTTP status codes
status_codes = [200, 404, 500]

# List of possible HTTP methods
http_methods = ['GET', 'POST', 'PUT', 'DELETE']

# List of possible URLs
urls = ['/home', '/about', '/contact', '/product', '/service']

# Function to generate a random log entry
def generate_log_entry():
    timestamp = datetime.now().strftime('%d/%b/%Y:%H:%M:%S')
    http_method = random.choice(http_methods)
    url = random.choice(urls)
    status_code = random.choice(status_codes)
    bytes_sent = random.randint(100, 10000)
    referer = "-"
    user_agent = "-"
    
    log_entry = f'127.0.0.1 - - [{timestamp}] "{http_method} {url} HTTP/1.0" {status_code} {bytes_sent} "{referer}" "{user_agent}"\n'
    return log_entry

# Function to continuously generate logs
def generate_logs():
    while True:
        with open('thapar-logs.txt', 'a') as log_file:
            log_entry = generate_log_entry()
            log_file.write(log_entry)
        time.sleep(0.2)  # Wait for 1 second before generating the next log

# Run the log generation process
if __name__ == "__main__":
    generate_logs()

from collections import defaultdict

LOG_FILE = "security_logs.txt"
THRESHOLD = 3

failed_attempts = defaultdict(int)

try:
    with open(LOG_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if " - " not in line:
                continue

            ip, action = line.split(" - ", 1)

            if action.lower() == "login failed":
                failed_attempts[ip] += 1

    print("Suspicious IPs:")
    found = False

    for ip, count in failed_attempts.items():
        if count >= THRESHOLD:
            print(f"{ip} had {count} failed login attempts")
            found = True

    if not found:
        print("No suspicious activity detected.")

except FileNotFoundError:
    print(f"Error: Could not find {LOG_FILE}")
except Exception as error:
    print(f"Unexpected error: {error}")

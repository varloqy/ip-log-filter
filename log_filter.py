import re
import http

def extract_and_geoip(log_file_path, output_file_path):
    # Regex for IPv4 addresses at the start of Apache log lines
    ip_pattern = re.compile(r'^(\d{1,3}(?:\.\d{1,3}){3})')
    unique_ips = set()

    # Step 1: Extract unique IPs
    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            match = ip_pattern.match(line)
            if match:
                unique_ips.add(match.group(1))

    sorted_ips = sorted(unique_ips)

    print(sorted_ips)

    print(f"[+] Processed {len(sorted_ips)} unique IPs.")
    print(f"[+] Results saved to {output_file_path}")


if __name__ == "__main__":
    log_path = "access.log"       # Path to your Apache log
    output_path = "geoip_results.txt"
    extract_and_geoip(log_path, output_path)

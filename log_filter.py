#!/usr/bin/python3
import re
import requests
import time
import argparse
URL = "http://ip-api.com/json/"

def extract_and_locate(log_file_path, output_file_path):
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

    with open(output_file_path, 'w') as out_file:
        for ip in sorted_ips:
            #print current working ip in console
            time.sleep(0.034)
            print(ip)
            #send GET request to API and write response to output file
            try:
                response = requests.get(f"{URL}{ip}")
                out_file.write(f"{ip} - {response.json()}\n")
            except Exception as e:
                out_file.write(f"{ip} - ERROR: {e}\n")

    print(f"[+] Processed {len(sorted_ips)} unique IPs.")
    print(f"[+] Results saved to {output_file_path}")

def main():
    #add arguments function
    parser = argparse.ArgumentParser("server log file geolocater")
    parser.add_argument("input", help="Path to input file")
    parser.add_argument("-o", "--output", default="geoip_results.txt", help="Output file name")

    args = parser.parse_args()
    #run main script
    extract_and_locate(args.input, args.output)

if __name__ == "__main__":
    main() #run main function

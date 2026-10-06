import whois
import time
import argparse

parser = argparse.ArgumentParser(description="Bulk WHOIS lookup from a file of domains")
parser.add_argument("filepath", help="Path to file containing domains, one per line")
parser.add_argument("-d", "--delay", type=float, default=2, help="Seconds to wait between lookups")
args = parser.parse_args()


#domain=open("/Users/srivatsask/Desktop/Python/Basics_Python/Project/sample.txt","r")  # Open the file in read mode
#data=domain.readlines()
#domain.close()  # Close the file after reading

with open(args.filepath, "r") as domain:
    data = domain.readlines()

for line in data:
    line = line.strip()
    if not line:
        continue

    try:
        domain_info = whois.whois(line)
        print(f"--- Results for {line} ---")
        print(f"registrar: {domain_info.get('registrar')}")

    except Exception as e:
        error_message = str(e).splitlines()[0] if str(e) else str(e)
        print(f"Error retrieving WHOIS information for {line}: {error_message}")

    finally:
        time.sleep(args.delay)  # pause between requests regardless of success/failure
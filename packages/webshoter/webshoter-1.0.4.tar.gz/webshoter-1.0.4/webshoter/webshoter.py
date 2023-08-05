import argparse
import sys
import os
import requests
from huepy import *

def banner():
    return f"""┬ ┬┌─┐┌┐ ┌─┐┬ ┬┌─┐┌┬┐┌─┐┬─┐
│││├┤ ├┴┐└─┐├─┤│ │ │ ├┤ ├┬┘ {blue('v1')}
└┴┘└─┘└─┘└─┘┴ ┴└─┘ ┴ └─┘┴└─ 
   Web screenshoting tool
     """

# Get url host
def get_host_by_url(url):
    return url.split("/")[2]

# Get first 2 chars of host
def get_host_short(host):
    return host[0:2]

# Request BGP toolkit
def get_bgp_toolkit(host):
    url = "https://bgp.he.net/dns/" + host
    response = requests.get(url)
    return response.text

# Download screenshot
def download_screenshot(host, output):
    url = f"https://bgp.he.net/webthumbs/{host[:1]}/{host[1:2]}/{host}_720.png"
    # Download image by url, using browser headers
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    # Save image to file
    with open(f"{output}/{host}.png", "wb") as f:
        f.write(response.content)

# Generate HTML report by directory
def generate_html_report(dir):
    # Get all files in directory
    files = os.listdir(dir)
    # Filter out files that are not png
    files = list(filter(lambda x: x.endswith(".png"), files))
    # Sort files by name
    files.sort()
    # Generate HTML
    html = "<html><head><title>WebShot Report</title></head><body><table>"
    for file in files:
        domain = file.replace(".png", "")
        html += f"<tr><td><a href='https://{domain}'>{domain}</a></td><td><img src='{file}'></td></tr>"
    html += "</table></body></html>"
    # Write HTML to file
    with open(f"{dir}/report.html", "w") as f:
        f.write(html)

def main():
    print('\033c')
    print(banner())
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", help="Output directory", required=True)
    urls = []

    # Check if there is data piped into the script
    if not sys.stdin.isatty():
        urls = sys.stdin.read().splitlines()
    else:
        # Read cli arguments
        parser.add_argument("-u", "--url", help="URL to take screenshot of")
        args = parser.parse_args()

        # Filter out the url
        urls.append(args.url)

    # Check if output directory exists
    if not os.path.exists(parser.parse_args().output):
        os.makedirs(parser.parse_args().output)

    # Take screenshot for each URL
    for url in urls:
        try:
            # Get url host
            host = get_host_by_url(url)

            # Request BGP toolkit
            get_bgp_toolkit(host)

            # Download a Screenshot
            download_screenshot(host, parser.parse_args().output)

            print(f"[{green('SUCCESS')}] {url}")
        except Exception as e:
            print(f"[{red('FAILED')}] {url}")

    generate_html_report(parser.parse_args().output)
    print("\nReport saved to " + parser.parse_args().output + "/report.html")
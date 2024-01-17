import argparse
import requests

# Set up the argument parser
parser = argparse.ArgumentParser(description='Download content from a URL and save it to a file.')
parser.add_argument('--url', required=True, help='The URL to download from.')
parser.add_argument('--output', required=True, help='The output filename.')
args = parser.parse_args()

# Download the content
response = requests.get(args.url)
response.raise_for_status()  # Raise an error for bad status codes

# Save the content to a file
with open(args.output, 'wb') as file:
    file.write(response.content)

print(f'Content downloaded from {args.url} and saved to {args.output}')

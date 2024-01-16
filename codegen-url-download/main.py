import argparse
import requests

# Set up the argument parser
parser = argparse.ArgumentParser(description='Download contents of a URL and save to a file.')
parser.add_argument('--url', required=True, help='The URL to download.')
parser.add_argument('--output', required=True, help='The output filename.')
args = parser.parse_args()

# Download the URL contents
response = requests.get(args.url)
response.raise_for_status()  # Raise an exception for HTTP errors

# Write the contents to the output file
with open(args.output, 'wb') as file:
    file.write(response.content)

print(f'Download complete. File saved as: {args.output}')

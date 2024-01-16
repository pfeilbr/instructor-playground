# URL Downloader

This command line program allows you to download the contents of a specified URL and save it to a file.

## Installation

First, create a virtual environment to manage the dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Next, install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To use the program, run the following command:

```bash
python main.py --url <URL> --output <FILENAME>
```

Replace `<URL>` with the URL you want to download and `<FILENAME>` with the desired output filename.

For example:

```bash
python main.py --url http://example.com --output example.html
```

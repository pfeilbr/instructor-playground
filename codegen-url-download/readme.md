# URL Downloader

This command line program downloads the contents of a specified URL and saves it to a given output filename.

## Installation

First, create a virtual environment to manage the dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Then, install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To use the program, run the following command:

```bash
python main.py --url <URL> --output <FILENAME>
```

Replace `<URL>` with the URL you want to download from, and `<FILENAME>` with the desired output filename.

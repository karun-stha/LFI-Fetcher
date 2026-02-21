# LFI-Fetcher

A simple LFI (Local File Inclusion) fetcher tool written in Python.

This tool helps you interactively test and fetch files from a vulnerable
LFI endpoint.

------------------------------------------------------------------------

## Requirements

-   Python 3
-   requests

Install dependencies:
```bash
pip install -r requirements.txt
```
------------------------------------------------------------------------

## Usage
```python
python3 lfi.py 'http://site.com/index.php?file='
```
Example:
```python
python3 lfi.py 'http://target.com/page.php?file=' -v
```
------------------------------------------------------------------------

## Options
```
-v, --verbose
Show extra connection/debug details.

-o, --output <file>
Save fetched file contents into a local file.
```

Example with output saving:
```python
python3 lfi.py 'http://target.com/page.php?file=' -o output.txt
```
------------------------------------------------------------------------

## Interactive Shell

After starting the tool, you'll enter interactive mode:
```
shell >>>
```
Type the filename you want to fetch:
```
shell >>> ../../../../etc/passwd
```
Type `exit` or `quit` to close the tool.

------------------------------------------------------------------------

## Features

-   Interactive LFI shell
-   Command history support
-   Optional verbose debugging
-   Optional output file logging
-   Graceful exit handling

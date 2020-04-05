# Windows 10 ISO CLI Downloader
 Python tool to download latest Windows 10 ISO direct from Microsoft through CLI.

Currently, downloading Windows 10 ISOs requires the Windows installation media creator tool on Windows, or a GUI interface on non-windows devices. This CLI tool allows you to download the latest 32bit or 64bit Windows 10 ISO straight from Microsoft.

## Requirements:
* Python 3
* Chrome (headless)
* Selenium

## Usage:
* Download script to your ISOs directory
```
git clone https://github.com/guyturner797/Win10-ISO-CLI-Downloader.git
```
* Install headless Chrome, pip selenium, and copy the latest chromedriver to the directory: https://chromedriver.chromium.org/
* Run the script
```
python Windows10ISOdownloader.py
```
* Enter either 1 or 2 for 32bit/64bit, and wait for the file to download
* Profit!

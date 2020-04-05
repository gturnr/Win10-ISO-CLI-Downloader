# Python 3.7. Written by Guy Turner 2020
import urllib.request, sys, os
from sm import get_latest_links

def chunk_report(bytes_so_far, chunk_size, total_size):
   percent = float(bytes_so_far) / total_size
   percent = round(percent*100, 2)
   sys.stdout.write("Progress: %f of %f gigabytes (%0.2f%%)\r" %
       (bytes_so_far*10**-9, total_size*10**-9, percent))
   if bytes_so_far >= total_size:
      sys.stdout.write('\n')

def chunk_read(response, filename="Windows10.iso", chunk_size=1024, report_hook=None):
   total_size = response.headers.get('Content-Length').strip()
   total_size = int(total_size)
   bytes_so_far = 0
   with open(filename, "wb") as f:
       while True:
          chunk = response.read(chunk_size)
          f.write(chunk)
          bytes_so_far += len(chunk)
          if not chunk:
             break
          if report_hook:
             report_hook(bytes_so_far, chunk_size, total_size)

if __name__ == '__main__':
    ## get latest url from Microsoft
    print("Please wait.. fetching latest download links from Microsoft...")
    print("==============================================================")
    print("Ignore Selenium warnings/errors")
    print("==============================================================")
    bit32, bit64 = get_latest_links()
    print("links valid for 24 hours:\n", bit32, "\n", bit64, "\n")

    bit_type = input("Please enter (1) 32-bit ISO, (2) 64-bit ISO: ")
    if bit_type == '1':
        url = bit32
    elif bit_type == '2':
        url = bit64
    else:
        exit

    filename = url.split('/')[4].split('?')[0]
    req = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        })
    if os.path.isfile(filename):
        print("File already exists with filename:", filename, "- press any key to override or exit to cancel.")
        input()

    response = urllib.request.urlopen(req);
    print("Saving Windows ISO.. Filename:", filename)
    chunk_read(response, filename, report_hook=chunk_report)  # reports on download progress

# Python 3.7. Written by Guy Turner 2020
import urllib.request, sys, os

## get latest url from Microsoft

url = "https://software-download.microsoft.com/pr/Win10_1909_English_x64.iso?t=ffb7e4ff-8ab5-4ae8-8a32-83d92cc8895c&e=1586171554&h=b28f19c4d4e89e032ce94cfa8205a110"
filename = url.split('/')[4].split('?')[0]
req = urllib.request.Request(
    url,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)


### Progress bar modified from somada141: https://gist.github.com/somada141/b3c21f7462b7f237e522
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
###

if __name__ == '__main__':
   bit_type = input("Please enter (1) 32-bit ISO, (2) 64-bit ISO: ")
   if bit_type not in ['1', '2']:
       exit
   if os.path.isfile(filename):
       print("File already exists with filename:", filename, "- press any key to override or exit to cancel.")
       input()

   response = urllib.request.urlopen(req);
   print("Saving Windows ISO.. Filename:", filename)
   chunk_read(response, filename, report_hook=chunk_report)  # reports on download progress

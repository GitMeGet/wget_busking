import difflib
import wget
import os
import sys
import time

url = 'https://www.nac.gov.sg/whatwedo/engagement/artsforall/busking.html'

html1_filename = wget.download(url)

count = int(html1_filename[html1_filename.find("(")+1:html1_filename.find(")")])

html2_filename = "busking (" + str(count-1) + ").html"

with open(html1_filename, 'r') as f:
    html1_str = f.read()
    
with open(html2_filename, 'r') as f:
    html2_str = f.read()

print()
    
if html1_str == html2_str:
    print("no changes")
    os.remove(html1_filename)
else:
    print("site changed")
    d = difflib.Differ()
    result = d.compare(html1_str, html2_str)
    sys.stdout.writelines(result)

time.sleep(5)

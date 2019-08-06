#!/usr/bin/env python3
import re
import requests
import sys

from tabulate import tabulate

URL_FAHRPLAN = 'https://flipdot.org/wiki/0xA?action=raw'
CW = 30 # COLUMN WIDTH

r = requests.get(URL_FAHRPLAN)
if r.status_code != 200:
    print(f"Couldn't download URL: {URL_FAHRPLAN}")
    sys.exit(1)

ds = [['\n'.join(y.strip()[i:i + CW] for i in range(0, len(y.strip()), CW)) for y in x.split('||')[1:-1]] for x in re.search(r'/\* FAHRPLAN BEGIN \*/\s*(.+)\s*/\* FAHRPLAN END \*/', r.text, re.DOTALL).groups()[0].split('\r\n') if x]
print(tabulate(ds, tablefmt='fancy_grid'))

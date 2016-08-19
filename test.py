import sys
import os
import re

search_IP = re.compile(r'\w*,\w*@\w*:\w*')
for args in sys.argv:
    IP =''.join(search_IP.findall(args))
    print IP


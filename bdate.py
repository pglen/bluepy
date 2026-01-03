#!/usr/bin/env python

# Use this to re-generate header with date

from datetime import *
today = datetime.now()
print("char *bdate=\"" + datetime.ctime(today) + '";')
# EOF

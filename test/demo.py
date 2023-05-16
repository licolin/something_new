# -*- encoding: utf-8 -*-
# Author: li_colin

import re

ret = re.compile(r".*[0-9]$").match("yyyy_9")

print("ret ", ret)

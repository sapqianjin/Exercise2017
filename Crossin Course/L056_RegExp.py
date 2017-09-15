# -*- coding: utf-8 -*
# Dorian Wang 2017.09.02
# lesson 56: Regular Expression

import re

text = "site sea sue sweet see case sse ssee loses"
m = re.findall(r"\bs\S*e\b", text)
# m = re.findall(r"\bs\S*?e\b", text)
if m:
    print(m)
else:
    print("not match")
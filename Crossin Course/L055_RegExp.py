# -*- coding: utf-8 -*
# Dorian Wang 2017.09.02
# lesson 55: Regular Expression

import re

text = "Hi, I'm Shirley Hiton. I am his wife."
m = re.findall(r"\b[Hh]i\b", text)
if m:
    print(m)
else:
    print("not match")
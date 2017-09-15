#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Dorian Wang 2017.09.04
# lesson: String Output with Format

import math

a = 5
b = 3
c = math.pi

print('%d' % a)
print('%8d' % a)
print('%08d' % a)

print('%f' % c)
print('%8.3f' % c)
print('%08.3f' % c)

scoreLastYear = 72
scoreThisYear = 85
improveRate = (scoreThisYear - scoreLastYear) / scoreThisYear * 100
print("His score is improved %2.2f%%." % improveRate)

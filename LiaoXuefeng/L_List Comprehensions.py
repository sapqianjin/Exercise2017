#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Dorian Wang 2017.09.05
# lesson: List Comprehensions

import os

print('list(range(1,11)):')
print(list(range(1,11)))
print()

print('[x for x in range(1,11)]:')
print([x for x in range(1,11)])
print()

print('[x * x for x in range(1,11)]:')
print([x * x for x in range(1,11)])
print()

print('[x * x for x in range(1,11) if x % 2 == 0]:')
print([x * x for x in range(1,11) if x % 2 == 0])
print()

print("[m + n for m in 'ABC' for n in 'XYZ']:")
print([m + n for m in 'ABC' for n in 'XYZ'])
print()

print("[d for d in os.listdir('.')]:")
print([d for d in os.listdir('.')])
print()
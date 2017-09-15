#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Dorian Wang 2017.09.04
# lesson: Unicode

print('English:')
print('ABC'.encode("utf-8"))
print((len('ABC')))

print(b'ABC'.decode("utf-8"))
print((len(b'ABC')))

print('\nChinese:')
print('测试'.encode("utf-8"))
print((len('测试')))

print(b'\xe6\xb5\x8b\xe8\xaf\x95'.decode("utf-8"))
print((len(b'\xe6\xb5\x8b\xe8\xaf\x95')))

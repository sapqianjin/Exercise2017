# -*- coding: utf-8 -*
# Dorian Wang 2017.09.02
# lesson 66: List Comprehension

print(';'.join(str(i) for i in range(1,101) if (i % 2 == 0) and (i % 3 == 0) and (i % 5 == 0)))


# -*- coding: utf-8 -*
# Dorian Wang 2017.09.02
# lesson 61: Time

import time

starttime = time.time()
print('start: %f' % starttime)
for i in range(1000):
    print(i)

endtime = time.time()
print('end: %f' % endtime)

print('total time: %f' % (endtime - starttime))

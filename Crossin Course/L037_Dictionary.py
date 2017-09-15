#-*- coding: utf-8 -*
# Dorian Wang 2017.08.31
# lesson 37: Dictionary

#字典和List的不同点在于，字典只能通过Key来访问，所以通过Key来定位比较方便
# 而List只能通过位置索引

# 字典的本质是hash表
# hash表的数据结构注定它就是无序的。
# 至于hash表的内部结构以及实现，可以参考《算法导论》。

# 但在Python3中，字典似乎默认是有序的
# 至少在这个测试中，可以看到打印的时候是按照顺序的
score = {
    'Xiao': 95,
    'Duan': 97,
    'Xu': 89
}

print(score['Duan'])

for name in score:
    print(score[name])

score['Xu']=91

score['Mu'] = 88

del score['Xiao']

for name in score:
    print(name, score[name])
#-*- coding: utf-8 -*
# Dorian Wang 2017.08.31
# lesson 33: Process File

scoreFile = open('L033_Score.txt','rb')
eachlines = scoreFile.readlines()
scoreFile.close()

print(eachlines)

results = []
for line in eachlines:
    print(line.decode('utf-8'))
    data = line.split()
    name = data[0].decode('utf-8')
    sum = 0
    result = ''
    for score in data[1:]:
        sum = sum + int(score)
    result = '%s %d\n' %(name, sum)
    print(result)
    results.append(result)

print(results)
resultFile = open('L033_Result.txt','w')
resultFile.writelines(results)
resultFile.close()


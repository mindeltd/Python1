"""
Scenarijus, kuris skaito duomenys is tekstionio failo,
juos apdoroja ir iraso i kita faila
"""
# Evaluation 1

with open('input01.csv') as f:
    LINES = f.readlines()
DATA = []
DATA.append(LINES[0][0:len(LINES[0])-1].upper().split(','))
for line in LINES[1:]:
    temp = line.split(',')
    if  temp[3].endswith('SET'):
        temp[19], temp[16] = temp[19], temp[16]
        temp[21] = float(temp[21])
        DATA.append(temp)
DATA[1:] = sorted(DATA[1:], key=lambda l: l[21], reverse=True)
with open('output01_1612799.txt', 'w') as w:
    for values in DATA:
        values[21]=str(values[21])
        w.write(";".join(values) + '\n')
        
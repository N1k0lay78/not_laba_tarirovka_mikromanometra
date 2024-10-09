# для пучарма
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import csv

from eval_Spr import eval_Spr


def get_values():
    with open('izmerenia.csv', newline='') as csvfile:
        lines = csv.reader(csvfile)
        ql, qr, hl, hr = [], [], [], []
        line_n = 0
        for line in lines:
            if line_n == 0:
                line_n += 1
                continue
            ql.append(int(line[0])*10**(-3))
            qr.append(int(line[1])*10**(-3))
            hl.append(int(line[2]))
            hr.append(int(line[3]))
    return ql, qr, hl, hr


def eval_table():
    ql, qr, hl, hr = get_values()
    
    g = 9.81
    spr = eval_Spr()

    dm = []
    dg = []
    dp = []
    dh = []
    k =  []
    for i in range(len(ql)):
        dm.append(round(abs(ql[i] - qr[i]), 2))
        dg.append(round(g * dm[i], 2))
        dp.append(round(dg[i] / spr, 1))
        dh.append(round(abs(hl[i] - hr[i])))
        k.append(round(abs(dp[i] - dh[i]), 1))
    return dm, dg, dp, hl, hr, dh, k


def get_table():
    rows = eval_table()
    table = []
    for i in range(len(rows[0])):
        table.append([i+1])
        for ii in range(len(rows)):
            table[-1].append(rows[ii][i])
    
    # for i in range(len(table)):
    #     print(table[i])

    return table


def eval_mean_k():
    k = eval_table()[-1]
    return round(sum(k) / len(k), 1)

def save_image():
    data = []
    for dp_i, k_i in zip(eval_table()[2], eval_table()[-1]):
        data.append([dp_i, k_i])
    data.sort(key=lambda el: el[0])
    dp = list(map(lambda el: el[0], data))
    k = list(map(lambda el: el[1], data))
    # dp, k = eval_table()[2], eval_table()[-1]
    plt.plot(dp, k)
    plt.xlabel('Давление ')
    plt.ylabel('Тарировочный коэффициент')
    plt.title('Зависимость тарировочного коэффициента микроманометра от давления')
    plt.savefig('plot.png', bbox_inches='tight')

save_image()
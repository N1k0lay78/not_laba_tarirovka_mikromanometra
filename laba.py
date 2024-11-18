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
    for i in range(1, len(ql)):
        # TODO  (ql[i] - ql[0]) - (qr[i] - qr[0])
        dm.append(round((ql[i] - ql[0]) - (qr[i] - qr[0]), 3))
        dg.append(round(g * dm[i - 1], 3))
        # OK
        dp.append(round(dg[i - 1] / spr, 5))
        # TODO (Hl[i] - Hl[0]) - (Hr[i] - Hr[0])
        dh.append(round((hl[i] - hl[0]) - (hr[i] - hr[0])))
        print(round((ql[i] - ql[0]) - (qr[i] - qr[0]), 2), round(abs(dp[i - 1] / dh[i - 1]), 1))
        k.append(round(abs(dp[i - 1] / dh[i - 1]), 2))
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
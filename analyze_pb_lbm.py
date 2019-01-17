#!/usr/bin/env python

import re
import matplotlib.pyplot as plt

regex = re.compile ('^Timer Wall Time: ([\d.]+)\s*$')
def parse (filename):
    with open (filename, 'r') as fdi:
        for line in fdi:
            m = regex.match (line)

            if m:
                runtime = float (m.group (1))
                break

    return runtime

def stratify (data, keyOrder):
    sData = {'solo':    {'vals': [], 'pct': [], 'nvals': [], 'ticks': [], 'lbl': 'Solo',                'hch': '..'  },
             'defw':    {'vals': [], 'pct': [], 'nvals': [], 'ticks': [], 'lbl': 'Co-Sched',            'hch': '\\\\'},
             'thrt':    {'vals': [], 'pct': [], 'nvals': [], 'ticks': [], 'lbl': 'Co-Sched (Throttle)', 'hch': '//'},
             'gngw':    {'vals': [], 'pct': [], 'nvals': [], 'ticks': [], 'lbl': 'RT-Gang (Throttle)',  'hch': 'xx'  }}

    runs = len (sData.keys ())
    xNames = []

    bIdx = 0
    for benchmark in data.keys ():
        idx = 0
        for run in keyOrder:
            sData [run]['vals'].append (data [benchmark][idx])
            sData [run]['nvals'].append (data [benchmark][idx] / data [benchmark][0])
            sData [run]['pct'].append ((sData [run]['nvals'][-1] - 1.0) * 100)
            sData [run]['ticks'].append (idx + bIdx * (runs + 2))
            idx += 1

        bIdx += 1

    for benchmark in data.keys ():
        xNames.append (benchmark.capitalize ())

    return sData, xNames

def plotData (data):
    keyOrder = ['solo', 'defw', 'thrt', 'gngw']
    sData, xNames = stratify (data, keyOrder)

    # fig = plt.figure (figsize = (30, 10))

    # p = plt.subplot (3, 1, 1)
    # for key in keyOrder:
    #     plt.bar (sData [key]['ticks'], sData [key]['vals'], width = 1.0, lw = 2.0, label = sData [key]['lbl'], color = 'white', edgecolor = 'black', hatch = sData [key]['hch'])

    # plt.gca ().yaxis.grid (True, linestyle = '--')
    # plt.legend (loc = 'upper left', fontsize = 'large')
    # # plt.xticks ([])
    # plt.xticks ([x - 0.5 for x in sData ['defw']['ticks']], xNames, fontweight = 'bold')
    # plt.xlim (0, sData ['defw']['ticks'][-1] + 1)
    # plt.ylim (0, 130)
    # plt.ylabel ('Runtime (secs)', fontsize = 'large', fontweight = 'bold')

    for key in keyOrder:
        plt.bar (sData [key]['ticks'], sData [key]['nvals'], width = 1.0, lw =
                1.5, label = sData [key]['lbl'], color = 'white', edgecolor = 'k', hatch = sData [key]['hch'])

    plt.gca ().yaxis.grid (True, linestyle = '--')
    xNames = ['Lbm/%s' % x for x in xNames]
    plt.xticks ([x + 0.5 for x in sData ['defw']['ticks']], xNames, fontweight =
            'bold', rotation = 45)
    plt.xlim (-2, sData ['defw']['ticks'][-1] + 4)
    plt.ylim (0, 3)
    plt.ylabel ('Normalized Runtime', fontsize = 'large', fontweight = 'bold')
    plt.legend (loc = 'upper center', ncol = 2, fontsize = 'medium')

    # p = plt.subplot (3, 1, 3)
    # for key in keyOrder:
    #     plt.bar (sData [key]['ticks'], sData [key]['pct'], width = 1.0, lw = 2.0, label = sData [key]['lbl'], color = 'white', edgecolor = 'black', hatch = sData [key]['hch'])

    # plt.gca ().yaxis.grid (True, linestyle = '--')
    # plt.xticks ([x - 0.5 for x in sData ['defw']['ticks']], xNames, fontweight = 'bold')
    # plt.xlim (0, sData ['defw']['ticks'][-1] + 1)
    # plt.ylim (0, 100)
    # plt.xlabel ('Benchmarks', fontsize = 'x-large', fontweight = 'bold')
    # plt.ylabel ('Slowdown (%)', fontsize = 'large', fontweight = 'bold')

    plt.savefig ('parboil_lbm_tx2.pdf', bbox_inches = 'tight')

    return

def main ():
    data = {'spmv'      : [],
            'stencil'   : [],
            'sgemm'     : [],
            'cutcp'     : [],
            'tpacf'     : [],
            'bfs'       : [],
            'lbm'       : []}

    for benchmark in data.keys ():
        filename = 'rtg/lbm_solo.log'
        runtime = parse (filename)
        data [benchmark].append (runtime)

    for benchmark in data.keys ():
        for run in ['cosched_lbm', 'cosched_lbm_th', 'rtg_lbm_th']:
            filename = 'rtg/%s_%s.log' % (benchmark, run)
            runtime = parse (filename)
            data [benchmark].append (runtime)

    plotData (data)

    return

if __name__ == '__main__':
    main ()

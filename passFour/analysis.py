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
    sData = {'solo':    {'vals': [], 'nvals': [], 'ticks': [], 'lbl': 'Solo',            'hch': '..'  },
             'defr':    {'vals': [], 'nvals': [], 'ticks': [], 'lbl': 'Default (Read)',  'hch': '//'  },
             'defw':    {'vals': [], 'nvals': [], 'ticks': [], 'lbl': 'Default (Write)', 'hch': '\\\\'},
             'gngr':    {'vals': [], 'nvals': [], 'ticks': [], 'lbl': 'Gang (Read)',     'hch': 'xx'  },
             'gngw':    {'vals': [], 'nvals': [], 'ticks': [], 'lbl': 'Gang (Write)',    'hch': '++'  }}

    runs = len (sData.keys ())
    xNames = []

    bIdx = 0
    for benchmark in data.keys ():
        idx = 0
        for run in keyOrder:
            sData [run]['vals'].append (data [benchmark][idx])
            sData [run]['nvals'].append (data [benchmark][idx] / data [benchmark][0])
            sData [run]['ticks'].append (idx + bIdx * (runs + 2))
            idx += 1

        bIdx += 1

    for benchmark in data.keys ():
        xNames.append (benchmark.capitalize ())

    return sData, xNames

def plotData (data):
    keyOrder = ['solo', 'gngr', 'gngw', 'defr', 'defw']
    sData, xNames = stratify (data, keyOrder)

    fig = plt.figure (figsize = (20, 10))

    p = plt.subplot (2, 1, 1)
    for key in keyOrder:
        plt.bar (sData [key]['ticks'], sData [key]['vals'], width = 1.0, lw = 2.0, label = sData [key]['lbl'], color = 'white', edgecolor = 'black', hatch = sData [key]['hch'])

    plt.gca ().yaxis.grid (True, linestyle = '--')
    plt.legend (ncol = len (sData.keys ()), loc = 'upper center', fontsize = 'large')
    plt.xticks ([])
    plt.xlim (0, sData ['defw']['ticks'][-1] + 1)
    plt.ylim (0, 130)
    plt.ylabel ('Runtime (secs)', fontsize = 'x-large', fontweight = 'bold')

    p = plt.subplot (2, 1, 2)
    for key in keyOrder:
        plt.bar (sData [key]['ticks'], sData [key]['nvals'], width = 1.0, lw = 2.0, label = sData [key]['lbl'], color = 'white', edgecolor = 'black', hatch = sData [key]['hch'])

    plt.gca ().yaxis.grid (True, linestyle = '--')
    plt.xticks ([x - 0.5 for x in sData ['defw']['ticks']], xNames, fontweight = 'bold')
    plt.xlim (0, sData ['defw']['ticks'][-1] + 1)
    plt.ylim (0, 2)
    plt.xlabel ('Benchmark', fontsize = 'x-large', fontweight = 'bold')
    plt.ylabel ('Normalized Runtime', fontsize = 'x-large', fontweight = 'bold')
    plt.show ()
    # fig.savefig ('parboil_tx2.pdf', bbox_inches = 'tight')

    return

def main ():
    data = {'spmv'      : [],
            'stencil'   : [],
            'sgemm'     : [],
            'cutcp'     : [],
            'tpacf'     : [],
            'bfs'       : [],
            'histo'     : [],
            'mri-q'     : []}

    execType = ['Solo', 'Gang (read)', 'Gang (write)', 'Default (read)', 'Default (write)']

    for benchmark in data.keys ():
        for execution in ['solo']:
            filename = 'mint/%s_%s.perf' % (benchmark, execution)
            runtime = parse (filename)
            data [benchmark].append (runtime)

    for benchmark in data.keys ():
        for run in ['gang', 'mint']:
            for execution in ['read', 'write']:
                filename = '%s/%s_%s.perf' % (run, benchmark, execution)
                runtime = parse (filename)
                data [benchmark].append (runtime)

    plotData (data)

    return

if __name__ == '__main__':
    main ()

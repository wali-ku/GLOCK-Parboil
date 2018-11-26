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

def stratify (data):
    sData = {}
    sData ['xAxis'] = []
    sData ['xVals'] = []
    sData ['xLabs'] = []
    sData ['hatch'] = []
    sData ['xTicks'] = []
    sData ['xNames'] = []

    index = 0
    lastTick = 0
    basicSeparation = 2
    maxY = 0

    for benchmark in data.keys ():
        for cluster in data [benchmark].keys ():
            separation = (basicSeparation * 2) if (index % 2 == 0) else (basicSeparation)
            label = '%s (%s)' % (benchmark.capitalize (), cluster.capitalize ())
            ticks = [lastTick + separation + offset for offset in range (len (data [benchmark][cluster]['data']))]
            lastTick = ticks [-1]
            index += 1

            y = max (data [benchmark][cluster]['data'])
            maxY = (y) if (maxY < y) else (maxY)

            sData ['xAxis'].append (ticks)
            sData ['xVals'].append (data [benchmark][cluster]['data'])
            sData ['hatch'].append (data [benchmark][cluster]['hatch'])
            sData ['xLabs'].append (label)
            sData ['xTicks'] += ticks
            sData ['xNames'] += ['solo', 'read', 'write']

    sData ['maxY'] = maxY


    return sData

def plotData (data):
    sData = stratify (data)

    fig = plt.figure (figsize = (20, 10))

    p = plt.subplot (2, 1, 1)
    for item in range (len (sData ['xAxis'])):
        plt.bar (sData ['xAxis'][item], sData ['xVals'][item], width = 1.0, lw = 2.0, label = sData ['xLabs'][item], color = 'white', edgecolor = 'black', hatch = sData ['hatch'][item])

    plt.gca ().yaxis.grid (True, linestyle = '--')
    plt.legend (ncol = len (sData ['xLabs']) / 5, loc = 'upper left', fontsize = 'large')
    plt.xticks ([])
    plt.xlim (0, sData ['xTicks'][-1] + 5)
    plt.ylim (0, 1.05 * sData ['maxY'])
    plt.ylabel ('Runtime (secs)', fontsize = 'x-large', fontweight = 'bold')

    p = plt.subplot (2, 1, 2)
    for item in range (len (sData ['xAxis'])):
        plt.bar (sData ['xAxis'][item], [val / sData ['xVals'][item][0] for val in sData ['xVals'][item]], width = 1.0, lw = 2.0, label = sData ['xLabs'][item], color = 'white', edgecolor = 'black', hatch = sData ['hatch'][item])

    plt.gca ().yaxis.grid (True, linestyle = '--')
    plt.xticks (sData ['xTicks'], sData ['xNames'], rotation = 45, fontweight = 'bold')
    plt.xlim (0, sData ['xTicks'][-1] + 5)
    plt.ylim (0, 2)
    plt.xlabel ('Execution Scenario', fontsize = 'x-large', fontweight = 'bold')
    plt.ylabel ('Normalized Runtime', fontsize = 'x-large', fontweight = 'bold')
    fig.savefig ('parboil_tx2.pdf', bbox_inches = 'tight')

    return

def main ():
    data = {'spmv'      : {'cortex': {'data': [], 'hatch': '/'}, 'denver': {'data': [], 'hatch': '\\'}},
            'stencil'   : {'cortex': {'data': [], 'hatch': '.'}, 'denver': {'data': [], 'hatch': '**'}},
            'sgemm'     : {'cortex': {'data': [], 'hatch': 'x'}, 'denver': {'data': [], 'hatch': '++'}},
            'cutcp'     : {'cortex': {'data': [], 'hatch': '-'}, 'denver': {'data': [], 'hatch': '//'}},
            'lbm'       : {'cortex': {'data': [], 'hatch': 'xx'}, 'denver': {'data': [], 'hatch': '..'}}}

    execType = ['solo', 'read', 'write']

    for benchmark in data.keys ():
        for cluster in data [benchmark].keys ():
            for execution in execType:
                filename = '%s_%s_%s.perf' % (benchmark, cluster, execution)
                runtime = parse (filename)
                data [benchmark][cluster]['data'].append (runtime)

    plotData (data)

    return

if __name__ == '__main__':
    main ()

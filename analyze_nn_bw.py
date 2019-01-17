#!/usr/bin/env python

import os, re, sys
import numpy as np
from matplotlib import pyplot as plt

def analyze (filename):
    inferTime = []
    # regex = '^\s+([\d,]+)\s+ instructions.*$'
    regex = '^.*#\s+([\d.]+) CPUs utilized.*$'
    with open (filename, 'r') as fdi:
        for line in fdi:
            match = re.match (regex, line)

            if match:
                # instructions = int ((match.group (1)).replace (',', ''))
                util = float (match.group (1))

    # return instructions
    return util 

def plotData (data, platform):
    fontSizeLabels = 'x-large'
    fontWeightLabels = 'bold'

    keys = ['Default', 'Throttle', 'RTG', 'RTG-Throttle']
    for exp in keys:
        plt.bar (data [exp]['ticks'], data [exp]['vals'], edgecolor = 'k', width = 1.0, lw = 1.5, label = exp)

    plt.xlim (0, 12)
    plt.ylim (0, 0.8)
    plt.xticks (fontsize = 'large', fontweight = 'bold')
    plt.yticks (fontsize = 'large', fontweight = 'bold')
    # plt.ylabel ('Instructions Executed', fontsize = fontSizeLabels, fontweight = fontWeightLabels)
    plt.ylabel ('CPU Utilization (%)', fontsize = fontSizeLabels, fontweight = fontWeightLabels)
    plt.legend (loc = 'upper center', ncol = 4, fontsize = 'medium')
    # plt.grid ()
    plt.savefig ('%s_2n5c_bw.pdf' % platform, bbox_inches = 'tight')

    return

def main ():
    data = {'Default': {}, 'Throttle': {}, 'RTG': {}, 'RTG-Throttle': {}}
    platform = sys.argv [1]
    bwcd = analyze ('rtg_nn/bw_cpu_nobl.log')
    bwmd = analyze ('rtg_nn/bw_mem_nobl.log')
    bwct = analyze ('rtg_nn/bw_cpu_no.log')
    bwmt = analyze ('rtg_nn/bw_mem_no.log')
    bwcr = analyze ('rtg_nn/bw_cpu_rgbl.log')
    bwmr = analyze ('rtg_nn/bw_mem_rgbl.log')
    bwcrt = analyze ('rtg_nn/bw_cpu_rg.log')
    bwmrt = analyze ('rtg_nn/bw_mem_rg.log')

    data ['Default']['vals']    = [bwcd, bwmd]
    data ['Default']['ticks']   = [1,2]

    data ['Throttle']['vals']   = [bwct, bwmt]
    data ['Throttle']['ticks']  = [4,5]

    data ['RTG']['vals']        = [bwcr, bwcd]
    data ['RTG']['ticks']       = [7,8]

    data ['RTG-Throttle']['vals']   = [bwcrt, bwmrt]
    data ['RTG-Throttle']['ticks']  = [10,11]

    plotData (data, platform)
    return

if __name__ == "__main__":
    main ()

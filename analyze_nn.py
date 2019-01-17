#!/usr/bin/env python

import os, re, sys
import numpy as np
from matplotlib import pyplot as plt

def analyze (filename):
    inferTime = []
    regex = '^.*took: ([\d.]+) ms.*$'
    with open (filename, 'r') as fdi:
        for line in fdi:
            match = re.match (regex, line)

            if match:
                time = float (match.group (1))
                inferTime.append (time)

    sortedTimes = sorted (inferTime)
    cutoff = np.percentile (sortedTimes, 99.5)
    filteredTimes = [t for t in sortedTimes if t < cutoff]
    return (filteredTimes)

def plotData (data, platform):
    num_bins = 1000
    lineType = {'hptr': 'b-', 'hpt': 'b--', 'hpr': 'b-.', 'hp': 'b:', 'lptr': 'r-', 'lpt': 'r--', 'lpr': 'r-.', 'lp': 'r:'}
    lineLabels = {'hptr': 'HP (RTG-Throttle)', 'hpt': 'HP (Throttle)', 'hpr': 'HP (RTG)', 'hp': 'HP', 'lptr': 'LP (RTG-Throttle)', 'lpt': 'LP (Throttle)', 'lpr': 'LP (RTG)', 'lp': 'LP'}
    fontSizeLabels = 'x-large'
    fontWeightLabels = 'bold'
    margins = 0.15
    xLimLeft = min ([min (x) for x in data.values ()])
    xLimRight = max ([max (x) for x in data.values ()])
    xRange = xLimRight - xLimLeft
    xLimLeft = 0 if 'pi' in platform else 5
    xLimRight = 850 if 'pi' in platform else 15

    logs = ['hptr', 'hpr', 'hpt', 'hp', 'lptr', 'lpr', 'lpt', 'lp']
    for exp in logs:
        counts, bin_edges = np.histogram (data [exp], bins = num_bins, normed = True)
        cdf = np.cumsum (counts)
        plt.plot (bin_edges [1:], cdf/cdf[-1], lineType [exp], lw = 2.0, label = lineLabels [exp])
    # plt.plot ([xLimLeft, xLimRight], [1, 1], 'k--', lw = 1)
    # plt.xlim (xLimLeft, xLimRight)
    plt.xlim (5, 15)
    plt.ylim (0, 1.00)
    plt.xticks (fontsize = 'large', fontweight = 'bold')
    plt.yticks (fontsize = 'large', fontweight = 'bold')
    plt.ylabel ('CDF', fontsize = fontSizeLabels, fontweight = fontWeightLabels)
    plt.xlabel ('DNN Inference Time (msec)', fontsize = fontSizeLabels, fontweight = fontWeightLabels)
    plt.legend (loc = 'lower right', ncol = 1, fontsize = 'medium')
    plt.grid ()
    plt.savefig ('%s_2n5c.pdf' % platform, bbox_inches = 'tight')

    return

def main ():
    data = {}
    platform = sys.argv [1]
    data ['hptr'] = analyze ('rtg_nn/x2_n1c5_hp_rg.perf')
    data ['hpt'] = analyze ('rtg_nn/x2_n1c5_hp_no.perf')
    data ['hpr'] = analyze ('rtg_nn/x2_n1c5_hp_rgbl.perf')
    data ['hp']  = analyze ('rtg_nn/x2_n1c5_hp_nobl.perf')
    data ['lptr']  = analyze ('rtg_nn/x2_n1c5_lp_rg.perf')
    data ['lpt']  = analyze ('rtg_nn/x2_n1c5_lp_no.perf')
    data ['lpr'] = analyze ('rtg_nn/x2_n1c5_lp_rgbl.perf')
    data ['lp']  = analyze ('rtg_nn/x2_n1c5_lp_nobl.perf')

    plotData (data, platform)

    return

if __name__ == "__main__":
    main ()

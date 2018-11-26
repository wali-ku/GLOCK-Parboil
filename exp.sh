#!/bin/bash

# Subject benchmarks
benchmarks=(	'spmv'	   'stencil'  'cutcp'	 'sgemm'    'lbm'	)
versions=(	'omp_base' 'omp_base' 'omp_base' 'omp_base' 'omp_cpu'	)
datasets=(	'large'	   'default'  'large'	 'medium'   'short'	)

# Execution parameters
cpuTypes=(	'cortex'   'denver'   )
cores=(		'0,3,4,5'  '1,2'      )
corunTypes=(	'read'     'write'    )
corunCpuTypes=( 'denver'   'cortex'   )
cortexCores=(3 4 5)
denverCores=(2)
soloCores=()

for clusterNum in `seq 0 $((${#cpuTypes[@]} - 1))`; do
	clusterName=${cpuTypes[${clusterNum}]}
	clusterCpus=${cores[${clusterNum}]}
	corunCpuType=${corunCpuTypes[${clusterNum}]}

	for corunType in ${corunTypes[@]}; do
		corunCores=${corunCpuType}Cores[@]

		# Start the corunners
		for core in ${!corunCores}; do
			printf '[STATUS] Starting bandwidth (%5s) corunners on <%s> cluster\n' ${corunType} ${corunCpuType}
				chrt -f 10 bandwidth -c ${core} -m 16384 -t 10000 -a ${corunType} &> /dev/null &
		done
		sleep 2

		# Run subject benchmarks
		for benchmarkNum in `seq 0 $((${#benchmarks[@]} - 1))`; do
			benchmark=${benchmarks[${benchmarkNum}]}
			dataset=${datasets[${benchmarkNum}]}
			version=${versions[${bnechmarkNum}]}

			printf '[STATUS] Running <%s> on <%s> cluster\n' ${benchmark} ${clusterName}
			taskset -c ${clusterCpus} chrt -f 15 ./parboil run ${benchmark} ${version} ${dataset} 2>&1 | tee ${benchmark}_${clusterName}_${corunType}.perf
			echo '-----------------------------------------'
			sleep 2
		done
		echo '[STATUS] Stopping bandwidth...'
		killall bandwidth
		echo
		echo
	done
done

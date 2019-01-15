MAIN_printInfo:
	grid size      : 120 x 120 x 150 = 2.16 * 10^6 Cells
	nTimeSteps     : 3000
	result file    : /home/nvidia/ssd/gits/BWLOCK-GPU/benchmarks/parboil/benchmarks/lbm/run/long/reference.dat
	action         : store
	simulation type: lid-driven cavity
	obstacle file  : /home/nvidia/ssd/gits/BWLOCK-GPU/benchmarks/parboil/datasets/lbm/long/input/120_120_150_ldc.of

LBM_allocateGrid: allocated 169.2 MByte
LBM_allocateGrid: allocated 169.2 MByte
LBM_showGridStatistics:
	nObstacleCells:  343321 nAccelCells:   26912 nFluidCells: 1789767
	minRho:   1.0000 maxRho:   1.0000 mass: 2.160000e+06
	minU: 0.000000e+00 maxU: 0.000000e+00

timestep: 64
timestep: 128
timestep: 192
timestep: 256
MAIN_stopClock:
	usr:  189.49 sys:    0.09 tot:  189.58 wct:   50.07 MLUPS: 129.42

LBM_showGridStatistics:
	nObstacleCells:  343321 nAccelCells:   26912 nFluidCells: 1789767
	minRho:   0.9187 maxRho:   1.0844 mass: 2.159998e+06
	minU: 2.219546e-06 maxU: 3.243893e-02

Compute   : 51.881094
Timer Wall Time: 51.881096
Final simulated flow volume does not match expected flow volume

Mismatch
Parboil parallel benchmark suite, version 0.2

Output checking tool detected a mismatch

 Performance counter stats for './parboil run lbm omp_cpu long':

     197811.688256      task-clock (msec)         #    3.421 CPUs utilized          
             2,488      context-switches          #    0.013 K/sec                  
               115      cpu-migrations            #    0.001 K/sec                  
           418,341      page-faults               #    0.002 M/sec                  
   400,768,735,532      cycles                    #    2.026 GHz                    
   <not supported>      stalled-cycles-frontend  
   <not supported>      stalled-cycles-backend   
   642,027,511,058      instructions              #    1.60  insns per cycle        
   <not supported>      branches                 
        36,238,129      branch-misses             #    0.00% of all branches        

      57.830090276 seconds time elapsed


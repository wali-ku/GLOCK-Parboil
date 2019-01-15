Opening file:/home/nvidia/ssd/gits/BWLOCK-GPU/benchmarks/parboil/datasets/sgemm/medium/input/matrix1.txt
Matrix dimension: 1024x992
Opening file:/home/nvidia/ssd/gits/BWLOCK-GPU/benchmarks/parboil/datasets/sgemm/medium/input/matrix2t.txt
Matrix dimension: 1056x992
Opening file:/home/nvidia/ssd/gits/BWLOCK-GPU/benchmarks/parboil/benchmarks/sgemm/run/medium/matrix3.txt for write.
Matrix dimension: 1024x1056
GFLOPs = 0.107854
IO        : 2.646486
Compute   : 19.891623
Timer Wall Time: 22.538214
Pass
Parboil parallel benchmark suite, version 0.2


 Performance counter stats for './parboil run sgemm omp_base medium':

      71614.787232      task-clock (msec)         #    2.872 CPUs utilized          
               625      context-switches          #    0.009 K/sec                  
                40      cpu-migrations            #    0.001 K/sec                  
            82,050      page-faults               #    0.001 M/sec                  
   145,146,128,624      cycles                    #    2.027 GHz                    
   <not supported>      stalled-cycles-frontend  
   <not supported>      stalled-cycles-backend   
    60,660,990,597      instructions              #    0.42  insns per cycle        
   <not supported>      branches                 
        28,719,034      branch-misses             #    0.00% of all branches        

      24.934869513 seconds time elapsed


CPU-based sparse matrix vector multiplication****
Original version by Li-Wen Chang <lchang20@illinois.edu> and Shengzhao Wu<wu14@illinois.edu>
This version maintained by Chris Rodrigues  ***********
Converting COO to JDS format (146689x146689)
3636649 matrix entries, warp size = 1, row padding align = 1, pack size = 1

Padding data....146689 rows, 146689 groups
Allocating data space: 3636649 entries (0.000000% padding)
Finished converting.
JDS format has 146689 columns, 49 rows.
nz_count_len = 146689
IO        : 3.201846
Compute   : 1.376513
Timer Wall Time: 4.578363
Pass
Parboil parallel benchmark suite, version 0.2


 Performance counter stats for './parboil run spmv omp_base large':

       8305.915296      task-clock (msec)         #    1.683 CPUs utilized          
               305      context-switches          #    0.037 K/sec                  
                 7      cpu-migrations            #    0.001 K/sec                  
            41,708      page-faults               #    0.005 M/sec                  
    16,804,087,330      cycles                    #    2.023 GHz                    
   <not supported>      stalled-cycles-frontend  
   <not supported>      stalled-cycles-backend   
    20,666,942,120      instructions              #    1.23  insns per cycle        
   <not supported>      branches                 
        35,960,738      branch-misses             #    0.00% of all branches        

       4.934087911 seconds time elapsed


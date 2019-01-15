CPU-based 7 points stencil codes****
Original version by Li-Wen Chang <lchang20@illinois.edu> and I-Jui Sung<sung10@illinois.edu>
This version maintained by Chris Rodrigues  ***********
IO        : 0.114309
Compute   : 78.438554
Timer Wall Time: 78.552864
Pass
Parboil parallel benchmark suite, version 0.2


 Performance counter stats for './parboil run stencil omp_base default':

     342189.584864      task-clock (msec)         #    4.067 CPUs utilized          
             4,306      context-switches          #    0.013 K/sec                  
               103      cpu-migrations            #    0.000 K/sec                  
           103,291      page-faults               #    0.302 K/sec                  
   694,024,869,480      cycles                    #    2.028 GHz                    
   <not supported>      stalled-cycles-frontend  
   <not supported>      stalled-cycles-backend   
   259,951,548,800      instructions              #    0.37  insns per cycle        
   <not supported>      branches                 
        51,707,213      branch-misses             #    0.00% of all branches        

      84.145068090 seconds time elapsed


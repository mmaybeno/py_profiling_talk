# Quick profiling talk

Based off blog post from [nylas](https://www.nylas.com/blog/performance)  
Simple talk about local profiling and simple solution for profiling web apps.

## cProfile
```
python app/cprofile_demo.py
         506 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 cprofile_demo.py:10(sort_fast)
        1    0.000    0.000    0.000    0.000 random.py:277(shuffle)
        1    0.000    0.000    0.000    0.000 {len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      499    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {range}
        1    0.000    0.000    0.000    0.000 {sorted}


         500006 function calls in 0.568 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.008    0.008    0.568    0.568 <string>:1(<module>)
        1    0.002    0.002    0.560    0.560 cprofile_demo.py:16(sort_slow)
        1    0.262    0.262    0.294    0.294 random.py:277(shuffle)
        1    0.000    0.000    0.000    0.000 {len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   499999    0.032    0.000    0.032    0.000 {method 'random' of '_random.Random' objects}
        1    0.010    0.010    0.010    0.010 {range}
        1    0.255    0.255    0.255    0.255 {sorted}
```

## Line and memory profiler
```
pip install -r requirements.txt
./line_mem_demo.sh 
+ kernprof -l -v app/fast_demo.py
Wrote profile results to fast_demo.py.lprof
Timer unit: 1e-06 s

Total time: 0.000627 s
File: app/fast_demo.py
Function: sort_fast at line 6

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     6                                           @profile
     7                                           def sort_fast():
     8         1           13     13.0      2.1      number_list = range(500)
     9         1          524    524.0     83.6      random.shuffle(number_list)
    10         1           90     90.0     14.4      sorted(number_list)

+ python -m memory_profiler app/fast_demo.py
Filename: app/fast_demo.py

Line #    Mem usage    Increment   Line Contents
================================================
     6   10.461 MiB    0.000 MiB   @profile
     7                             def sort_fast():
     8   10.473 MiB    0.012 MiB       number_list = range(500)
     9   10.473 MiB    0.000 MiB       random.shuffle(number_list)
    10   10.473 MiB    0.000 MiB       sorted(number_list)


+ kernprof -l -v app/slow_demo.py
Wrote profile results to slow_demo.py.lprof
Timer unit: 1e-06 s

Total time: 0.910497 s
File: app/slow_demo.py
Function: sort_slow at line 6

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     6                                           @profile
     7                                           def sort_slow():
     8         1         9739   9739.0      1.1      number_list = range(500000)
     9         1       593153 593153.0     65.1      random.shuffle(number_list)
    10         1       307605 307605.0     33.8      sorted(number_list)

+ python -m memory_profiler app/slow_demo.py
Filename: app/slow_demo.py

Line #    Mem usage    Increment   Line Contents
================================================
     6   10.707 MiB    0.000 MiB   @profile
     7                             def sort_slow():
     8   26.230 MiB   15.523 MiB       number_list = range(500000)
     9   26.230 MiB    0.000 MiB       random.shuffle(number_list)
    10   33.832 MiB    7.602 MiB       sorted(number_list)
```

## Build docker images for web profiling using docker-compose 
`./build_images.sh`

## Boot up flask app and nylas collection/visualizer
`docker-compose up`

## Run Wrk benchmarking tool
```
./make_wrk.sh

# https://github.com/wg/wrk
$ wrk -t1 -c1 -d5s http://localhost:8000/fast
Running 5s test @ http://localhost:8000/fast
  1 threads and 1 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    18.56ms    1.75ms  27.19ms   60.82%
    Req/Sec    53.04      5.74    60.00     60.00%
  268 requests in 5.05s, 45.02KB read
Requests/sec:     53.07
Transfer/sec:      8.91KB
$ wrk -t1 -c1 -d5s http://localhost:8000/slow
Running 5s test @ http://localhost:8000/slow
  1 threads and 1 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    31.66ms    1.23ms  37.21ms   79.87%
    Req/Sec    30.96      3.91    40.00     82.00%
  159 requests in 5.09s, 26.71KB read
Requests/sec:     31.23
Transfer/sec:      5.25KB
```

## View flask app endpoints
http://localhost:8000/fast  
http://localhost:8000/slow

## View flask app stack samples
http://localhost:8000

## View flamegraph of stack samples
http://localhost:8001

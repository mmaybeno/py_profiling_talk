#!/bin/bash
set -x
kernprof -l -v app/fast_demo.py
python -m memory_profiler app/fast_demo.py

kernprof -l -v app/slow_demo.py
python -m memory_profiler app/slow_demo.py

#!/bin/bash
wrk -t1 -c1 -d20s http://localhost:8000/fast
wrk -t1 -c1 -d20s http://localhost:8000/slow

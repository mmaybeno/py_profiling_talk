#!/bin/bash
gunicorn -D -w1 -b 0.0.0.0:8001 --pythonpath=/app/app appviz:visualizer.app
python collector.py --host=flask-demo --ports=8000 --interval=5

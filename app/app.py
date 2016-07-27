import sys
from flask import Flask
from flask import request
sys.path.append('/nylas-perftools')
import stacksampler
import cprofile_demo as cpd

app = Flask(__name__)
sampler = stacksampler.Sampler()
sampler.start()


@app.route("/fast")
def fast():
    cpd.sort_fast()
    return "Hello Fast World!"


@app.route("/slow")
def slow():
    cpd.sort_slow()
    return "Hello Slow World!"


@app.route("/")
def emit():
    stats = sampler.output_stats()
    if request.args.get("reset", "false") == 'true':
        sampler.reset()
    return stats

# Use gunicorn because flask debug mode will fail if you use it enough
import sys
sys.path.append('/nylas-perftools/stackcollector')
import visualizer

# Override visualizer app to make sure it uses the collector db
visualizer.app.config['DBPATH'] = "/var/lib/stackcollector/db"

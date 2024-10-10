from app import app
from monitor import monitor_channels
import threading

if __name__ == '__main__':
    monitor_thread = threading.Thread(target=monitor_channels)
    monitor_thread.start()
    app.run(debug=True, use_reloader=False)
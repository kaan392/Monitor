import psutil
import json
import time
from datetime import datetime

def get_stats():
    data = {
        "timestamp": datetime.now().strftime("/ %Y-%m-%d %H:%M:%S"),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "ram_used": psutil.virtual_memory().used // (1024 * 1024),
        "ram_total": psutil.virtual_memory().total // (1024 * 1024),
        "uptime_sec": int(time.time() - psutil.boot_time())
    }
    return data

while True:
    stats = get_stats()
    with open("stats.json", "w") as f:
        json.dump(stats, f, indent=2)
    time.sleep(1)  # Her 2 saniyede bir günceller

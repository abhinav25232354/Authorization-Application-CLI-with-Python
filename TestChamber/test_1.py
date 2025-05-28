import psutil
import time
from datetime import datetime

def system_activity_log(interval=5, duration=60):
    """Logs and prints system activity every `interval` seconds for `duration` seconds."""
    import time
    import psutil
    from datetime import datetime

    start_time = time.time()
    log_file = "system_activity.txt"

    with open(log_file, "w") as log:
        while time.time() - start_time < duration:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cpu = psutil.cpu_percent(interval=1)
            mem = psutil.virtual_memory().percent
            procs = [p.info['name'] for p in psutil.process_iter(['name'])]

            log_entry = (
                f"\n[{timestamp}]\n"
                f"CPU Usage: {cpu}%\n"
                f"Memory Usage: {mem}%\n"
                f"Running Processes: {', '.join(procs[:10])}...\n"
            )

            print(log_entry)       # Optional: remove if you don't want terminal output
            log.write(log_entry)
            log.flush()            # <-- force writing to file immediately

            if interval > 1:
                time.sleep(interval - 1)


system_activity_log()
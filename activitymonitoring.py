from libraries import *

def system_activity_log(interval=5, duration=60):
    """Logs and prints system activity every `interval` seconds for `duration` seconds."""
    start_time = time.time()
    log_file = "system_activity.log"

    with open(log_file, "a") as log:
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
            
            # print(log_entry)
            log.write(log_entry)
            time.sleep(interval - 1)
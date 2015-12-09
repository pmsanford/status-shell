from datetime import timedelta

class UptimeCommand:
    def __init__(self):
        self.name = 'uptime'

    def run(self, command, healthreport):
        with open('/proc/uptime', 'r') as f:
            uptime_sec = float(f.readline().split()[0])
            uptime_str = str(timedelta(seconds = uptime_sec))
            healthreport['uptime'] = uptime_str

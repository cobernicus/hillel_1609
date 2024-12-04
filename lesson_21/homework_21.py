import logging
from datetime import datetime


logging.basicConfig(
    filename='hb_test.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    force=True
)
logger = logging.getLogger("log_event")


def check_logs(logs_to_read):

    with open(logs_to_read, 'r') as log_file:
        content = log_file.read()
        lines = content.splitlines()
        previous_date = None

        for line in lines:
            if "Key TSTFEED0300|7E3E|0400" in line:
                if "Timestamp " in line:
                    timestamp_str = line.split("Timestamp ")[1].split(" ")[0]
                    date = datetime.strptime(timestamp_str, "%H:%M:%S")

                    if not previous_date:
                        previous_date = date
                        continue

                    diff_time = previous_date - date
                    write_new_logs(diff_time.total_seconds(), date, line)

                    previous_date = date


def write_new_logs(dif_time, date, line):

    msg = f"[HEARTBEAT = {dif_time}] [Time = {date.strftime('%H:%M:%S')}] Log = {line}"
    if 31 <= dif_time < 33:
        logger.warning(f"WARNING {msg}")
    elif dif_time >= 33:
        logger.error(f"ERROR {msg}")


if __name__ == "__main__":
    check_logs("hblog.txt")

    with open("hb_test.log", 'r') as log_file:
        content = log_file.read()
        if not content:
            print("Log file is empty! Make sure there are relevant entries in hblog.txt")
        else:
            print("Log file analysis completed. Check hb_test.log for details.")
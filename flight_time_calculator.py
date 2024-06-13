import os
import glob
from pyulog import ULog

def get_logging_duration(ulog_file):
    ulog = ULog(ulog_file)
    duration_s = (ulog.last_timestamp - ulog.start_timestamp) / 1e6  # Convert microseconds to seconds
    return duration_s / 60  # Convert seconds to minutes

def get_total_logging_duration(directory):
    total_logging_duration = 0.0
    for ulog_file in glob.glob(os.path.join(directory, '*.ulg')):
        logging_duration = get_logging_duration(ulog_file)
        total_logging_duration += logging_duration
        print(f"File: {ulog_file} - Logging Duration: {logging_duration:.2f} minutes")
    return total_logging_duration

def main():
    directory = input("Enter the directory containing the .ulog files: ")
    total_logging_duration = get_total_logging_duration(directory)
    print(f"\nTotal Logging Duration: {total_logging_duration:.2f} minutes")

if __name__ == "__main__":
    main()


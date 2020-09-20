from datetime import datetime
from winevt import EventLog


class EventLogWriter:
    _file_path = None
    _log_depth = None

    def __init__(self, file_path, log_depth=10):
        self._file_path = file_path
        self._log_depth = log_depth

    def __event_finder(self):
        query = EventLog.Query("System", "*[System[Provider[@Name='Microsoft-Windows-Kernel-General'] and (EventID=1)]]"
                               , "backward", )

        time_log_string = ""
        i = 0
        for event in query:
            i = i + 1

            dates = [datetime]*2
            for j in range(2):
                item = event.EventData.Data[j]
                time_data = str(item.cdata)
                date_time = datetime.strptime(time_data[0:19], '%Y-%m-%dT%H:%M:%S')
                dates[j] = date_time

            time_diff = dates[0] - dates[1]
            time_log_string = time_log_string + str(abs(time_diff.total_seconds()/60))
            if i >= 40:
                break
            time_log_string = time_log_string + "\n"

        return time_log_string

    def string_dump(self):
        return self.__event_finder()

    def file_dump(self):
        text_file = open(str(self._file_path) + ".txt", "w")
        text_file.write(self.__event_finder())
        text_file.close()

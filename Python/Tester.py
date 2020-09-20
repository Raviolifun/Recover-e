import EventLogWriter

EventLog = EventLogWriter.EventLogWriter("Test", 30)
EventLog.file_dump()
print(EventLog.string_dump())
class Logger:
    def __init__(self):
        # Store the last successful print time for each message
        self.last_printed = {}

    def shouldPrintMessage(self, timestamp, message):
        if message in self.last_printed:
            previous_time = self.last_printed[message]

            # Reject without changing the saved timestamp
            if timestamp - previous_time < 10:
                return False

        # Outside both if blocks: the message is allowed
        self.last_printed[message] = timestamp
        return True
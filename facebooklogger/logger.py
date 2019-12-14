from pymessenger.bot import Bot
import logging
from facebooklogger.settings import PAGE_ACCESS_TOKEN, FB_USER_ID


class FacebookLogger(logging.Handler):
    def __init__(
        self, user_id=FB_USER_ID, access_token=PAGE_ACCESS_TOKEN, level=logging.NOTSET
    ):
        if access_token is None:
            raise ValueError(
                "access_token not provided, set the PAGE_ACCESS_TOKEN environment variable"
            )
        if access_token is None:
            raise ValueError(
                "user_id not provided, set the FB_USER_ID environment variable"
            )
        logging.Handler.__init__(self, level)
        if FB_USER_ID is None:
            raise ValueError("FB_USER_ID not set")
        logging.Handler.__init__(self, level)
        self.setFormatter(FacebookLoggerFormatter())
        self.user_id = user_id
        self.bot = Bot(access_token)

    def emit(self, record: logging.LogRecord):
        self.bot.send_text_message(self.user_id, self.format(record))


class FacebookLoggerFormatter(logging.Formatter):
    level_formats = {
        "CRITICAL": "❌❌❌ {}: {}",
        "ERROR": "❌ {}: {}",
        "WARNING": "⚠ {}: {}",
        "INFO": "✅ {}: {}",
        "DEBUG": "🐛 {}: {}",
    }

    def format(self, record: logging.LogRecord):
        record.message = record.getMessage()
        if self.usesTime():
            record.asctime = self.formatTime(record, self.datefmt)
        return self.formatMessage(record)

    def formatMessage(self, record: logging.LogRecord):

        try:
            msg_format = self.level_formats[record.levelname]
        except KeyError:
            return "🍆 {} errno {}: {}".format(
                record.name, record.levelno, record.getMessage()
            )
        return msg_format.format(record.name, record.getMessage())

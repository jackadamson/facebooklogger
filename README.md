# Facebook Logger

A logging handler that sends you log entries on Facebook Messenger

```python
import logging
from facebooklogger import FacebookLogger
logger = logging.getLogger("Home Server")
logger.setLevel(logging.INFO)
fb = FacebookLogger(level=logging.INFO)
logger.addHandler(fb)

logger.info("Server Started")
logger.warning("Something might be wrong")
logger.error("EVERYTHING IS ON FIRE")
```


## Getting Started

To use the Facebook logger, you will need to create a Facebook page and get two pieces
of information. A Page Access Token to authenticate as the page, and the User ID you
want logs sent to.

### Page Access Token

Note that to use this logger you DO NOT need to have your app verified by Facebook, you
can just stay in development mode.

Follow the getting started section of https://developers.facebook.com/docs/messenger-platform/getting-started/quick-start



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
![Screenshot 1](https://github.com/jackadamson/facebooklogger/raw/master/images/screenshot1.png)

## Getting Started


Install facebooklogger with
```bash
pip install facebooklogger
```

To use the Facebook logger, you will need to create a Facebook page and get two pieces
of information. A Page Access Token to authenticate as the page, and the User ID you
want logs sent to.

### Configuration

The logger requires two configuration options set:
- `PAGE_ACCESS_TOKEN`
- `FB_USER_ID`

They can be provided as environment variables, or by creating a file called `.env` in
the working directory that looks like:
```.env
PAGE_ACCESS_TOKEN=ABCDEFGH12345abcefweeaABCDEFGH12345abcefweeaABCDEFGH12345abcefweeaABCDEFGH12345abcefweeaABCDEFGH12345abcefweeaABCDEFGH12345abcefweeaABCDEFGH12345abcefweeaABCDEFGH12345abcefwe
FB_USER_ID=1234567891234567
```
Replacing the token and user ID with your own obtained below

### Page Access Token

Note that to use this logger you DO NOT need to have your app verified by Facebook, you
can just stay in development mode.

Follow the getting started section of  
https://developers.facebook.com/docs/messenger-platform/getting-started/quick-start

### User ID

Facebook Page IDs are unique to the page, and as such if you change page you will need
to re-acquire the user id.  
Note: You will have to already have the page access token  

To get user id, run the following
```bash
PAGE_ACCESS_TOKEN=YOURTOKEN python3 -m facebooklogger
```
and follow the prompts

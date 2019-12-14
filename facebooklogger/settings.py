from environs import Env

env = Env()
env.read_env()

PAGE_ACCESS_TOKEN = env.str("PAGE_ACCESS_TOKEN", default=None)
FB_USER_ID = env.str("FB_USER_ID", default=None)

import requests
import urllib.parse
from facebooklogger.settings import PAGE_ACCESS_TOKEN

FB_BASE = "https://graph.facebook.com"


def check_success(req):
    r = req.json()
    if req.status_code != 200:
        if "error" in r and "message" in r["error"]:
            raise ValueError(f"Received error: {r['error']['message']}")
        raise ValueError(f"Received error: {r!r}")


def get_users(page_id):
    conversations_request = requests.get(
        f"{FB_BASE}/{page_id}",
        params={"access_token": PAGE_ACCESS_TOKEN, "fields": "conversations"},
    )
    check_success(conversations_request)
    conv_data = conversations_request.json()["conversations"]["data"]
    return [resolve_conversation(page_id, conv["id"]) for conv in conv_data]


def resolve_conversation(page_id, conv_id):
    participants_request = requests.get(
        f"{FB_BASE}/{conv_id}",
        params={"access_token": PAGE_ACCESS_TOKEN, "fields": "participants"},
    )
    check_success(participants_request)
    participants = participants_request.json()["participants"]["data"]
    assert len(participants) == 2
    return [p for p in participants if p["id"] != page_id][0]


def main():
    if PAGE_ACCESS_TOKEN is None:
        print("Missing environment variable 'PAGE_ACCESS_TOKEN', check README.md")
    me_request = requests.get(
        FB_BASE + "/me", params={"access_token": PAGE_ACCESS_TOKEN}
    )
    check_success(me_request)
    page_id = me_request.json()["id"]
    page_name = me_request.json()["name"]
    escaped_page_name = urllib.parse.quote(page_name)
    users = get_users(page_id)
    while True:
        if len(users) == 0:
            print("No conversations found")
            print(f"Send a message to your bot at: https://m.me/{escaped_page_name}")
            print("Press enter once you've sent a message")
            input()
        else:
            print("App User IDs for conversations with page:")
            for user in users:
                print(f"{user['name']!r} => {user['id']}")
            break

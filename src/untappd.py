import os

import requests
from requests.auth import HTTPBasicAuth, AuthBase
from dotenv import load_dotenv


def try_fetch(menu_id: int, auth: AuthBase):
    response = requests.get(
        url=f"https://business.untappd.com/api/v1/items/{menu_id}", auth=auth
    )
    print(menu_id, response.json())


if __name__ == "__main__":
    load_dotenv()
    start = 30458500
    for i in range(start, start + 100):
        try_fetch(
            menu_id=i,
            auth=HTTPBasicAuth(
                username=os.environ["UNTAPPD_USER"],
                password=os.environ["UNTAPPD_PASS"],
            ),
        )

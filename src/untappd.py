import os

import requests
from requests.auth import HTTPBasicAuth, AuthBase
from dotenv import load_dotenv


def try_fetch(menu_id: str, auth: AuthBase):
    response = requests.get(
        url=f"https://business.untappd.com/api/v1/items/{menu_id}", auth=auth
    )
    print(menu_id, response.json())


if __name__ == "__main__":
    load_dotenv()
    basic_auth = HTTPBasicAuth(os.environ["UNTAPPD_USER"], os.environ["UNTAPPD_PASS"])
    for i in range(100):
        print(str(i).rjust(2, "0"))
        try_fetch("304585" + str(i).rjust(2, "0"), auth=basic_auth)

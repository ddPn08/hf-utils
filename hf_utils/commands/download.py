import os
import requests

from huggingface_hub import HfApi

from hf_utils.util import get_hf_token

api = HfApi()


BASE_URL = "https://huggingface.co"


def cli(location: str, repo_type: str = "datasets", dest: str = None):
    location = location.split("/")
    repo_id, location = "/".join(location[:2]), "/".join(location[2:])

    if dest is None:
        dest = os.path.basename(location)

    url = f"{BASE_URL}/{repo_type}/{repo_id}/resolve/main/{location}"

    token = get_hf_token()

    with requests.get(url, headers={"Authorization": f"Bearer {token}"}) as r:
        with open(dest, "wb") as f:
            f.write(r.content)

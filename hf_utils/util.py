import os
from huggingface_hub import constants


def get_hf_token():
    with open(os.path.join(constants.HF_TOKEN_PATH), "r") as f:
        return f.read().strip()

import os

from huggingface_hub import HfApi

api = HfApi()


def cli(
    src: str,
    repo_id: str,
    dest: str = None,
    repo_type: str = "dataset",
    ignore_patterns: list[str] = [],
):
    assert os.path.exists(src), "Source is not exists."

    repo_url = api.create_repo(repo_id=repo_id, repo_type=repo_type, exist_ok=True)
    repo = repo_url.repo_id

    if dest is None:
        dest = os.path.basename(src)

    if os.path.isfile(src):
        api.upload_file(
            path_or_fileobj=src, path_in_repo=dest, repo_id=repo, repo_type=repo_type
        )
    else:
        api.upload_folder(
            folder_path=src,
            path_in_repo=dest,
            repo_id=repo,
            repo_type=repo_type,
            ignore_patterns=ignore_patterns,
        )

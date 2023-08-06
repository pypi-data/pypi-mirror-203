import os
import glob
import sys
import io
from huggingface_hub import HfApi
from huggingface_hub.utils import HfHubHTTPError
import argparse


parser = argparse.ArgumentParser(
    description="Upload a MiniChain app to the HuggingFace hub. "
)

parser.add_argument('repo', type=str)
parser.add_argument('app_file', type=str)
parser.add_argument('-r', '--requirements', type=str)
parser.add_argument('--readme', type=str)
parser.add_argument('--name', type=str)
parser.add_argument('--extra', type=str)

args = parser.parse_args()
api = HfApi()

repo_id = args.repo
app = args.app_file

readme = f"""
---
title: {args.name}
emoji: ⛓️
colorFrom: purple
colorTo: blue
sdk: gradio
sdk_version: 3.24.0
app_file: app.py
pinned: true
python_version: 3.9.0
---
"""

readme_file = args.readme
if not args.readme:
    readme_file = io.BytesIO(bytes(readme, "utf-8"))

requirements = """
minichain
"""

requirements_file = args.requirements
if not args.requirements:
    requirements_file = io.BytesIO(bytes(requirements, "utf-8"))

try:
    api.create_repo(repo_id=repo_id, repo_type="space", space_sdk="gradio")
except HfHubHTTPError:
    pass

for p in args.extra.split(","):
    api.upload_file(repo_id=repo_id, repo_type="space", path_or_fileobj=p, path_in_repo=p)
api.upload_file(repo_id=repo_id, repo_type="space", path_or_fileobj=readme_file, path_in_repo="README.md")
api.upload_file(repo_id=repo_id, repo_type="space", path_or_fileobj=requirements_file, path_in_repo="requirements.txt")
api.upload_file(repo_id=repo_id, repo_type="space", path_or_fileobj=app, path_in_repo="app.py")

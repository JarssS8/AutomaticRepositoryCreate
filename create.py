"""Create repository in github and clone it locally."""
import argparse
import json
import os

import requests

defaul_path = "~/Programming/"


def main():
    """Principal logic of the script."""
    try:
        args = parse_args()
        repo_name, url_to_clone = create_repo_github(args)
        clone_repo(args, repo_name, url_to_clone)
    except Exception as e:
        print(e)


def parse_args():
    """Parse arguments from command line."""
    parser = argparse.ArgumentParser(
        description="Create repository in github and clone it locally"
    )

    parser.add_argument("-n", "--name", help="Rapository name", required=True)
    parser.add_argument(
        "-d",
        "--description",
        help="Project description",
        required=False,
        default=None,
    )
    parser.add_argument(
        "-p",
        "--private",
        help="Project privacity",
        required=False,
        default=None,
        action="store_true",
    )
    parser.add_argument(
        "-r",
        "--route",
        help="Custom route/path to the project",
        required=False,
        default=defaul_path,
    )

    return parser.parse_args()


def create_repo_github(args):
    """Create repository in github with the client arguments."""
    if not os.environ.get("GITHUB_TOKEN"):
        raise Exception("GITHUB_TOKEN not found on enviroment variables")

    url = "https://api.github.com/user/repos"
    data = {
        "name": args.name,
        "description": args.description,
        "private": args.private,
        "auto_init": True,
        "license_template": "gpl-3.0",
    }
    headers = {
        "Authorization": "token " + os.environ["GITHUB_TOKEN"],
        "Content-Type": "application/json",
    }
    response = requests.post(url, data=json.dumps(data), headers=headers)
    if response.status_code == 201:
        print("Repository created successfully")
        url_to_clone = response.json()["clone_url"]
        repo_name = response.json()["name"]
        return repo_name, url_to_clone
    else:
        raise Exception(
            "Error creating repository. Probably that repository already "
            "exists"
        )


def clone_repo(args, repo_name, url_to_clone):
    """Clone repository from github to local machine."""
    path = "{}{}".format(args.route, repo_name)
    os.system("mkdir -p {}".format(path))
    url_to_clone = url_to_clone.replace("https://", "")
    command = 'git clone https://oauth2:{token}@{clone_url} "{path}"'.format(
        token=os.environ["GITHUB_TOKEN"], clone_url=url_to_clone, path=path
    )
    os.system(command)
    print("Repository cloned successfully on {path}".format(path=path))


if __name__ == "__main__":
    main()

from github import Github
from repository import RepoLocal
from git import Repo
import json, sys

json_path = '/home/jars/Programming/Python/GithubAPI/credentials.json'
root_path_to_clone = "/home/jars/Programming/Autocreated/"

try:
    f = open(json_path,) 
    data = json.load(f)
except Exception:
    print('ERROR: The path or the JSON of the credentials is not correct.')
    exit()

username = data['username']
password = data['password']
f.close()


def create_repo_github(repoLocal):
    g = Github(username, password)
    user = g.get_user()
    repoGithub = user.create_repo(name = repoLocal.name, description = repoLocal.description, private = repoLocal.private, license_template = repoLocal.license, auto_init= repoLocal.auto_init)
    print('Repository created on github')
    get_clone_url(repoGithub)


def get_clone_url(repoGithub):
    path = root_path_to_clone+repoLocal.name
    clone_url = repoGithub.clone_url
    Repo.clone_from(url=clone_url, to_path=path)
    print('Cloned in path {} succesfully!'.format(path))

if __name__ == "__main__":
    

    description = ''
    private = ''
    try:
        name = str(sys.argv[1])
        print(str(sys.argv[0]))
        if "-help"==name or "-h"==name:
            print('The structure is REPO_NAME FLAGS [DESCRIPTION]')
            print('If the REPO_NAME or the DESCRIPTION have more than ONE word should go between \" \"')
            print('Order of the flags is indiferent and must start with \'-\'')
            print('Flags could be:\n  p for make it private, for default is public\n  d for add a description after the flags')
            print('Example: \"Test name for the repo\" -dp \"This is the example for the description\"')
            exit()
        elif name.startswith('-'):
            print('ERROR: The name could not start with \"-\"')
            exit()
    except IndexError:
        print("ERROR: Needs a name for the repository!")
        print("If you need help type -h or -help")
        exit()

    try:
        flags = str(sys.argv[2])
        if "p" in flags:
            private = True
        else:
            private = None

        if "d" in flags:
            i = 3
            while i < len(sys.argv):
                description += "{} ".format(sys.argv[i])
                i=i+1
        else:
            description = None
        if "-help"==flags or "-h"==flags:
            print()
    except IndexError:
        description = None
        if private == '':
            private = None
    repoLocal = RepoLocal(name = name, description = description, private = private)
    print('Repository Object created')
    create_repo_github(repoLocal)

from github import Github, Repository
import json

json_path = '/home/jars/Programming/Python/GithubAPI/credentials.json'

try:
    f = open(json_path,) 
    data = json.load(f)
except Exception:
    print('ERROR: The path or the JSON of the credentials is not correct.')
    exit()

username = data['username']
password = data['password']
f.close()


def get_repos():
    g = Github(username, password)
    user = g.get_user()
    repos = user.get_repos(sort='created_at', direction='asc')
    print('------------------REPOSITORIES------------------------')
    print('------------------------------------------------------')
    count_repos = 0
    for repo in repos:
        count_repos+=1
        print('{}.- {}'.format(count_repos,repo.name))
    print('------------------------------------------------------')
    return repos


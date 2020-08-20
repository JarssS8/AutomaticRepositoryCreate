from github import Github, Repository
import json
from get_repos import get_repos

def remove():

    repos = get_repos()
    id_repo=int(input('Repository that you want to delete: '))
    print('Sure you want to delete:  {}.- {}'.format(id_repo,repos[id_repo-1].name))
    if int(input('1.- YES, 2.- NO\n')) == 1:
        print('Removed')
    else:
        print('Not Removed')

remove()
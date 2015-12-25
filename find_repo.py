#! /usr/bin/python

import os

repodir = ".repo"
S_repo = "repo"
REPO_MAIN = S_repo + "/main.py"

curdir = os.getcwd()
print "Current directory is ", curdir

repo = None
olddir = None

print "repo is ", repo

while curdir != '/'\
    and curdir != olddir\
    and not repo:
    repo = os.path.join(curdir, repodir, REPO_MAIN)
    print "repo is ", repo
    if not os.path.isfile(repo):
        repo = None
        olddir = curdir
        curdir = os.path.dirname(curdir)
print "repo is ", repo
print "repo dir is ", os.path.join(curdir, repodir)
